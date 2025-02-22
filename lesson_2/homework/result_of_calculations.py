from random import randint


def get_result_of_calculations(n: int, k: int, m: int) -> float:
    """
    Raises the number n to the 10th power,
    records k times in a row and extracts m-th root

    Args:
        n (int): The three-digit number.
        k (int): The number of times.
        m (int): The root power.

    Returns:
        float: The resulting number.
    """
    if not isinstance(n, int):
        raise ValueError("Object n must be integer")
    if not 100 <= n <= 999:
        raise ValueError("Number n must be between 100 and 999")
    for number in (k, m):
        if not isinstance(number, int):
            raise ValueError("Args (k, m) must be integers")
        if number <= 0:
            raise ValueError("Numbers (k, m) must be positive")
    return int(str(n ** 10) * k ) ** (1 / m)


if __name__ == "__main__":
    n, k, m = randint(100, 999), randint(1, 10), randint(1, 50)
    print("n =", n, "\nk =", k, "\nm =", m)
    result = get_result_of_calculations(n, k, m)
    print("Result: %.3f" %result)
