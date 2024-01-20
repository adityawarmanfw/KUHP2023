import duckdb

con = duckdb.connect()
con.sql("""
        CREATE TABLE kuhp_ayat AS (
            SELECT *
            FROM read_csv_auto('././KUHP - AYAT.tsv', sep='\t')
        );
        """)

def test_ayat_more_than_or_equal_to_zero():
    """
    Test whether all values in the 'ayat' column are greater than or equal to zero.
    """
    result = con.sql("SELECT bool_and(ayat >= 0) FROM kuhp_ayat;").fetchone()[0]
    assert result == True