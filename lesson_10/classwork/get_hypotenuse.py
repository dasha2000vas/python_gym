from math import sqrt
from random import randint


def get_hypotenuse(leg1: int, leg2: int) -> float:
    """
    Calculates hypotenuse of rectangular
    triangle by its two legs(leg1, leg2).

    Args:
        leg1 (int): First leg of triangle.
        leg2 (int): Second leg of triangle.

    Returns:
        float: Hypotenuse of triangle.
    """
    for i in (leg1, leg2):
        if not isinstance(i, int):
            raise ValueError("Legs must be integers")
        if i <= 0:
            raise ValueError("Legs must be positive")
    return round(sqrt(leg1**2 + leg2**2), 3)


if __name__ == '__main__':
    leg1, leg2 = randint(1, 100), randint(1, 100)
    print(f"Leg1: {leg1}, Leg2: {leg2}")
    print(f"Hypotenuse: {get_hypotenuse(leg1, leg2)}")
