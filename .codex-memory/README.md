# Codex Memory

Folder ini adalah memori proyek berbasis file untuk membantu Codex tetap konsisten lintas sesi tanpa membaca seluruh riwayat kerja.

## Tujuan

- Menyimpan pengetahuan yang tahan lama dan berguna ulang
- Mengurangi token dengan retrieval berbasis index
- Membantu agent baru memahami konteks penting sebelum mulai kerja

## Alur yang disarankan

1. Jalankan `./scripts/project-health.sh --auto`
2. Baca `.codex-memory/index.json`
3. Pilih maksimal 3 entry paling relevan
4. Baca file detail hanya untuk entry yang benar-benar dibutuhkan
5. Setelah task selesai, update entry yang relevan
6. Jaga ringkasan tetap padat dan mudah di-scan

## Yang layak disimpan

- preferensi user
- keputusan arsitektur atau workflow
- constraint environment
- bug/fix yang berulang
- command verifikasi penting

## Yang tidak layak disimpan

- secret
- token API
- dump log mentah
- transcript percakapan penuh
- hasil sementara yang tidak akan dipakai lagi

## Format

- `index.json`: katalog ringkas untuk retrieval cepat
- `maintenance-log.json`: status maintenance lokal dan waktu maintenance terakhir
- `entries/*.md`: detail memory yang sudah dikompak
- `../scripts/memory-find.py`: cari memory relevan dari index
- `../scripts/memory-upsert.py`: tambah atau merge memory entry dan sinkronkan index
- `../scripts/memory-health.py`: audit index dan entry agar memory tetap konsisten
- `../scripts/maintenance-check.py`: cek apakah maintenance sudah overdue
- `../scripts/project-health.sh`: jalankan audit otomatis jika maintenance sudah lewat jadwal

## Praktik hemat token

- summary pada index harus singkat
- satu memory entry mewakili satu fakta atau topik stabil
- gabungkan memory yang mirip daripada menambah file baru terus-menerus

## Contoh penggunaan

```bash
./scripts/project-health.sh --auto
python3 scripts/maintenance-check.py
./scripts/memory-find.py filesystem ext4
./scripts/memory-find.py --limit 3 memory maintenance
python3 scripts/memory-health.py
./scripts/memory-upsert.py --id user-preferences --stable-note "Contoh note baru" --dry-run
./scripts/memory-upsert.py \
  --id system-environment \
  --kind environment \
  --stable-note "Gunakan ext4 untuk workspace aktif agar install dan watcher lebih stabil" \
  --impact "Jika task terasa lambat, cek dulu lokasi filesystem dan free space" \
  --reference docs/workspace-setup.md
```

## Checklist maintenance

- jalankan `./scripts/project-health.sh --auto` sebelum pekerjaan non-trivial
- jalankan `python3 scripts/memory-health.py`
- pastikan tidak ada entry file yatim yang belum masuk index
- compact summary jika terlalu panjang
- update memory yang sudah ada, jangan bikin duplikat topik yang sama
