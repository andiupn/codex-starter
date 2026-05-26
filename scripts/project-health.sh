#!/usr/bin/env bash

set -u

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_PATH="$PWD"
MODE="full"
NOTE="Routine project maintenance"
RUN_SYSTEM="yes"
RUN_RULES="yes"
RUN_MEMORY="yes"
RUN_RESEARCH="yes"

usage() {
  cat <<'EOF'
Usage:
  ./scripts/project-health.sh [--auto] [--target PATH] [--note TEXT]

Modes:
  --auto        Check maintenance log first. If overdue, run full maintenance.
                If still fresh, only update last_checked_at and exit.
  --target PATH Pass a target path to check-system.sh.
  --note TEXT   Note stored when maintenance is recorded.
  --no-system   Skip system check.
  --no-rules    Skip rules audit.
  --no-memory   Skip memory checks.
  --no-research Skip research archive checks.
  --help        Show this help.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --auto)
      MODE="auto"
      shift
      ;;
    --target)
      TARGET_PATH="$2"
      shift 2
      ;;
    --note)
      NOTE="$2"
      shift 2
      ;;
    --no-system)
      RUN_SYSTEM="no"
      shift
      ;;
    --no-rules)
      RUN_RULES="no"
      shift
      ;;
    --no-memory)
      RUN_MEMORY="no"
      shift
      ;;
    --no-research)
      RUN_RESEARCH="no"
      shift
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage
      exit 1
      ;;
  esac
done

run_full_maintenance() {
  local failed=0

  echo "Running project health maintenance"
  echo "Target path: $TARGET_PATH"

  if [[ "$RUN_SYSTEM" == "yes" ]]; then
    "$ROOT_DIR/scripts/check-system.sh" "$TARGET_PATH" || failed=1
  fi

  if [[ "$RUN_RULES" == "yes" ]]; then
    python3 "$ROOT_DIR/scripts/rules-health.py" || failed=1
  fi

  if [[ "$RUN_MEMORY" == "yes" ]]; then
    python3 "$ROOT_DIR/scripts/memory-health.py" --strict || failed=1
    "$ROOT_DIR/scripts/memory-find.py" --limit 3 maintenance health project || failed=1
  fi

  if [[ "$RUN_RESEARCH" == "yes" ]]; then
    python3 "$ROOT_DIR/scripts/research-health.py" || failed=1
    "$ROOT_DIR/scripts/research-find.py" --limit 3 maintenance research archive || failed=1
  fi

  if [[ $failed -eq 0 ]]; then
    python3 "$ROOT_DIR/scripts/maintenance-check.py" --record-maintenance --note "$NOTE"
  else
    echo ""
    echo "Project health maintenance failed before maintenance log could be recorded as successful." >&2
  fi

  return $failed
}

if [[ "$MODE" == "auto" ]]; then
  echo "Checking maintenance cadence"
  python3 "$ROOT_DIR/scripts/maintenance-check.py" --record-check
  status=$?

  if [[ $status -eq 0 ]]; then
    echo ""
    echo "Maintenance is still within the 7-day window. No full maintenance run is required."
    exit 0
  fi

  if [[ $status -ne 10 ]]; then
    exit $status
  fi

  echo ""
  echo "Maintenance is overdue. Running automatic maintenance now."
fi

run_full_maintenance
