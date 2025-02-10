from math import radians, sin, tan
from random import randint


def calculate_f2(a: int) -> float:
    """
    Calculates the value of the expression.

    Args:
        a (int): Angle value in degrees.

    Returns:
        float: The resulting number.
    """
    a = radians(a)
    return abs(tan(a) - sin(a ** 3))


if __name__ == "__main__":
     a = randint(-360, 360)
     print("a =", a)
     f = calculate_f2(a)
     print("Result: f = %.3f" %f)
