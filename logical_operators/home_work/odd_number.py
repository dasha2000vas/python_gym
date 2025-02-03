from random import randint

def is_odd(a: int) -> bool:
    """
    Defines if number is odd.

    Args:
        a (int): Number to check.

    Returns:
        bool: True if number is odd, else False.
    """
    return bool(a % 2)


if __name__ == "__main__":
    a = randint(-100, 100)
    print(f"Number {a} is odd.")
    print(is_odd(a))
