""" Util Functions """
import math


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
