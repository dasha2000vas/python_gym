from random import randint


def glue_numbers(a: int, b: int) -> int:
    """
    Adds the second number from the right.

    Args:
        a (int): The first three-digit number.
        b (int): The second three-digit number.

    Returns:
        int: The resulting of the gluing.
    """
    return a * 1000 + b


if __name__ == '__main__':
    a, b = randint(100, 999), randint(100, 999)
    print("a =", a, "\nb =", b)
    print("Result:", glue_numbers(a, b))
