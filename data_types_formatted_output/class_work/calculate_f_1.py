from math import radians, sin, tan
from random import randint


def calculate_f_1(a: int, in_degrees: bool = False) -> float:
    """
        Data: number - a
        Task: calculate the value of the expression f = tg(a) - sin(a)
              two ways: first - a in radians, second - a in degrees
    """
    if in_degrees:
        a = radians(a)
    return round(tan(a) - sin(a), 5)


if __name__ == '__main__':
    a = randint(-100, 100)
    print("a =", a)
    print("Result if a in radians: %10.5f" % calculate_f_1(a))
    print("Result if a in degrees: %10.5f" % calculate_f_1(a, True))
