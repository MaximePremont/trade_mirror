##
## EPITECH PROJECT, 2022
## B-CNA-410-LYN-4-1-trade-ahmed.abouelleil-sayed
## File description:
## strategy_dumb
##

# import sys
# from datetime import datetime
# from typing import final
import actions
import statistics

def dumb(self, period):
    # time = datetime.fromtimestamp(self.date)
    usd = "USDT"
    btc = "BTC"
    money = self.stacks["USDT"]
    money_btc = self.stacks["BTC"]
    btcPrice = actions.getCurrencyPrice(self, usd, btc)

    ratio = btcPrice / statistics.mean(self.charts["USDT_BTC"].closes[-period:])
    # print("RATIO ->", ratio, flush=True, file=sys.stderr)
    amount = money
    toSell = money_btc
    if ratio < 1.1 or ratio > 0.9 :
        amount = money / 2
        toSell = money_btc / 2
    if ratio < 1 and actions.canUseXCurrency(self, amount, usd):
        finalAmount = actions.currencyConverter(self, amount, usd, btc)
        if finalAmount < 0.01:
            self.doNothing()
            return
        self.buyXFromTo(finalAmount, usd, btc, 1, btcPrice)
    elif ratio > 1 and actions.canUseXCurrency(self, toSell, btc) and toSell > 0.01:
        self.sellXOfTo(toSell, usd, btc, 1, btcPrice)
    else:
        self.doNothing()
