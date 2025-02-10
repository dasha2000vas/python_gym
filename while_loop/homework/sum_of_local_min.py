from random import choice, randint


def sum_of_local_min(numbers: list[int]) -> int:
    """
    Calculates sum of local minimums from list.

    Args:
        numbers (list[int]): List of non-zero numbers.

    Returns:
        int: Sum of local minimums.
    """
    for number in numbers:
        if not isinstance(number, int):
            raise ValueError("All numbers must be an integers")
        if number == 0:
            raise ValueError("All numbers cannot be 0")
    result = 0
    min_number = min(numbers)
    for number in numbers:
        if number == min_number:
            result += min_number
    return result


if __name__ == "__main__":
    n = randint(1, 10)
    numbers_list = [i for i in range(-10, 11) if i != 0]
    numbers = [choice(numbers_list) for _ in range(n)]
    print(f"Number list: {numbers}")
    print(f"Sum of local minimums: {sum_of_local_min(numbers)}")
