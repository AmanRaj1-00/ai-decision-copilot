import pandas as pd


def load_sales(filepath: str) -> pd.DataFrame:
    """
    Load raw sales data
    """
    df = pd.read_csv(filepath, parse_dates=["date"])
    return df


def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and validate sales data
    """
    df = df.copy()

    # Remove invalid values
    df = df[df["units_sold"] >= 0]

    # Ensure correct types
    df["revenue"] = df["revenue"].astype(float)
    df["cost"] = df["cost"].astype(float)

    # Add profit column (important for decisions later)
    df["profit"] = df["revenue"] - df["cost"]

    return df


def aggregate_monthly(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate data monthly by region
    """
    df["month"] = df["date"].dt.to_period("M")

    monthly = (
        df.groupby(["month", "region"])
        .agg({
            "revenue": "sum",
            "cost": "sum",
            "profit": "sum"
        })
        .reset_index()
    )

    return monthly
