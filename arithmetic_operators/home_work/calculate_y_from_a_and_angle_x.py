from random import randint
from math import radians, e, sin


def calculate_y_from_a_and_angle_x(a: int, x: int, in_degrees: bool = False) -> float:
    """
    Calculates the value of the expression:
    e ** a * (sin x) ** 2 - (|x - a|) / 7.

    Args:
        a (int): The first number.
        x (int): Angle value.
        in_degrees (bool): True if x is in degrees.
         (default: False)  False if x is in radians.


    Returns:
        y (float): The resulting number.
    """
    if in_degrees is True:
        x = radians(x)
    return round(e ** a * sin(x) ** 2 - abs(x - a) / 7, 3)


if __name__ == "__main__":
    a, x = randint(-50, 50), randint(-50, 50)
    print("a =", a, "\nx =", x)
    print("Result if x in radians:", calculate_y_from_a_and_angle_x(a, x))
    print("Result if x in degrees:", calculate_y_from_a_and_angle_x(a, x, True))
