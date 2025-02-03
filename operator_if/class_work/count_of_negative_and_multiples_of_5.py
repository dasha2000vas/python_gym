from random import randint


def count_of_negative_and_multiples_of_five(num1: int, num2: int, num3: int) -> int:
    """
    Calculates count of negative numbers what are multiples of 5.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.
        num3 (int): The third number.

    Returns:
        count (int): The result of count.
    """
    count = 0
    if num1 < 0 and not num1 % 5: count += 1
    if num2 < 0 and not num2 % 5: count += 1
    if num3 < 0 and not num3 % 5: count += 1
    return count


if __name__ == "__main__":
    num1, num2, num3 = randint(-100, 100), randint(-100, 100), randint(-100, 100)
    print(f"Numbers: {num1}, {num2}, {num3}")
    count = count_of_negative_and_multiples_of_five(num1, num2, num3)
    print(f"Count of negative numbers what are multiples of 5: {count}")
