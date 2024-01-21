# Kitab Undang-Undang Hukum Pidana (KUHP) 2023 (UU No. 1 Tahun 2023)

Masih dalam pengerjaan.

* Sumber file: https://peraturan.bpk.go.id/Details/234935/uu-no-1-tahun-2023
* Draf (baca-saja): 
  - [Google Sheets](https://docs.google.com/spreadsheets/d/1ymN2lIvQJmYY53oO9jyYWlCKSPhjKxXjDqdiwT-CkIg/edit#gid=989803682)
  - [DuckDB Playground (SQL)](https://sekuel.com/playground/?q=Q1JFQVRFIE9SIFJFUExBQ0UgVEFCTEUga3VocF9idWt1IEFTICgKICAgIFNFTEVDVCAqIEZST00gcmVhZF9jc3ZfYXV0bygnaHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vc3ByZWFkc2hlZXRzL2V4cG9ydD9mb3JtYXQ9dHN2JmlkPTF5bU4ybEl2UUptWVk1M29POWp5WVdsQ0tTUGhqS3hYakRxZGl3VC1Da0lnJmdpZD0wJykKKTsKCkNSRUFURSBPUiBSRVBMQUNFIFRBQkxFIGt1aHBfYmFiIEFTICgKICAgIFNFTEVDVCAqIEZST00gcmVhZF9jc3ZfYXV0bygnaHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vc3ByZWFkc2hlZXRzL2V4cG9ydD9mb3JtYXQ9dHN2JmlkPTF5bU4ybEl2UUptWVk1M29POWp5WVdsQ0tTUGhqS3hYakRxZGl3VC1Da0lnJmdpZD0xNDQ4NjcwMDQzJykKKTsKCkNSRUFURSBPUiBSRVBMQUNFIFRBQkxFIGt1aHBfYXlhdCBBUyAoCiAgICBTRUxFQ1QgKiBGUk9NIHJlYWRfY3N2X2F1dG8oJ2h0dHBzOi8vZG9jcy5nb29nbGUuY29tL3NwcmVhZHNoZWV0cy9leHBvcnQ%2FZm9ybWF0PXRzdiZpZD0xeW1OMmxJdlFKbVlZNTNvTzlqeVlXbENLU1Boakt4WGpEcWRpd1QtQ2tJZyZnaWQ9OTg5ODAzNjgyJykKKTsKCkNSRUFURSBPUiBSRVBMQUNFIFRBQkxFIGt1aHBfaHVydWYgQVMgKAogICAgU0VMRUNUICogRlJPTSByZWFkX2Nzdl9hdXRvKCdodHRwczovL2RvY3MuZ29vZ2xlLmNvbS9zcHJlYWRzaGVldHMvZXhwb3J0P2Zvcm1hdD10c3YmaWQ9MXltTjJsSXZRSm1ZWTUzb085anlZV2xDS1NQaGpLeFhqRHFkaXdULUNrSWcmZ2lkPTQwNTA3MjkxJykKKTsKCg%3D%3D)


## Pengubahan dari Pasal ke tabel

### Teks Pasal

```
Pasal 71
(1) Jika seseorang melakukan Tindak Pidana yang hanya diancam dengan pidana penjara di bawah 5 (lima) tahun, sedangkan hakim berpendapat tidak perlu menjatuhkan pidana penjara setelah mempertimbangkan tujuan pemidanaan dan pedoman pemidanaan sebagaimana dimaksud dalam Pasal 51 sampai dengan Pasal 54, orang tersebut dapat dijatuhi pidana denda.
(2) Pidana denda sebagaimana dimaksud pada ayat (1) hanya dapat dijatuhkan jika:
    a. tanpa Korban;
    b. Korban tidak mempermasalahkan; atau
    c. bukan pengulangan Tindak Pidana.
(3) Pidana denda yang dapat dijatuhkan berdasarkan ketentuan sebagaimana dimaksud pada ayat (1) adalah pidana denda paling banyak kategori V dan pidana denda paling sedikit kategori III.
(4) Ketentuan sebagaimana dimaksud pada ayat (2) huruf c tidak berlaku bagi orang yang pernah dijatuhi pidana penjara untuk Tindak Pidana yang dilakukan sebelum berumur 18 (delapan belas) tahun.
```

### Tabel

```
KUHP - AYAT.tsv
┌───────┬───────┬───────────────┬──────────────┬───────────────┬───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ pasal │ ayat  │ pasal_rujukan │ ayat_rujukan │ huruf_rujukan │                                                                           teks                                                                            │
│ int64 │ int64 │    varchar    │   varchar    │    varchar    │                                                                          varchar                                                                          │
├───────┼───────┼───────────────┼──────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│    71 │     1 │ 51,52,53,54   │              │               │ Jika seseorang melakukan Tindak Pidana yang hanya diancam dengan pidana penjara di bawah 5 (lima) tahun, sedangkan hakim berpendapat tidak perlu menjat…  │
│    71 │     2 │ 71            │ 1            │               │ Pidana denda sebagaimana dimaksud pada ayat (1) hanya dapat dijatuhkan jika:                                                                              │
│    71 │     3 │ 71            │ 1            │               │ Pidana denda yang dapat dijatuhkan berdasarkan ketentuan sebagaimana dimaksud pada ayat (1) adalah pidana denda paling banyak kategori V dan pidana den…  │
│    71 │     4 │ 71            │ 2            │ c             │ Ketentuan sebagaimana dimaksud pada ayat (2) huruf c tidak berlaku bagi orang yang pernah dijatuhi pidana penjara untuk Tindak Pidana yang dilakukan se…  │
└───────┴───────┴───────────────┴──────────────┴───────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

KUHP - HURUF.tsv
┌───────┬───────┬─────────┬───────────────┬──────────────┬───────────────┬─────────────────────────────────────┐
│ pasal │ ayat  │  huruf  │ pasal_rujukan │ ayat_rujukan │ huruf_rujukan │                teks                 │
│ int64 │ int64 │ varchar │    varchar    │   varchar    │    varchar    │               varchar               │
├───────┼───────┼─────────┼───────────────┼──────────────┼───────────────┼─────────────────────────────────────┤
│    71 │     2 │ a       │               │              │               │ tanpa Korban;                       │
│    71 │     2 │ b       │               │              │               │ Korban tidak mempermasalahkan; atau │
│    71 │     2 │ c       │               │              │               │ bukan pengulangan Tindak Pidana.    │
└───────┴───────┴─────────┴───────────────┴──────────────┴───────────────┴─────────────────────────────────────┘

```
### Pasal Rujukan

Pasal 71 ayat (1) merujuk ke "Pasal 51 sampai dengan Pasal 54", sehingga baris pertama kolom `pasal_rujukan` dari pertama berisi `'51,52,53,54'`.

### Ayat Rujukan

Pasal 71 ayat (2) merujuk ke ayat (1) Pasal yang sama, sehingga baris ketiga kolom `ayat_rujukan` dari tabel pertama berisi `'1'`.

### Huruf Rujukan
Pasal 71 ayat (4) merujuk ke ayat (2) huruf c Pasal yang sama, sehingga baris keempat kolom `huruf_rujukan` dari tabel pertama berisi `c`.

## Contoh

```sql
-- Mengubah kolom `*_rujukan` ke format baris
SELECT 
    pasal, 
    ayat, 
    unnest(string_split(pasal_rujukan, ','))::int AS pasal_rujukan
FROM read_csv_auto('./KUHP - AYAT.tsv') 
WHERE pasal = 71;
```

```
┌───────┬───────┬───────────────┐
│ pasal │ ayat  │ pasal_rujukan │
│ int64 │ int64 │     int32     │
├───────┼───────┼───────────────┤
│    71 │     1 │            51 │
│    71 │     1 │            52 │
│    71 │     1 │            53 │
│    71 │     1 │            54 │
│    71 │     2 │            71 │
│    71 │     3 │            71 │
│    71 │     4 │            71 │
└───────┴───────┴───────────────┘
```