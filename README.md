📊 Technical Analysis Dashboard
📜 Description
This Python-based Technical Analysis Dashboard application is designed to analyze and visualize stock data. Utilizing Plotly, yfinance, and TA-Lib libraries, it dynamically visualizes price movements and technical analysis indicators.

🚀 Features
📈 Candlestick Chart: Provides a detailed view of stock price movements.
🔵 Simple Moving Average (SMA): Displays the 20-day average of price movements.
🟢 Exponential Moving Average (EMA): Calculates the 15-day exponential average of price movements.
📊 Bollinger Bands: Analyzes price volatility with upper, middle, and lower bands.
📉 RSI (Relative Strength Index): Shows overbought or oversold conditions of the price.
💻 Installation
Install the required libraries using the following command:

pip install plotly yfinance TA-Lib
🔧 Usage
Clone or download the project.

Open the technical_analysis_dashboard.py file and import the necessary libraries.

Run the application with:

python technical_analysis_dashboard.py
Enter the stock ticker symbol and start date.

📝 Example Usage

if __name__ == "__main__":
    ticker = input("Please enter the stock ticker symbol: ")
    start_date = input("Please enter the start date (YYYY-MM-DD)")
    dashboard = TechnicalAnalysisDashboard(ticker, start_date)
    dashboard.calculate_indicators()
    dashboard.create_plot()


🌐 License
This project is licensed under the MIT License. See the LICENSE File for details.