from random import randint


def are_even_numbers(a: int, b: int) -> bool:
    """
    Defines if a and b are even numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        bool: True if a and b are even numbers, else False.
    """
    return not a % 2 and not b % 2


if __name__ == "__main__":
    a, b = randint(-100, 100), randint(-100, 100)
    print(f"Both {a} and {b} are even numbers.")
    print(are_even_numbers(a, b))
