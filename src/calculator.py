def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


class Calculator:
    result = 0

    def __init__(self):  # Object Oriented Programming "Things you can go to the store and buy it = class / object"
        x = 2 + 2
        self.result = x
        pass  # if you can't then it's a static class

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result