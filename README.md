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
3. Data Cleaning & Validation
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

-Displays dataset dimensions (rows and columns).
-Lists all available column names.
-Examines data types and overall dataset information.
-Previews the first and last records.
-Generates descriptive statistics for numerical variables.
-Identifies missing values and reports their distribution.
-Detects duplicate records.
-Counts unique values for each feature.
-Explores the distribution of categorical variables.
-Summarizes numerical variables using statistical measures.
-Checks for negative values in numerical columns.
-Identifies stock-out records where inventory equals zero.
-Examines the distribution of promotional activities.
-Computes correlations among numerical variables.
-Provides an initial data quality checklist highlighting potential issues such as:
    -Missing values
    -Duplicate records
    -Incorrect data types
    -Negative values
    -Outliers
    -Inconsistent categorical labels

Outcome

The module provides a comprehensive overview of the raw dataset, helping identify data quality issues and ensuring that the data is well understood before preprocessing, feature engineering, and subsequent analysis.