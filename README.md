# Kitab Undang-undang Hukum Pidana (KUHP) 2023 (UU No. 1 Tahun 2023)

Masih dalam pengerjaan.

Sumber file: https://peraturan.bpk.go.id/Details/234935/uu-no-1-tahun-2023

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
┌───────┬───────┬───────┬───────┬───────────────┬──────────────┬───────────────┬───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ buku  │  bab  │ pasal │ ayat  │ pasal_rujukan │ ayat_rujukan │ huruf_rujukan │                                                                   teks                                                                    │
│ int64 │ int64 │ int64 │ int64 │    varchar    │   varchar    │    varchar    │                                                                  varchar                                                                  │
├───────┼───────┼───────┼───────┼───────────────┼──────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│     1 │     3 │    71 │     1 │ 51,52,53,54   │              │               │ Jika seseorang melakukan Tindak Pidana yang hanya diancam dengan pidana penjara di bawah 5 (lima) tahun, sedangkan hakim berpendapat ti…  │
│     1 │     3 │    71 │     2 │ 71            │ 1            │               │ Pidana denda sebagaimana dimaksud pada ayat (1) hanya dapat dijatuhkan jika:                                                              │
│     1 │     3 │    71 │     3 │ 71            │ 1            │               │ Pidana denda yang dapat dijatuhkan berdasarkan ketentuan sebagaimana dimaksud pada ayat (1) adalah pidana denda paling banyak kategori …  │
│     1 │     3 │    71 │     4 │ 71            │ 2            │ c             │ Ketentuan sebagaimana dimaksud pada ayat (2) huruf c tidak berlaku bagi orang yang pernah dijatuhi pidana penjara untuk Tindak Pidana y…  │
└───────┴───────┴───────┴───────┴───────────────┴──────────────┴───────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

KUHP - HURUF.tsv
┌───────┬───────┬─────────┬─────────────────────────────────────┐
│ pasal │ ayat  │  huruf  │                teks                 │
│ int64 │ int64 │ varchar │               varchar               │
├───────┼───────┼─────────┼─────────────────────────────────────┤
│    71 │     2 │ a       │ tanpa Korban;                       │
│    71 │     2 │ b       │ Korban tidak mempermasalahkan; atau │
│    71 │     2 │ c       │ bukan pengulangan Tindak Pidana.    │
└───────┴───────┴─────────┴─────────────────────────────────────┘

```
### Pasal Rujukan

Pasal 71 ayat (1) merujuk ke "Pasal 51 sampai dengan Pasal 54", sehingga baris pertama kolom `pasal_rujukan` dari pertama berisi `'51,52,53,54'`.

### Ayat Rujukan

Pasal 71 ayat (2) merujuk ke ayat (1) Pasal yang sama, sehingga baris ketiga kolom `ayat_rujukan` dari tabel pertama berisi `'1'`.

### Huruf Rujukan
Pasal 71 ayat (4) merujuk ke ayat (2) huruf c Pasal yang sama, sehingga baris keempat kolom `huruf_rujukan` dari tabel pertama berisi `c`.

## Contoh tabel AYAT dan HURUF

```
-- Baca dengan DuckDB
D SELECT * FROM read_csv_auto('./KUHP - AYAT.tsv') LIMIT 5;
┌───────┬───────┬───────┬───────┬───────────────┬──────────────┬───────────────┬───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ buku  │  bab  │ pasal │ ayat  │ pasal_rujukan │ ayat_rujukan │ huruf_rujukan │                                                                   teks                                                                    │
│ int64 │ int64 │ int64 │ int64 │    varchar    │   varchar    │    varchar    │                                                                  varchar                                                                  │
├───────┼───────┼───────┼───────┼───────────────┼──────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│     1 │     1 │     1 │     1 │               │              │               │ Tidak ada satu perbuatan pun yang dapat dikenai sanksi pidana dan/atau tindakan, kecuali atas kekuatan peraturan pidana dalam peraturan…  │
│     1 │     1 │     1 │     2 │               │              │               │ Dalam menetapkan adanya Tindak Pidana dilarang digunakan analogi.                                                                         │
│     1 │     1 │     2 │     1 │ 1             │ 1            │               │ Ketentuan sebagaimana dimaksud dalam Pasal 1 ayat (1) tidak mengurangi berlakunya hukum yang hidup dalam masyarakat yang menentukan bah…  │
│     1 │     1 │     2 │     2 │ 2             │ 1            │               │ Hukum yang hidup dalam masyarakat sebagaimana dimaksud pada ayat (1) berlaku dalam tempat hukum itu hidup dan sepanjang tidak diatur da…  │
│     1 │     1 │     2 │     3 │               │              │               │ Ketentuan mengenai tata cara dan kriteria penetapan hukum yang hidup dalam masyarakat diatur dengan Peraturan Pemerintah.                 │
└───────┴───────┴───────┴───────┴───────────────┴──────────────┴───────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

D SELECT * FROM read_csv_auto('./KUHP - HURUF.tsv') LIMIT 5;
┌───────┬───────┬─────────┬────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ pasal │ ayat  │  huruf  │                                                                                              teks                                                                                              │
│ int64 │ int64 │ varchar │                                                                                            varchar                                                                                             │
├───────┼───────┼─────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│     4 │     0 │ a       │ Tindak Pidana di wilayah Negara Kesatuan Republik Indonesia;                                                                                                                                   │
│     4 │     0 │ b       │ Tindak Pidana di Kapal Indonesia atau di Pesawat Udara Indonesia; atau                                                                                                                         │
│     4 │     0 │ c       │ Tindak Pidana di bidang teknologi informasi atau Tindak Pidana lainnya yang akibatnya dialami atau terjadi di wilayah Negara Kesatuan Republik Indonesia atau di Kapal Indonesia dan di Pesa…  │
│     5 │     0 │ a       │ keamanan negara atau proses kehidupan ketatanegaraan;                                                                                                                                          │
│     5 │     0 │ b       │ martabat Presiden, Wakil Presiden, dan/atau Pejabat Indonesia di luar negeri;                                                                                                                  │
└───────┴───────┴─────────┴────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

-- Mengubah kolom `*_rujukan` ke format baris
D SELECT 
>     pasal, 
>     ayat, 
>     unnest(string_split(pasal_rujukan, ',')):int AS pasal_rujukan
> FROM read_csv_auto('./KUHP - AYAT.tsv') 
> WHERE pasal = 71;
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