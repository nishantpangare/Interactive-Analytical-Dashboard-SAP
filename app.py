import streamlit as st
import pandas as pd
from dashboard.data_preprocessing import preprocess_data
from dashboard.eda import run_eda
from dashboard.main_dashboard import run_dashboard, sidebar_filters, download_filtered_data

# Streamlit page configuration
st.set_page_config(page_title="Analytics Interactive Dashboard", layout="wide")

# Load and preprocess data
@st.cache_data
def load_data():
    df = pd.read_csv("data/Sample - Superstore.csv", encoding='latin1')
    df = preprocess_data(df)
    return df

# Main Streamlit app
def main():
    st.title("Analytics Dashboard (Superstore Data)")

    # Sidebar navigation
    st.sidebar.title("Navigation")
    option = st.sidebar.radio("Go to", ["Overview", "EDA", "Dashboard"])

    # Load data
    df = load_data()

    if option == "Overview":
        st.subheader("Project Overview")
        st.markdown("""
        This interactive web app was built using **Streamlit** to showcase end-to-end analytics using the *Sample Superstore* dataset.

        It includes:
        - Data preprocessing and cleaning
        - Exploratory Data Analysis (EDA)
        - A modern interactive dashboard
        - KPIs, regional breakdowns, product performance

        **Purpose**: Demonstrate my cloud-native data analytics skillset for a real-world business scenario.
        """)
        st.markdown("---")
        st.write("Data Preview:")
        st.dataframe(df.head())

    elif option == "EDA":
        st.subheader("Exploratory Data Analysis")
        run_eda(df)

    elif option == "Dashboard":
        st.subheader("Interactive Dashboard")

        # Apply filters from sidebar
        filtered_df, date_range, categories, subcategories, regions = sidebar_filters(df)

        # Run the dashboard section
        run_dashboard(filtered_df)

        # Download filtered data
        download_filtered_data(filtered_df)

if __name__ == "__main__":
    main()
