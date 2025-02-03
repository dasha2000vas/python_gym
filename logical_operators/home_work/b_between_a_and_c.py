from random import randint


def b_between_a_and_c(a: int, b: int, c: int) -> int:
    """
    Defines if b is between a and c.

    Args:
        a (int): The first number.
        b (int): The second number.
        c (int): The third number.

    Returns:
        int: 1 if b is between a and c, else 0.
    """
    return int(a < b < c)


if __name__ == "__main__":
    a, b, c = randint(0, 49), randint(1, 99), randint(50, 100)
    print(f"Number {b} is between {a} and {c}.")
    print(b_between_a_and_c(a, b, c))
