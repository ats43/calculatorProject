from src.Calculator.Addition import addition
from src.Calculator.Division import division


def mean(data):
    try:
        total = 0
        length = len(data)
        for num in data:
            total = addition(total, num)
        return division(total, length)
    except ZeroDivisionError:
        print("Error: Cannot divide by 0!")
    except ValueError:
        print("Error: Incorrect data values given")
# def mean(num):
    # try:
    #     num_values = len(num)
    #     total = sum(num)
    #     return division(total, num_values)
    # except ZeroDivisionError:
    #     print("Error: Can't Divide by 0")
    # except ValueError:
    #     print("Error: Check your data inputs")
