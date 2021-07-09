from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division
import math


class Calculator:   # defines the blueprints of the object
    result = 0  # temporary placeholder for the "result property"

    def __init__(self):  # Object Oriented Programming "Things you can go to the store and buy it = class / object"
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = multiplication(a, a)
        return self.result

    def sqrt(self, a):
        self.result = float(math.sqrt(a))
        return self.result
