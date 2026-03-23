from app.etl import load_sales, clean_sales


def test_load_and_clean():
    df = load_sales("data/raw/sales.csv")
    df_clean = clean_sales(df)

    assert not df_clean.empty
    assert "profit" in df_clean.columns
