from src.Calculator.Addition import addition
from src.Calculator.Subtraction import subtraction
from src.Calculator.Multiplication import multiplication
from src.Calculator.Division import division
from src.Calculator.Square import square
from src.Calculator.SquareRoot import sqrt


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
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = sqrt(a)
        return self.result
