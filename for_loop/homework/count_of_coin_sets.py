from random import randint


def count_of_coin_sets(
    a1: int, a2: int, a5: int, a10: int, target_sum: int
) -> int:
    """
    Counts number of coin sets
    that can compose target sum.

    Args:
        a1 (int): Count of one-ruble coins.
        a2 (int): Count of two-ruble coins.
        a5 (int): Count of five-ruble coins.
        a10 (int): Count of ten-ruble coins.
        target_sum (int): Sum that need to compose.

    Returns:
        count (int): Number of coin sets.
    """
    for number in (a1, a2, a5, a10, target_sum):
        if not isinstance(number, int):
            raise ValueError("All numbers must be integers")
        if number <= 0:
            raise ValueError("All numbers must be positive")
    count = 0
    for i1 in range(a1 + 1):
        for i2 in range(a2 + 1):
            for i5 in range(a5 + 1):
                for i10 in range(a10 + 1):
                    if 1 * i1 + 2 * i2 + 5 * i5 + 10 * i10 == target_sum:
                        count += 1
    return count


if __name__ == "__main__":
    a1, a2, a5, a10 = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 5)
    target_sum = randint(10, 50)
    print(f"Target sum is {target_sum}")
    print(f"1r: {a1}, 2r: {a2}, 5r: {a5}, 10r: {a10}")
    print(f"Count of coin sets: {count_of_coin_sets(a1, a2, a5, a10, target_sum)}")
