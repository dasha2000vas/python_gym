from random import randint


def three_digit_with_end_one(num1: int, num2: int) -> bool:
    """
    Defines if all numbers are
    three-digit and ends with 1.

    Args:
        num1 (int): The first positive number.
        num2 (int): The second positive number.

    Returns:
        bool: True if all numbers are three-digit and ends with 1, else False.
    """
    return (
            len(str(num1)) == 3 and num1 % 10 == 1 and
            len(str(num2)) == 3 and num2 % 10 == 1
    )


if __name__ == "__main__":
    num1, num2 = randint(1, 200), randint(1, 200)
    print(f"Numbers: {num1}, {num2}")
    result = three_digit_with_end_one(num1, num2)
    print(f"All numbers are three-digit and ends with 1: {result}")
