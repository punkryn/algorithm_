import ccxt
from datetime import datetime
import math
import time

apiKeyValue = ''
secretValue = ''

with open('./apikey.txt', 'r') as aktr:
    rl = aktr.readlines()
    for i, line in enumerate(rl):
        if 'api key' in line:
            apiKeyValue = rl[i + 1].strip()
        if 'secret key' in line:
            secretValue = rl[i + 1].strip()



binance = ccxt.binance({
            'apiKey': apiKeyValue,
            'secret': secretValue,
            'enableRateLimit': True,
            'options': {
                'defaultType': 'future',  # ←-------------- quotes and 'future'
            },
        })

symbol = 'BTC/USDT'

ohlcvs = binance.fetch_ohlcv(symbol, '1d')

for ohlc in ohlcvs:
    print(datetime.fromtimestamp(ohlc[0]/1000).strftime('%Y-%m-%d %H:%M:%S'), end=' ')
    print(ohlc[1:])

totalU = 0
totalD = 0

high = 2
low = 3
for i in range(-1, -16, -1):
    print(datetime.fromtimestamp(ohlcvs[i][0] / 1000).strftime('%Y-%m-%d %H:%M:%S'), end=' ')
    print(ohlcvs[i][1:])

    if ohlcvs[i-1][high] < ohlcvs[i][high]:
        totalU += (ohlcvs[i][high] - ohlcvs[i-1][high])
        #print(1, ohlcvs[i][high], ohlcvs[i-1][high])
    elif ohlcvs[i-1][low] < ohlcvs[i][low]:
        la = (ohlcvs[i-1][high] - ohlcvs[i-1][low]) / 2
        ta = (ohlcvs[i][high] - ohlcvs[i][low]) / 2
        if la < ta:
            totalU += (ta - la)
            #print(2)
        else:
            totalD += (la - ta)
            #print(3, ohlcvs[i][high], ohlcvs[i-1][high])
    else:
        totalD += (ohlcvs[i-1][low] - ohlcvs[i][low])
        #print(4)

print('totalU', totalU, 'totalD', totalD, 'AU', totalU/7, 'DU', totalD/7)
AU = totalU/7
AD = totalD/7
RS = AU/AD
RSI = (AU / (AU + AD)) * 100
print('RS', RS, 'RSI', RSI)

totalClose = 0
close = 4
for i in range(-2, -9, -1):
    print(datetime.fromtimestamp(ohlcvs[i][0] / 1000).strftime('%Y-%m-%d %H:%M:%S'), end=' ')
    print(ohlcvs[i][1:])

    totalClose += ohlcvs[i][close]

print('ma', totalClose / 7)

print(math.floor((round(3.12345, 4) * 10**4) / 10 ) / 10 ** 3)

orders = binance.fetch_orders(symbol)
print(len(orders))
for order in orders:
    print(order)

while True:
    ohlcvs = binance.fetch_ohlcv(symbol, '1d')
    for i in range(-1, -3, -1):
        print(datetime.fromtimestamp(ohlcvs[i][0] / 1000).strftime('%Y-%m-%d %H:%M:%S'), end=' ')
        print(ohlcvs[i][1:])

        fi = ohlcvs[i][-1] * (ohlcvs[i][-2] - ohlcvs[i-1][-2])
        print('fi', fi)
    time.sleep(2)