from random import randint


def find_min_number(num1: int, num2: int, num3: int) -> int:
    """
    Defines the smallest number.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.
        num3 (int): The third number.

    Returns:
        min_num (int): The smallest number.
    """
    min_num = num1
    if num2 < min_num: min_num = num2
    if num3 < min_num: min_num = num3
    return min_num


if __name__ == "__main__":
    num1, num2, num3 = randint(-100, 100), randint(-100, 100), randint(-100, 100)
    print(f"Numbers: {num1}, {num2}, {num3}")
    print(f"The smallest number: {find_min_number(num1, num2, num3)}")
