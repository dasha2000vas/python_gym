from random import randint, uniform


def create_n_numbers(n: int) -> list[float]:
    """
    Creates n random float numbers from -5 to 5
    with three digits after dot.

    Args:
        n (int): Count of random float numbers.

    Returns:
        result (list[float]): List of n random float numbers.
    """
    if not isinstance(n, int):
        raise ValueError("n must be integer")
    if n <= 0:
        raise ValueError("n must be positive")
    result = [round(uniform(-5, 5), 3) for _ in range(n)]
    return result


if __name__ == "__main__":
    n = randint(1, 10)
    print(f"n = {n}")
    print(f"n created numbers = {create_n_numbers(n)}")
