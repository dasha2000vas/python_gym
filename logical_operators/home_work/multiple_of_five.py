from random import randint


def multiple_of_five(a: int, b: int) -> bool:
    """
    Defines if a or b are multiples of 5.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        bool: True if a or b are multiples of 5, else False.
    """
    return not a % 5 or not b % 5


if __name__ == '__main__':
    a, b = randint(-100, 100), randint(-100, 100)
    print(f"{a} or {b} are multiples of 5.")
    print(multiple_of_five(a, b))
