import unittest
from src.CsvReader.csvReader import CsvReader
from src.Calculator.Calculator import Calculator
from src.Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):
    test_data = CsvReader('/src/Tests/Data/Unit Test Data.csv').data
    test_stats_answers = CsvReader('/src/Tests/Data/Unit Stats Answers.csv').data

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)
        print("Completed Stats Calc Instantiate Test")

    def test_results_property_calculator(self):
        self.assertEqual(self.statistics.result, 0)
        print("Completed Stats Calc Property Test")

    def test_mean_method_calculator(self):
        print("Beginning Mean Test")
        for row in self.test_stats_answers:
            print(row["Mean"])
            self.assertEqual(self.statistics.mean(row['Value 1']))
        print("Completed Mean Test")


if __name__ == '__main__':
    unittest.main()
