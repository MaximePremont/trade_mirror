##
## EPITECH PROJECT, 2022
## B-CNA-410-LYN-4-1-trade-ahmed.abouelleil-sayed
## File description:
## strategy_shortMomentum
##

# import sys
# from datetime import datetime
import actions
# import statistics
import Tools

def momentum(self, period):
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
        self.initialDate = self.date
        return
    amount = 100
    if Tools.getTrend(self, period) == 1 and money >= amount:
        finalAmount = actions.currencyConverter(self, amount, usd, btc)
        self.buyXFromTo(finalAmount, usd, btc, 1, btcPrice)
    elif Tools.getTrend(self, period) == 0 and money_btc > 0:
        self.sellXOfTo((money_btc), usd, btc, 1, btcPrice)
    else:
        self.doNothing()
