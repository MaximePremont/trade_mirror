##
## EPITECH PROJECT, 2022
## B-CNA-410-LYN-4-1-trade-ahmed.abouelleil-sayed
## File description:
## actions
##

import sys

def doNothing(self):
    print("no_moves", flush=True)
    print("NOTHING", flush=True, file=sys.stderr)
    print(flush=True, file=sys.stderr)

def canUseXCurrency(self, amount, currency):
    if (amount > self.stacks[currency]) or amount == 0:
        return False
    print("CANUSE", amount, "|",  self.stacks[currency] - self.stacks[currency] * 0.2, flush=True, file=sys.stderr)
    return True

def getCurrencyPrice(self, in_currency, of_currency):
    label = in_currency + "_" + of_currency
    price = self.charts[label].closes[-1]
    return price

def currencyConverter(self, amount, from_currency, to_currency):
    label = from_currency + "_" + to_currency
    to_currencyPrice = self.charts[label].closes[-1]
    finalAmount = amount / to_currencyPrice
    return finalAmount

def buyXFromTo(self, amount, from_currency, to_currency, from_price, to_price):
    label = from_currency + "_" + to_currency
    self.stacks[from_currency] -= to_price * amount
    self.stacks[to_currency] += amount * ( 1 - self.transactionFee / 100 )
    for v in self.stacks.keys():
        print(f'MY MONEY {v} is {self.stacks[v]}', flush=True, file=sys.stderr)
    if not(self.test):
        print(f'buy {label} {amount}', flush=True)
    else:
        print("no_moves", flush=True)
    print("BUY", flush=True, file=sys.stderr)
    print(flush=True, file=sys.stderr)

def sellXOfTo(self, amount, to_currency, of_currency, to_price, of_price):
    label = to_currency + "_" + of_currency
    self.stacks[to_currency] += (of_price * amount) * ( 1 - self.transactionFee / 100 )
    self.stacks[of_currency] -= amount
    for v in self.stacks.keys():
        print(f'MY MONEY {v} is {self.stacks[v]}', flush=True, file=sys.stderr)
    print(f"Trying to sell this -> {label} {amount}", flush=True, file=sys.stderr)
    if amount <= 0 and not(self.test):
        print("DID NOT SELL", flush=True, file=sys.stderr)
        print(flush=True, file=sys.stderr)
        print("no_moves", flush=True)
        return
    if not(self.test):
        print(f'sell {label} {amount}', flush=True)
    else:
        print("no_moves", flush=True)
    print("SELL", flush=True, file=sys.stderr)
    print(flush=True, file=sys.stderr)

def firstMove(self, usd, currencyToBuy, currencyPrice):
    finalAmount = currencyConverter(self, 100, usd, currencyToBuy)
    buyXFromTo(finalAmount, usd, currencyToBuy)
    self.buys.append(currencyPrice)
    self.first = False