from random import randint


def range_up_to_n(n: int) -> str:
    """
    Writes all natural numbers from
    0 to n separated by commas.

    Args:
        n (int): Natural number (>10).

    Returns:
        result (str): Resulting string.
    """
    if n <= 10:
        raise ValueError("n must be greater than 10")
    if not isinstance(n, int):
        raise ValueError("n must be integer")
    result = ""
    for i in range(n):
        if i + 1 == n:
            result += f"{i}"
        else:
            result += f"{i}, "
    return result


if __name__ == "__main__":
    n = randint(10, 40)
    print(f"n = {n}")
    print(range_up_to_n(n))
