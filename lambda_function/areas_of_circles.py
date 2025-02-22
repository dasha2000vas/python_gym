from math import pi
from random import randint

calculation = lambda a, b: [round(pi * i ** 2, 3) for i in range(a, b+1)]


def get_areas_of_circles(start: int, end: int) -> list[float]:
    """
    Calculates areas of circles with radius
    value from start number to end number
    using lambda function.

    Args:
        start (int): Start radius value.
        end (int): End radius value.

    Returns:
        list(float): List with areas of circles.
    """
    for number in (start, end):
        if not isinstance(number, (int, float)):
            raise ValueError('All args must be integers')
        if number <= 0:
            raise ValueError('All numbers must be positive')
    return calculation(start, end)


if __name__ == '__main__':
    start, end = randint(1, 5), randint(6, 10)
    print(f"Start radius: {start}, end radius: {end}")
    print(f"Areas of circles: {get_areas_of_circles(start, end)}")
