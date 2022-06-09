##
## EPITECH PROJECT, 2022
## B-CNA-410-LYN-4-1-trade-ahmed.abouelleil-sayed
## File description:
## strategy_shortMomentum
##

import actions
import statistics

def getTrend(self, period):
    actual = statistics.mean(self.charts["USDT_BTC"].closes[-period:])
    before = statistics.mean(self.charts["USDT_BTC"].closes[-period - 3:])
    if actual > before:
        return 1
    else:
        return 0

def followTrend(self, period):
    usd = "USDT"
    btc = "BTC"
    money = self.stacks["USDT"]
    money_btc = self.stacks["BTC"]
    btcPrice = actions.getCurrencyPrice(self, usd, btc)

    if self.first:
        self.first = False
        self.initialDate = self.date
        return
    amount = 100
    if getTrend(self, period) == 1 and money >= amount:
        finalAmount = actions.currencyConverter(self, amount, usd, btc)
        self.buyXFromTo(finalAmount, usd, btc, 1, btcPrice)
    elif getTrend(self, period) == 1 and money_btc > 0:
        self.sellXOfTo(money_btc, usd, btc, 1, btcPrice)
    else:
        self.doNothing()
