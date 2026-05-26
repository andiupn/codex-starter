# Project Folder System

Dokumen ini menjelaskan sistem folder aplikasi atau project di repo ini, diadaptasi dari pola workspace sibling yang memisahkan project aktif, template, archive, dan eksperimen.

## Goal

Pisahkan dengan jelas:

- app atau project yang masih aktif
- template yang reusable
- hasil staging sementara
- arsip project lama
- artifacts generated output

Tanpa mencampur semuanya dengan:

- `experiments/` untuk benchmark dan uji agent
- `research/` untuk riset reusable
- `docs/` untuk dokumentasi aturan
- `devops/` untuk infra helpers

## Folder Map

| Folder | Fungsi | Isi yang cocok | Isi yang tidak cocok |
|---|---|---|---|
| `active/` | rumah utama project/app yang masih hidup | app yang sedang dikembangkan atau dipelihara | benchmark agent, research archive |
| `active/web/` | app web aktif | Next.js, PHP web, gateway UI, dashboard | mobile app |
| `active/mobile/` | app mobile aktif | Flutter, React Native, mobile prototype | app web |
| `staging/` | tempat transit untuk project yang belum rapi | import awal, hasil unpack, draft migrasi | project aktif jangka panjang |
| `templates/` | starter yang reusable | skeleton app, boilerplate minimal, preset stack | data runtime, output generated |
| `shared/` | aset atau modul yang dipakai lintas project | shared assets, common snippets, reusable config | project yang punya lifecycle sendiri |
| `artifacts/` | output generated dari app/project work | screenshots, exported reports, temporary captures | source code utama |
| `archive/` | project lama yang disimpan | snapshot app lama, retired prototype, historical state | project aktif |
| `experiments/` | eksperimen agent/benchmark | eval, benchmark, prompt comparison | source code app utama |

## Naming Rules

- App aktif gunakan bentuk `active/web/<app-name>/` atau `active/mobile/<app-name>/`
- Gunakan `kebab-case` untuk nama folder app
- Satu app utama satu folder
- Jika sebuah app diarsipkan, pindahkan ke `archive/<year>/<app-name>/`

## Repo-Specific Notes

- Repo ini sudah punya `devops/`, jadi kita tetap memakai `devops/` sebagai rumah infra. Tidak perlu rename ke `ops/` hanya demi menyamakan sibling repo.
- Repo ini sudah punya `experiments/`, jadi benchmark dan percobaan agent tetap tinggal di sana.
- Sistem folder ini ditambahkan untuk app/project lifecycle, bukan untuk mengganti struktur governance yang sudah ada.

## Placement Rules

Gunakan aturan ini saat membuat project baru:

1. Jika user meminta app nyata atau prototype yang bisa dijalankan, taruh di `active/`.
2. Jika materialnya masih mentah atau sedang dipilah sebelum jadi app aktif, taruh sementara di `staging/`.
3. Jika hasilnya reusable sebagai starter, pindahkan atau salin versi generiknya ke `templates/`.
4. Jika hanya output generated, taruh di `artifacts/`.
5. Jika project sudah tidak aktif tetapi masih perlu disimpan, pindahkan ke `archive/`.

## Documentation Rule

Setiap app atau project runnable di `active/` sebaiknya punya README terdekat yang minimal menjelaskan:

- objective
- stack
- how to run
- status

## Minimal Skeleton

Sistem ini minimalnya berarti repo punya folder berikut:

- `active/web/`
- `active/mobile/`
- `staging/`
- `templates/`
- `shared/`
- `artifacts/`
- `archive/`

Folder-folder ini boleh tetap hampir kosong sampai ada app nyata yang masuk.
