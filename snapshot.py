import os
import yfinance as yf
from datetime import date
from dateutil.relativedelta import relativedelta

end = str(date.today() + relativedelta(days=-1))
start = str(date.today() + relativedelta(months=-12))

if not os.path.exists("datasets"):
        os.mkdir("datasets")

with open('SP500_symbols.csv') as f:
    lines = f.read().splitlines()
    for symbol in lines:
        print(symbol)
        data = yf.download(symbol, start=start, end=end)
        data.to_csv("datasets/{}.csv".format(symbol))

with open('Russell2000_symbols.csv') as f:
    lines = f.read().splitlines()
    for symbol in lines:
        print(symbol)
        data = yf.download(symbol, start=start, end=end)
        data.to_csv("datasets/{}.csv".format(symbol))
