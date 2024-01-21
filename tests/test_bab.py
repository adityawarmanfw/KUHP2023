import duckdb

con = duckdb.connect()
con.sql("""
            CREATE TABLE kuhp_bab AS (
                SELECT *
                FROM read_csv_auto('././KUHP - BAB.tsv', sep='\t')
            );
        """)


def test_kolom():
    """
    Pastikan hanya ada kolom ['bab','buku','pasal_akhir','pasal_awal','teks'].
    """
    result = con.sql("""
                        SELECT 
                            LIST(DISTINCT column_name ORDER BY column_name) = ['bab','buku','pasal_akhir','pasal_awal','teks']
                        FROM information_schema.columns WHERE table_name = 'kuhp_bab';
                    """).fetchone()[0]
    assert result


def test_pasal_konsekutif():
    """
    Pastikan rentang pasal awal dan akhir konsekutif dengan baris selanjutnya.
    """
    result = con.sql(
        "SELECT bool_and(konsekutif) FROM (SELECT pasal_awal - LAG(pasal_akhir) OVER (ORDER BY pasal_akhir) = 1 AS konsekutif FROM kuhp_bab);").fetchone()[0]
    assert result


def test_jumlah_pasal():
    """
    Pastikan jumlah pasal 624.
    """
    result = con.sql("""
                        SELECT count(pasal) = 624
                        FROM (SELECT unnest(generate_series(pasal_awal, pasal_akhir)) AS pasal FROM kuhp_bab)
                    """).fetchone()[0]
    assert result
