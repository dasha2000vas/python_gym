from math import pi

from random import randint, uniform, choice

calculation = lambda r: round(pi * r ** 2, 3)


def get_area_of_circle(radius: int | float) -> float:
    """
    Calculates area of circle
    using lambda function.

    Args:
        radius (int|float): Radius of circle.

    Returns:
        float: Area of circle.
    """
    if not isinstance(radius, (int, float)):
        raise ValueError('Radius must be integer or float')
    if radius <= 0:
        raise ValueError('Radius value must be positive')
    return calculation(radius)


if __name__ == '__main__':
    radius = choice([randint(1, 100), round(uniform(1, 100), 3)])
    print(f"Radius of circle: {radius}")
    print(f"Area of circle: {get_area_of_circle(radius)}")
