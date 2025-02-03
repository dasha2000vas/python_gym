from random import randint


def is_enough_one_rook_move(x1: int, y1: int, x2: int, y2: int) -> bool:
    """
    Defines if it is enough to make one
    rook move to reach the second point.

    Args:
        x1 (int): x coordinate of rook.
        y1 (int): y coordinate of rook.
        x2 (int): x coordinate of second point.
        y2 (int): y coordinate of second point.

    Returns:
        bool: True if one move is enough, else False.
    """
    return x1 == x2 or y1 == y2


if __name__ == "__main__":
    x1, y1, x2, y2 = randint(1, 8), randint(1, 8), randint(1, 8), randint(1, 8)
    print(f"x1 = {x1}, y1 = {y1}\nx2 = {x2}, y2 = {y2}")
    result = is_enough_one_rook_move(x1, y1, x2, y2)
    print(f"Rook can reach the second point by one move: {result}")
