from src.Calculator.Calculator import Calculator
from src.Statistics.Mean import mean


class Statistics(Calculator):
    data = []

    def init(self):
        super().__init__()

    def mean(self, a):
        self.result = mean(a)
        return self.result
