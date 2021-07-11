from src.Calculator.Calculator import Calculator
from src.Statistics.Mean import mean
from src.CsvReader.csvReader import CsvReader
from src.Statistics.SampleMean import sample_mean

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
