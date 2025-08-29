# anomaly_detection.py
import pandas as pd
from scipy.stats import zscore

def detect_sales_anomalies(monthly_sales):
    """
    Detect anomalies in monthly sales using Z-score.
    :param monthly_sales: DataFrame with 'Month' as index and 'Sales' column.
    :return: DataFrame of anomalies.
    """
    monthly_sales_df = monthly_sales.reset_index()
    monthly_sales_df['z_score'] = zscore(monthly_sales_df['Sales'])

    anomalies = monthly_sales_df[
        (monthly_sales_df['z_score'] > 2) | (monthly_sales_df['z_score'] < -2)
    ]

    return anomalies

