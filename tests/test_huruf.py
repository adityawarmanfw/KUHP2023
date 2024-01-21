import duckdb

con = duckdb.connect()
con.sql("""
            CREATE TABLE kuhp_huruf AS (
                SELECT *
                FROM read_csv_auto('././KUHP - HURUF.tsv', sep='\t')
            );
        """)


def test_kolom():
    """
    Pastikan hanya ada kolom ['ayat','ayat_rujukan','huruf','huruf_rujukan','pasal','pasal_rujukan','teks'].
    """
    result = con.sql("""
                        SELECT 
                            LIST(DISTINCT column_name ORDER BY column_name) = ['ayat','ayat_rujukan','huruf','huruf_rujukan','pasal','pasal_rujukan','teks']
                        FROM information_schema.columns WHERE table_name = 'kuhp_huruf';
                    """).fetchone()[0]
    assert result


def test_huruf_tidak_null():
    """
    Pastikan nilai dalam kolom 'huruf' tidak null.
    """
    result = con.sql(
        "SELECT bool_and(huruf IS NOT NULL) FROM kuhp_huruf;").fetchone()[0]
    assert result


def test_huruf_bernilai_huruf_kecil():
    """
    Pastikan nilai dalam kolom 'huruf' hanya berisi huruf kecil.
    """
    result = con.sql(
        "SELECT bool_and(regexp_full_match(huruf, '[a-z]+')) FROM kuhp_huruf;").fetchone()[0]
    assert result


def test_ayat_lebih_dari_sama_dengan_nol():
    """
    Pastikan nilai dalam kolom 'ayat' lebih dari atau sama dengan nol.
    """
    result = con.sql(
        "SELECT bool_and(ayat >= 0) FROM kuhp_huruf;").fetchone()[0]
    assert result
