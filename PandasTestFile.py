import pandas as pd
import yfinance as yf
import matplotlib.pyplot as mplt 

Cash = 1000
Profit = 0
Shares = 0
buy = 0
dat = yf.Ticker("AAPL")
df = pd.DataFrame(dat.history(period='12mo'))

df["ma_10"] = df["Close"].rolling(window=10).mean()
df["ma_50"] = df["Close"].rolling(window=50).mean()

df = df.dropna()

'''Strat Function'''

for i in range(len(df)):
    price = df["Close"].iloc[i]
    
    if (price > df["ma_10"].iloc[i]) and (price > df["ma_50"].iloc[i]) and buy == 0:
        buy = 1
        Shares = Cash / price 
        Cash = 0

    elif (price < df["ma_10"].iloc[i]) and buy == 1:
        buy = 0
        Cash = Shares * price 
        Shares = 0



current_price = df["Close"].iloc[-1]
Total_Value = Cash + (Shares * current_price)
Profit = Total_Value - 1000

print("Final Value: $" + str(round(Total_Value, 2)))
print("Total Profit: $" + str(round(Profit, 2)))
print("Percent Profit: %" + str(round((Profit / 1000) * 100, 2)))
