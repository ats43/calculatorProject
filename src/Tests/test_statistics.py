import statistics
import unittest
from src.CsvReader.csvReader import CsvReader
from src.Calculator.Calculator import Calculator
from src.Statistics.Statistics import Statistics
from pprint import pprint
import random


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()
        self.random_int_list = [random.seed(5)]
        self.testData = random.randint(0, 10)
        self.test_lst = [1, 2, 3]


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)
        print("Completed Stats Calc Instantiate Test")

    def test_results_property_calculator(self):
        self.assertEqual(self.statistics.result, 0)
        print("Completed Stats Calc Property Test")

    def test_mean(self):
        print("Beginning Mean Test")
        mean = self.statistics.mean(self.test_lst)  # uses my mean function
        self.assertEqual(mean, 2)
        self.assertEqual(statistics.mean(self.test_lst), 2) # uses built-in stats mean function
        print("Completed Mean Test")

    # def test_mean_csv(self):
    #     print(self.random_int_list)
    #     print(type(self.random_int_list))
    #     mean = self.statistics.mean(self.random_int_list)
    #     self.assertEqual(mean, 5)


if __name__ == '__main__':
    unittest.main()
