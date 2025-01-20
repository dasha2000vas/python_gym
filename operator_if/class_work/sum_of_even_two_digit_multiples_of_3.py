from random import randint


def sum_of_even_two_digit_multiples_of_three(num1: int, num2: int, num3: int) -> int:
    """
    Calculates the sum of even two-digit numbers what are multiples of 3.

    Args:
        num1 (int): The first positive number.
        num2 (int): The second positive number.
        num3 (int): The third positive number.

    Returns:
        result (int): The resulting number.
    """
    result = 0
    if not num1 % 2 and len(str(num1)) == 2 and not num1 % 3:
        result += num1
    if not num2 % 2 and len(str(num2)) == 2 and not num2 % 3:
        result += num2
    if not num3 % 2 and len(str(num3)) == 2 and not num3 % 3:
        result += num3
    return result


if __name__ == "__main__":
    num1, num2, num3 = randint(1, 200), randint(1, 200), randint(1, 200)
    print(f"Numbers: {num1}, {num2}, {num3}")
    result = sum_of_even_two_digit_multiples_of_three(num1, num2, num3)
    print(f"Sum of even two-digit numbers what are multiples of 3: {result}")
