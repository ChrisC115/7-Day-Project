import pandas as pd
import yfinance as yf
import matplotlib.pyplot as mplt

def Strategy(stock):
    cash = 1000.0  # Use floats for trading math
    shares = 0.0
    buy = False
    
    # Download data with proper multi-level index handling
    df = yf.download(stock, period="12mo", auto_adjust=False, multi_level_index=False)
    
    # Calculate Moving Averages
    df["ma_10"] = df["Adj Close"].rolling(window=10).mean()
    df["ma_50"] = df["Adj Close"].rolling(window=50).mean()
    df = df.dropna()

    for i in range(len(df) - 1):
        price = df["Adj Close"].iloc[i]
        next_day_open = df["Open"].iloc[i+1]
        
        # Buy Logic: Price above both MAs and not already holding
        if (price > df["ma_10"].iloc[i]) and (price > df["ma_50"].iloc[i]) and not buy:
            buy = True
            shares = cash / (next_day_open * 1.001) # Including tax
            cash = 0.0
            
        # Sell Logic: Price falls below 10MA
        elif (price < df["ma_10"].iloc[i]) and buy:
            buy = False
            cash = shares * (next_day_open * 0.999) # Including tax
            shares = 0.0

    # Final valuation
    current_price = df["Adj Close"].iloc[-1]
    total_value = cash + (shares * current_price)
    profit = total_value - 1000
    
    print(f"Final Value: ${round(total_value, 2)}")
    print(f"Total profit: ${round(profit, 2)}")
    print(f"Percent profit: {round((profit / 1000) * 100, 2)}%")

def Main():
    ticker = input("What stock do you want to test? (e.g., AAPL): ")
    Strategy(ticker)

if __name__ == "__main__":
    Main()
