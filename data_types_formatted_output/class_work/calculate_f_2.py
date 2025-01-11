from math import radians, sin, tan
from random import randint


def calculate_f_2(a: int) -> float:
    """
        Data: number - a (degrees)
        Task: calculate the value of the expression f = |tg(a) - sin(a ** 3)|
              result with three digit after dot
              format with operator %
    """
    a = radians(a)
    return abs(tan(a) - sin(a ** 3))


if __name__ == "__main__":
     a = randint(-360, 360)
     print("a =", a)
     f = calculate_f_2(a)
     print("Result: f = %.3f" %f)
