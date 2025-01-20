from random import randint


def get_absolute_value(number: int) -> int:
    """
    Gets the absolute value of number.

    Args:
        number (int): Entered number.

    Returns:
       int: Absolute value of number.

    """
    return number if number > 0 else -number


if __name__ == "__main__":
    number = randint(-100, 100)
    print(f"|{number}| = {get_absolute_value(number)}")
