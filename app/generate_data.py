import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_sales_data(days=365):
    np.random.seed(42)

    start_date = datetime(2023, 1, 1)
    regions = ["North", "South", "East", "West"]
    products = ["P1", "P2", "P3"]

    data = []

    for day in range(days):
        date = start_date + timedelta(days=day)

        for region in regions:
            for product in products:
                base_demand = np.random.randint(20, 50)

                seasonal_factor = 1 + 0.2 * np.sin(day / 30)
                noise = np.random.normal(0, 5)

                units = max(0, int(base_demand * seasonal_factor + noise))

                price = np.random.uniform(10, 20)
                revenue = units * price
                cost = revenue * np.random.uniform(0.5, 0.7)

                promo = np.random.choice([0, 1], p=[0.8, 0.2])

                data.append([
                    date.strftime("%Y-%m-%d"),
                    region,
                    product,
                    units,
                    round(revenue, 2),
                    round(cost, 2),
                    promo
                ])

    df = pd.DataFrame(data, columns=[
        "date", "region", "product_id",
        "units_sold", "revenue", "cost", "promotion_flag"
    ])

    return df


if __name__ == "__main__":
    df = generate_sales_data()
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/sales.csv", index=False)
    print("✅ Sales data generated successfully!")
