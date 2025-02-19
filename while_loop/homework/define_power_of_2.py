from random import randint


def define_power_of_2(n: int) -> int:
    """
    Defines with which power 2 is greater or equal to n.

    Args:
        n (int): Entered number.

    Returns:
        power (int): Power of 2.
    """
    if not isinstance(n, int):
        raise ValueError("n must be integer")
    if n <= 0:
        raise ValueError("n must be positive")
    power = 1
    two_in_power = 2
    while not two_in_power >= n:
        two_in_power *= 2
        power += 1
    return power


if __name__ == '__main__':
    n = randint(1, 100)
    print(f"n = {n}")
    print(f"Power of 2: {define_power_of_2(n)}")
