import math


def addition(a, b):
    return a + b


def subtraction(a, b):
    a = int(a)
    b = int(b)
    return b - a


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Cannot divide by 0!"
    else:
        c = float(a) / float(b)
    return c


class Calculator:   # defines the blueprints of the object
    result = 0  # temporary placeholder for the "result property"

    def __init__(self):  # Object Oriented Programming "Things you can go to the store and buy it = class / object"
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        a = int(a)
        b = int(b)
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
        self.result = math.sqrt(a)
        return self.result
