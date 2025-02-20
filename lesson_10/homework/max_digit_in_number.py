from random import randint


def get_max_digit_in_number(num: int) -> int:
    """
    Gets maximum digit in number.

    Args:
        num (int): Entered number.

    Returns:
        int: Maximum digit.
    """
    if not isinstance(num, int):
        raise ValueError('num must be integer')
    if num <= 0:
        raise ValueError('num must be positive')
    max_digit = 0
    for digit in str(num):
        if int(digit) > max_digit:
            max_digit = int(digit)
    return max_digit


if __name__ == '__main__':
    num = randint(1, 10000)
    print(f"Number: {num}")
    print(f"Maximum digit: {get_max_digit_in_number(num)}")
