from src.Calculator.Addition import addition
from src.Calculator.Division import division


def sample_mean(data, sample_size):
    total = 0
    length = len(data)
    for num in data:
        total = addition(total, num)
        return division(total, length)

