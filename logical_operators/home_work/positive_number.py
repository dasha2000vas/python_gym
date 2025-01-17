from random import randint


def is_positive(a: int) -> bool:
    """
    Defines if number is positive.

    Args:
        a (int): Number to check.

    Returns:
        bool: True if number is positive, else False.
    """
    return a > 0


if __name__ == "__main__":
    a = randint(-100, 100)
    print(f"Number {a} is positive.")
    print(is_positive(a))
