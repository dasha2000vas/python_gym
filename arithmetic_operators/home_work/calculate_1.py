from random import randint
from math import radians, e, sin


def calculate_1(a: int, x: int, in_degrees: bool = False) -> float:
    """
        Data: numbers - a, x
        Task: calculate the value of the expression y = e ** a * (sin x) ** 2 - (|x - a|) / 7
              two ways: first - x in radians, second - x in degrees
    """
    if in_degrees is True:
        x = radians(x)
    return round(e ** a * sin(x) ** 2 - abs(x - a) / 7, 3)


if __name__ == "__main__":
    a, x = randint(-50, 50), randint(-50, 50)
    print("a =", a, "\nx =", x)
    print("Result if x in radians:", calculate_1(a, x))
    print("Result if x in degrees:", calculate_1(a, x, True))
