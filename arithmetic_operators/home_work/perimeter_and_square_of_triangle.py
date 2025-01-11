from math import sqrt
from random import randint


def find_perimeter_and_square(
        x1: int, x2: int, x3: int, y1: int, y2: int, y3: int
) -> tuple[float, float]:
    """
    Calculates the perimeter and square of the triangle
    by coordinates and returns the result.

    Args:
        x1 (int): The x coordinate of point 1.
        x2 (int): The x coordinate of point 2.
        x3 (int): The x coordinate of point 3.
        y1 (int): The y coordinate of point 1.
        y2 (int): The y coordinate of point 2.
        y3 (int): The y coordinate of point 3.

    Returns:
        perimeter (float): The perimeter of the triangle.
        square (float): The square of the triangle.
    """
    ab = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    ac = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    bc = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    perimeter = round(ab + ac + bc, 2)
    square = abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)) / 2
    return perimeter, square


if __name__ == "__main__":
    x1, x2, x3 = randint(-10, -1), randint(0, 5), randint(6, 10)
    y1, y2, y3 = randint(0, 5), randint(6, 10), randint(0, 5)
    print("x1 =", x1, "\nx2 =", x2, "\nx3 =", x3)
    print("y1 =", y1, "\ny2 =", y2, "\ny3 =", y3)
    perimeter, square = find_perimeter_and_square(x1, x2, x3, y1, y2, y3)
    print("Perimeter =", perimeter)
    print("Square =", square)
