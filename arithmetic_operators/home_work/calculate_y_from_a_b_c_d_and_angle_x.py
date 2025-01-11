from math import radians, e, sin, sqrt
from random import randint


def calculate_y_from_a_b_c_d_and_angle_x(a: int, b: int, c: int, d: int, x: int, in_degrees: bool = False) -> float:
    """
    Calculates the value of the expression:
    e ** a * (sin x) ** 2 - sqrt(|(c - b ** 2) / a|) + d
    and returns the result.

    Args:
        a (int): The first number.
        b (int): The second number.
        c (int): The third number.
        d (int): The fourth number.
        x (int): Angle value.
        in_degrees (bool): True if x is in degrees.
         (default: False)  False if x is in radians.

    Returns:
        y (float): The resulting number.
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
    print("Result if x in radians:", calculate_y_from_a_b_c_d_and_angle_x(a, b, c, d, x))
    print("Result if x in degrees:", calculate_y_from_a_b_c_d_and_angle_x(a, b, c, d, x, True))
