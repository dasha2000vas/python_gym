from random import choice


def orientation_of_locator(n1: int, n2: int) -> str:
    """
    Defines orientation of locator.
    Start orientation is North, then it can
    move like this:
    (1) - turn left,
    (-1) - turn right,
    (2) - 180-degree turn.

    Args:
        n1 (int): First turn value.
        n2 (int): Second turn value.

    Returns:
        str: New orientation of the locator.
    """
    if n1 not in [-1, 1, 2] or n2 not in [-1, 1, 2]:
        raise ValueError("Turns can be just -1, 1 or 2.")
    sides = ["North", "West", "South", "East"]
    return sides[0 if (n := n1 + n2) == 4 else n]


if __name__ == "__main__":
    print("Start orientation is North")
    n1 = choice([-1, 1, 2])
    n2 = choice([-1, 1, 2])
    print(f"Turn1: {n1}, turn2: {n2}")
    print(f"New orientation is {orientation_of_locator(n1, n2)}")
