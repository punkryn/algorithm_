import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

import onebutton

form_class = uic.loadUiType("tradingbot.ui")[0]

class testDialog(QMainWindow, form_class):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.apiKeyValue = None
        self.secretValue = None

        self.buy.clicked.connect(self.buy_crypto_currency)
        self.sell.clicked.connect(self.sell_crypto_currency)
        self.cancel_btn.clicked.connect(self.cancel)

        self.get_apiKey_from_text()
        self.apiKey.setText(self.apiKeyValue)
        self.secret.setText(self.secretValue)

        self.symbol.setText('BTC/USDT')
        self.ticker.setText('USDT')

        self.ob = onebutton.oneButton(self.apiKey.text(), self.secret.text())
        self.log.append('잔고' + '(' + self.ticker.text() + ')' + ': ' + str(self.ob.balance[self.ticker.text()]['free']))

    def get_apiKey_from_text(self):
        with open('./apikey.txt', 'r') as aktr:
            rl = aktr.readlines()
            for i, line in enumerate(rl):
                if 'api key' in line:
                    self.apiKeyValue = rl[i+1].strip()
                if 'secret key' in line:
                    self.secretValue = rl[i+1].strip()

        return self.apiKeyValue, self.secretValue

    def buy_crypto_currency(self):
        print(1)
        self.log.append('매수중...')
        #try:
        self.ob = onebutton.oneButton(self.apiKey.text(), self.secret.text())
        order = self.ob.buy_crypto_currency(self.ticker.text(), self.symbol.text())
        if order == -1:
            self.log.append('주문실패')
        else:
            self.log.append('매도호가' + '(' + self.symbol.text() + ')' + ': ' + str(self.ob.sell_price))
            self.log.append('수량' + '(' + self.symbol.text() + ')' + ': ' + str(self.ob.unit) + '\n')
            self.log.append('잔고' + '(' + self.ticker.text() + ')' + ': ' + str(self.ob.balance[self.ticker.text()]['free']))
        #except:
            #self.log.append('매수실패')

        return order

    def sell_crypto_currency(self):
        self.log.append('매도중...')
        #try:
        self.ob = onebutton.oneButton(self.apiKey.text(), self.secret.text())
        order = self.ob.sell_crypto_currency(self.ticker.text(), self.symbol.text())
        if order == -1:
            self.log.append('주문실패')
        else:
            self.log.append('매수호가' + '(' + self.symbol.text() + ')' + ': ' + str(self.ob.buy_price))
            self.log.append('수량' + '(' + self.symbol.text() + ')' + ': ' + str(self.ob.unit) + '\n')
            self.log.append('남은개수' + '(' + self.ticker.text() + ')' + ': ' + str(self.ob.balance[self.ticker.text()]['free']))
        #except:
            #self.log.append('매도실패')

        return order

    def cancel(self):
        self.ob = onebutton.oneButton(self.apiKey.text(), self.secret.text())

        resp = self.ob.cancel(self.symbol.text(), -1)
        print('resp', resp)
        if self.ob.cancelSuccess == True:
            self.log.append('주문취소ID' + '(' + self.symbol.text() + ')' + ': ' + str(self.ob.orderId))
            self.log.append('주문취소가격' + '(' + self.symbol.text() + ')' + ': ' + str(self.ob.orderPrice))
        else:
            self.log.append('주문취소실패')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dl = testDialog()
    dl.show()
    app.exec_()
    sys.exit(app.closeAllWindows())
