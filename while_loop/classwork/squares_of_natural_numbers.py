from random import randint


def get_squares_of_natural_numbers(n: int) -> list[int]:
    """
    Finds all squares of natural numbers up to n.

    Args:
        n (int): Max number (>0).

    Returns:
        squares (list[int]): List of squares of natural numbers.
    """
    if not isinstance(n, int):
        raise ValueError("n must be integer")
    if n <= 0:
        raise ValueError("n must be natural number")
    squares = []
    num = 1
    while (square := num ** 2 ) <= n:
        squares.append(square)
        num += 1
    return squares


if __name__ == "__main__":
    n = randint(1, 100)
    print(f"n = {n}")
    squares = get_squares_of_natural_numbers(n)
    print(f"Squares of natural numbers up to n: {squares}")
