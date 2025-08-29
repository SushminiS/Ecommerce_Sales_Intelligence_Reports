#Handles data loading, cleaning, and KPI calculations.


import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(
        filepath,
        parse_dates=["Order Date"],
        encoding="Windows-1252"
    )
    df.dropna(subset=["Sales", "Profit"], inplace=True)
    return df

def calculate_kpis(df):
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_orders = df["Order ID"].nunique()
    avg_profit_order = total_profit / total_orders
    return total_sales, total_profit, total_orders, avg_profit_order

    

