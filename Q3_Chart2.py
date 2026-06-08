import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

df = pd.read_csv("stock_analysis.csv")
colors = []

#Chart2: Portfolio Performance Comparison
for value in df["Return Percentage (%)"]:
    if value < 0:
        colors.append("red")
    else:
        colors.append("green")

plt.figure(figsize=(10, 6))

plt.bar(df["Ticker"],
        df["Return Percentage (%)"],
        color=colors)

plt.title("Return Percentage Comparison of Selected Bursa Malaysia Stocks")
plt.xlabel("Ticker")
plt.ylabel("Return Percentage (%)")

for i, value in enumerate(df["Return Percentage (%)"]):
    plt.text(
        i, 
        value, 
        f"{value}%", 
        ha="center", 
        va="bottom")

# Create custom legend entries
red_patch = mpatches.Patch(color="red", label="Negative Return")
green_patch = mpatches.Patch(color="green", label="Positive Return")
plt.legend(handles=[red_patch, green_patch])

plt.show()
