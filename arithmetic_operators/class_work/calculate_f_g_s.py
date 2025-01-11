from math import cos, sin
from random import randint


def calculate_f_g_s(a: int, b: int) -> tuple[float, float, float]:
    """
    Calculates the values of the expressions:
    f = (a ** b) ** 0.5,
    g = f - sin(a ** 3.5),
    g * f + cos(a - 2 * b) ** 2.
    Rounds the result to two digits after the dot.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        f (float): The first resulting number.
        g (float): The second resulting number.
        s (float): The third resulting number.
    """
    f = (a ** b) ** 0.5
    g = f - sin(a ** 3.5)
    s = g * f + cos(a - 2 * b) ** 2
    return round(f, 2), round(g, 2), round(s, 2)


if __name__ == "__main__":
    a, b = randint(0, 50), randint(0, 50)
    print("a =", a, "\nb =", b)
    f, g, s, = calculate_f_g_s(a, b)
    print(f, g, s, sep="\n")
