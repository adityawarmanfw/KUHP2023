import duckdb

con = duckdb.connect()
con.sql("""
            CREATE TABLE kuhp_buku AS (
                SELECT *
                FROM read_csv_auto('././KUHP - BUKU.tsv', sep='\t')
            );
        """)


def test_kolom():
    """
    Pastikan hanya ada kolom ['buku','teks'].
    """
    result = con.sql("""
                        SELECT 
                            LIST(DISTINCT column_name ORDER BY column_name) = ['buku','teks']
                        FROM information_schema.columns WHERE table_name = 'kuhp_buku';
                    """).fetchone()[0]
    assert result


def test_jumlah_baris():
    """
    Pastikan hanya ada 2 baris.
    """
    result = con.sql(
        "SELECT count(*) = 2 FROM kuhp_buku;").fetchone()[0]
    assert result
