from src.Calculator.Calculator import Calculator
from src.CsvReader.csvReader import CsvReader
from src.Statistics.Mean import mean
from src.Statistics.SampleMean import sample_mean
from src.Statistics.Median import median
from src.Statistics.Mode import mode
from src.Statistics.Variance import variance
from src.Statistics.StandardDeviation import std


class Statistics(Calculator):
    data = []

    def init(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def mean(self):
        self.result = mean(self.data)
        return self.result

    def sample_mean(self, sample_size):
        self.result = sample_mean(self.data, sample_size)
        return self.result

    def median(self):
        self.result = median(self.data)
        return self.result

    def mode(self):
        self.result = mode(self.data)
        return self.result

    def variance(self):
        self.result = variance(self.data)
        return self.result

    def std(self):
        self.result = std(self.data)
        return self.result