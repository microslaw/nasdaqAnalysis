import yfinance as yf
import pandas as pd

## nasdaq list: https://www.slickcharts.com/nasdaq100

nasdaq_top_10 = ["AAPL", "NVDA", "MSFT", "AMZN", "AVGO", "TSLA", "META", "GOOGL", "GOOG", "COST"]

start_date = "2021-01-01"
end_date = "2021-12-31"

all_stock_data = pd.DataFrame()

for ticker in nasdaq_top_10:
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    stock_data.reset_index(inplace=True)
    stock_data = stock_data[["Date", "Open", "High", "Low", "Close", "Volume"]]
    stock_data.columns = ["date", "open", "high", "low", "close", "volume"] 
    stock_data["company"] = ticker  
    all_stock_data = pd.concat([all_stock_data, stock_data], ignore_index=True)

all_stock_data.to_csv("nasdaq_top_10_stock_data_2021.csv", index=False)


