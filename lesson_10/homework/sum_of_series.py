from random import randint

from tools import get_factorial, get_power

def get_sum_of_series(n: int, h: int) -> float:
    """
    Calculates sum of series.

    Args:
        n (int): Count of elements in series.
        h (int): Number that would be converted.

    Returns:
        float: Resulting number.
    """
    for num in (n, h):
        if not isinstance(num, int):
            raise ValueError('All args must be integers')
    if n <= 0:
        raise ValueError('n must be positive')
    if h == 0:
        raise ValueError('h cannot be zero')
    result = 0
    for i in range(1, n + 1):
        result += get_power(h, i) / get_factorial(i)
    return round(result, 3)


if __name__ == '__main__':
    n, h = randint(1, 10), randint(1, 10)
    print(f"Count of elements in series: {n}")
    print(f"Number that would be converted: {h}")
    print(f"Result: {get_sum_of_series(n, h)}")
