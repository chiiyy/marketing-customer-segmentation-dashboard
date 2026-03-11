# Marketing Customer Segmentation Dashboard

This project analyzes marketing campaign customer data to identify meaningful customer segments using K-Means clustering and presents the results through an interactive Streamlit dashboard.

## Project Overview

The goal of this project is to group customers based on demographic and spending characteristics, then visualize these segments in a clear and interactive dashboard for business analysis.

The project includes:
- data quality assessment
- exploratory data analysis
- customer segmentation using K-Means clustering
- export of clustered customer data
- interactive dashboard development with Streamlit

## Objectives

- examine and clean the dataset
- explore customer demographics, spending patterns, and campaign responses
- identify customer groups using clustering
- interpret cluster characteristics for business insights
- build an interactive dashboard to support segment exploration

## Dataset

The project uses a marketing campaign dataset containing customer-related information such as:

- income
- age
- education level
- recency
- tenure
- total spending
- campaign response
- cluster label

## Methods Used

### 1. Data Cleaning and Preparation
The dataset was checked for:
- missing values
- duplicate records
- incorrect data types
- inconsistent entries
- outliers where applicable

### 2. Exploratory Data Analysis
EDA was performed to understand:
- demographic patterns
- spending behavior
- campaign response trends
- differences across customer groups

### 3. Customer Segmentation
K-Means clustering was applied to group customers with similar characteristics.

The elbow method was used to determine the optimal number of clusters.

### 4. Dashboard Development
A Streamlit dashboard was built to allow interactive exploration of customer segments.

## Dashboard Features

The dashboard includes:
- cluster filter
- education level filter
- KPI summary cards
- cluster size bar chart
- histogram of selected numeric variables
- income vs total spending scatterplot
- average spending by cluster
- campaign response rate by cluster
- filtered data preview table

## Key Insight

This project helps identify customer groups with different income levels, spending patterns, and response behaviors, which can support more targeted marketing strategies.

For example, high-income and high-spending clusters can be distinguished from lower-value segments, allowing better campaign targeting and customer profiling.

## Tools and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit

## Files

- `customer_segmentation_analysis.ipynb` — notebook for data cleaning, EDA, and clustering
- `streamlit_dashboard.py` — Streamlit dashboard application
- `marketing_campaign_clustered.csv` — clustered output dataset

## Resume Relevance

This project demonstrates practical skills in:
- data preprocessing
- exploratory data analysis
- unsupervised learning
- customer segmentation
- dashboard development
- translating analytical results into business insights
