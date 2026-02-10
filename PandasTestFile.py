import pandas as pd
import yfinance as yf
import matplotlib.pyplot as mplt 

def Strategy(ticker) :
    cash = float(1000)
    profit = int(0)
    shares = 0
    buy = False
    df = yf.download(ticker, period = "12mo", auto_adjust = False, multi_level_index= False)

    df["ma_10"] = df["Adj Close"].rolling(window=10).mean()
    df["ma_50"] = df["Adj Close"].rolling(window=50).mean()
    df = df.dropna()
    df["daily_return"] = df["Adj Close"].pct_change()



    for i in range(len(df)-1):
        price = df["Adj Close"].iloc[i]
    
        if (price > df["ma_10"].iloc[i]) and (price > df["ma_50"].iloc[i]) and buy == False:
            buy = bool(True)
            shares = cash / (df["Open"].iloc[i+1] * 1.001) #This is for buying on next day to remove same day buying bias and the 0.001 percent increase is for trading tax
            cash = int(0)

        elif (price < df["ma_10"].iloc[i]) and buy == True:
            buy = bool(False)
            cash = shares * (df["Open"].iloc[i+1] * 0.999) #Sell on the next day to remove same day bias, -0.001 equals trading tax
            shares = int(0)



    current_price = df["Adj Close"].iloc[-1]
    Total_Value = float(cash + (shares * current_price))
    profit = float(Total_Value - 1000)
    
    print(df["daily_return"])
    print("Standard Deviation: " + str(print(df["daily_return"].std())))
    print("Final Value: $" + str(round(Total_Value, 2)))
    print("Total profit: $" + str(round(profit, 2)))
    print("Percent profit: %" + str(round((profit / 1000) * 100, 2)))


def Main():
    ticker = input("What stock do you want to test? (e.g., AAPL): ")
    Strategy(ticker)

Main()