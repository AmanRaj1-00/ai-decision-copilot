import pandas as pd

def adapt_dataset(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Normalize column names (stronger)
    df.columns = [col.lower().strip().replace("_", " ") for col in df.columns]

    # Helper function for flexible matching
    def find_column(possible_names):
        for col in df.columns:
            for name in possible_names:
                if name in col:
                    return col
        return None

    # Detect columns
    date_col = find_column(["date", "order"])
    revenue_col = find_column(["revenue", "sales", "amount"])
    profit_col = find_column(["profit", "margin"])
    region_col = find_column(["region", "country", "location"])
    units_col = find_column(["units", "quantity", "qty"])

    # Validate required columns
    if not date_col:
        raise ValueError(f"No date column detected. Found columns: {df.columns.tolist()}")

    if not revenue_col:
        raise ValueError(f"No revenue/sales column detected. Found columns: {df.columns.tolist()}")

    # Rename
    df = df.rename(columns={
        date_col: "date",
        revenue_col: "revenue"
    })

    if profit_col:
        df = df.rename(columns={profit_col: "profit"})
    if region_col:
        df = df.rename(columns={region_col: "region"})
    if units_col:
        df = df.rename(columns={units_col: "units_sold"})

    # Convert date
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Fill missing
    if "region" not in df:
        df["region"] = "Unknown"

    if "units_sold" not in df:
        df["units_sold"] = 1

    if "profit" not in df:
        df["profit"] = df["revenue"] * 0.3

    if "cost" not in df:
        df["cost"] = df["revenue"] - df["profit"]

    if "product_id" not in df:
        df["product_id"] = "P1"

    if "promotion_flag" not in df:
        df["promotion_flag"] = 0

    return df
