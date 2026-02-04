import pandas as pd
import yfinance as yf
import matplotlib.pyplot as mplt 

dat = yf.Ticker("AAPL")
df = pd.DataFrame(dat.history(period='12mo'))

df["ma_10"] = df["Close"].rolling(window=10).mean()
df["ma_50"] = df["Close"].rolling(window=50).mean()


print(df[["Open","Close","ma_10","ma_50"]].dropna())


for _ in len(df):
    if df["Close"] > df["ma_10"] & df["ma_50"]:
        print("Hello")