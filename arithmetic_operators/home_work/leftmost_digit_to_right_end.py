from random import randint


def move_leftmost_digit_to_right_end(number: int) -> int:
    """
    Moves the leftmost digit to the right end of the number
    and returns the result.

    Args:
        number (int): The three-digit number.

    Returns:
        int: The resulting number.
    """
    last_digit = number // 100
    return number % 100 * 10 + last_digit


if __name__ == "__main__":
    number = randint(100, 999)
    print("Number:", number)
    print("Result:", move_leftmost_digit_to_right_end(number))
