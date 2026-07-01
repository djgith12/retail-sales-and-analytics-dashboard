import pandas as pd
from load_data import load_raw_data


def data_cleaning():

    # Load raw data
    df = load_raw_data()

    print("\n" + "=" * 80)
    print("DATA CLEANING & VALIDATION")
    print("=" * 80)

    # ==========================================================
    # 1. STANDARDIZE COLUMN NAMES
    # ==========================================================
    print("\n1. Standardizing column names...")

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    print("Column names standardized.")

    # ==========================================================
    # 2. DATA TYPE CONVERSION
    # ==========================================================
    print("\n2. Converting data types...")

    # Date conversion
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Numeric conversion
    numeric_cols = [
        "price_unit",
        "delivery_days",
        "stock_available",
        "delivered_qty",
        "units_sold"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    print("Data types converted.")

    # ==========================================================
    # 3. MISSING VALUE HANDLING
    # ==========================================================
    print("\n3. Handling missing values...")

    missing_before = df.isnull().sum().sum()

    # Fill numeric missing values with median
    for col in numeric_cols:
        if col in df.columns:
            df[col].fillna(df[col].median(), inplace=True)

    # Fill categorical missing values with mode
    categorical_cols = [
        "sku", "brand", "segment", "category",
        "channel", "region", "pack_type"
    ]

    for col in categorical_cols:
        if col in df.columns:
            df[col].fillna(df[col].mode()[0], inplace=True)

    missing_after = df.isnull().sum().sum()

    print(f"Missing values before: {missing_before}")
    print(f"Missing values after: {missing_after}")

    # ==========================================================
    # 4. REMOVE DUPLICATES
    # ==========================================================
    print("\n4. Removing duplicates...")

    duplicates_before = df.duplicated().sum()
    df = df.drop_duplicates()

    print(f"Duplicate rows removed: {duplicates_before}")

    # ==========================================================
    # 5. TRIM & STANDARDIZE TEXT COLUMNS
    # ==========================================================
    print("\n5. Cleaning categorical text values...")

    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.title()

    print("Text columns cleaned.")

    # ==========================================================
    # 6. HANDLE INVALID VALUES
    # ==========================================================
    print("\n6. Removing invalid values...")

    initial_rows = df.shape[0]

    if "price_unit" in df.columns:
        df = df[df["price_unit"] >= 0]

    if "delivery_days" in df.columns:
        df = df[df["delivery_days"] >= 0]

    if "units_sold" in df.columns:
        df = df[df["units_sold"] >= 0]

    final_rows = df.shape[0]

    print(f"Rows before: {initial_rows}")
    print(f"Rows after: {final_rows}")
    print(f"Rows removed: {initial_rows - final_rows}")

    # ==========================================================
    # 7. OUTLIER CHECK SUMMARY
    # ==========================================================
    print("\n7. Outlier summary (basic check)...")

    if "price_unit" in df.columns:
        print("Price range:")
        print(df["price_unit"].describe())

    if "units_sold" in df.columns:
        print("\nUnits sold range:")
        print(df["units_sold"].describe())

    # ==========================================================
    # 8. FEATURE PREPARATION (BASIC)
    # ==========================================================
    print("\n8. Creating basic features...")

    if "price_unit" in df.columns and "units_sold" in df.columns:
        df["revenue"] = df["price_unit"] * df["units_sold"]

    if "date" in df.columns:
        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month_name()

    if "promotion_flag" in df.columns:
        df["promotion_category"] = df["promotion_flag"].map({
            1: "Promoted",
            0: "Non-Promoted"
        })

    print("Basic features created.")

    # ==========================================================
    # 9. VALIDATION CHECKS
    # ==========================================================
    print("\n9. Data validation checks...")

    if "units_sold" in df.columns and "delivered_qty" in df.columns:
        invalid_sales = (df["units_sold"] > df["delivered_qty"]).sum()
        print(f"Invalid sales records (units_sold > delivered_qty): {invalid_sales}")

    if "stock_available" in df.columns:
        stock_outs = (df["stock_available"] == 0).sum()
        print(f"Stock-out records: {stock_outs}")

    # ==========================================================
    # 10. SAVE CLEANED DATA
    # ==========================================================
    print("\n10. Saving cleaned dataset...")

    output_path = "data/cleaned_sales_data.csv"
    df.to_csv(output_path, index=False)

    print(f"Cleaned dataset saved at: {output_path}")

    print("\n" + "=" * 80)
    print("DATA CLEANING COMPLETED")
    print("=" * 80)

    return df


if __name__ == "__main__":
    data_cleaning()
