""" Util Functions """
import math
import numpy as np
import random


def addition(first: int, second: int) -> int:
    """
    Returns sum of two integers.

    Parameters:
        first (int) : First Integer
        second (int) : Second Integer
    """
    return first + second


def subtraction(first: int, second: int) -> int:
    """
    Returns subtraction of two integers.

    Parameters:
        first (int) : First Integer
        second (int) : Second Integer
    """
    return first - second


def multiplication(first: int, second: int) -> int:
    """
    Returns multiplication of two integers.

    Parameters:
        first (int) : First Integer
        second (int) : Second Integer
    """
    return first * second


def division(first: int, second: int) -> float:
    """
    Returns float division of two integers.

    Parameters:
        first (int) : First Integer
        second (int) : Second Integer
    """
    return first / second


def integer_division(first: int, second: int) -> int:
    """
    Returns integer division of two integers.

    Parameters:
        first (int) : First Integer
        second (int) : Second Integer
    """
    return first // second


def power(base_int: int, power_int: int) -> int:
    """
    Returns base raised to the power.

    Parameters:
        first (int) : First Integer
        second (int) : Second Integer
    """
    return base_int ** power_int


def modulo(dividend: int, divisor: int) -> int:
    """
    Returns remainder of dividend // divisor.

    Parameters:
        first (int) : First Integer
        second (int) : Second Integer
    """
    return dividend % divisor


def log(first: int, base: int) -> float:
    """
    Returns sum of two integers.

    Parameters:
        first (int) : Value to calculate base for. Should be > 0.
        second (int) : Logarithmic base to use.
    """
    return math.log(first, base)


def sigmoid(z):
    """
    Compute the sigmoid of z

    Arguments:
    x -- A scalar or numpy array of any size.

    Return:
    s -- sigmoid(z)
    """

    # START CODE HERE ### (≈ 1 line of code)
    s = 1 / (1 + np.exp(-z))
    ### END CODE HERE ###

    return s


def rand_between(start: int, stop: int) -> int:
    """
    Returns a random number between two integers.
    Parameters:
        start (int) : Lower limit of Random Number
        stop (int) : Upper Limit of Random Number
    """
    return random.randint(start, stop)


def mean(numbers: list) -> float:
    """
    Returns an float of the mean of numbers provided in mean 64 for more accuracy.
    Parameters:
        numbers (list) : A list of numbers
    """
    return np.mean(np.array(numbers), dtype=np.float64)


def range(first: int, second: int) -> float:
    """
    Returns the range between 2 numbers.
    Parameters:
        start (int) : First number
        end (int) : Second number
    """

    biggest = 0

    if (first < second):
        biggest = second
        return biggest - first

    return first - second


def median(numbers: list) -> float:
    """
    Returns the median of a list of numbers.
    Parameters:
         numbers (list) : A list of numbers
    """
    list_size = len(numbers)
    numbers.sort()

    if list_size % 2 == 0:
        median1 = numbers[list_size//2]
        median2 = numbers[list_size//2 - 1]
        median = (median1 + median2)/2
    else:
        median = numbers[list_size//2]

    return median


def mode(numbers: list) -> dict:
    """
    Returns the mode of a list of numbers as a dictionary.
    Parameters:
         numbers (list) : A list of numbers
    """
    numbers.sort()
    ordered_list = []

    i = 0
    while i < len(numbers):
        ordered_list.append(numbers.count(numbers[i]))
        i += 1

    count_num_dict = dict(zip(numbers, ordered_list))
    filter_dict = {k for (k, v) in count_num_dict.items()
                   if v == max(ordered_list)}

    return int(str(filter_dict).replace("{", "").replace("}", ""))


def hcf(x, y):
    while(y):
        x, y = y, x % y
    return x

def factorial(num: int) -> int:
    if num <= 1:
        return 1
    else:
        return factorial(num-1) * num
