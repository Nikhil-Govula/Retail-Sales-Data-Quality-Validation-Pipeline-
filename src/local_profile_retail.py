import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw/retail_store_sales_dirty.csv")

def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Missing file: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    print("=== Shape ===")
    print(df.shape)

    print("\n=== Columns ===")
    print(df.dtypes)

    print("\n=== Sample rows ===")
    print(df.head(10))

    print("\n=== Null counts ===")
    print(df.isna().sum())

    print("\n=== Basic summary (numeric) ===")
    print(df.describe(include="number"))

    print("\n=== Value counts for some key columns ===")
    for col in ["store_id", "product_id", "payment_method", "location"]:
        if col in df.columns:
            print(f"\n-- {col} --")
            print(df[col].value_counts(dropna=False).head(10))

if __name__ == "__main__":
    main()
