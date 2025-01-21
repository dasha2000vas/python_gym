from random import randint


def calculate_values(a: int, b: int) -> tuple[float, float, float]:
    """
    Calculates the values of the expressions.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        tuple[float, float, float]: The resulting numbers.
    """
    return (
        a + b + a / b,
        2 * a - a / (3 * b),
        (3 * a) ** 0.5 / (2 * b)
    )


if __name__ == "__main__":
    a, b = randint(0, 50), randint(0, 50)
    print("a =", a, "\nb =", b)
    result_1, result_2, result_3 = calculate_values(a, b)
    print(result_1, result_2, result_3, sep="\n")
