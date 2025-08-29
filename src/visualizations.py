import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure the images folder exists
os.makedirs("images", exist_ok=True)

def plot_monthly_sales(df):
    df["Month"] = df["Order Date"].dt.to_period("M").dt.to_timestamp()
    monthly_sales = df.groupby("Month")["Sales"].sum()

    plt.figure(figsize=(8,5))
    sns.lineplot(x=monthly_sales.index, y=monthly_sales.values)
    plt.title("Monthly Sales Trend")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=45)
    
    # Save plot inside images folder
    plt.savefig(os.path.join("images", "monthly_sales.png"))
    plt.show()
    
    return monthly_sales

def plot_region_sales(df):
    region_sales = df.groupby("Region")["Sales"].sum().sort_values()

    plt.figure(figsize=(8,5))
    sns.barplot(x=region_sales.index, y=region_sales.values)
    plt.title("Sales by Region")
    plt.ylabel("Sales ($)")
    
    # Save plot inside images folder
    plt.savefig(os.path.join("images", "sales_by_region.png"))
    plt.show()
    
    return region_sales

def plot_forecast(monthly_sales):
    monthly_sales = monthly_sales.reset_index()
    monthly_sales["Forecast"] = monthly_sales["Sales"].rolling(window=3).mean()

    plt.figure(figsize=(8,5))
    sns.lineplot(data=monthly_sales, x="Month", y="Sales", label="Actual")
    sns.lineplot(data=monthly_sales, x="Month", y="Forecast", label="Forecast (SMA)")
    plt.title("Sales Forecast")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=45)
    plt.legend()
    
    # Save plot inside images folder
    plt.savefig(os.path.join("images", "sales_forecast.png"))
    plt.show()

def plot_segmentation(df):
    segmentation = df.groupby(['Region', 'Category'])['Sales'].sum().reset_index()

    plt.figure(figsize=(10,6))
    sns.barplot(data=segmentation, x='Region', y='Sales', hue='Category')
    plt.title('Sales by Region and Category')
    plt.ylabel('Total Sales')
    
    # Save plot inside images folder
    plt.savefig(os.path.join("images", "segmentation.png"))
    plt.show()
    
    return segmentation
