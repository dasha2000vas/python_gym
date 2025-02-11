from math import  sin


def solving_equation() -> float:
    """
    Solves equation.

    Returns:
        x (float): Root of equation.
    """
    a = 0
    b = 1
    x = 0
    while b - a >= 0.0001:
        x = (b + a) / 2
        result = 0.5 * x - 0.5 + sin(x)
        if result == 0:
            return x
        elif result < 0:
            a = x
        elif result > 0:
            b = x
    return x


if __name__ == "__main__":
    print(solving_equation())
