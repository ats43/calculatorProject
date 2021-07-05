import unittest
from calculator import Calculator    # take calculator.py (module) and import the Calculator (class)
from csvReader import CsvReader
# from pprint import pprint


class MyTestCase(unittest.TestCase):    # unit tests are tests we write to test code. (TDD) test driven development
    def setUp(self) -> None:
        self.calculator = Calculator()  # instantiates calculator in each test.

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)    # tests if there is a calculator (instance, isItAClass?)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        print("Begin Addition Test")
        test_data_add = CsvReader('/src/Unit Test Addition.csv').data
        for row in test_data_add:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
        print("Completed Addition Test")

    def test_subtract_method_calculator(self):
        print("Begin Subtraction Test")
        test_data_subtract = CsvReader('/src/Unit Test Subtraction.csv').data
        for row in test_data_subtract:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
        print("Completed Subtraction Test")

    # def test_multiplication_method_calculator(self):
    #     test_data = CsvReader('/src/Unit Test Multiplication.csv').data
    #     pprint(test_data)
    #     for row in test_data:
    #         self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
    #         self.assertEqual(self.calculator.result, int(row['Result']))
    #
    # def test_division_method_calculator(self):
    #     test_data = CsvReader('/src/Unit Test Division.csv').data
    #     pprint(test_data)
    #     for row in test_data:
    #         self.assertAlmostEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
    #         self.assertAlmostEqual(self.calculator.result, float(row['Result']))

    # def test_division_method_calculator_by_zero(self):
    #     # self.assertEqual(self.calculator.divide((1234, 0), "Cannot divide by 0!"),
    #     with self.assertRaises(ZeroDivisionError):
    #         self.calculator.divide(12, 0)

    # def test_square_method_calculator(self):
    #     test_data = CsvReader('/src/Unit Test Square.csv').data
    #     pprint(test_data)
    #     for row in test_data:
    #         self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
    #         self.assertEqual(self.calculator.result, int(row['Result']))

    # def test_sqrt_method_calculator(self):
    #     test_data = CsvReader('/src/Unit Test Square Root.csv').data
    #     pprint(test_data)
    #     for row in test_data:
    #         self.assertAlmostEqual(self.calculator.sqrt(float(row['Value 1'])), float(row['Result']))
    #         self.assertAlmostEqual(self.calculator.result, float(row['Result']))

    # def test_sqrt_negatives_method_calculator(self):
    #     with self.assertRaises(ValueError):
    #         math.sqrt(-25)


if __name__ == '__main__':
    unittest.main()
