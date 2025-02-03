from math import sin, cos, sqrt
from random import randint


def calculate_y(x: int) -> float | str:
    """
    Calculates the value of the expression.

    Args:
        x (int): Entered number.

    Returns:
        float|str: The resulting number or message what result doesn't exist.
    """
    if x >= 0:
        if (y1 := 2 * sin(x) - 0.116) >= 0:
            y = sqrt(y1)
        else: return "There is no solution"
    else:
        if (y2 := sin(x) - 2 * cos(x)) != 0:
            y = 1 / y2
        else: return "There is no solution"
    return round(y, 3)


if __name__ == "__main__":
    y = 57
    print(f"y = {y}")
    result = calculate_y(y)
    if isinstance(result, str):
        print(result)
    else:
        print(f"Result: {result}")
