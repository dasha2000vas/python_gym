from random import randint


def sum_of_digits(number: int) -> int:
    """
    Calculates the sum of digits of the
    number using next operations: %, //.

    Args:
        number (int): The three-digit number.

    Returns:
        int: The sum of digits.
    """
    return number // 100 + number // 10 % 10 + number % 10


if __name__ == "__main__":
    number = randint(100, 999)
    print("Integer:", number)
    print("Sum of digits:", sum_of_digits(number))
