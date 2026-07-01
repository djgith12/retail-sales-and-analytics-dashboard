import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from load_data import load_raw_data


def eda_analysis():

    # Load data
    df = load_raw_data()

    print("\n" + "=" * 80)
    print("EXPLORATORY DATA ANALYSIS (EDA)")
    print("=" * 80)

    # ==========================================================
    # 1. BASIC INFO
    # ==========================================================
    print("\n1. DATA OVERVIEW")
    print("-" * 80)
    print(df.shape)
    print(df.columns)
    print(df.info())

    # ==========================================================
    # 2. SUMMARY STATISTICS
    # ==========================================================
    print("\n2. DESCRIPTIVE STATISTICS")
    print("-" * 80)
    print(df.describe())

    # ==========================================================
    # 3. MISSING VALUES
    # ==========================================================
    print("\n3. MISSING VALUES")
    print("-" * 80)
    print(df.isnull().sum())

    # ==========================================================
    # 4. DUPLICATES
    # ==========================================================
    print("\n4. DUPLICATES")
    print("-" * 80)
    print(df.duplicated().sum())

    # ==========================================================
    # 5. REVENUE CREATION (if not exists)
    # ==========================================================
    if "price_unit" in df.columns and "units_sold" in df.columns:
        df["revenue"] = df["price_unit"] * df["units_sold"]

    # ==========================================================
    # 6. UNIVARIATE ANALYSIS
    # ==========================================================

    # Units Sold Distribution
    if "units_sold" in df.columns:
        plt.figure()
        plt.hist(df["units_sold"], bins=30)
        plt.title("Distribution of Units Sold")
        plt.xlabel("Units Sold")
        plt.ylabel("Frequency")
        plt.show()

    # Price Distribution
    if "price_unit" in df.columns:
        plt.figure()
        plt.hist(df["price_unit"], bins=30)
        plt.title("Distribution of Unit Price")
        plt.xlabel("Price")
        plt.ylabel("Frequency")
        plt.show()

    # Revenue Distribution
    if "revenue" in df.columns:
        plt.figure()
        plt.hist(df["revenue"], bins=30)
        plt.title("Distribution of Revenue")
        plt.xlabel("Revenue")
        plt.ylabel("Frequency")
        plt.show()

    # ==========================================================
    # 7. CATEGORY ANALYSIS
    # ==========================================================

    if "region" in df.columns:
        plt.figure()
        df["region"].value_counts().plot(kind="bar")
        plt.title("Sales Count by Region")
        plt.show()

    if "category" in df.columns:
        plt.figure()
        df["category"].value_counts().plot(kind="bar")
        plt.title("Sales Count by Category")
        plt.show()

    if "channel" in df.columns:
        plt.figure()
        df["channel"].value_counts().plot(kind="bar")
        plt.title("Sales Count by Channel")
        plt.show()

    # ==========================================================
    # 8. BIVARIATE ANALYSIS
    # ==========================================================

    # Revenue by Region
    if "revenue" in df.columns and "region" in df.columns:
        plt.figure()
        df.groupby("region")["revenue"].sum().plot(kind="bar")
        plt.title("Revenue by Region")
        plt.show()

    # Revenue by Category
    if "revenue" in df.columns and "category" in df.columns:
        plt.figure()
        df.groupby("category")["revenue"].sum().plot(kind="bar")
        plt.title("Revenue by Category")
        plt.show()

    # Promotion impact
    if "promotion_flag" in df.columns and "units_sold" in df.columns:
        plt.figure()
        df.groupby("promotion_flag")["units_sold"].mean().plot(kind="bar")
        plt.title("Promotion Impact on Units Sold")
        plt.show()

    # ==========================================================
    # 9. CORRELATION HEATMAP
    # ==========================================================

    numeric_cols = df.select_dtypes(include="number")

    if not numeric_cols.empty:
        plt.figure(figsize=(10, 6))
        sns.heatmap(numeric_cols.corr(), annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.show()

    # ==========================================================
    # 10. TIME SERIES ANALYSIS
    # ==========================================================

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

        monthly_sales = df.groupby(df["date"].dt.to_period("M"))["units_sold"].sum()

        plt.figure()
        monthly_sales.plot()
        plt.title("Monthly Sales Trend")
        plt.xlabel("Month")
        plt.ylabel("Units Sold")
        plt.show()

    # ==========================================================
    # FINAL OUTPUT
    # ==========================================================
    print("\nEDA COMPLETED SUCCESSFULLY")
    print("=" * 80)

    return df


if __name__ == "__main__":
    eda_analysis()