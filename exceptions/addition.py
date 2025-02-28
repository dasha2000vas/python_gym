from string import ascii_lowercase, digits
from random import randint, choice

from tools import random_string


def check_values(obj1 : int|str, obj2: int|str) -> None:
    for value in (obj1, obj2):
        if not isinstance(value, (int, str)):
            raise ValueError("All args must be of type str or int")


def add_strings_and_integers(obj1 : int|str, obj2: int|str) -> int|str:
    check_values(obj1, obj2)
    try:
        return int(obj1) + int(obj2)
    except ValueError:
        return str(obj1) + str(obj2)


if __name__ == '__main__':
    obj1 = random_string(
        words=1,
        letters=choice([ascii_lowercase, digits, ascii_lowercase+digits])
    )
    obj2 = randint(1, 100)
    print(f"Object 1: {obj1}, object 2: {obj2}")
    print(f"Result of adding: {add_strings_and_integers(obj1, obj2)}")
