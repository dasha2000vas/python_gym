from random import randint


def nth_fibonacci_number(n: int) -> int:
    """
    Calculates n-th Fibonacci number.

    Args:
        n (int): Number of number.

    Returns:
        (int): n-th Fibonacci number.
    """
    if not isinstance(n, int):
        raise ValueError("n must be integer")
    if n <= 0:
        raise ValueError("n must be positive")
    a1 = 0
    a2 = 0
    for i in range(n):
        if i == 0:
            a2 += 1
        else:
            a1, a2 = a2, a1 + a2
    return a2


if __name__ == "__main__":
    n = randint(1, 100)
    print(f"n = {n}")
    print(f"N-th Fibonacci number = {nth_fibonacci_number(n)}")
