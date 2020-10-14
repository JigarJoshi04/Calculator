"""
Python Calculator App
Github: https://github.com/JigarJoshi04/Calculator
"""

from operations import (
    addition,
    subtraction,
    multiplication,
    division,
    integer_division,
    modulo,
    power,
    log,
    sigmoid,
    rand_between,
    hcf,
    factorial,
    exponential
)

RUNNING = True

while RUNNING:
    print("-" * 50)
    num1 = int(input("Enter First Integer  :--> "))
    num2 = int(input("Enter Second Integer :--> "))
    print(
        """
    Addition              -->  1     Subraction      -->  2
    Multiplication        -->  3     Division        -->  4
    Integer Division      -->  5     Power           -->  6
    Modulo                -->  7     Log             -->  8
    Sigmoid of sum        -->  9     Random Number   -->  10
    Highest common factor --> 11     Factorial (of first number) --> 12
    Exponential of number --> 13
    Exit            -->  14
    """
    )

    operator = int(input("Please Enter Your Choice :--> "))

    if operator == 1:
        result = addition(num1, num2)
    elif operator == 2:
        result = subtraction(num1, num2)
    elif operator == 3:
        result = multiplication(num1, num2)
    elif operator == 4:
        result = division(num1, num2)
    elif operator == 5:
        result = integer_division(num1, num2)
    elif operator == 6:
        result = power(num1, num2)
    elif operator == 7:
        result = modulo(num1, num2)
    elif operator == 8:
        result = log(num1, num2)
    elif operator == 9:
        result = sigmoid(num1 + num2)
    elif operator == 10:
        result = rand_between(num1, num2)
    elif operator == 11:
        result = hcf(num1, num2)
    elif operator ==12:
        result = factorial(num1)
    elif operator == 13:
        result = exponential(num1)
    elif operator == 14:
        break
    else:
        result = "Enter a valid input. Try again!"

    print(f"\nThe output of the selected operation is {result}")

    choice = input("\nDo you wish to continue? (y/n) :--> ").lower()
    RUNNING = True if choice == 'y' else False
