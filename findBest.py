# Bot.py trade Epitech

import Chart
import sys
import copy
import actions

def findBestAlgo(self):
    print(">> START ALGO FINDER", file=sys.stderr)
    results = dict()
    for al in range(0, 17):
        bot = copy.deepcopy(self)
        bot.date = 0
        bot.algo = al
        bot.charts = dict()
        bot.test = True
        for k in self.charts.keys():
            for i in range(0, len(self.charts[k].dates)):
                if not(k in bot.charts.keys()):
                    bot.charts[k] = Chart.Chart()
                bot.charts[k].dates.append(self.charts[k].dates[i])
                bot.charts[k].opens.append(self.charts[k].opens[i])
                bot.charts[k].highs.append(self.charts[k].highs[i])
                bot.charts[k].lows.append(self.charts[k].lows[i])
                bot.charts[k].closes.append(self.charts[k].closes[i])
                bot.charts[k].volumes.append(self.charts[k].volumes[i])
                bot.date = self.charts[k].dates[i]
                bot.useAction()
        total = 0
        default = "USDT"
        for k in bot.stacks.keys():
            if k == default:
                total += bot.stacks[k]
            else:
                total += actions.getCurrencyPrice(bot, default, k) * bot.stacks[k]
        print(f'>> generated {total}$', flush=True, file=sys.stderr)
        results[al] = total
    print("=================================" , flush=True, file=sys.stderr)
    for al in results.keys():
        print(f'>> ALGO {al} generated {results[al]}$', flush=True, file=sys.stderr)
    sortedList = sorted(results.items(), key = lambda item: item[1], reverse = False)
    self.algo = sortedList[-1][0]
    print("=================================" , flush=True, file=sys.stderr)
    if sortedList[-1][1] <= 1000:
        self.algo = 0
    print(f'>> SO THE BEST IS ALGO {self.algo}', flush=True, file=sys.stderr)