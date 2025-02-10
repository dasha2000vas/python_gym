from random import randint


def  define_third_digit_from_end(number: int) -> int:
    """
    Defines third digit from end and returns it.

    Args:
        number (int): The number with min three digits.

    Returns:
        int: The third digit from end.
    """
    return number // 100 % 10


if __name__ == "__main__":
    number = randint(100, 999999)
    print("Integer:", number)
    print(f"Third digit from end:", define_third_digit_from_end(number))
