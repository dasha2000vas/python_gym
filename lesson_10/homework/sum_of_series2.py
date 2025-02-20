from math import sin, cos
from random import randint, choice

from tools import get_factorial, get_power


def get_sum_of_series2(n: int, h: int, x: int) -> float:
    """
    Calculates sum of series.

    Args:
        n (int): Count of elements in series.
        h (int): Number that would be converted.
        x (int): Value of angle.

    Returns:
        float: Resulting number.
    """
    for num in (n, h, x):
        if not isinstance(num, int):
            raise ValueError('All args must be integers')
    if n <= 0:
        raise ValueError('n must be positive')
    if h == 0:
        raise ValueError('h cannot be zero')
    result = 0
    count_sin = 0
    count_cos = 0
    for i in range(0, n + 1):
        multiplier = get_power(h, i) / get_factorial(i)
        if i % 2 == 0:
            count_sin += 1
            if count_sin == 2:
                multiplier *= -1
                count_sin = 0
            result += multiplier * sin(x)
        else:
            count_cos += 1
            if count_cos == 2:
                multiplier *= -1
                count_cos = 0
            result += multiplier * cos(x)

    return round(result, 3)


if __name__ == '__main__':
    n, x = randint(1, 10), randint(-20, 20)
    h = choice([randint(-10, 1), randint(1, 10)])
    print(f"Count of elements in series: {n}")
    print(f"Number that would be converted: {h}")
    print(f"Angle value: {x}")
    print(f"Result: {get_sum_of_series2(n, h, x)}")
