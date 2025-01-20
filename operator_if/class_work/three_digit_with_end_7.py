from random import randint


def three_digit_with_end_seven(num1: int, num2: int) -> bool:
    """
    Defines if there is at least one
    three-digit number what ends with 7.

    Args:
        num1 (int): The first positive number.
        num2 (int): The second positive number.

    Returns:
        bool: True if there is three digit with end 7, else False.
    """
    return (
            len(str(num1)) == 3 and num1 % 10 == 7 or
            len(str(num2)) == 3 and num2 % 10 == 7
    )


if __name__ == "__main__":
    num1, num2 = randint(1, 200), randint(1, 200)
    print(f"Numbers: {num1}, {num2}")
    result = three_digit_with_end_seven(num1, num2)
    print(f"There is at least one three-digit number what ends with 7: {result}")
