from random import randint


def check_same_digits(num: int) -> bool:
    """
    Checks if number has same digits.

    Args:
        num (int): Entered number.

    Returns:
        bool: True if number has same digits, else False.
    """
    if not isinstance(num, int):
        raise ValueError("Number must be integer")
    num_str = str(num)
    for digit in num_str:
        if num_str.count(digit) > 1:
            return True
    return False


if __name__ == '__main__':
    num = randint(1, 1000)
    print(f"Number = {num}")
    print(f"Number has same digits: {check_same_digits(num)}")
