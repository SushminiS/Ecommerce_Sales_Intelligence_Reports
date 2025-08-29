E-Commerce Sales Intelligence Dashboard

A data analytics and visualization project built with Python, Pandas, Matplotlib, Seaborn, and Prophet to provide business intelligence insights for e-commerce sales.
This dashboard generates an interactive HTML report with KPIs, trends, forecasts, customer segmentation, and anomaly detection.

🚀 Features

✅ Automated Data Cleaning — Removes missing values and standardizes date formats.
✅ Key Performance Indicators (KPIs) — Total Sales, Total Profit, Orders, and Avg Profit per Order.
✅ Sales Trends — Monthly sales trend visualization.
✅ Regional Insights — Sales by region and category segmentation.
✅ Forecasting —
        SMA (Simple Moving Average) short-term trends.
        Prophet advanced time-series forecasting.
✅ Anomaly Detection — Highlights unusual sales spikes/drops using z-scores.
✅ Professional HTML Report — Styled dashboard ready for business presentations.

📂 Project Structure

📦 ecommerce-sales-intelligence
 ┣ 📂 data
 ┃ ┗ ecommerce_sales.csv
 ┣ 📜 main.py
 ┣ 📜 analysis.py
 ┣ 📜 visualizations.py
 ┣ 📜 forecasting.py
 ┣ 📜 anomaly_detection.py
 ┣ 📜 generate_report.py
 ┣ 📜 report.html
 ┣ 📜 requirements.txt
 ┗ 📜 README.md

🖥️ How It Works

Load Data → analysis.py

Clean Data & Calculate KPIs

Generate Plots → visualizations.py

Run Forecasts → forecasting.py (SMA + Prophet)

Detect Anomalies → anomaly_detection.py

Build HTML Dashboard → generate_report.py

📸 Sample Dashboard Preview

(Sample preview — real dashboard contains interactive business insights)

⚙️ Installation
# Clone repository
git clone https://github.com/SushminiS/Ecommerce_Sales_Intelligence_Reports.git
cd ecommerce-sales-intelligence

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

▶️ Usage
python main.py


This will:

Generate all KPIs & plots

Run sales forecasts

Detect anomalies

Save a styled report.html in your project folder

📊 Tech Stack

Python 3.9+

Pandas — Data manipulation

Matplotlib & Seaborn — Visualizations

Prophet — Time-series forecasting

Scikit-learn — Anomaly detection

HTML + CSS — Styled dashboard output

🔒 Repository Privacy

This project is private on GitHub — visible only to you and collaborators you invite.

✨ Author

Your Name
📧 sushminisunilkumar@gmail.com
💼 LinkedIn

📌 Future Improvements

Add interactive dashboard using Streamlit or Plotly Dash

Deploy report generation as a FastAPI microservice

Integrate live data from an API or database

📜 License

This project is private and not licensed for public use.