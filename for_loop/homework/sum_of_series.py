from random import randint


def sum_of_series(n: int) -> int:
    """
    Calculates sum of series made up n times.

    Args:
        n (int): Count of times.

    Returns:
        result (int): Sum of series.
    """
    if not isinstance(n, int):
        raise ValueError("n must be integer")
    if n <= 0:
        raise ValueError("n must be positive")
    result = 0
    for i in range(1, n + 1):
        term = 1
        for j in range(i, 2 * i + 1):
             term *= j
        result += term
    return result


if __name__ == "__main__":
    n = randint(1, 10)
    print(f"n = {n}")
    print(f"Result = {sum_of_series(n)}")
