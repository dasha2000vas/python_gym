from random import randint


def sum_of_series_signs_rotate(n: int) -> float:
    """
    Calculates the sum of series up to nth term.
    Note: signs rotate, first plus then minus.

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
        result += (-1) ** (i + 1) / i
    return round(result, 2)


if __name__ == "__main__":
    n = randint(1, 100)
    print(f"n = {n}")
    print(f"Result: {sum_of_series_signs_rotate(n)}")
