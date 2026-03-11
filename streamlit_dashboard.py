import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration and basic style
st.set_page_config(
    page_title="Marketing Campaign – Customer Segments",
    layout="wide"
)

sns.set(style="whitegrid")


# Load clustered data
@st.cache_data
def load_data():
    df = pd.read_csv("marketing_campaign_clustered.csv")
    return df

df = load_data()

# Sidebar – filters
st.sidebar.title("Filters")

# Filter by cluster
cluster_options = sorted(df["Cluster"].unique())
selected_clusters = st.sidebar.multiselect(
    "Select clusters to view:",
    cluster_options,
    default=cluster_options
)

edu_options = ["All"] + sorted(
    df["Education_Level"].dropna().unique().tolist()
)
selected_edu = st.sidebar.selectbox(
    "Filter by education level:",
    edu_options
)

# Apply filters
df_filtered = df[df["Cluster"].isin(selected_clusters)]
if selected_edu != "All":
    df_filtered = df_filtered[df_filtered["Education_Level"] == selected_edu]

# KPI cards (high level summary)
st.title("Customer Segments Dashboard")
st.markdown("Using K-Means clusters from `marketing_campaign_clustered.csv`.")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Number of customers",
        f"{len(df_filtered):,}"
    )

with col2:
    avg_income = df_filtered["Income"].mean()
    st.metric(
        "Average income",
        f"{avg_income:,.0f}"
    )

with col3:
    avg_spent = df_filtered["TotalMntSpent"].mean()
    st.metric(
        "Avg total spent (2 yrs)",
        f"{avg_spent:,.0f}"
    )

with col4:
    if "Response" in df_filtered.columns:
        resp_rate = df_filtered["Response"].mean()
        st.metric(
            "Campaign response rate",
            f"{resp_rate * 100:,.1f}%"
        )

st.markdown("---")

# Visual 1 – Cluster size bar chart
st.subheader("Cluster Size")

cluster_counts = (
    df_filtered["Cluster"]
    .value_counts()
    .sort_index()
)

st.bar_chart(cluster_counts)

# Visual 2 – Histogram of a numeric variable
st.subheader("Distribution of Selected Numeric Variable")

numeric_cols = ["Age", "Income", "TotalMntSpent", "Recency", "Tenure_days"]
numeric_cols = [c for c in numeric_cols if c in df_filtered.columns]

selected_num = st.selectbox(
    "Choose a variable:",
    numeric_cols,
    index=0
)

fig1, ax1 = plt.subplots(figsize=(6, 4))
sns.histplot(df_filtered[selected_num], bins=20, kde=True, ax=ax1)
ax1.set_xlabel(selected_num)
ax1.set_ylabel("Count")
st.pyplot(fig1)

# Visual 3 – Income vs TotalMntSpent scatterplot
if {"Income", "TotalMntSpent"}.issubset(df_filtered.columns):
    st.subheader("Income vs Total Amount Spent (coloured by cluster)")
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    sns.scatterplot(
        data=df_filtered,
        x="Income",
        y="TotalMntSpent",
        hue="Cluster",
        alpha=0.7,
        ax=ax2
    )
    ax2.set_xlabel("Income")
    ax2.set_ylabel("TotalMntSpent (2 years)")
    ax2.legend(title="Cluster")
    st.pyplot(fig2)

# Visual 4 – Average spending by cluster
st.subheader("Average Total Spending by Cluster")

spend_by_cluster = (
    df_filtered
    .groupby("Cluster")["TotalMntSpent"]
    .mean()
    .reset_index()
    .sort_values("Cluster")
)

fig3, ax3 = plt.subplots(figsize=(6, 4))
sns.barplot(
    data=spend_by_cluster,
    x="Cluster",
    y="TotalMntSpent",
    ax=ax3
)
ax3.set_xlabel("Cluster")
ax3.set_ylabel("Avg TotalMntSpent")
st.pyplot(fig3)

# Visual 5 – Campaign response rate by cluster
if "Response" in df_filtered.columns:
    st.subheader("Campaign Response Rate by Cluster")

    resp_by_cluster = (
        df_filtered
        .groupby("Cluster")["Response"]
        .mean()
        .reset_index()
        .sort_values("Cluster")
    )

    fig4, ax4 = plt.subplots(figsize=(6, 4))
    sns.barplot(
        data=resp_by_cluster,
        x="Cluster",
        y="Response",
        ax=ax4
    )
    ax4.set_xlabel("Cluster")
    ax4.set_ylabel("Response rate")
    ax4.set_ylim(0, 1)
    st.pyplot(fig4)

# show a sample of the filtered data
st.subheader("Sample of Filtered Data")
st.dataframe(df_filtered.head(20))
