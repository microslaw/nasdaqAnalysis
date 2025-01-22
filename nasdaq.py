import yfinance as yf
import pandas as pd

## nasdaq list: https://www.slickcharts.com/nasdaq100


def load_nasdaq_data():
    nasdaq_top_10 = [
        "AAPL",
        "NVDA",
        "MSFT",
        "AMZN",
        "AVGO",
        "TSLA",
        "META",
        "GOOGL",
        "GOOG",
        "COST",
    ]

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

    all_stock_data[["open", "high", "low", "close", "volume"]] = all_stock_data[
        ["open", "high", "low", "close", "volume"]
    ].round(2)

    short_to_full = {
        "AAPL": "Apple Inc.",
        "NVDA": "NVIDIA Corporation",
        "MSFT": "Microsoft Corporation",
        "AMZN": "Amazon.com, Inc.",
        "AVGO": "Broadcom Inc.",
        "TSLA": "Tesla, Inc.",
        "META": "Meta Platforms, Inc.",
        "GOOGL": "Alphabet Inc. (Class A)",
        "GOOG": "Alphabet Inc. (Class C)",
        "COST": "Costco Wholesale Corporation",
    }

    all_stock_data["company"] = all_stock_data["company"].replace(short_to_full)
    
    all_stock_data.to_csv("nasdaq_top_10_stock_data_2021.csv", index=False)
