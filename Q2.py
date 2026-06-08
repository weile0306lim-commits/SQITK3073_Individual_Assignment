import pandas as pd

#Read the CSV file from Q1
df = pd.read_csv("stock_analysis.csv")

#Question 2(a): Data Filtering Using Pandas Slicing
portfolio_summary = df.loc[:,[
    "Ticker",
    "Previous Closing Price (RM)",
    "Latest Closing Price (RM)",
    "Estimated Total Return (RM)",
    "Return Percentage (%)"
    ]
]

print("PORTFOLIO SUMMARY TABLE")
print(portfolio_summary)

#Question 2(b): GroupBy Analysis
#Function for classifying performance categories based on return percentage
def classify_performance(return_percentage):
    if return_percentage<0:
        return "Negative Return"
    elif return_percentage<=2:         #elif 0<=return_percentage<=2:
        return "Moderate Return"
    else:
        return "High Return"
    
df["Performance Category"] = df["Return Percentage (%)"].apply(classify_performance)
print("\nPORTFOLIO PERFORMANCE CATEGORIES")
print(df[
    [
        "Ticker", 
        "Return Percentage (%)", 
        "Performance Category"
        ]
])

#GroupBy analysis
group_summary = df.groupby("Performance Category")["Estimated Total Return (RM)"].mean().reset_index()
print("\nGROUP BY SUMMARY")
print(group_summary)
