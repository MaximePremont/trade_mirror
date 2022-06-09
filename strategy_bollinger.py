##
## EPITECH PROJECT, 2022
## B-CNA-410-LYN-4-1-trade-ahmed.abouelleil-sayed
## File description:
## bollinger
##

# import sys
# from datetime import datetime
import actions
import statistics
# import Tools
# import Bot

def buyCondition(self, upperBand, lowerBand):
    if actions.getCurrencyPrice(self, "USDT", "BTC") < lowerBand:
        return True
    return False

def sellCondition(self, upperBand, lowerBand):
    if actions.getCurrencyPrice(self, "USDT", "BTC") > upperBand:
        return True
    return False


def bollingerStrat(self, period):
    # time = datetime.fromtimestamp(self.date)
    # print(time, flush=True, file=sys.stderr)    
    # print(self.stacks, flush=True, file=sys.stderr)
    usd = "USDT"
    btc = "BTC"
    money = self.stacks["USDT"]
    money_btc = self.stacks["BTC"]
    ma20 = statistics.mean(self.charts["USDT_BTC"].closes[-period:])
    btcPrice = actions.getCurrencyPrice(self, usd, btc)

    if len(self.charts["USDT_BTC"].closes[-period:]) > 2:
        upperBand = ma20 + (2 * statistics.stdev(self.charts["USDT_BTC"].closes[-period:]))
        lowerBand = ma20 - (2 * statistics.stdev(self.charts["USDT_BTC"].closes[-period:]))
    else:
        upperBand = btcPrice
        lowerBand = btcPrice
    amount = money
    if buyCondition(self, upperBand, lowerBand) and actions.canUseXCurrency(self, amount, usd):
        finalAmount = actions.currencyConverter(self, amount, usd, btc)
        self.buyXFromTo(finalAmount, usd, btc, 1, btcPrice)
    elif sellCondition(self, upperBand, lowerBand) and int(money_btc) > 0:
        self.sellXOfTo(money_btc, usd, btc, 1, btcPrice)
    else:
        self.doNothing()