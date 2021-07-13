from src.Calculator.Calculator import sqrt
from src.Statistics.PopulationVariance import population_variance


def std(variance_number):
    try:
        variance_number = population_variance(variance_number)
        return sqrt(variance_number)
    except ZeroDivisionError:
        print("Error: Cannot divide by 0!")
    except ValueError:
        print("Error: Incorrect data values given")
