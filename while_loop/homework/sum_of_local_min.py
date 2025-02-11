from random import choice, randint


def sum_of_local_min(numbers: list[int]) -> int:
    """
    Calculates sum of local minimums from list.

    Args:
        numbers (list[int]): List of non-zero numbers.

    Returns:
        result(int): Sum of local minimums.
    """
    for number in numbers:
        if not isinstance(number, int):
            raise ValueError("All numbers must be an integers")
        if number == 0:
            raise ValueError("All numbers cannot be 0")
    result = 0
    for i in range(1, len(numbers) - 2):
        if numbers[i-1] > numbers[i] < numbers[i+1]:
            result += numbers[i]
    return result


if __name__ == "__main__":
    n = randint(1, 10)
    numbers_list = [i for i in range(-10, 11) if i != 0]
    numbers = [choice(numbers_list) for _ in range(n)]
    print(f"Number list: {numbers}")
    print(f"Sum of local minimums: {sum_of_local_min(numbers)}")
