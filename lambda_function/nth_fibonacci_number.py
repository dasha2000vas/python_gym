from random import randint

fibonacci = lambda x, y: (y, x + y)


def get_nth_fibonacci_number(n: int) -> int:
    """
    Gets n-th fibonacci number
    using lambda function.

    Args:
        n (int): Member's index.

    Returns:
        int: N-th fibonacci number.
    """
    if not isinstance(n, int):
        raise ValueError('Object n must be integer')
    if n < 0:
        raise ValueError('Number n cannot be negative')
    if n == 0:
        return 0
    x, y = 1, 1
    for _ in range(3, n + 1):
        x, y = fibonacci(x, y)
    return y


if __name__ == '__main__':
    n = randint(1, 20)
    print(f"n = {n}")
    print(f"N-th fibonacci number: {get_nth_fibonacci_number(n)}")
