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
    Pastikan hanya ada kolom ['ayat', 'ayat_rujukan', 'bab','buku', 'huruf_rujukan', 'pasal', 'pasal_rujukan', 'teks'] 
    """
    result = con.sql("""
                        SELECT 
                            LIST(DISTINCT k ORDER BY k) = ['ayat', 'ayat_rujukan', 'bab','buku', 'huruf_rujukan', 'pasal', 'pasal_rujukan', 'teks'] 
                        FROM (UNPIVOT kuhp_ayat ON * INTO NAME k VALUE v);
                    """).fetchone()[0]
    assert result == True


def test_pasal_tidak_null():
    """
    Pastikan nilai dalam kolom 'pasal' tidak null.
    """
    result = con.sql(
        "SELECT bool_and(pasal IS NOT NULL) FROM kuhp_ayat;").fetchone()[0]
    assert result == True


def test_ayat_lebih_dari_sama_dengan_nol():
    """
    Pastikan nilai dalam kolom 'ayat' lebih dari atau sama dengan nol.
    """
    result = con.sql(
        "SELECT bool_and(ayat >= 0) FROM kuhp_ayat;").fetchone()[0]
    assert result == True
