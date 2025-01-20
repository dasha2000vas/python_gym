from random import randint


def sum_of_positive_numbers(num1: int, num2: int, num3: int) -> int:
    """
    Calculates the sum of positive numbers.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.
        num3 (int): The third number.

    Returns:
        result (int): The resulting number.
    """
    result = 0
    if num1 > 0: result += num1
    if num2 > 0: result += num2
    if num3 > 0: result += num3
    return result


if __name__ == "__main__":
    num1, num2, num3 = randint(-100, 100), randint(-100, 100), randint(-100, 100)
    print(f"Numbers: {num1}, {num2}, {num3}")
    print(f"Sum of positive numbers: {sum_of_positive_numbers(num1, num2, num3)}")
