from random import randint


def are_rectangles_cross(
    x1: int, y1: int, a1: int, b1: int, x2: int, y2: int, a2: int, b2: int
) -> tuple[int, int, int, int] | str:
    """
    Defines if two rectangles are crossed.
    If they are: finds coordinates
    of lower-left and upper-right
    corners of rectangle formed
    by intersection of two rectangles.
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
        tuple[int]|str: lower-left and upper-right coordinates or
                        message what rectangles are not crossed.
    """
    x1_right = x1 + a1
    y1_top = y1 + b1
    x2_right = x2 + a2
    y2_top = y2 + b2
    if x2_right < x1 or x2 > x1_right or y2 > y1_top or y2_top < y1:
        return "Rectangles are not crossed"
    return max(x1, x2), max(y1, y2), min(x1_right, x2_right), min(y1_top, y2_top)


if __name__ == "__main__":
    x1, y1, a1, b1 = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
    x2, y2, a2, b2 = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
    print(f"x1 = {x1}, y1 = {y1}, a1 = {a1}, b1 = {b1}")
    print(f"x2 = {x2}, y2 = {y2}, a2 = {a2}, b2 = {b2}")
    result = are_rectangles_cross(x1, y1, a1, b1, x2, y2, a2, b2)
    if isinstance(result, str):
        print(result)
    else:
        print("Two rectangles form rectangle by intersection")
        print(f"Lower-left corner: {result[0:2]}")
        print(f"Upper-right corner: {result[2:]}")
