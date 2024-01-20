import duckdb

con = duckdb.connect()
con.sql("""
        CREATE TABLE kuhp_ayat AS (
            SELECT *
            FROM read_csv_auto('././KUHP - AYAT.tsv', sep='\t')
        );
        """)

def test_ayat_lebih_dari_sama_dengan_nol():
    """
    Cek nilai dalam kolom 'ayat' lebih dari atau sama dengan nol.
    """
    result = con.sql("SELECT bool_and(ayat >= 0) FROM kuhp_ayat;").fetchone()[0]
    assert result == True