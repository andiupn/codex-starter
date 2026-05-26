# Research System

Dokumen ini menjelaskan sistem arsip riset untuk repo template ini.

## Goal

- menyimpan hasil riset ke tempat yang konsisten
- memudahkan pencarian ulang hasil riset lama
- memisahkan riset berbasis sumber dari memory yang lebih ringkas

## Recommended Structure

```text
research/
├── index.json
└── entries/
    └── <id>/
        ├── report.md
        └── sources.json
```

## What Goes Into Research

- hasil berbasis sumber
- perbandingan opsi
- riset yang panjang atau bernuansa
- hasil yang kemungkinan dipakai ulang nanti

## What Goes Into Memory Instead

- preferensi user
- keputusan project
- constraint environment
- workflow stabil
- meta-insight yang pendek dan tahan lama

## Suggested Workflow

1. Jalankan `./scripts/project-health.sh --auto`
2. Cari riset yang sudah ada dengan `./scripts/research-find.py <query>`
3. Jika perlu riset baru atau update, simpan dengan `./scripts/research-upsert.py`
4. Audit dengan `python3 scripts/research-health.py`
5. Promote insight yang benar-benar stabil ke memory

Jika nanti repo ini bertambah kompleks, Anda bisa menambahkan skill riset khusus. Template starter ini sengaja tidak membundel repo skill bawaan.
