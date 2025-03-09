from math import sqrt
from random import randint


def check_values(first: int, last: int) -> None:
    for value in (first, last):
        if not isinstance(value, int):
            raise ValueError("All args must be of type int")
        if value < 0:
            raise ValueError("Numbers cannot be negative")


def get_square_roots(first: int, last: int) -> list:
    check_values(first, last)
    if first > last:
        first, last = last, first
    return [round(sqrt(i), 3) for i in range(first, last + 1)]


if __name__ == '__main__':
    first, last = randint(1, 50), randint(1, 50)
    print(f"First: {first}, last: {last}")
    print(f"Result: {get_square_roots(first, last)}")
