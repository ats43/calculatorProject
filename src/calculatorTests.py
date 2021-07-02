import unittest
from calculator import Calculator #take calculator.py (module) and import the Calculator (class)


class MyTestCase(unittest.TestCase): #unit tests are tests we write to test code. (TDD) test driven development

    def setUp(self) -> None:
        self.calculator = Calculator() #instantiates calculator in each test.

    def test_instantiate_calculator(self):
        #calculator = Calculator() #instaniates the calculator
        self.assertIsInstance(self.calculator,Calculator)    #tests if there is a calculator (instance, isItAClass?)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2,3),5)
        self.assertEqual(self.calculator.result,5)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2,3),-1)
        self.assertEqual(self.calculator.result,-1)

    def test_multiplication_method_calculator(self):
        self.assertEqual(self.calculator.multiply(5,2),10)
        self.assertEqual(self.calculator.result,10)


if __name__ == '__main__':
    unittest.main()
