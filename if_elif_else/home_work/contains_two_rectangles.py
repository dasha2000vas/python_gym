from random import randint


def contains_two_rectangles(
     x1: int, y1: int, a1: int, b1: int, x2: int, y2: int, a2: int, b2: int
) -> tuple[int, int, int, int]:
    """
    Finds coordinates of lower-left and upper-right
    corners of rectangle that contains two rectangles.
    Note: sides are parallel or perpendicular to axes.

    Args:
        x1 (int): X coordinate of lower-left corner of first rectangle.
        y1 (int): Y coordinate of lower-left corner of first rectangle.
        a1 (int): First side of first rectangle.
        b1 (int): Second side of first rectangle.
        x2 (int): X coordinate of lower-left corner of second rectangle.
        y2 (int): Y coordinate of lower-left corner of second rectangle.
        a2 (int): First side of second rectangle.
        b2 (int): Second side of second rectangle.

    Returns:
       tuple[int]: Lower-left and upper-right coordinates.
    """
    return min(x1, x2), min(y1, y2), max(x1 + a1, x2 + a2), max(y1 + b1, y2 + b2)


if __name__ == "__main__":
    x1, y1, a1, b1 = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
    x2, y2, a2, b2 = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
    print(f"x1 = {x1}, y1 = {y1}, a1 = {a1}, b1 = {b1}")
    print(f"x2 = {x2}, y2 = {y2}, a2 = {a2}, b2 = {b2}")
    result = contains_two_rectangles(x1, y1, a1, b1, x2, y2, a2, b2)
    print(f"Lower-left corner: {result[0:2]}")
    print(f"Upper-right corner: {result[2:]}")
