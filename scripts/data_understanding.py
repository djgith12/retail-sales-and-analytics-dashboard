import pandas as pd
from load_data import load_raw_data


def data_understanding():

    # Load dataset
    df = load_raw_data()

    print("\n" + "=" * 80)
    print("DATA UNDERSTANDING REPORT")
    print("=" * 80)
    # ==========================================================
    # 1. DATASET OVERVIEW
    # ==========================================================
    print("\n1. DATASET OVERVIEW")
    print("-" * 80)

    print(f"Number of Rows: {df.shape[0]}")
    print(f"Number of Columns: {df.shape[1]}")

    print("\nColumn Names:")
    print(df.columns.tolist())

    # ==========================================================
    # 2. DATA TYPES
    # ==========================================================
    print("\n2. DATA TYPES")
    print("-" * 80)

    print(df.dtypes)

    print("\nDataset Information:")
    df.info()

    # ==========================================================
    # 3. DATA PREVIEW
    # ==========================================================
    print("\n3. FIRST 5 ROWS")
    print("-" * 80)
    print(df.head())

    print("\n4. LAST 5 ROWS")
    print("-" * 80)
    print(df.tail())

    # ==========================================================
    # 4. DESCRIPTIVE STATISTICS
    # ==========================================================
    print("\n5. DESCRIPTIVE STATISTICS")
    print("-" * 80)
    print(df.describe())

    # ==========================================================
    # 5. MISSING VALUE ANALYSIS
    # ==========================================================
    print("\n6. MISSING VALUE ANALYSIS")
    print("-" * 80)

    missing_values = df.isnull().sum()

    print(missing_values)

    total_missing = missing_values.sum()

    print(f"\nTotal Missing Values: {total_missing}")

    # ==========================================================
    # 6. DUPLICATE ANALYSIS
    # ==========================================================
    print("\n7. DUPLICATE ANALYSIS")
    print("-" * 80)

    duplicate_count = df.duplicated().sum()

    print(f"Duplicate Rows: {duplicate_count}")

    # ==========================================================
    # 7. UNIQUE VALUE ANALYSIS
    # ==========================================================
    print("\n8. UNIQUE VALUE ANALYSIS")
    print("-" * 80)

    print(df.nunique())

    # ==========================================================
    # 8. CATEGORICAL VARIABLE EXPLORATION
    # ==========================================================
    print("\n9. CATEGORICAL VARIABLE EXPLORATION")
    print("-" * 80)

    categorical_columns = [
        "sku",
        "brand",
        "segment",
        "category",
        "channel",
        "region",
        "pack_type"
    ]

    for col in categorical_columns:
        if col in df.columns:
            print(f"\nTop values for '{col}':")
            print(df[col].value_counts().head(10))

    # ==========================================================
    # 9. NUMERICAL VARIABLE EXPLORATION
    # ==========================================================
    print("\n10. NUMERICAL VARIABLE EXPLORATION")
    print("-" * 80)

    numerical_columns = [
        "price_unit",
        "delivery_days",
        "stock_available",
        "delivered_qty",
        "units_sold"
    ]

    existing_numeric_cols = [
        col for col in numerical_columns if col in df.columns
    ]

    print(df[existing_numeric_cols].describe())

    # ==========================================================
    # 10. NEGATIVE VALUE CHECK
    # ==========================================================
    print("\n11. NEGATIVE VALUE CHECK")
    print("-" * 80)

    for col in existing_numeric_cols:
        negative_count = (df[col] < 0).sum()
        print(f"{col}: {negative_count} negative values")

    # ==========================================================
    # 11. STOCK-OUT ANALYSIS
    # ==========================================================
    print("\n12. STOCK-OUT ANALYSIS")
    print("-" * 80)

    if "stock_available" in df.columns:
        stock_outs = (df["stock_available"] == 0).sum()
        print(f"Stock-out Records: {stock_outs}")

    # ==========================================================
    # 12. PROMOTION DISTRIBUTION
    # ==========================================================
    print("\n13. PROMOTION DISTRIBUTION")
    print("-" * 80)

    if "promotion_flag" in df.columns:
        print(df["promotion_flag"].value_counts())

    # ==========================================================
    # 13. CORRELATION ANALYSIS
    # ==========================================================
    print("\n14. CORRELATION ANALYSIS")
    print("-" * 80)

    correlation_matrix = df[existing_numeric_cols].corr()

    print(correlation_matrix)

    # ==========================================================
    # 14. INITIAL DATA QUALITY ASSESSMENT
    # ==========================================================
    print("\n15. INITIAL DATA QUALITY ASSESSMENT")
    print("-" * 80)

    print("Check the following manually:")
    print("• Incorrect data types")
    print("• Missing values")
    print("• Duplicate rows")
    print("• Negative values")
    print("• Outliers")
    print("• Inconsistent category names")

    print("\n" + "=" * 80)
    print("DATA UNDERSTANDING COMPLETED")
    print("=" * 80)

    return df


if __name__ == "__main__":
    data_understanding()
