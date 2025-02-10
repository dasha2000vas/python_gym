from random import randint


def get_lowest_simple_divider(num: int) -> int:
    """
    Defines lowest simple divider for number.

    Args:
        num (int): Entered number (>2).

    Returns:
        divider (int): Lowest simple divider.
    """
    if not isinstance(num, int):
        raise ValueError("num must be integer")
    if num < 2:
        raise ValueError("num cannot be less than 2")
    divider = 2
    while True:
        simple = True
        for j in range(2, divider // 2 + 1):
            if divider % j == 0:
                simple = False
        if simple and num % divider == 0:
            return divider
        divider += 1


if __name__ == '__main__':
    n = randint(2, 100)
    print(f"n = {n}")
    print(f"Lowest simple divider: {get_lowest_simple_divider(n)}")
