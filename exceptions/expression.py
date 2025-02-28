from math import sqrt
from random import randint


def check_values(number1: int, number2: int) -> None:
    for value in (number1, number2):
        if not isinstance(value, int):
            raise ValueError("All args must be integers")


def check_if_expression_is_valid(number1: int, number2: int) -> float | str:
    check_values(number1, number2)
    try:
        return round(sqrt(number1) / number2, 3)
    except ZeroDivisionError:
        return "Number2 cannot be zero"
    except ValueError:
        return "Number1 cannot be negative"


if __name__ == '__main__':
    number1, number2 = randint(-10, 10), randint(-10, 10)
    print(f"Number1: {number1}. Number2: {number2}")
    result = check_if_expression_is_valid(number1, number2)
    if isinstance(result, str):
        print(result)
    else:
        print(f"Result: {result}")
