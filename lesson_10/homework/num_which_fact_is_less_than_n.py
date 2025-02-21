from random import randint

from tools import get_factorial


def find_num_which_fact_is_less_than_n(n: int) -> list[int]:
    """
    Finds all numbers which
    factorial is less than n.

    Args:
        n (int): Entered number.

    Returns:
        result (list[int]): Resulting list of numbers.
    """
    if not isinstance(n, int):
        raise ValueError('n must be integer')
    if n <= 0:
        raise ValueError('n must be greater than 0')
    result = []
    num = 0
    while get_factorial(num) < n:
        result.append(num)
        num += 1
    return result


if __name__ == '__main__':
    n = randint(1, 200)
    print(f"n = {n}")
    result = find_num_which_fact_is_less_than_n(n)
    print(f"Numbers which factorial is less than n: {result}")
