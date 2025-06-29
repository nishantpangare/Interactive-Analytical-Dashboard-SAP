import streamlit as st
import pandas as pd

# ---------------------------------------
# Dashboard with Important KPIs and What-if analysis.
# ---------------------------------------
def run_dashboard(df):
    st.header("Key Performance Indicators (KPIs)")

    total_sales = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    avg_discount = df['Discount'].mean()
    avg_profit_margin = df['Profit Margin (%)'].mean()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Sales", f"${total_sales:,.0f}")
    col2.metric("Total Profit", f"${total_profit:,.0f}")
    col3.metric("Avg Discount", f"{avg_discount:.2%}")
    col4.metric("Avg Profit Margin", f"{avg_profit_margin:.2f}%")

    st.markdown("---")

    # What-if Analysis: Hypothetical Discount
    st.subheader("What-If Analysis: Adjust Discount as you wish.")
    hypothetical_discount = st.slider("Select Hypothetical Discount Rate", 0.0, 0.5, float(avg_discount), 0.01)
    projected_profit = (df['Sales'] * (1 - hypothetical_discount)).sum()
    st.write(f"Projected Profit with {hypothetical_discount:.0%} discount: **${projected_profit:,.2f}**")

    st.markdown("---")
    st.subheader("Sales Breakdown by Region")

    # Region filter dropdown inside dashboard
    regions = df['Region'].unique()
    selected_region = st.selectbox("Select Region", options=regions)

    filtered_region_df = df[df['Region'] == selected_region]

    sales_by_category = filtered_region_df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
    st.bar_chart(sales_by_category)

    st.subheader(f"Top 5 Products in {selected_region} by Sales")
    top_products = filtered_region_df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)
    st.bar_chart(top_products)

    st.subheader(f"Monthly Sales Trend in {selected_region}")
    monthly_sales = filtered_region_df.groupby('Order Month')['Sales'].sum().reindex(range(1, 13), fill_value=0)
    st.line_chart(monthly_sales)


# ---------------------------------------
# Sidebar filters function
# ---------------------------------------
def sidebar_filters(df):
    st.sidebar.header("Filters")

    min_date = df['Order Date'].min()
    max_date = df['Order Date'].max()
    date_range = st.sidebar.date_input("Select Date Range", [min_date, max_date],
                                       min_value=min_date, max_value=max_date)

    categories = df['Category'].unique().tolist()
    selected_categories = st.sidebar.multiselect("Select Category", categories, default=categories)

    filtered_subcat = df[df['Category'].isin(selected_categories)]['Sub-Category'].unique().tolist()
    selected_subcategories = st.sidebar.multiselect("Select Sub-Category", filtered_subcat, default=filtered_subcat)

    regions = df['Region'].unique().tolist()
    selected_regions = st.sidebar.multiselect("Select Region", regions, default=regions)

    filtered_df = df[
        (df['Order Date'] >= pd.to_datetime(date_range[0])) &
        (df['Order Date'] <= pd.to_datetime(date_range[1])) &
        (df['Category'].isin(selected_categories)) &
        (df['Sub-Category'].isin(selected_subcategories)) &
        (df['Region'].isin(selected_regions))
    ]
    return filtered_df, date_range, selected_categories, selected_subcategories, selected_regions

# ---------------------------------------
# Download CSV button
# ---------------------------------------
def download_filtered_data(df):
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Filtered Data as CSV",
        data=csv,
        file_name='filtered_superstore_data.csv',
        mime='text/csv',
    )

# # ---------------------------------------
# # Generate shareable link with filters encoded
# # ---------------------------------------
# def generate_shareable_link(date_range, categories, subcategories, regions):
#     params = {
#         'start_date': date_range[0].strftime("%Y-%m-%d"),
#         'end_date': date_range[1].strftime("%Y-%m-%d"),
#         'categories': ','.join(categories),
#         'subcategories': ','.join(subcategories),
#         'regions': ','.join(regions)
#     }
#     base_url = st.experimental_get_query_params().get('base_url', ['http://localhost:8501'])[0]
#     url = f"{base_url}?{urlencode(params)}"
#     st.markdown(f"Shareable Link: [Click here]({url})")
