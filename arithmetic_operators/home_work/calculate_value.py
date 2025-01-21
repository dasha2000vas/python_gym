from random import choice


def calculate_value(a: int, b: int, c: int, d: int) -> float:
    """
    Calculates the value of the expression.
    Note: if a=0 or b=0 the value will always be negative,
    if c=0 or d=0 there will always be division by zero.

    Args:
        a (int): The first number, not zero.
        b (int): The second number, not zero.
        c (int): The third number, not zero.
        d (int): The fourth number, not zero.

    Returns:
        float: The resulting number.
    """
    return round(3 * a * b - 4 / (c * d), 3)


if __name__ == "__main__":
    numbers = [i for i in range(-50, 50) if i != 0]
    a, b, c, d = choice(numbers), choice(numbers), choice(numbers), choice(numbers)
    print("a =", a, "\nb =", b, "\nc =", c, "\nd =", d)
    print("Result:", calculate_value(a, b, c, d))
