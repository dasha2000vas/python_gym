from random import randint


def get_sum_from_1_to_n(n: int) -> int:
    """
    Calculates sum from 1 to n using recursion.

    Args:
        n (int): Positive number.

    Returns:
        int: Sum from 1 to n.
    """
    if not isinstance(n, int):
        raise ValueError('N must be integer')
    if n < 1:
        raise ValueError('N must be positive')
    if n == 1: return 1
    return n + get_sum_from_1_to_n(n-1)


if __name__ == '__main__':
    n = randint(1, 100)
    print(f"n = {n}")
    print(f"Sum from 1 to n: {get_sum_from_1_to_n(n)}")
