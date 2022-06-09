# Bot.py trade Epitech

import sys
import statistics

def showError(message):
    print("Error: " + message, file= sys.stderr)
    sys.exit(84)

def calculMean(list):
    if len(list) == 0:
        return -1
    return sum(list) / len(list)

def getXLastHighs(self, x, stock):
    return self.charts[stock].highs[-x]

def getXLastLows(self, x, stock):
    return self.charts[stock].lows[-x]

def getXLastOpens(self, x, stock):
    return self.charts[stock].opens[-x]

def getXLastCloses(self, x, stock):
    return self.charts[stock].closes[-x]

def getTrend(self, period):
    actual = statistics.mean(self.charts["USDT_BTC"].closes[-period:])
    before = statistics.mean(self.charts["USDT_BTC"].closes[-2*period:])
    if actual > before:
        return 1
    else:
        return 0