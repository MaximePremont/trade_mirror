# Chart.py trade Epitech

import Tools

class Candle:
    def __init__(self, format, intel):
        tmp = intel.split(',')
        for (i, key) in enumerate(format):
            value = tmp[i]
            if key == "pair":
                self.pair = "pair"
            elif key == "date":
                self.date = int(value)
            elif key == "high":
                self.high = float(value)
            elif key == "low":
                self.low = float(value)
            elif key == "open":
                self.open = float(value)
            elif key == "close":
                self.close = float(value)
            elif key == "volume":
                self.volume = float(value)
            else:
                Tools.showError("Invalid candle key")
    
    def __repr__(self):
        return str(self.pair) + str(self.date) + str(self.close) + str(self.volume)
