import pandas as pd

def adapt_dataset(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Normalize column names
    df.columns = [col.lower().strip() for col in df.columns]

    # Mapping dictionary
    column_map = {
        "date": ["date", "order date", "timestamp"],
        "revenue": ["revenue", "sales", "amount"],
        "profit": ["profit", "margin"],
        "region": ["region", "country", "location"],
        "units_sold": ["units", "quantity", "qty"]
    }

    mapped = {}

    for target, options in column_map.items():
        for opt in options:
            if opt in df.columns:
                mapped[target] = opt
                break

    # Rename detected columns
    df = df.rename(columns={v: k for k, v in mapped.items()})

    # Handle missing required columns
    if "date" not in df:
        raise ValueError("No date column detected")

    if "revenue" not in df:
        raise ValueError("No revenue/sales column detected")

    # Convert date
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Add missing fields
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
