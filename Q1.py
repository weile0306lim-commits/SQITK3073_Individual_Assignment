import yfinance as yf
import pandas as pd

stocks = {
    "Maybank": "1155.KL",
    "Maxis": "6012.KL", 
    "Inari": "0166.KL",
    "Tenaga Nasional": "5347.KL",
    "Sunway": "5211.KL"
}

results = []
all_data=[]

for stock_name, ticker in stocks.items():
   
   #Download 1 month stock data
    data= yf.download(ticker,
                      start="2026-05-01",
                      end="2026-06-01",
                      progress = False)
    
      # Flatten MultiIndex columns
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    
    data = data.reset_index()

    # Rename index column to Date if needed
    if "index" in data.columns:
        data = data.rename(columns={"index": "Date"})

    data = data[["Date", "Open", "High", "Low", "Close", "Volume"]]

    data["Stock"]=stock_name
    data["Ticker"] = ticker

    all_data.append(data)

    #Yesterday closing price
    yesterday_close = data["Close"].iloc[-2].item()

    #Today closing price
    today_close = data["Close"].iloc[-1].item()

    #Daily return
    daily_return=today_close-yesterday_close

    #Share purchaseble with RM1000
    shares=1000/yesterday_close

    #Estimated total return
    estimated_return=daily_return*shares

    #Return percentage
    return_percentage=(estimated_return/1000)*100

    results.append({
        "Stock": stock_name,
        "Ticker": ticker,
        "Previous Closing Price (RM)": round(yesterday_close, 2),
        "Latest Closing Price (RM)": round(today_close, 2),
        "Daily Return (RM)": round(daily_return, 2),
        "Shares Purchasable with RM1000": round(shares, 2),
        "Estimated Total Return (RM)": round(estimated_return, 2),
        "Return Percentage (%)": round(return_percentage, 2)
    })

#Save raw 1 month data to CSV for all stocks
raw_data =pd.concat(all_data, ignore_index=True)
raw_data.to_csv("bursa_1month_data.csv", index=False)

#Save analysis results to CSV
df = pd.DataFrame(results)
print(df)
df.to_csv("stock_analysis.csv", index=False)
