from random import randint


def move_leftmost_digit_to_right_end(number: int) -> int:
    """
    Moves the leftmost digit to the right end of the number.

    Args:
        number (int): The three-digit number.

    Returns:
        int: The resulting number.
    """
    return number % 100 * 10 + number // 100


if __name__ == "__main__":
    number = randint(100, 999)
    print("Number:", number)
    print("Result:", move_leftmost_digit_to_right_end(number))
