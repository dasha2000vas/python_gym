from random import randint


def one_positive_even_number(num1: int, num2: int, num3: int) -> bool:
    """
    Define if at least one number is positive and even.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.
        num3 (int): The third number.

    Returns:
        bool: True if at least one number is positive and even, else False.
    """
    return (
            num1 > 0 and num1 % 2 == 0 or
            num2 > 0 and num2 % 2 == 0 or
            num3 > 0 and num3 % 2 == 0
    )


if __name__ == "__main__":
    num1, num2, num3 = randint(0, 100), randint(0, 100), randint(0, 100)
    print(f"Numbers: {num1}, {num2}, {num3}")
    result = one_positive_even_number(num1, num2, num3)
    print(f"At least one number is positive and even: {result}")
