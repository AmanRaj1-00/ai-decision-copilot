import pandas as pd


def detect_revenue_drop(df: pd.DataFrame, threshold=0.1):
    """
    Detect revenue drops greater than threshold (default 10%)
    """
    df = df.sort_values("month")

    df["prev_revenue"] = df.groupby("region")["revenue"].shift(1)

    df["change_pct"] = (df["revenue"] - df["prev_revenue"]) / df["prev_revenue"]

    drops = df[df["change_pct"] < -threshold]

    signals = []

    for _, row in drops.iterrows():
        signals.append({
            "type": "revenue_drop",
            "region": row["region"],
            "month": str(row["month"]),
            "change_pct": round(row["change_pct"], 2)
        })

    return signals
