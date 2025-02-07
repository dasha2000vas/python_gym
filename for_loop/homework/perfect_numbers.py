from random import randint


def get_perfect_numbers(n: int) -> list[int]:
    """
    Finds all perfect numbers from 1 to n.

    Args:
        n (int): Max number.

    Returns:
        result (list[int]): List of perfect numbers.
    """
    if not isinstance(n, int):
        raise ValueError("n must be integer")
    if n <= 0:
        raise ValueError("n must be positive")
    result = []
    for i in range(1, n + 1):
        sum_of_dividers = 0
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                sum_of_dividers += j
        if sum_of_dividers == i:
            result.append(i)
    return result


if __name__ == "__main__":
    n = randint(1, 10000)
    print(f"n = {n}")
    print(f"Perfect numbers up to n: {get_perfect_numbers(n)}")
