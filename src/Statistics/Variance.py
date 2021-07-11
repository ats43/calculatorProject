from src.Calculator.Addition import addition
from src.Calculator.Division import division
from src.Calculator.Square import square
from src.Statistics.Mean import mean


def variance(data):
    try:
        mean_data = mean(data)  # mean of data
        length = len(data)  # length of data
        i = 0   # starting value for i
        for i in data:  # for each element (i) in data...
            i = addition(i, (square(i-mean_data)))  # add i and square(i - mean_data)
        return division(i, length)  # return i divided by length
    except ZeroDivisionError:
        print("Error: Cannot divide by 0!")
    except ValueError:
        print("Error: Incorrect data values given")
