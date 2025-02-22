from random import randint


def glue_numbers_without_last_digits(a: int, b: int) -> int:
    """
    Adds the second number from the right
    to the first, without the last digits of each.

    Args:
        a (int): The first three-digit number.
        b (int): The second three-digit number.

    Returns:
        int: The resulting number.
    """
    for number in (a, b):
        if not isinstance(number, int):
            raise ValueError("All args must be an integers")
        if not 100 <= number <= 999:
            raise ValueError("All numbers must be between 100 and 999")
    return a // 10 * 100 + b // 10


if __name__ == "__main__":
    a, b = randint(100, 999), randint(100, 999)
    print("a =", a, "\nb =", b)
    print("Result:", glue_numbers_without_last_digits(a, b))
