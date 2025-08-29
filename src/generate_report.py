def create_html_report(total_sales, total_profit, total_orders, avg_profit_order,
                       region_sales, segmentation_img="segmentation.png",
                       anomaly_df=None, monthly_img="monthly_sales.png",
                       region_img="sales_by_region.png", sma_forecast_img="sales_forecast.png",
                       prophet_forecast_img="prophet_forecast.png"):

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>E-Commerce Sales Intelligence Report</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, sans-serif;
                background-color: #f4f6f8;
                color: #2c3e50;
                margin: 0;
                padding: 0;
            }}
            header {{
                background: linear-gradient(90deg, #2c3e50, #4ca1af);
                color: white;
                padding: 20px;
                text-align: center;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}
            h1 {{
                margin: 0;
            }}
            .container {{
                padding: 20px;
                max-width: 1200px;
                margin: auto;
            }}
            .kpi-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }}
            .kpi-card {{
                background: white;
                border-radius: 8px;
                padding: 20px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.05);
                text-align: center;
            }}
            .kpi-card h2 {{
                font-size: 1.1em;
                margin-bottom: 10px;
                color: #555;
            }}
            .kpi-card p {{
                font-size: 1.4em;
                font-weight: bold;
                margin: 0;
                color: #2c3e50;
            }}
            .charts img {{
                width: 100%;
                max-width: 600px;
                border-radius: 6px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                margin-bottom: 30px;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                background: white;
                border-radius: 6px;
                overflow: hidden;
                box-shadow: 0 2px 8px rgba(0,0,0,0.05);
                margin-bottom: 30px;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 10px;
                text-align: left;
            }}
            th {{
                background-color: #4ca1af;
                color: white;
            }}
            tr:nth-child(even) {{
                background-color: #f9f9f9;
            }}
            h2 {{
                margin-top: 40px;
                color: #34495e;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>E-Commerce Sales Intelligence Report</h1>
        </header>
        <div class="container">
            <div class="kpi-grid">
                <div class="kpi-card">
                    <h2>Total Sales</h2>
                    <p>${total_sales:,.2f}</p>
                </div>
                <div class="kpi-card">
                    <h2>Total Profit</h2>
                    <p>${total_profit:,.2f}</p>
                </div>
                <div class="kpi-card">
                    <h2>Total Orders</h2>
                    <p>{total_orders}</p>
                </div>
                <div class="kpi-card">
                    <h2>Avg Profit / Order</h2>
                    <p>${avg_profit_order:,.2f}</p>
                </div>
            </div>

            <h2>Monthly Sales Trend</h2>
            <img src="{monthly_img}" alt="Monthly Sales Trend">

            <h2>Sales by Region</h2>
            <img src="{region_img}" alt="Sales by Region">

            <h2>Short-Term Trend Forecast (SMA)</h2>
            <img src="{sma_forecast_img}" alt="SMA Forecast">

            <h2>Advanced Forecast (Prophet)</h2>
            <img src="{prophet_forecast_img}" alt="Prophet Forecast">

            <h2>Customer Segmentation</h2>
            <img src="{segmentation_img}" alt="Customer Segmentation">

            <h2>Sales by Region (Table)</h2>
            <table>
                <thead>
                    <tr><th>Region</th><th>Sales ($)</th></tr>
                </thead>
                <tbody>
    """
    for region, sales in region_sales.items():
        html_content += f"<tr><td>{region}</td><td>{sales:,.2f}</td></tr>\n"

    html_content += """
                </tbody>
            </table>
    """

    if anomaly_df is not None and not anomaly_df.empty:
        html_content += """
        <h2>Detected Sales Anomalies</h2>
        <table>
            <thead>
                <tr><th>Month</th><th>Sales</th><th>Z-Score</th></tr>
            </thead>
            <tbody>
        """
        for _, row in anomaly_df.iterrows():
            html_content += f"<tr><td>{row['Month'].strftime('%Y-%m')}</td><td>${row['Sales']:,.2f}</td><td>{row['z_score']:.2f}</td></tr>\n"
        html_content += """
            </tbody>
        </table>
        """

    html_content += """
        </div>
    </body>
    </html>
    """

    with open("report.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Report saved as report.html")
