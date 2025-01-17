from random import randint


def is_disparities_true(a: int, b: int) -> bool:
    """
    Defines if disparities a > 2 and b <= 3 are true.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        bool: True if a > 2 and b <= 3, else False.
    """
    return a > 2 and b <= 3


if __name__ == '__main__':
    a, b = randint(-100, 100), randint(-100, 100)
    print(f"Disparities {a} > 2 and {b} <= 3 are true.")
    print(is_disparities_true(a, b))
