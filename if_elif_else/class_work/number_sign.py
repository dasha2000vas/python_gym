from random import randint


def number_sign(num: int) -> str:
    """
    Defines if number sign is plus or minus or number is zero.

    Args:
        num (int): Entered number.

    Returns:
       str: Resulting string.
    """
    if num == 0:
        return "Number is zero"
    else:
        if num > 0:
            return f"Sign of number {num} is plus"
        else:
            return f"Sign of number {num} is minus"


if __name__ == "__main__":
    num = randint(-100, 100)
    print(number_sign(num))
