import math
import unittest
from calculator import Calculator    # take calculator.py (module) and import the Calculator (class)
from csvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):    # unit tests are tests we write to test code. (TDD) test driven development
    def setUp(self) -> None:
        self.calculator = Calculator()  # instantiates calculator in each test.

#    def test_instantiate_calculator(self):
        # # calculator = Calculator() instantiates the calculator
        # self.assertIsInstance(self.calculator, Calculator)    # tests if there is a calculator (instance, isItAClass?)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    # def test_add_method_calculator(self):
    #     test_data = CsvReader('/src/Unit Test Addition.csv').data
    #     pprint(test_data)
    #     for row in test_data:
    #         self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
    #         self.assertEqual(self.calculator.result, int(row['Result']))

    # def test_subtract_method_calculator(self):
    #     test_data = CsvReader('/src/Unit Test Subtraction.csv').data
    #     pprint(test_data)
    #     for row in test_data:
    #         self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
    #         self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Multiplication.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
    #
    # def test_division_method_calculator(self):
    #     self.assertEqual(self.calculator.divide(100, 5), 20)
    #     self.assertEqual(self.calculator.result, 20)

    # def test_division_method_calculator_by_zero(self):
    #     # self.assertEqual(self.calculator.divide((1234, 0), "Cannot divide by 0!"),
    #     with self.assertRaises(ZeroDivisionError):
    #         self.calculator.divide(12, 0)

    # def test_square_method_calculator(self):
    #     self.assertEqual(self.calculator.square(10), 100)
    #     self.assertEqual(self.calculator.result, 0)

    # def test_sqrt_method_calculator(self):
    #     self.assertEqual(self.calculator.sqrt(25), 5)
    #     self.assertEqual(self.calculator.result, 5)
    #
    # def test_sqrt_negatives_method_calculator(self):
    #     with self.assertRaises(ValueError):
    #         math.sqrt(-25)


if __name__ == '__main__':
    unittest.main()
