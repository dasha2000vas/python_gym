from random import choice, randint, uniform


def are_all_numbers_even(numbers: list[int]) -> str:
    """
    Defines if all numbers in list are even or not.

    Args:
        numbers (list[int]): List of numbers.

    Returns:
        str: Resulting string.
    """
    if not isinstance(numbers, list):
        raise ValueError("Numbers is not a list")
    for number in numbers:
        if not isinstance(number, int):
            raise ValueError("Items of list numbers must be integers")
    for number in numbers:
        if number % 2:
            return "There are odd numbers"
    return "All numbers are even"


if __name__ == "__main__":
    n = randint(1, 20)
    numbers = [randint(-100, 100) for _ in range(n + 1)]
    print(f"{n} numbers:")
    for i in range(n-1):
        print(numbers[i], end=", ")
    else:
        print(numbers[-1])
    print(are_all_numbers_even(numbers))
