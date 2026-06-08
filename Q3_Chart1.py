import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

stocks = {
    "Maybank": "1155.KL",
    "Maxis": "6012.KL", 
    "Inari": "0166.KL",
    "Tenaga Nasional": "5347.KL",
    "Sunway": "5211.KL"
}

plt.figure(figsize=(12, 6))

for stock_name, ticker in stocks.items():
    data = yf.download(ticker,
                       start="2026-05-01",
                       end="2026-06-01",
                       progress=False)
    
    plt.plot(
        data.index, 
        data["Close"],
        label=stock_name)
    
plt.title("Closing Price Trends of Selected Bursa Malaysia Stocks (May 2026)")
plt.xlabel("Date")
plt.ylabel("Closing Price (RM)")
plt.legend()
plt.grid(True)
plt.show()