# Bot.py trade Epitech

import sys

import Tools
import Chart
import Candle

class Bot:
    def __init__(self):
        self.timeBank = 2000
        self.maxTimeBank = 2000
        self.timePerMove = 100
        self.candleInterval = 3600000
        self.candleFormat = ['pair','date','high','low','open','close','volume']
        self.candleTotal = 0
        self.candleGiven = 0
        self.initialStack = 1000
        self.stacks = dict()
        self.transactionFee = 0.2
        self.date = 0
        self.charts = dict()
        self.playerName = "Ahmed"
        self.your_bot = "Maxime"
        self.buys = []
        self.first = True
        self.test = False
        self.risk = False
        self.algo = -1
        self.initialDate = 0
        self.ma = []
        self.purchasePrice = []

    from strategy_bollinger import bollingerStrat
    from strategy_ma import maStrat
    from findBest import findBestAlgo
    from strategy_momentum import momentum
    from strategy_followtrend import followTrend
    from strategy_everything import everything
    from strategy_dumb import dumb
    from actions import buyXFromTo, sellXOfTo, currencyConverter, doNothing
    
    def runLine(self):
        for line in sys.stdin:
            line = line.rstrip()
            self.parse(line)
    
    def sendLine(self, line):
        line = line.rstrip()
        self.parse(line)

    def parse(self, line: str):
        cmd = line.split(' ')
        if cmd[0] == 'settings':
            if len(cmd) < 3:
                Tools.showError("Invalid settings command args lenght")
            self.updateSettings(cmd[1], cmd[2])
        elif cmd[0] == 'update':
            if len(cmd) < 4:
                Tools.showError("Invalid update command args lenght")
            if cmd[1] == 'game':
                self.updateGame(cmd[2], cmd[3])
            else:
                Tools.showError("Invalid update command arg")
        elif cmd[0] == 'action':
            print("CALL ACTION", flush=True, file=sys.stderr)
            self.useAction()
        else:
            Tools.showError("Invalid command")
    
    def updateSettings(self, key: str, value: str):
        if key == "transaction_fee_percent":
            try:
                float(value)
            except ValueError:
                Tools.showError("transaction_fee_percent value is not a float")
        elif key != "candle_format" and key != "player_names" and key != "your_bot":
            try:
                int(value)
            except ValueError:
                Tools.showError("settings value is supposed to be an int")
        if key == "timebank":
            self.maxTimeBank = int(value)
            self.timeBank = int(value)
        elif key == "time_per_move":
            self.timePerMove = int(value)
        elif key == "candle_interval":
            self.candleInterval = int(value)
        elif key == "candle_format":
            self.candleFormat = value.split(",")
        elif key == "candles_given":
            self.candleGiven = int(value)
        elif key == "initial_stack":
            self.initialStack = int(value)
        elif key == "transaction_fee_percent":
            self.transactionFee = float(value)
        elif key == "player_names":
            self.playerName = value
        elif key == "your_bot":
            self.your_bot = value
        elif key == "candles_total":
            self.candles_total = int(value)
        else:
            Tools.showError("Invalid settings key")

    def updateGame(self, key: str, value: str):
        if key == "next_candles":
            new_candles = value.split(';')
            self.date = int(new_candles[0].split(',')[1])
            for candle_str in new_candles:
                candle_infos = candle_str.strip().split(',')
                self.updateChart(candle_infos[0], candle_str)
        elif key == "stacks":
            new_stacks = value.split(',')
            for stack_str in new_stacks:
                stack_infos = stack_str.strip().split(':')
                self.stacks[stack_infos[0]] = float(stack_infos[1])
        else:
            Tools.showError("Invalid update game arg")
    
    def updateChart(self, pair: str, new_candle_str: str):
        if not (pair in self.charts):
            self.charts[pair] = Chart.Chart()
        new_candle_obj = Candle.Candle(self.candleFormat, new_candle_str)
        self.charts[pair].add_candle(new_candle_obj)

    def useAction(self):
        if self.algo == -1:
            self.findBestAlgo()
        print("Algo n° ->", self.algo, flush=True, file=sys.stderr)
        if self.algo == 0:
            self.maStrat(20, 2)
        elif self.algo == 1:
            self.maStrat(10, 2)
        elif self.algo == 2:
            self.maStrat(20, 4)
        elif self.algo == 3:
            self.maStrat(30, 10)
        elif self.algo == 4:
            self.bollingerStrat(2)
        elif self.algo == 5:
            self.bollingerStrat(5)
        elif self.algo == 6:
            self.bollingerStrat(10)
        elif self.algo == 7:
            self.bollingerStrat(20)
        elif self.algo == 8:
            self.bollingerStrat(30)
        elif self.algo == 9:
            self.dumb(2)
        elif self.algo == 10:
            self.dumb(5)
        elif self.algo == 11:
            self.dumb(10)
        elif self.algo == 12:
            self.dumb(20)
        elif self.algo == 13:
            self.everything(2, self.risk)
        elif self.algo == 14:
            self.everything(5, self.risk)
        elif self.algo == 15:
            self.everything(10, self.risk)
        else:
            self.everything(20, self.risk)