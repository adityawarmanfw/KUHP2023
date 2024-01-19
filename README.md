# Kitab Undang-undang Hukum Pidana (KUHP) 2023 (UU No. 1 Tahun 2023)

Masih dalam pengerjaan.

```sql
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
```