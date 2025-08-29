import matplotlib.pyplot as plt
from prophet import Prophet
import os

def forecast_sales(monthly_sales, months_ahead=6):
    """
    Perform sales forecasting using Prophet.
    
    Parameters:
        monthly_sales: pd.Series - indexed by month, values are sales
        months_ahead: int - how many months to forecast into the future
    Returns:
        forecast: pd.DataFrame - Prophet forecast results
    """
    # Prepare data for Prophet
    sales_ts = monthly_sales.reset_index()
    sales_ts.columns = ['ds', 'y']  # Prophet requires these column names

    # Create and train model
    model = Prophet()
    model.fit(sales_ts)

    # Create future dataframe for forecasting
    future = model.make_future_dataframe(periods=months_ahead, freq='M')

    # Predict future sales
    forecast = model.predict(future)

    # Plot forecast
    fig = model.plot(forecast)
    plt.title('Sales Forecast with Prophet')
    plt.tight_layout()
    plt.savefig(os.path.join("images", "prophet_forecast.png"))
    plt.show()

    return forecast