import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os
import io

def run_eda(df):
    os.makedirs("reports", exist_ok=True) 

    st.subheader("Basic Data Info")
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_text = buffer.getvalue()
    
    st.code(info_text)  # or st.code(info_text)

    st.subheader("Descriptive Statistics (Numerical Columns)")
    st.dataframe(df.describe())

    st.subheader("Categorical Column Distributions")
    categorical_cols = ['Segment', 'Region', 'Category', 'Sub-Category', 'Ship Mode']
    for col in categorical_cols:
        st.write(f"{col} value counts:")
        st.dataframe(df[col].value_counts())

    # Correlation Heatmap
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df[['Sales', 'Profit', 'Discount', 'Quantity', 'Profit Margin (%)']].corr(), annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Heatmap")
    fig.savefig("reports/correlation_heatmap.png")
    st.pyplot(fig)

    # Sales by Category
    st.subheader("Sales and Profit by Category")
    cat_sales = df.groupby('Category')[['Sales', 'Profit']].sum().reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=cat_sales, x='Category', y='Sales', ax=ax)
    ax.set_title("Sales by Category")
    fig.savefig("reports/sales_by_category.png")
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=cat_sales, x='Category', y='Profit', ax=ax)
    ax.set_title("Profit by Category")
    fig.savefig("reports/profit_by_category.png")
    st.pyplot(fig)

    # Monthly Sales
    st.subheader("Monthly Sales Trend")
    monthly_sales = df.groupby('Order Month')['Sales'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=monthly_sales, x='Order Month', y='Sales', marker='o', ax=ax)
    ax.set_title("Monthly Sales Trend")
    ax.set_xticks(range(1, 13))
    ax.grid(True)
    fig.savefig("reports/monthly_sales_trend.png")
    st.pyplot(fig)

    # Segment Profit
    st.subheader("Profit by Segment")
    segment_data = df.groupby('Segment')[['Sales', 'Profit']].sum().reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=segment_data, x='Segment', y='Profit', ax=ax)
    ax.set_title("Profit by Segment")
    fig.savefig("reports/profit_by_segment.png")
    st.pyplot(fig)

    # Region Sales
    st.subheader("Sales by Region")
    region_data = df.groupby('Region')[['Sales', 'Profit']].sum().reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=region_data, x='Region', y='Sales', ax=ax)
    ax.set_title("Sales by Region")
    fig.savefig("reports/sales_by_region.png")
    st.pyplot(fig)

    # Ship Duration
    st.subheader("Shipping Duration Distribution")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df["Ship Duration"], bins=10, kde=True, ax=ax)
    ax.set_title("Shipping Duration Distribution")
    ax.set_xlabel("Shipping Duration (days)")
    fig.savefig("reports/shipping_duration.png")
    st.pyplot(fig)

    # Top Products
    st.subheader("Top 10 Products by Sales")
    top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_products.values, y=top_products.index, ax=ax)
    ax.set_title("Top 10 Products by Sales")
    ax.set_xlabel("Sales")
    fig.savefig("reports/top_10_products.png")
    st.pyplot(fig)
