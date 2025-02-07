from random import randint


def sum_of_series_up_to_nth_term(n: int) -> float:
    """
    Calculates the sum of series up to nth term.

    Args:
        n (int): Count of terms.

    Returns:
        result (float): Resulting number.
    """
    if not isinstance(n, int):
        raise ValueError("n must be integer")
    if n <= 0:
        raise ValueError("n must be positive")
    result = 0
    for i in range(1, n + 1):
        result += 1 / i
    return round(result, 3)


if __name__ == "__main__":
    n = randint(1, 100)
    print(f"n = {n}")
    print(f"Sum = {sum_of_series_up_to_nth_term(n)}")
