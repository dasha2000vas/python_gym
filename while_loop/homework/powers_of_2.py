from random import randint


def get_powers_of_2(n: int) -> list[int]:
    """
    Finds all integer powers of 2
    that are less or equal to n.

    Args:
        n (int): Natural number.

    Returns:
        result (list[int]): List of powers of 2.
    """
    if not isinstance(n, int):
        raise ValueError("n must be integer")
    if n <= 0:
        raise ValueError("n must be positive")
    result = []
    power = 1
    two_in_power = 2
    while two_in_power <= n:
        result.append(power)
        two_in_power *= 2
        power += 1
    return result


if __name__ == '__main__':
    n = randint(1, 100)
    print(f"n = {n}")
    print(f"Powers of 2: {get_powers_of_2(n)}")
