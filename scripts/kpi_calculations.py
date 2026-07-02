import pandas as pd
from load_data import load_raw_data


def calculate_kpis():

    # Load data
    df = load_raw_data()

    print("\n" + "=" * 80)
    print("KPI DEVELOPMENT")
    print("=" * 80)

    # ==========================================================
    # BASIC PREPARATION
    # ==========================================================
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Ensure correct data types
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    numeric_cols = [
        "price_unit",
        "units_sold",
        "stock_available",
        "delivery_days"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # ==========================================================
    # CREATE REVENUE (CORE KPI INPUT)
    # ==========================================================
    if "price_unit" in df.columns and "units_sold" in df.columns:
        df["revenue"] = df["price_unit"] * df["units_sold"]

    # ==========================================================
    # 1. TOTAL REVENUE
    # ==========================================================
    total_revenue = df["revenue"].sum()
    print(f"\n1. Total Revenue: {total_revenue:,.2f}")

    # ==========================================================
    # 2. TOTAL UNITS SOLD
    # ==========================================================
    total_units = df["units_sold"].sum()
    print(f"2. Total Units Sold: {total_units:,.0f}")

    # ==========================================================
    # 3. AVERAGE UNIT PRICE
    # ==========================================================
    avg_price = df["price_unit"].mean()
    print(f"3. Average Unit Price: {avg_price:.2f}")

    # ==========================================================
    # 4. REVENUE BY REGION
    # ==========================================================
    if "region" in df.columns:
        revenue_by_region = df.groupby("region")["revenue"].sum()
        print("\n4. Revenue by Region:")
        print(revenue_by_region.sort_values(ascending=False))

    # ==========================================================
    # 5. REVENUE BY CATEGORY
    # ==========================================================
    if "category" in df.columns:
        revenue_by_category = df.groupby("category")["revenue"].sum()
        print("\n5. Revenue by Category:")
        print(revenue_by_category.sort_values(ascending=False))

    # ==========================================================
    # 6. REVENUE BY BRAND
    # ==========================================================
    if "brand" in df.columns:
        revenue_by_brand = df.groupby("brand")["revenue"].sum()
        print("\n6. Revenue by Brand:")
        print(revenue_by_brand.sort_values(ascending=False))

    # ==========================================================
    # 7. PROMOTION EFFECTIVENESS
    # ==========================================================
    if "promotion_flag" in df.columns and "units_sold" in df.columns:

        promo_effect = df.groupby("promotion_flag")["units_sold"].mean()

        print("\n7. Promotion Effectiveness (Avg Units Sold):")
        print(promo_effect)

        if len(promo_effect) == 2:
            lift = promo_effect.max() - promo_effect.min()
            print(f"\nPromotion Lift: {lift:.2f} units")

    # ==========================================================
    # 8. STOCK-OUT RATE
    # ==========================================================
    if "stock_available" in df.columns:

        stock_out_count = (df["stock_available"] == 0).sum()
        stock_out_rate = (stock_out_count / len(df)) * 100

        print(f"\n8. Stock-Out Rate: {stock_out_rate:.2f}%")

    # ==========================================================
    # 9. AVERAGE DELIVERY DAYS
    # ==========================================================
    if "delivery_days" in df.columns:

        avg_delivery = df["delivery_days"].mean()
        print(f"\n9. Average Delivery Days: {avg_delivery:.2f}")

    # ==========================================================
    # 10. STOCK UTILIZATION KPI
    # ==========================================================
    if "stock_available" in df.columns and "units_sold" in df.columns:

        df["stock_utilization"] = df["units_sold"] / df["stock_available"]
        df["stock_utilization"] = df["stock_utilization"].replace([float("inf")], 0)

        avg_utilization = df["stock_utilization"].mean()

        print(f"\n10. Average Stock Utilization: {avg_utilization:.2f}")

    # ==========================================================
    # SAVE KPI SUMMARY (OPTIONAL)
    # ==========================================================
    kpi_summary = {
        "Total Revenue": total_revenue,
        "Total Units Sold": total_units,
        "Average Price": avg_price,
        "Stock-Out Rate (%)": stock_out_rate if "stock_available" in df.columns else None,
        "Average Delivery Days": avg_delivery if "delivery_days" in df.columns else None,
        "Stock Utilization": avg_utilization if "stock_available" in df.columns and "units_sold" in df.columns else None
    }

    kpi_df = pd.DataFrame([kpi_summary])
    kpi_df.to_csv("data/kpi_summary.csv", index=False)

    print("\nKPI summary saved to data/kpi_summary.csv")

    print("\n" + "=" * 80)
    print("KPI CALCULATION COMPLETED")
    print("=" * 80)

    return df, kpi_df


if __name__ == "__main__":
    calculate_kpis()