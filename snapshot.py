import os
import yfinance as yf
from datetime import date
from dateutil.relativedelta import relativedelta

end = str(date.today())
start = str(date.today() + relativedelta(months=-6))

with open('symbols.csv') as f:
    lines = f.read().splitlines()
    for symbol in lines:
        print(symbol)
        data = yf.download(symbol, start=start, end=end)
        data.to_csv("datasets/{}.csv".format(symbol))
