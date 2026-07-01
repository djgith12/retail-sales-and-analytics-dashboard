import pandas as pd
from load_data import load_raw_data


def feature_engineering():

    # Load cleaned/raw data
    df = load_raw_data()

    print("\n" + "=" * 80)
    print("FEATURE ENGINEERING")
    print("=" * 80)

    # ==========================================================
    # 1. STANDARDIZE COLUMN NAMES (safety step)
    # ==========================================================
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # ==========================================================
    # 2. REVENUE CALCULATION (MOST IMPORTANT KPI)
    # ==========================================================
    print("\n1. Creating Revenue column...")

    if "price_unit" in df.columns and "units_sold" in df.columns:
        df["revenue"] = df["price_unit"] * df["units_sold"]

    # ==========================================================
    # 3. DATE-BASED FEATURES
    # ==========================================================
    print("\n2. Creating time-based features...")

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month_name()
        df["month_number"] = df["date"].dt.month
        df["day"] = df["date"].dt.day

    # ==========================================================
    # 4. PROMOTION FEATURE
    # ==========================================================
    print("\n3. Creating promotion category...")

    if "promotion_flag" in df.columns:
        df["promotion_category"] = df["promotion_flag"].map({
            1: "Promoted",
            0: "Non-Promoted"
        })

    # ==========================================================
    # 5. STOCK UTILIZATION (DEMAND EFFICIENCY)
    # ==========================================================
    print("\n4. Creating stock utilization...")

    if "stock_available" in df.columns and "units_sold" in df.columns:
        df["stock_utilization"] = df["units_sold"] / df["stock_available"]

        # Avoid infinity values
        df["stock_utilization"] = df["stock_utilization"].replace([float("inf")], 0)

    # ==========================================================
    # 6. DELIVERY PERFORMANCE CATEGORY
    # ==========================================================
    print("\n5. Creating delivery performance category...")

    if "delivery_days" in df.columns:
        df["delivery_performance"] = pd.cut(
            df["delivery_days"],
            bins=[-1, 2, 5, 10, 100],
            labels=["Fast", "Moderate", "Slow", "Very Slow"]
        )

    # ==========================================================
    # 7. PRICE SEGMENTATION
    # ==========================================================
    print("\n6. Creating price segment...")

    if "price_unit" in df.columns:
        df["price_segment"] = pd.cut(
            df["price_unit"],
            bins=3,
            labels=["Low", "Medium", "High"]
        )

    # ==========================================================
    # 8. DEMAND FLAG (HIGH / LOW SALES)
    # ==========================================================
    print("\n7. Creating demand flag...")

    if "units_sold" in df.columns:
        threshold = df["units_sold"].median()

        df["demand_level"] = df["units_sold"].apply(
            lambda x: "High Demand" if x >= threshold else "Low Demand"
        )

    # ==========================================================
    # 9. TOTAL COST / REVENUE CHECK (OPTIONAL KPI VALIDATION)
    # ==========================================================
    print("\n8. Creating revenue validation column...")

    if "revenue" in df.columns:
        df["log_revenue"] = df["revenue"].apply(
            lambda x: None if x <= 0 else x
        )

    # ==========================================================
    # 10. FINAL SUMMARY
    # ==========================================================
    print("\nFEATURE ENGINEERING COMPLETED")

    print("\nNew Columns Added:")
    new_columns = [
        "revenue",
        "year",
        "month",
        "month_number",
        "day",
        "promotion_category",
        "stock_utilization",
        "delivery_performance",
        "price_segment",
        "demand_level"
    ]

    for col in new_columns:
        if col in df.columns:
            print(f"✔ {col}")

    # ==========================================================
    # 11. SAVE OUTPUT
    # ==========================================================
    output_path = "data/feature_engineered_data.csv"
    df.to_csv(output_path, index=False)

    print(f"\nFeature engineered dataset saved at: {output_path}")

    print("\n" + "=" * 80)
    print("DONE")
    print("=" * 80)

    return df


if __name__ == "__main__":
    feature_engineering() 
