from random import randint


def is_three_digit_even(number: int) -> bool:
    """
    Defines if number is three-digit and even.

    Args:
        number (int): Number to check.

    Returns:
        int: True if number is three-digit and even, else False.
    """
    return len(str(number).strip("-")) == 3 and not number % 2


if __name__ == "__main__":
    number = randint(-200, 200)
    print(f"{number} is three-digit and even: {is_three_digit_even(number)}")
