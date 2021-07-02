def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

class Calculator: #defines the blueprints of the object
    result = 0 #temporary placeholder for the "result property"

    def __init__(self):  # Object Oriented Programming "Things you can go to the store and buy it = class / object"
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication (a, b)
        return self.result