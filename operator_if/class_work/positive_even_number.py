from random import randint


def is_there_positive_even_number(num1: int, num2: int) -> str:
    """
    Defines if there is at least one positive even number.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        str: Says there are positive even numbers or not.
    """
    return (
        "There are positive even numbers"
        if num1 > 0 and not num1 % 2 or num2 > 0 and not num2 % 2
        else "There are no positive even numbers"
    )


if __name__ == "__main__":
    num1, num2 = randint(-100, 100), randint(-100, 100)
    print(f"Numbers: {num1}, {num2}")
    print(is_there_positive_even_number(num1, num2))
