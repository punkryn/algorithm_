import ccxt
import time
import datetime
import math

class oneButton():
    def __init__(self, apiKey, secret):
        self.apiKey = apiKey
        self.secret = secret

        self.orderId = None
        self.orderPrice = None

        self.order = None

        self.leverage = 10

        self.sell_price = None
        self.buy_price = None
        self.unit = None

        self.cancelSuccess = False
        self.cancelFail = False

        self.binance = self.init_binance()

        self.market = self.binance.load_markets()
        print(self.market)
        self.balance = self.binance.fetch_balance()
        print(self.balance['USDT']['free'])

    def init_binance(self):
        binance = ccxt.binance({
            'apiKey': self.apiKey,
            'secret': self.secret,
            'enableRateLimit': True,
            'options': {
                'defaultType': 'future',  # ←-------------- quotes and 'future'
            },
        })

        return binance

    def buy_crypto_currency(self, ticker, symbol):
        used = self.balance[ticker]['used']
        free = self.balance[ticker]['free']
        print('free', free)
        if free >= 1 and used < 0.1:
            orderbook = self.binance.fetch_order_book(symbol)
            self.sell_price = orderbook['asks'][0][0]
            print('sell_price', self.sell_price)

            self.unit = self.make_float(round((free / float(self.sell_price)) * self.leverage, 4))
            print('unit', self.unit)
            try:
                self.order = self.binance.create_limit_buy_order(symbol, self.unit, self.sell_price)
                print('buy success')
                return self.order
            except:
                print('buy fail')
                return -1
        else:
            orderbook = self.binance.fetch_order_book(symbol)
            self.sell_price = orderbook['asks'][0][0]
            print('sell_price', self.sell_price)

            self.unit = self.make_float(round((used / float(self.sell_price)) * self.leverage, 4))
            print('unit', self.unit)
            try:
                self.order = self.binance.create_limit_buy_order(symbol, self.unit, self.sell_price)
                print('buy success')
                return self.order
            except:
                print('buy fail')
                return -1


    def sell_crypto_currency(self, ticker, symbol):
        used = self.balance[ticker]['used']
        free = self.balance[ticker]['free']
        print('used', used)
        print('free', free)
        if used >= 0.1:
            orderbook = self.binance.fetch_order_book(symbol)
            self.buy_price = orderbook['bids'][0][0]
            print('buy_price', self.buy_price)

            self.unit = self.make_float(round((used / float(self.buy_price)) * self.leverage, 4))
            print('unit', self.unit)
            try:
                self.order = self.binance.create_limit_sell_order(symbol, self.unit, self.buy_price)
                print('sell success')
                return self.order
            except:
                print('sell fail')
                return -1
        else:
            orderbook = self.binance.fetch_order_book(symbol)
            self.buy_price = orderbook['bids'][0][0]
            print('buy_price', self.buy_price)

            self.unit = self.make_float(round((free / float(self.buy_price)) * self.leverage, 4))
            print('unit', self.unit)
            try:
                self.order = self.binance.create_limit_sell_order(symbol, self.unit, self.buy_price)
                print('sell success')
                return self.order
            except:
                print('sell error')
                return -1



    def cancel(self, symbol, flow):
        orders = self.binance.fetch_orders(symbol)
        total = len(orders)
        self.orderId = orders[flow]['info']['orderId']
        self.orderPrice = orders[flow]['info']['price']
        if orders[flow]['info']['status'] == 'NEW' or flow == -10:
            try:
                resp = self.binance.cancel_order(self.orderId, symbol)
                print('cancel success')
                print(resp)
                self.cancelSuccess = True
                return resp
            except:
                print('cancel fail')
                self.cancelFail = True
                return -1
        else:
            self.cancel(symbol, flow-1)
            self.cancelFail = True




    def make_float(self, num):
        return (math.floor((num * 10 ** 4) / 10) / 10 ** 3)

