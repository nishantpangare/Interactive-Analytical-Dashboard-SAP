# Interactive Analytical Dashboard – SAP

This project deploys an interactive web app built using **Streamlit** to showcase end-to-end analytics on the **Sample Superstore** dataset.

It was specifically created to enhance my portfolio while applying for a **Working Student – Analytics Consulting** position at **SAP**.

---

## 🚀 Features

- ✅ Data cleaning & preprocessing (duplicates, missing values, type conversions)
- 📊 Exploratory Data Analysis (EDA): distributions, summary statistics, heatmaps
- 📈 Interactive Dashboard:
  - Filter by Date, Category, Sub-category, and Region
  - View KPIs: Sales, Profit, Profit Margin, Discounts
  - Regional breakdowns and product-level insights
  - What-If analysis via a dynamic discount slider
- 📥 Download filtered data as CSV

---

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Python** | Core logic & analysis |
| **Streamlit** | Web app deployment |
| **Pandas** | Data Loading and Handling |
| **Matplotlib & Seaborn** | Data Visualizations |
| **Git/GitHub** | Version control & portfolio |

---

## 📁 Project Structure

```
.
├── app.py                         # Main Streamlit application file
├── data/                          # Contains project datasets
│   └── Sample - Superstore.csv    # Primary dataset for analysis
├── dashboard/                     # Modules for dashboard functionalities
│   ├── data_preprocessing.py      # Script for data cleaning and preparation
│   ├── eda.py                     # Script for Exploratory Data Analysis (EDA) functions
│   └── main_dashboard.py          # Script containing the main interactive dashboard layouts and logic
└── reports/                       # Directory for saving generated visualizations and reports.
```
## 🚀 Access the Live Web App

🔗 [Click here to launch the Interactive Analytics Dashboard](https://nishantpangare-interactive-analytical-dashboard-sap-app-paztrm.streamlit.app/)

You can use the link given above to browse the webapp and then select from the buttons on the left hand side to navigate through the webapp.

