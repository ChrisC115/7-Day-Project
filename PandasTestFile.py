import pandas as pd
import yfinance as yf
import matplotlib.pyplot as mplt 

dat = yf.Ticker("AAPL")
print(dat.history(period='12mo'))
df = pd.DataFrame(dat.history(period='12mo'))

print("\nSimple Day Moving Average 10 Day","\n\n\n",(df.rolling(window=10).mean()))

print("\nSimple Day Moving Average 50 Day","\n\n\n",(df.rolling(window=50).mean()))