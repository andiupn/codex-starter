#!/usr/bin/env bash

set -u

TARGET_PATH="${1:-$PWD}"

command_exists() {
  command -v "$1" >/dev/null 2>&1
}

section() {
  printf '\n== %s ==\n' "$1"
}

line() {
  printf '%s\n' "$1"
}

safe_realpath() {
  if command_exists realpath; then
    realpath "$1" 2>/dev/null || printf '%s\n' "$1"
  else
    printf '%s\n' "$1"
  fi
}

safe_run() {
  local label="$1"
  shift
  printf '\n[%s]\n' "$label"
  if "$@" 2>/dev/null; then
    :
  else
    printf 'Unavailable or failed: %s\n' "$*"
  fi
}

TARGET_PATH="$(safe_realpath "$TARGET_PATH")"
NOW="$(date '+%Y-%m-%d %H:%M:%S %Z (%z)')"
USER_NAME="$(whoami 2>/dev/null || printf 'unknown')"
SHELL_NAME="${SHELL:-unknown}"
HOST_NAME="$(hostname 2>/dev/null || printf 'unknown')"
FS_TYPE="$(stat -f -c '%T' "$TARGET_PATH" 2>/dev/null || printf 'unknown')"

PATH_AVAIL_GB="$(df -BG --output=avail "$TARGET_PATH" 2>/dev/null | tail -n 1 | tr -dc '0-9')"
ROOT_AVAIL_GB="$(df -BG --output=avail / 2>/dev/null | tail -n 1 | tr -dc '0-9')"

MEM_AVAILABLE_MB="$(awk '/MemAvailable:/ {printf "%d", $2/1024}' /proc/meminfo 2>/dev/null)"
SWAP_TOTAL_MB="$(awk '/SwapTotal:/ {printf "%d", $2/1024}' /proc/meminfo 2>/dev/null)"
SWAP_FREE_MB="$(awk '/SwapFree:/ {printf "%d", $2/1024}' /proc/meminfo 2>/dev/null)"

if [[ -n "${SWAP_TOTAL_MB:-}" && -n "${SWAP_FREE_MB:-}" ]]; then
  SWAP_USED_MB="$((SWAP_TOTAL_MB - SWAP_FREE_MB))"
else
  SWAP_USED_MB=""
fi

HAS_NODE="no"
HAS_PYTHON="no"
HAS_GIT="no"
HAS_RG="no"

command_exists node && HAS_NODE="yes"
command_exists python3 && HAS_PYTHON="yes"
command_exists git && HAS_GIT="yes"
command_exists rg && HAS_RG="yes"

section "Snapshot"
line "Time: $NOW"
line "User: $USER_NAME"
line "Shell: $SHELL_NAME"
line "Host: $HOST_NAME"
line "Target path: $TARGET_PATH"
line "Target filesystem: $FS_TYPE"

section "System"
safe_run "uname -a" uname -a
safe_run "os-release" cat /etc/os-release
safe_run "hostnamectl" hostnamectl

section "Compute"
safe_run "lscpu" lscpu
safe_run "memory" free -h
safe_run "swap" swapon --show
safe_run "uptime" uptime

section "Storage"
safe_run "df target" df -h "$TARGET_PATH"
safe_run "df root" df -h /
safe_run "lsblk" lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS

section "Graphics"
if command_exists inxi; then
  safe_run "inxi -c 0 -Gxx" inxi -c 0 -Gxx
elif command_exists lspci; then
  safe_run "lspci graphics" bash -lc "lspci | grep -Ei 'vga|3d|display'"
else
  line "No graphics inspection tool found."
fi

section "Toolchain"
if command_exists node; then
  safe_run "node -v" node -v
fi
if command_exists npm; then
  safe_run "npm -v" npm -v
fi
if command_exists python3; then
  safe_run "python3 --version" python3 --version
fi
if command_exists git; then
  safe_run "git --version" git --version
fi
if command_exists rg; then
  safe_run "rg --version" bash -lc "rg --version | head -n 1"
fi

section "Codex Readiness"
line "Node available: $HAS_NODE"
line "Python available: $HAS_PYTHON"
line "Git available: $HAS_GIT"
line "ripgrep available: $HAS_RG"

if [[ -n "${MEM_AVAILABLE_MB:-}" ]]; then
  line "Available memory: ${MEM_AVAILABLE_MB} MB"
fi

if [[ -n "${SWAP_USED_MB:-}" ]]; then
  line "Swap used: ${SWAP_USED_MB} MB of ${SWAP_TOTAL_MB} MB"
fi

if [[ -n "${PATH_AVAIL_GB:-}" ]]; then
  line "Free space on target path filesystem: ${PATH_AVAIL_GB} GB"
fi

if [[ -n "${ROOT_AVAIL_GB:-}" ]]; then
  line "Free space on Linux root filesystem: ${ROOT_AVAIL_GB} GB"
fi

line ""
line "Assessment:"

if [[ "$FS_TYPE" == "fuseblk" || "$FS_TYPE" == "ntfs" || "$FS_TYPE" == "ntfs3" ]]; then
  line "- Target path is on a Windows-style filesystem. Codex can work here, but native Linux ext4 is better for installs, git, watchers, and build speed."
fi

if [[ -n "${PATH_AVAIL_GB:-}" && "$PATH_AVAIL_GB" -lt 10 ]]; then
  line "- Free space on the target path is under 10 GB. This is a high-risk condition for dependency installs, caches, screenshots, logs, and build output."
fi

if [[ -n "${MEM_AVAILABLE_MB:-}" && "$MEM_AVAILABLE_MB" -lt 2048 ]]; then
  line "- Available RAM is under 2 GB. Heavy browser automation or large installs may become unstable."
elif [[ -n "${MEM_AVAILABLE_MB:-}" && "$MEM_AVAILABLE_MB" -lt 4096 ]]; then
  line "- Available RAM is under 4 GB. The system is still usable, but parallel tasks may slow down."
fi

if [[ -n "${SWAP_USED_MB:-}" && "$SWAP_USED_MB" -gt 0 ]]; then
  line "- Swap is already in use. This is not fatal, but it suggests some memory pressure is present."
fi

if [[ "$HAS_NODE" == "yes" && "$HAS_PYTHON" == "yes" && "$HAS_GIT" == "yes" && "$HAS_RG" == "yes" ]]; then
  line "- Core local tooling for Codex workflows is present."
else
  line "- Some local tooling is missing. Install Node, Python, Git, and ripgrep for the smoothest workflow."
fi

line ""
line "Recommended next step:"
if [[ "$FS_TYPE" == "fuseblk" || "$FS_TYPE" == "ntfs" || "$FS_TYPE" == "ntfs3" ]]; then
  line "- Move the active workspace to a native Linux filesystem (btrfs/ext4) under \$HOME when possible."
else
  line "- Keep this workspace on Linux ext4 and maintain at least 20 GB of free space."
fi
