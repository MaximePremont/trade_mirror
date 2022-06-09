##
## EPITECH PROJECT, 2022
## B-CNA-410-LYN-4-1-trade-ahmed.abouelleil-sayed
## File description:
## strategy_dumb
##

# from distutils.util import byte_compile
# import sys
# from datetime import datetime
import actions
import statistics

def buyConditionBo(self, upperBand, lowerBand):
    if actions.getCurrencyPrice(self, "USDT", "BTC") < lowerBand:
        return True
    return False

def sellConditionBo(self, upperBand, lowerBand):
    if actions.getCurrencyPrice(self, "USDT", "BTC") > upperBand:
        return True
    return False

def getTrend(self, period):
    actual = statistics.mean(self.charts["USDT_BTC"].closes[-period:])
    before = statistics.mean(self.charts["USDT_BTC"].closes[2 * -period:])
    if actual > before:
        return 1
    else:
        return 0

def everything(self, period, risk):
    # time = datetime.fromtimestamp(self.date)
    # print(time, flush=True, file=sys.stderr)
    usd = "USDT"
    btc = "BTC"
    money = self.stacks["USDT"]
    money_btc = self.stacks["BTC"]
    btcPrice = actions.getCurrencyPrice(self, usd, btc)
    amount = money
    toSell = money_btc

    if self.first:
        self.first = False
        self.ma.extend(self.charts["USDT_BTC"].closes)

    # TREND
    trend = getTrend(self, period)
    # print(f"TREND  ==> {trend}", flush=True, file=sys.stderr)

    # RATIO 
    ratio = btcPrice / statistics.mean(self.charts["USDT_BTC"].closes[-period:])
    if ratio > 1.07 and actions.canUseXCurrency(self, toSell, btc) and toSell > 0.01:
        self.sellXOfTo(toSell, usd, btc, 1, btcPrice)
    if trend == 1:
        if ratio < 0.93 and actions.canUseXCurrency(self, amount, usd) and amount > 0.01:
            finalAmount = actions.currencyConverter(self, amount, usd, btc)
            if finalAmount < 0.01:
                self.doNothing()
                return
            self.purchasePrice.append(btcPrice)
            self.buyXFromTo(finalAmount, usd, btc, 1, btcPrice)
            return
    elif risk == True:
        if ratio < 0.93 and actions.canUseXCurrency(self, amount, usd) and amount > 0.01:
            finalAmount = actions.currencyConverter(self, amount, usd, btc)
            if finalAmount < 0.01:
                self.doNothing()
                return
            self.purchasePrice.append(btcPrice)
            self.buyXFromTo(finalAmount, usd, btc, 1, btcPrice)
            return

    # BOLLINGER
    ma20 = statistics.mean(self.charts["USDT_BTC"].closes[-period:])
    if len(self.charts["USDT_BTC"].closes[-period:]) > 2:
        upperBand = ma20 + (2 * statistics.stdev(self.charts["USDT_BTC"].closes[-period:]))
        lowerBand = ma20 - (2 * statistics.stdev(self.charts["USDT_BTC"].closes[-period:]))
    else:
        upperBand = btcPrice
        lowerBand = btcPrice

    # DUMB
    sellRatio = 1
    if (len(self.purchasePrice) > 0):
        sellRatio = btcPrice / self.purchasePrice[-1]
    # print(f"SELL RATIO  ==> {sellRatio}", flush=True, file=sys.stderr)
    if sellRatio > 1.07 and actions.canUseXCurrency(self, toSell, btc) and toSell > 0.01:
        self.sellXOfTo(toSell, usd, btc, 1, btcPrice)
    if sellRatio < 0.93 and actions.canUseXCurrency(self, toSell, btc) and toSell > 0.01:
        finalAmount = actions.currencyConverter(self, amount, usd, btc)
        if finalAmount < 0.01:
            self.doNothing()
            return
        self.purchasePrice.appennd(btcPrice)
        self.buyXFromTo(finalAmount, usd, btc, 1, btcPrice)
        return


    # Volume
    volume = self.charts["USDT_BTC"].volumes[-1]
    if trend == 1 and buyConditionBo(self, upperBand, lowerBand) and ratio < 1 and actions.canUseXCurrency(self, amount, usd):
        finalAmount = actions.currencyConverter(self, amount, usd, btc)
        if finalAmount < 0.01:
            self.doNothing()
            return
        self.purchasePrice.append(btcPrice)
        self.buyXFromTo(finalAmount, usd, btc, 1, btcPrice)
    elif risk == True and buyConditionBo(self, upperBand, lowerBand) and ratio < 1 and actions.canUseXCurrency(self, amount, usd):
        finalAmount = actions.currencyConverter(self, amount, usd, btc)
        if finalAmount < 0.01:
            self.doNothing()
            return
        self.purchasePrice.append(btcPrice)
        self.buyXFromTo(finalAmount, usd, btc, 1, btcPrice)
    elif sellConditionBo(self, upperBand, lowerBand) and ratio > 1 and actions.canUseXCurrency(self, toSell, btc) and toSell > 0.01:
        self.sellXOfTo(toSell, usd, btc, 1, btcPrice)
    else:
        self.doNothing()
