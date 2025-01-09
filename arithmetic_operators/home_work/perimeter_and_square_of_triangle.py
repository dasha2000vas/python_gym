from math import sqrt
from random import randint


def find_perimeter_and_square(
        x1: int, x2: int, x3: int, y1: int, y2: int, y3: int
) -> tuple[float, float]:
    """
        Data: coordinates of the three vertices of the triangle
              point1 - (x1, y1), point2 - (x2, y2), point3 - (x3, y3)
        Task: find the perimeter and square of the triangle
    """
    AB = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    AC = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    BC = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    perimeter = round(AB + AC + BC, 2)
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
