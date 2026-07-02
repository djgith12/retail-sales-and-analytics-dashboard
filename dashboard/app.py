import os
import sys

import pandas as pd
import plotly.express as px
import streamlit as st

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from scripts.load_data import load_raw_data


@st.cache_data(show_spinner="Loading sales data...")
def load_dashboard_data():
    csv_path = os.path.join(PROJECT_ROOT, "data", "cleaned_sales_data.csv")

    if os.path.exists(csv_path):
        data = pd.read_csv(csv_path)
    else:
        data = load_raw_data()

    data.columns = (
        data.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    if "date" in data.columns:
        data["date"] = pd.to_datetime(data["date"], errors="coerce")

    if "price_unit" in data.columns and "units_sold" in data.columns and "revenue" not in data.columns:
        data["revenue"] = data["price_unit"] * data["units_sold"]

    return data


# ==========================================================
# PAGE CONFIG & CSS
# ==========================================================
st.set_page_config(
    page_title="Retail Sales Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        .stApp {
            background: #ffffff;
            color: #ffffff;
        }

        html, body, .stApp, [data-testid="stAppViewContainer"] {
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }

        .block-container {
            padding-top: 1rem;
            padding-left: 1.5rem;
            padding-right: 1.5rem;
            padding-bottom: 1rem;
            max-width: 100%;
        }

        header[data-testid="stHeader"] {
            display: none;
        }

        [data-testid="stSidebar"] {
            display: none;
        }

        /* --- FIXED CLEAN TITLE BAND --- */
        .title-band {
            background: #7799bf;
            color: #07111f;
            text-align: center;
            font-size: 1.6rem;
            font-weight: 700;
            border-radius: 4px;
            padding: 1rem 0;
            margin-bottom: 1.2rem;
            width: 100%;
        }

        .filter-title {
            background: #24252e;
            color: white;
            padding: 0.6rem 0.75rem;
            margin-bottom: 0.6rem;
            border-radius: 6px;
            font-size: 16px;
            font-weight: 700;
        }

        /* --- REDUCED COMPACT KPI CARDS --- */
        .kpi-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            box-shadow: 0px 1px 3px rgba(0,0,0,0.05);
            color: #1f2937;
            text-align: center;
            padding: 0.45rem 0.25rem;
            line-height: 1.2;
            margin-bottom: 0.5rem;
        }

        .kpi-label {
            font-size: 0.78rem;
            font-weight: 600;
            color: #4b5563;
        }

        .kpi-value {
            font-size: 1.1rem;
            font-weight: 700;
            margin-top: 0.15rem;
        }

        div[data-testid="stVerticalBlock"] {
            gap: 0.5rem;
        }

        div[data-testid="stHorizontalBlock"] {
            gap: 0.6rem;
        }

        h3 {
            color: #f8fafc;
            background: #0e1117;
            padding: 0.35rem 0.8rem 0;
            margin: 0 !important;
            font-size: 1.2rem !important;
            line-height: 1.2 !important;
        }

        [data-testid="stDataFrame"] {
            background: #0e1117;
            border: 0;
            margin-top: 0.5rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Render the clean header inside the main container
st.markdown(
    '<div class="title-band">Retail Sales Analytics Dashboard</div>',
    unsafe_allow_html=True,
)


# ==========================================================
# LOAD DATA
# ==========================================================
df = load_dashboard_data()


# ==========================================================
# FILTER PANEL & DASHBOARD BODY
# ==========================================================
filter_col, content_col = st.columns([1, 4.2], gap="medium")

with filter_col:
    st.markdown('<div class="filter-title">Filters</div>', unsafe_allow_html=True)

    if "region" in df.columns:
        region = st.multiselect(
            "Select Region",
            sorted(df["region"].dropna().unique()),
            default=sorted(df["region"].dropna().unique()),
        )
        df = df[df["region"].isin(region)]

    if "category" in df.columns:
        category = st.multiselect(
            "Select Category",
            sorted(df["category"].dropna().unique()),
            default=sorted(df["category"].dropna().unique()),
        )
        df = df[df["category"].isin(category)]

    if "channel" in df.columns:
        channel = st.multiselect(
            "Select Channel",
            sorted(df["channel"].dropna().unique()),
            default=sorted(df["channel"].dropna().unique()),
        )
        df = df[df["channel"].isin(channel)]


with content_col:
    total_revenue = df["revenue"].sum() if "revenue" in df.columns else 0
    total_units = df["units_sold"].sum() if "units_sold" in df.columns else 0
    avg_price = df["price_unit"].mean() if "price_unit" in df.columns else 0
    stock_outs = (df["stock_available"] == 0).sum() if "stock_available" in df.columns else 0

    kpi_cols = st.columns(4)
    kpi_data = [
        ("Total Revenue", f"{total_revenue:,.0f}"),
        ("Total Units Sold", f"{total_units:,.0f}"),
        ("Avg Unit Price", f"{avg_price:.2f}"),
        ("Stock Out Cases", f"{stock_outs:,}"),
    ]

    for column, (label, value) in zip(kpi_cols, kpi_data):
        column.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">{label}</div>
                <div class="kpi-value">{value}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    def dashboard_chart(fig, height=205):
        fig.update_layout(
            height=height,
            paper_bgcolor="#0e1117",
            plot_bgcolor="#0e1117",
            font=dict(color="#f8fafc", size=9),
            title=dict(font=dict(size=11), x=0.02, y=0.92),
            margin=dict(l=15, r=15, t=40, b=15),
            legend=dict(font=dict(size=8), bgcolor="rgba(0,0,0,0)"),
        )
        fig.update_xaxes(title=None, gridcolor="#293142", tickfont=dict(size=8))
        fig.update_yaxes(title=None, gridcolor="#293142", tickfont=dict(size=8))
        return fig

    # Row 1: Triple charts
    chart_top_left, chart_top_mid, chart_top_right = st.columns([1, 1, 1])

    if "date" in df.columns and "revenue" in df.columns:
        trend = df.groupby(df["date"].dt.to_period("M"))["revenue"].sum().reset_index()
        trend["date"] = trend["date"].astype(str)
        fig = px.line(trend, x="date", y="revenue", markers=True, title="Sales Trend Over Time")
        chart_top_left.plotly_chart(dashboard_chart(fig, 200), use_container_width=True)

    if "region" in df.columns and "revenue" in df.columns:
        region_df = df.groupby("region", as_index=False)["revenue"].sum()
        fig = px.bar(region_df, x="region", y="revenue", color="region", title="Revenue by Region")
        chart_top_mid.plotly_chart(dashboard_chart(fig, 200), use_container_width=True)

    if "category" in df.columns and "revenue" in df.columns:
        category_df = df.groupby("category", as_index=False)["revenue"].sum()
        fig = px.bar(category_df, x="category", y="revenue", color="category", title="Revenue by Category")
        chart_top_right.plotly_chart(dashboard_chart(fig, 200), use_container_width=True)

    # Row 2: Bottom layout charts 
    chart_bottom_left, chart_bottom_right = st.columns([2, 3])

    if "promotion_flag" in df.columns and "units_sold" in df.columns:
        promo_df = df.groupby("promotion_flag", as_index=False)["units_sold"].mean()
        fig = px.bar(
            promo_df,
            x="promotion_flag",
            y="units_sold",
            color="promotion_flag",
            title="Promotion Impact",
        )
        chart_bottom_left.plotly_chart(dashboard_chart(fig, 220), use_container_width=True)

    numeric_df = df.select_dtypes(include="number")

    if not numeric_df.empty:
        fig = px.imshow(numeric_df.corr(), text_auto=True, aspect="auto", title="Correlation Heatmap")
        chart_bottom_right.plotly_chart(dashboard_chart(fig, 220), use_container_width=True)

    st.subheader("Raw Data Preview")
    st.dataframe(df.head(8), use_container_width=True, height=140)