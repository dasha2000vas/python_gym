from random import randint


def get_area_with_dot(x: int, y: int) -> str:
    """
    Defines to which area dot belongs.

    Args:
        x (int): x coordinate.
        y (int): y coordinate.

    Returns:
        str: Area where the point is located.
    """
    if x == 0 and y == 0:
        area = "origin of coordinates"
    elif x == 0 and y != 0:
        area = "y-axis"
    elif x != 0 and y == 0:
        area = "x-axis"
    elif y > 0:
        if x > 0:
            area = "first quarter"
        else:
            area = "second quarter"
    else:
        if x > 0:
            area = "fourth quarter"
        else:
            area = "third quarter"
    return area


if __name__ == "__main__":
    x, y = randint(-10, 10), randint(-10, 10)
    print(f"Dot {x, y} belongs to {get_area_with_dot(x, y)}")
