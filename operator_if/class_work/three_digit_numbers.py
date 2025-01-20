from random import randint


def one_three_digit_number(num1, num2, num3):
    """
    Defines if there is at least one three-digit number.

    Args:
        num1 (int): The first positive number.
        num2 (int): The second positive number.
        num3 (int): The third positive number.

    Returns:
        bool: True if at least one three-digit number is found, else False.
    """
    return len(str(num1)) == 3 or len(str(num2)) == 3 or len(str(num3)) == 3


def three_digit_numbers(num1, num2, num3):
    """
    Defines if all numbers are threedigits.

    Args:
        num1 (int): The first positive number.
        num2 (int): The second positive number.
        num3 (int): The third positive number.

    Returns:
        bool: True if all numbers are three-digits, else False.
    """
    return len(str(num1)) == 3 and len(str(num2)) == 3 and len(str(num3)) == 3


if __name__ == "__main__":
    num1, num2, num3 = randint(1, 200), randint(1, 200), randint(1, 200)
    print(f"Numbers: {num1}, {num2}, {num3}")
    result_1 = one_three_digit_number(num1, num2, num3)
    result_2 = three_digit_numbers(num1, num2, num3)
    print(f"There is at least one three-digit number: {result_1}")
    print(f"All numbers have three-digits: {result_2}")
