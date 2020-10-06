import os, pandas

targets_100 = []
targets_20 = []
targets_high = []

for filename in os.listdir('datasets'):
    #print(filename)
    symbol = filename.split(".")[0]
    #print(symbol)
    df = pandas.read_csv('datasets/{}'.format(filename))
    if df.empty:
        continue

    try:
        if df.iloc[-2].Close < 20:
            print("{} is a below $20 target".format(symbol))
            targets_20.append(symbol)
        elif df.iloc[-2].Close < 100:
            print("{} is a below $100 target".format(symbol))
            targets_100.append(symbol)
        else:
            print("{} is above $100".format(symbol))
            targets_high.append(symbol)
    except:
        pass

targets_20.sort()
targets_100.sort()
targets_high.sort()

with open('20_targets.csv', 'w') as file:
    for line in targets_20:
        file.write(line + '\n')
  
with open('100_targets.csv', 'w') as file:
    for line in targets_100:
        file.write(line + '\n')

with open('high_targets.csv', 'w') as file:
    for line in targets_high:
        file.write(line + '\n')