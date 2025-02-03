from random import randint


def will_closet_pass(a1: int, b1: int, a2: int, b2: int) -> str:
    """
    Defines if closet with sides (a2, b2)
    will pass through hole with sides (a1, b1).

    Args:
        a1 (int): First side of hole.
        b1 (int): Second side of hole.
        a2 (int): First side of closet.
        b2 (int): Second side of closet.

    Returns:
        str: Says if closet will pass or not.
    """
    for num in (a1, b1, a2, b2):
        if num <= 0:
            raise ValueError("All entered numbers must be positive.")
    if a1 * b1 > a2 * b2:
        return "Closet will pass"
    else:
        return "Closet will not pass"


if __name__ == "__main__":
    a1, b1, a2, b2 = randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)
    print(f"a1 = {a1}, b1 = {b1}, \na2 = {a2}, b2 = {b2}")
    print(will_closet_pass(a1, b1, a2, b2))
