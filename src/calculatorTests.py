import unittest
from calculator import Calculator #take calculator.py (module) and import the Calculator (class)


class MyTestCase(unittest.TestCase): #unit tests are tests we write to test code. (TDD) test driven development

    def test_instantiate_calculator(self):
        calculator = Calculator() #instaniates the calculator
        self.assertIsInstance(calculator,Calculator)    #tests if there is a calculator (instance, isItAClass?)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 0)

    def test_add_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2,3),5)
        self.assertEqual(calculator.result,5)

    def test_subtract_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(2,3),-1)
        self.assertEqual(calculator.result,-1)

if __name__ == '__main__':
    unittest.main()
