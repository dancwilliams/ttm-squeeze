import os, pandas

targets_100 = []
targets_20 = []

for filename in os.listdir('datasets'):
    #print(filename)
    symbol = filename.split(".")[0]
    #print(symbol)
    df = pandas.read_csv('datasets/{}'.format(filename))
    if df.empty:
        continue

if df.iloc[-2].Close < 20:
    print("{} is a below $20 target".format(symbol))
    targets_20.append(symbol)
elif df.iloc[-2].Close < 100:
    print("{} is a below $100 target".format(symbol))
    targets_100.append(symbol)

with open('20_targets.csv', 'w') as file:
    for line in targets_20:
        file.write(line)

with open('100_targets.csv', 'w') as file:
    for line in targets_100:
        file.write(line)