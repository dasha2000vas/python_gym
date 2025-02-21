from math import pi
from random import randint, choice


def get_circle_area(radius: int) -> float:
    """
    Calculates area of circle.

    Args:
        radius (int): Radius of circle.

    Returns:
        float: Area of circle.
    """
    return pi * radius ** 2


def get_cylinder_area(height: int, radius: int, mode: str) -> str | None:
    """
    Calculates area of cylinder
    by given height and radius.
    Three modes are supported:
    1. None - empty string
    2. Side surface area - side
    3. Area of entire surface - all

    Args:
        height (int): Height of cylinder.
        radius (int): Radius of cylinder.
        mode (str): Mode of program.

    Returns:
        str|None: Area or none.
    """
    for num in (height, radius):
        if not isinstance(num, int):
            raise ValueError("Height and radius must be of type int")
        if num <= 0:
            raise ValueError("Height and radius must be greater than zero")
    if mode not in ("side", "all", ""):
        raise ValueError("Invalid mode. Modes are: 'side', 'all' or empty string")
    if mode == "":
        return None
    area = 2 * pi * radius * height
    if mode == "side":
        return f"Side surface area is {area:.3f}"
    if mode == "all":
        area += get_circle_area(radius) * 2
        return f"Area of entire surface is {area:.3f}"


if __name__ == '__main__':
    height, radius = randint(1, 10), randint(1, 10)
    mode = choice(["side", "all", ""])
    print(f"Height: {height}, Radius: {radius}")
    print(f"Mode: {mode}")
    print(get_cylinder_area(height, radius, mode))
