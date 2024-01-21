import duckdb

con = duckdb.connect()
con.sql("""
            CREATE TABLE kuhp_ayat AS (
                SELECT *
                FROM read_csv_auto('././KUHP - AYAT.tsv', sep='\t')
            );
        """)


def test_kolom():
    """
    Pastikan hanya ada kolom ['ayat','ayat_rujukan','huruf_rujukan','pasal','pasal_rujukan','teks'].
    """
    result = con.sql("""
                        SELECT 
                            LIST(DISTINCT column_name ORDER BY column_name) = ['ayat','ayat_rujukan','huruf_rujukan','pasal','pasal_rujukan','teks']
                        FROM information_schema.columns WHERE table_name = 'kuhp_ayat';
                    """).fetchone()[0]
    assert result


def test_pasal_tidak_null():
    """
    Pastikan nilai dalam kolom 'pasal' tidak null.
    """
    result = con.sql(
        "SELECT bool_and(pasal IS NOT NULL) FROM kuhp_ayat;").fetchone()[0]
    assert result


def test_ayat_lebih_dari_sama_dengan_nol():
    """
    Pastikan nilai dalam kolom 'ayat' lebih dari atau sama dengan nol.
    """
    result = con.sql(
        "SELECT bool_and(ayat >= 0) FROM kuhp_ayat;").fetchone()[0]
    assert result


def test_pasal_rujukan_tidak_null():
    """
    Pastikan nilai dalam kolom 'pasal_rujukan' tidak null jika ada kata 'Pasal' pada kolom 'teks'.

    Cari baris bermasalah dengan kueri:

        SELECT pasal, ayat
        FROM kuhp_ayat
        WHERE regexp_matches(teks, 'Pasal') 
            AND pasal_rujukan IS NULL;
    """
    result = con.sql(
        "SELECT bool_and(if(regexp_matches(teks, 'Pasal'), pasal_rujukan IS NOT NULL, NULL)) FROM kuhp_ayat;").fetchone()[0]
    assert result


def test_pasal_dan_ayat_rujukan_tidak_null():
    """
    Pastikan nilai dalam kolom 'pasal_rujukan' dan 'ayat_rujukan' tidak null jika ada kata 'ayat (' pada kolom 'teks'.

    Cari baris bermasalah dengan kueri:

        SELECT pasal, ayat 
        FROM kuhp_ayat
        WHERE (regexp_matches(teks, 'ayat \(') AND ayat_rujukan IS NULL)
            OR (regexp_matches(teks, 'ayat \(') AND pasal_rujukan IS NULL);
    """
    result = con.sql(
        "SELECT bool_and(if(regexp_matches(teks, 'ayat \('), pasal_rujukan IS NOT NULL AND ayat_rujukan IS NOT NULL, NULL)) FROM kuhp_ayat;").fetchone()[0]
    assert result


def test_huruf_rujukan_bernilai_huruf_kecil_dan_koma():
    """
    Pastikan nilai dalam kolom 'huruf_rujukan' hanya berisi huruf kecil dan koma.
    """
    result = con.sql(
        "SELECT bool_and(regexp_full_match(huruf_rujukan, '[a-z,]+')) FROM kuhp_ayat;").fetchone()[0]
    assert result


def test_tidak_ada_spasi_setelah_koma_di_pasal_rujukan():
    """
    Pastikan tidak ada spasi setelah koma dalam kolom 'pasal_rujukan'.
    """
    result = con.sql(
        "SELECT bool_and(regexp_matches(pasal_rujukan, '[0-9\,\s]')) FROM kuhp_ayat;").fetchone()[0]
    assert result


def test_tidak_ada_spasi_setelah_koma_di_ayat_rujukan():
    """
    Pastikan tidak ada spasi setelah koma dalam kolom 'ayat_rujukan'.
    """
    result = con.sql(
        "SELECT bool_and(regexp_matches(ayat_rujukan, '[0-9\,\s]')) FROM kuhp_ayat;").fetchone()[0]
    assert result


def test_tidak_ada_spasi_setelah_koma_di_huruf_rujukan():
    """
    Pastikan tidak ada spasi setelah koma dalam kolom 'huruf_rujukan'.
    """
    result = con.sql(
        "SELECT bool_and(regexp_matches(huruf_rujukan, '[^\,\s]')) FROM kuhp_ayat;").fetchone()[0]
    assert result
