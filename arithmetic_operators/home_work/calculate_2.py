from math import radians, e, sin, sqrt
from random import randint


def calculate_2(a: int, b: int, c: int, d: int, x: int, in_degrees: bool = False) -> float:
    """
        Data: numbers - a, b, c, d, x
        Task: calculate the value of the expression y = e ** a * (sin x) ** 2 - sqrt(|(c - b ** 2) / a|) + d
              two ways: first - x in radians, second - x in degrees
    """
    if in_degrees is True:
        x = radians(x)
    return round(e ** a * sin(x) ** 2 - sqrt(abs((c - b ** 2) / a)) + d, 3)


if __name__ == "__main__":
    a, b, c, d, x = (
        randint(-50, 50),
        randint(-50, 50),
        randint(-50, 50),
        randint(-50, 50),
        randint(-50, 50)
    )
    print("a =", a, "\nb =", b, "\nc =", c, "\nd =", d, "\nx =", x)
    print("Result if x in radians:", calculate_2(a, b, c, d, x))
    print("Result if x in degrees:", calculate_2(a, b, c, d, x, True))
