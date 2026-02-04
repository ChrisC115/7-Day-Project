import pandas as pd
import yfinance as yf
import matplotlib.pyplot as mplt 

x = 0
Cash = 1000
Bal = 0
dat = yf.Ticker("AAPL")
df = pd.DataFrame(dat.history(period='12mo'))

df["ma_10"] = df["Close"].rolling(window=10).mean()
df["ma_50"] = df["Close"].rolling(window=50).mean()

df = df.dropna()

'''Strat Function'''

for i in range(len(df)):
    if (df["Close"].iloc[i] > df["ma_10"].iloc[i]) & (df["Close"].iloc[i] > df["ma_50"].iloc[i]):
        x = x + 1
        print(x)

'''Buy Function'''

def Buy() :
    Cash = Cash-100
    Bal = 100
