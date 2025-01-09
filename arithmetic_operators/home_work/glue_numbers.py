from random import randint


def glue_numbers(a: int, b: int) -> int:
    """
        Data: two three-digit numbers - a, b
        Task: glue those numbers
    """
    return a * 1000 + b


if __name__ == '__main__':
    a, b = randint(100, 999), randint(100, 999)
    print("a =", a, "\nb =", b)
    print("Result:", glue_numbers(a, b))
