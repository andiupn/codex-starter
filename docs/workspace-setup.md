# Recommended codex-starter Workspace Setup

Dokumen ini merangkum setup workspace yang aman dan portable untuk `codex-starter`.

## Recommendation

- Windows 11: simpan repo di path lokal biasa seperti `<drive>:\path\to\codex-starter` dan gunakan Git Bash untuk script shell.
- Linux/Fedora: simpan repo di filesystem native under `$HOME`, misalnya `/path/to/codex-starter`.
- Hindari menjalankan install besar, watcher, atau browser artifact dari mount NTFS/Windows.

## Repo Folder Layout

```text
codex-starter/
├── active/
├── staging/
├── templates/
├── shared/
├── artifacts/
├── archive/
├── experiments/
├── research/
├── docs/
└── scripts/
```

## Recommended Setup Commands

```bash
cd /path/to/codex-starter
chmod +x scripts/*.sh scripts/*.py
./scripts/project-health.sh --auto
```

Jika shell tidak membawa executable bit, fallback aman:

```bash
bash ./scripts/project-health.sh --auto
```

## Practical Rules

- gunakan filesystem Linux native untuk workspace aktif bila tersedia
- sisakan free space yang cukup untuk cache, logs, dan artifacts
- simpan screenshot atau output uji di `artifacts/` atau folder eksperimen terkait
- gunakan `scripts/check-system.sh` saat setup awal atau saat performa terasa aneh
