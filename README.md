Retail Sales Analytics Dashboard

This project analyzes retail sales data from an Excel dataset and presents the results in a Streamlit dashboard. 
It includes scripts for loading data, understanding data quality, cleaning records, engineering business features, 
calculating KPIs, running exploratory analysis, and visualizing retail performance.

Project Objectives

- Load retail sales data from `data/Sales_Dataset.xlsx`.
- Inspect data structure, missing values, duplicates, invalid values, and summary statistics.
- Clean and standardize the dataset for analysis.
- Create business-focused features such as revenue, promotion category, stock utilization, delivery performance, price segment, and demand level.
- Calculate retail KPIs including revenue, units sold, average price, stock-out rate, average delivery days, and stock utilization.
- Build an interactive Streamlit dashboard with filters and Plotly charts.

Technology Stack

- Python
- pandas
- numpy
- openpyxl
- matplotlib
- seaborn
- plotly
- streamlit

Project Workflow

1. Business Understanding
2. Data Loading and Understanding
3. Data Cleaning 
4. Feature Engineering
5. Exploratory Data Analysis (EDA)
6. KPI Development
7. Dashboard Development
8. Business Insights & Recommendations

1. Business Understanding

The Business Understanding phase establishes the business goals, identifies key challenges, and defines how data analytics can support informed decision-making. It provides the foundation for the entire analytics pipeline by aligning the project with real-world business objectives.

This phase includes:

- Business Context: Overview of the retail business and the sales dataset.
- Business Problem: Identification of challenges related to sales performance, inventory, promotions, and operations.
- Business Objectives: Definition of measurable goals to improve business performance.
- Stakeholders: Identification of the primary users of the dashboard and insights.
- Business Questions: Key business questions the analysis aims to answer.
- Success Criteria: Metrics used to evaluate the success of the project.
- Key Performance Indicators (KPIs): Business metrics used to measure performance.
- Business Hypotheses (Optional): Assumptions that will be validated through data analysis.

2. Data Loading and Understanding

Data Loading
load_data.py

Description

This module is responsible for loading the raw retail sales dataset into a pandas DataFrame. It centralizes data access so that the dataset can be imported consistently across different scripts in the project.

Features

Loads the Excel dataset from the project's data directory.
Uses pandas.read_excel() for efficient data import.
Provides an optional verbose mode to preview the loaded dataset.
Returns the dataset as a pandas DataFrame for further processing.
Includes a standalone execution block for quick testing.

Data Understanding
data_understanding.py

Description

This module performs an initial exploratory assessment of the raw dataset before data cleaning and analysis. The objective is to understand the dataset's structure, completeness, quality, and overall characteristics while identifying potential data issues that may affect downstream analysis.

Analyses Performed

- Displays dataset dimensions (rows and columns).
- Lists all available column names.
- Examines data types and overall dataset information.
- Previews the first and last records.
- Generates descriptive statistics for numerical variables.
- Identifies missing values and reports their distribution.
- Detects duplicate records.
- Counts unique values for each feature.
- Explores the distribution of categorical variables.
- Summarizes numerical variables using statistical measures.
- Checks for negative values in numerical columns.
- Identifies stock-out records where inventory equals zero.
- Examines the distribution of promotional activities.
- Computes correlations among numerical variables.
- Provides an initial data quality checklist highlighting potential issues such as:
    - Missing values
    - Duplicate records
    - Incorrect data types
    - Negative values
    - Outliers
    - Inconsistent categorical labels

Outcome

The module provides a comprehensive overview of the raw dataset, helping identify data quality issues and ensuring that the data is well understood before preprocessing, feature engineering, and subsequent analysis.

3. Data Cleaning
data_cleaning.py

Description

This module cleans and validates the raw retail sales dataset to improve data quality and prepare it for feature engineering, exploratory analysis, and dashboard development. It standardizes the dataset, handles missing and invalid values, removes duplicate records, performs validation checks, and generates a cleaned dataset suitable for downstream analytical tasks.

Cleaning Steps Performed
- Standardizes column names by converting them to lowercase, removing extra spaces, and replacing spaces with underscores for consistent naming.
- Converts data types by transforming the date column into a datetime format and converting numerical columns to appropriate numeric data types.
- Handles missing values by:
    - Replacing missing numerical values with the median of each column.
    - Replacing missing categorical values with the most frequent (mode) value.
- Removes duplicate records to ensure each transaction is represented only once.
- Cleans categorical text values by trimming whitespace and standardizing text formatting.
- Removes invalid records containing negative values in key numerical fields such as unit price, delivery days, and units sold.
- Performs a basic outlier assessment by summarizing the distribution of important numerical variables.
- Creates basic business features, including:
    - Revenue (price_unit × units_sold)
    - Year and month extracted from the transaction date
    - Promotion category labels (Promoted and Non-Promoted)
- Validates business rules by checking:
    - Transactions where units sold exceed delivered quantity.
    - Stock-out records where available inventory equals zero.

Output

The cleaned dataset is saved as:

data/cleaned_sales_data.csv

Outcome

The module produces a high-quality, standardized dataset with improved consistency, completeness, and validity. By addressing missing values, duplicate records, formatting inconsistencies, and invalid data, it ensures the dataset is ready for feature engineering, exploratory data analysis, visualization, and predictive modeling.

4. Feature Engineering

feature_engineering.py

Description

This module transforms the raw retail sales dataset into a business-ready dataset by creating meaningful features that support exploratory analysis, KPI reporting, and dashboard development. It derives new variables from existing data to improve analytical capabilities and provide deeper business insights.

Features Created

- Standardizes column names by converting them to lowercase, removing extra spaces, and replacing spaces with underscores to ensure consistent naming.
- Calculates revenue as the product of unit price and units sold, creating a key business performance metric.
- Extracts time-based features from the transaction date, including year, month, month number, and day, to support trend and seasonality analysis.
- Transforms promotion indicators into descriptive categories (Promoted and Non-Promoted) for improved readability and reporting.
- Computes stock utilization to measure inventory efficiency by comparing units sold with available stock while handling division-by-zero cases.
- Categorizes delivery performance into performance groups (Fast, Moderate, Slow, and Very Slow) based on delivery lead time.
- Segments products by price into Low, Medium, and High price categories for comparative analysis.
- Creates demand-level indicators by classifying products into High Demand or Low Demand using the median units sold as the threshold.
- Generates a revenue validation column (log_revenue) to facilitate future analytical transformations.

Output

The engineered dataset is saved as:

data/feature_engineered_data.csv

5. Exploratory Data Analysis (EDA)
eda_analysis.py

Description

This module performs Exploratory Data Analysis (EDA) on the retail sales dataset to uncover patterns, trends, relationships, and potential anomalies. It combines statistical summaries with visualizations to better understand the data and generate insights that support business decision-making, feature engineering, and dashboard development.

Analyses Performed
- Provides a dataset overview by displaying its dimensions, column names, data types, and general information.
- Generates descriptive statistics to summarize the distribution and central tendency of numerical variables.
- Analyzes missing values to identify incomplete data.
- Detects duplicate records to assess data quality.
- Calculates revenue as price_unit × units_sold if the feature is not already available.
- Performs univariate analysis using histograms to examine the distribution of:
    - Units sold
    - Unit price
    - Revenue
- Performs categorical analysis using bar charts to explore the distribution of:
    - Regions
    - Product categories
    - Sales channels
- Performs bivariate analysis to investigate relationships between key business variables, including:
    - Revenue by region
    - Revenue by product category
    - Promotion impact on average units sold
- Conducts correlation analysis by generating a heatmap of numerical variables to identify linear relationships.
- Performs time-series analysis by aggregating monthly sales and visualizing sales trends over time.
- 
Visualizations Generated

- Histograms for numerical feature distributions.
- Bar charts for categorical feature frequencies.
- Bar charts comparing revenue across regions and categories.
- Promotion effectiveness analysis.
- Correlation heatmap for numerical variables.
- Monthly sales trend line chart.

Output

The module produces statistical summaries and interactive visualizations that provide insights into the dataset. These outputs support data validation, business understanding, feature engineering, and dashboard design by highlighting sales patterns, customer behavior, and relationships among key variables.

6. KPI Development

The KPI Development module converts cleaned retail sales data into meaningful business metrics that help evaluate overall business performance and support data-driven decision-making.

Key Features
- Calculates Total Revenue and Total Units Sold
- Computes Average Unit Price
- Analyzes Revenue by Region, Category, and Brand
- Evaluates Promotion Effectiveness
- Measures Stock-Out Rate
- Calculates Average Delivery Days
- Computes Stock Utilization
- Exports a KPI summary to data/kpi_summary.csv for dashboard visualization.

This module provides a concise overview of financial, sales, operational, and marketing performance, serving as the foundation for the analytics dashboard.


7. Dashboard Development (Streamlit)

This step focuses on building an interactive Retail Sales Analytics Dashboard using Streamlit. The dashboard transforms processed sales data into business insights through KPIs, visualizations, and filters.

Objective

To create a user-friendly, interactive dashboard that enables stakeholders to explore sales performance, analyze trends, and make data-driven decisions.

Key Components
- Data Integration

The dashboard connects to the cleaned sales dataset (cleaned_sales_data.csv). If unavailable, it falls back to the raw dataset loader. Data is standardized and preprocessed for consistency before visualization.

- Page Configuration

Streamlit page settings are defined to optimize user experience:

Wide layout for better visualization space
Custom title: Retail Sales Dashboard
Sidebar disabled for a clean interface
- Data Preparation

Before visualization:

Column names are standardized
Date fields are converted to datetime format
Revenue is calculated as:
Revenue = Price Unit × Units Sold
- Interactive Filters

Users can dynamically filter data by:

Region
Category
Channel

These filters update all KPIs and charts in real time.

- KPI Dashboard

Key performance indicators displayed at the top:

Total Revenue
Total Units Sold
Average Unit Price
Stock-Out Cases

These KPIs provide a quick snapshot of business performance.

- Visual Analytics

The dashboard includes interactive Plotly visualizations:

Sales Trend Over Time (time-series analysis)
Revenue by Region (geographical performance)
Revenue by Category (product performance)
Promotion Impact Analysis (marketing effectiveness)
Correlation Heatmap (relationship between numerical variables)
- Data Exploration

A raw data preview table is included to:

Validate calculations
Inspect sample records
Improve transparency
Business Value

This dashboard enables stakeholders to:

- Monitor real-time sales performance
- Identify high and low-performing segments
- Evaluate marketing effectiveness
- Understand regional and category trends
- Support data-driven business decisions

Output

The final output is an interactive Streamlit dashboard that combines:

- KPIs
- Filters
- Charts
- Raw data inspection
