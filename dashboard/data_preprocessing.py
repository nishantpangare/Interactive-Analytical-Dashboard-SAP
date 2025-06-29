import pandas as pd

def preprocess_data(df):
    # # Load the data
    # df = pd.read_csv(r"data\\Sample - Superstore.csv")

    # ----------------------------
    # 1. Drop duplicate rows
    # ----------------------------
    df.drop_duplicates(inplace=True)

    # ----------------------------
    # 2. Handle missing values
    # ----------------------------
    print("Missing values:\n", df.isnull().sum())

    # For this dataset, we can see that these columns can provide valuable info for our dashboard.
    essential_columns = ["Order Date", "Sales", "Profit", "Region", "Category", "Sub-Category", "Segment"]
    df.dropna(subset=essential_columns, inplace=True)

    df.fillna("Unknown", inplace=True)

    # ----------------------------
    # 3. Here we Convert data types of Order Date and Ship Date columns 
    # ----------------------------
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

    numeric_cols = ["Sales", "Profit", "Quantity", "Discount"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Remove rows with NaT in Order Date
    df.dropna(subset=["Order Date"], inplace=True)

    # ----------------------------
    # 4. Feature engineering
    # ----------------------------
    # Add year, month, and weekday
    df['Order Year'] = df['Order Date'].dt.year
    df['Order Month'] = df['Order Date'].dt.month
    df['Order Weekday'] = df['Order Date'].dt.day_name()

    # Create Profit Margin (%)
    df['Profit Margin (%)'] = (df['Profit'] / df['Sales']) * 100
    df['Profit Margin (%)'] = df['Profit Margin (%)'].round(2)

    # Create Shipping Duration (days)
    df['Ship Duration'] = (df['Ship Date'] - df['Order Date']).dt.days

    # ----------------------------
    # 5. Filtering [remove negative or zero sales]
    # ----------------------------
    df = df[df["Sales"] > 0]
    df = df[df["Profit"].notnull()]

    # Reset index
    df.reset_index(drop=True, inplace=True)

    return df
