# Contributing

Dokumen ini memberi baseline kontribusi untuk `codex-starter`.

## Tujuan Kontribusi

- jaga template tetap ringan, portable, dan mudah dipahami
- utamakan perubahan kecil yang benar-benar reusable
- jangan masukkan data pribadi, secret, dump, atau runtime state lokal

## Workflow Ringkas

1. Jalankan `bash ./scripts/project-health.sh --auto`.
2. Buat perubahan sekecil mungkin.
3. Verifikasi minimal yang relevan:
   - `python3 scripts/rules-health.py`
   - `python3 scripts/memory-health.py`
   - `python3 scripts/research-health.py`
4. Pastikan tidak ada file sensitif atau generated output yang ikut.

## Aturan Konten

- gunakan `.env.example` atau placeholder yang jelas
- dokumentasikan perubahan perilaku di `README.md` atau doc terdekat
- jangan tambahkan dependency berat tanpa alasan kuat
- repo skills, custom agents, dan devops kompleks sebaiknya masuk `codex-pro`, bukan `codex-starter`

## Pull Request Checklist

- perubahan masih cocok untuk starter pemula
- tidak ada path host pribadi atau nama repo sumber
- health check lulus
- sanitasi file sensitif sudah dicek
