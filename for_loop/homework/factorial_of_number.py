from random import randint


def get_factorial_of_number(n: int) -> int:
    """
    Calculates factorial of given number.

    Args:
        n (int): Entered number.

    Returns:
        result (int): Factorial of number.
    """
    if not isinstance(n, int):
        raise ValueError("n must be integer")
    if n < 0:
        raise ValueError("n can't be negative")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    # n = randint(0, 20)
    n = 10
    print(f"Factorial of {n} is {get_factorial_of_number(n)}")
