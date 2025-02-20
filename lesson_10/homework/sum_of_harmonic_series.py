from random import randint


def get_sum_of_harmonic_series(n: int) -> float:
    """
    Calculates sum of harmonic series of n elements.

    Args:
         n (int): Count of elements.

    Returns:
         result (float): Resulting number.
    """
    if not isinstance(n, int):
        raise ValueError('n must be integer')
    if n <= 1:
        raise ValueError('n must grater than 1')
    result = 0
    for i in range(1, n + 1):
        result += 1 / i
    return round(result, 3)


if __name__ == '__main__':
    n = randint(1, 100)
    print(f"Count of elements: {n}")
    print(f"Sum of harmonic series: {get_sum_of_harmonic_series(n)}")
