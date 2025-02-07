from math import sqrt
from random import randint


def count_of_right_angled_triangles(min_side: int, max_side: int) -> int:
    """
    Finds count of right-angled triangles
    with side values between min_side and max_side.

    Args:
        max_side (int): Max value of any side.
        min_side (int): Min value of any side.

    Returns:
        count (int): Count of right-angled triangles.
    """
    if not isinstance(min_side, int) or not isinstance(max_side, int):
        raise ValueError("min_side and max_side must be integers")
    if min_side <= 0 or max_side <= 0:
        raise ValueError("min_side and max_side must be positive")
    if max_side <= min_side:
        raise ValueError("max_side must be greater than min_side")
    count = 0
    for a in range(min_side, max_side):
        for b in range(a, max_side):
            c2 = a ** 2 + b ** 2
            c = int(sqrt(c2))
            if c2 == c ** 2 and c < max_side:
                count += 1
    return count


if __name__ == "__main__":
    min_side, max_side = randint(1, 50), randint(51, 100)
    print(f"min_side: {min_side}, max_side: {max_side}")
    count = count_of_right_angled_triangles(min_side, max_side)
    print(f"Count of right-angled triangles: {count}")
