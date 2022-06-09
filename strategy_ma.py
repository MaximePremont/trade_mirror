# Algo.py trade Epitech

import actions
import statistics

def buyCondition(self, longVal, shortVal):
    shortTerm = statistics.mean(self.ma[-shortVal:])
    longTerm = statistics.mean(self.ma[-longVal:])
    shortTermBefore = statistics.mean(self.ma[-shortVal - 1:-1])
    longTermBefore = statistics.mean(self.ma[-longVal - 1:-1])

    if (shortTerm != -1 and shortTermBefore != -1 and longTerm != -1 and longTermBefore != -1):
        if (shortTerm > longTerm) and (shortTermBefore < longTermBefore):
            return True
    return False

def sellCondition(self, longVal, shortVal):
    shortTerm = statistics.mean(self.ma[-shortVal:])
    longTerm = statistics.mean(self.ma[-longVal:])
    shortTermBefore = statistics.mean(self.ma[-shortVal - 1:-1])
    longTermBefore = statistics.mean(self.ma[-longVal - 1:-1])
    if (shortTerm != -1 and shortTermBefore != -1 and longTerm != -1 and longTermBefore != -1):
        if (shortTerm < longTerm) and (shortTermBefore > longTermBefore):
            return True
    return False

def maStrat(self, longVal, shortVal):
    # time = datetime.fromtimestamp(self.date)
    # print(time, flush=True, file=sys.stderr)
    # print(self.stacks, flush=True, file=sys.stderr)
    usd = "USDT"
    btc = "BTC"
    money = self.stacks["USDT"]
    money_btc = self.stacks["BTC"]
    btcPrice = actions.getCurrencyPrice(self, usd, btc)
    if self.first:
        self.first = False
        self.ma.extend(self.charts["USDT_BTC"].closes)
    self.ma.append(btcPrice)
    amount = money
    if btcPrice < statistics.mean(self.charts["USDT_BTC"].closes[-30:]):
        amount = money - (money * 0.2)
    if buyCondition(self, longVal, shortVal) and actions.canUseXCurrency(self, amount, usd):
        finalAmount = actions.currencyConverter(self, amount, usd, btc)
        self.buyXFromTo(finalAmount, usd, btc, 1, btcPrice)
    elif sellCondition(self, longVal, shortVal) and actions.canUseXCurrency(self, money_btc, btc):
        self.sellXOfTo(money_btc, usd, btc, 1, btcPrice)
    else:
        self.doNothing()