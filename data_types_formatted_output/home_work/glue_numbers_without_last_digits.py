from random import randint


def glue_numbers_without_last_digits(a: int, b: int) -> int:
    """
        Data: two three-digit integers
        Task: get a new number by adding the second number from the right
              to the first, without the last digits of each
    """
    return a // 10 * 100 + b // 10


if __name__ == "__main__":
    a, b = randint(100, 999), randint(100, 999)
    print("a =", a, "\nb =", b)
    print("Result:", glue_numbers_without_last_digits(a, b))
