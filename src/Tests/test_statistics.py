import unittest
from src.CsvReader.csvReader import CsvReader
from src.Calculator.Calculator import Calculator
from src.Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)


if __name__ == '__main__':
    unittest.main()
