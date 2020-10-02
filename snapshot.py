import os
import yfinance as yf

with open('symbols.csv') as f:
    lines = f.read().splitlines()
    for symbol in lines:
        print(symbol)
        data = yf.download(symbol, start="2020-01-01", end="2020-10-01")
        data.to_csv("datasets/{}.csv".format(symbol))
