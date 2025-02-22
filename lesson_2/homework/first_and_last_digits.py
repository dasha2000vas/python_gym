from random import randint


def swap_first_and_last_digits(number: int) -> int:
    """
    Swaps first and last digits of the number.

    Args:
        number (int): Three-digit number.

    Returns:
        int: The resulting number.
    """
    if not isinstance(number, int):
        raise ValueError("Number must be an integer")
    if not 100 <= number <= 999:
        raise ValueError("Number must be between 100 and 999")
    return number % 10 * 100 + number // 10 % 10 * 10 + number // 100


if __name__ == "__main__":
    number = randint(100, 999)
    print("Number:", number)
    print("Result:", swap_first_and_last_digits(number))
