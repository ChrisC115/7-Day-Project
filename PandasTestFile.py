import pandas as pd
import yfinance as yf
import matplotlib.pyplot as mplt 

dat = yf.Ticker("AAPL")
print(dat.history(period='12mo'))
