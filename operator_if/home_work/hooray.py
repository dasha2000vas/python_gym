from random import randint


def belong_to_range(num1: int, num2: int, num3: int) -> str:
    """
    Checks if numbers belong to the range: from -3 to 3.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.
        num3 (int): The third number.

    Returns:
        str: Hooray if the numbers belong to the range.
    """
    return (
        "Hooray!" if -3 <= num1 <= 3 and
        -3 <= num2 <= 3 and
        -3 <= num3 <= 3 else ""
    )


if __name__ == "__main__":
    num1, num2, num3 = randint(-10, 10), randint(-10, 10), randint(-10, 10)
    print(f"Numbers: {num1}, {num2}, {num3}")
    print(belongs_to_range(num1, num2, num3))
