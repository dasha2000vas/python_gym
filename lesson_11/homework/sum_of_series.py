from random import randint
from time import perf_counter


def sum_of_series_iteratively(number: int, n: int) -> int:
    """
    Calculates sum of series
    up to n-th member iteratively.

    Args:
        number (int): Positive number (<100).
        n (int): Count of members (<100).

    Returns:
        sum_of_series (int): Sum of series.
    """
    for num in (number, n):
        if not isinstance(num, int):
            raise ValueError('All args must be integers')
        if num <= 0 or num >= 100:
            raise ValueError('All args must be between 0 and 100')
    sum_of_series = 0
    for i in range(1, n + 1):
        sum_of_series += number * i
    return sum_of_series


def recursive_calculation(number: int, n: int) -> int:
    """
    Calculates sum of series up to n-th
    member using recursion.

    Args:
        number (int): Positive number.
        n (int): Count of members.

    Returns:
        sum_of_series (int): Sum of series.
    """
    if n == 1: return number
    return number * n + recursive_calculation(number, n - 1)



def sum_of_series_recursively(number: int, n: int) -> int:
    """
    Calculates sum of series up to n-th
    member using recursive function.

    Args:
        number (int): Positive number (<100).
        n (int): Count of members (<100).

    Returns:
        sum_of_series (int): Sum of series.
    """
    for num in (number, n):
        if not isinstance(num, int):
            raise ValueError('All args must be integers')
        if num <= 0 or num >= 100:
            raise ValueError('All args must be between 0 and 100')
    return recursive_calculation(number, n)


if __name__ == '__main__':
    number, n = randint(1, 100), randint(1, 100)
    print(f"Number: {number}, n: {n}")
    time0 = perf_counter()
    result1 = sum_of_series_iteratively(number, n)
    time_iteratively = perf_counter() - time0
    print(f"Result iteratively: {result1}. Time: {time_iteratively:.10f}")
    time0 = perf_counter()
    result2 = sum_of_series_recursively(number, n)
    time_recursively = perf_counter() - time0
    print(f"Result recursively: {result2}. Time: {time_iteratively:.10f}")
