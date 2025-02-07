from random import randint


def range_from_a_to_b(a: int,b: int, s: int) -> str:
    """
    Writes all natural numbers from
    a to b with step s separated by commas.

    Args:
        a (int): Start number.
        b (int): End number.
        s (int): Step size.

    Returns:
        result (str): Resulting string.
    """
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(s, int):
        raise ValueError("a, b and s must be integers")
    if a <= 0 or b <= 0 or s <= 0:
        raise ValueError("a, b and s must be positive")
    if b <= a:
        raise ValueError("b must be greater than a")
    result = ""
    for i in range(a, b, s):
        if i + s >= b:
            result += f"{i}"
        else:
            result += f"{i}, "
    return result


if __name__ == "__main__":
    a, b, s = randint(1, 50), randint(51, 100), randint(1, 10)
    print(f"a={a}, b={b}, s={s}")
    print(range_from_a_to_b(a, b, s))
