from src.analysis import load_and_clean_data, calculate_kpis
from src.visualizations import plot_monthly_sales, plot_region_sales, plot_forecast, plot_segmentation
from src.generate_report import create_html_report
from src.forecasting import forecast_sales
from src.anomaly_detection import detect_sales_anomalies

def main():
    filepath = "data/ecommerce_sales.csv"
    df = load_and_clean_data(filepath)

    # 1️⃣ Calculate KPIs
    total_sales, total_profit, total_orders, avg_profit_order = calculate_kpis(df)
    print(f"Total Sales: ${total_sales:,.2f}")
    print(f"Total Profit: ${total_profit:,.2f}")
    print(f"Total Orders: {total_orders}")
    print(f"Average Profit per Order: ${avg_profit_order:,.2f}")

    # 2️⃣ Generate and SAVE all plots
    monthly_sales = plot_monthly_sales(df)
    region_sales = plot_region_sales(df)
    plot_forecast(monthly_sales)  # saves sales_forecast.png
    plot_segmentation(df)         # saves segmentation.png

    # 3️⃣ Prophet Forecast (Advanced)
    forecast_df = forecast_sales(monthly_sales, months_ahead=6)  # saves prophet_forecast.png

    # 4️⃣ Detect anomalies
    anomalies = detect_sales_anomalies(monthly_sales)
    print("\nAnomalies detected in monthly sales:")
    print(anomalies[['Month', 'Sales', 'z_score']])

    # 5️⃣ Create HTML Report with ALL features
    create_html_report(
    total_sales=total_sales,
    total_profit=total_profit,
    total_orders=total_orders,
    avg_profit_order=avg_profit_order,
    region_sales=region_sales,
    segmentation_img="images/segmentation.png",
    anomaly_df=anomalies,
    monthly_img="images/monthly_sales.png",
    region_img="images/sales_by_region.png",
    sma_forecast_img="images/sales_forecast.png",
    prophet_forecast_img="images/prophet_forecast.png"
)


if __name__ == "__main__":
    main()
