from random import randint, choice
from re import match
from typing import Any

def drop_fractional_part(number: float) -> int:
    return int(number)


def random_numbers_of_same_parity() -> tuple[int, int]:
    a = randint(1, 5)
    b = randint(15, 20)
    if not (a % 2 == 0 and b % 2 == 0) and not (a % 2 == 1 and b % 2 == 1):
        if a != 1:
            a -= 1
        else:
            a += 1
    return a, b


def generate_list_of_random_numbers() -> list[int]:
    return [randint(-100, 100) for _ in range(randint(1, 10))]


def check_values_list_of_int(entered_list: list[int]) -> None:
    if not isinstance(entered_list, list):
        raise ValueError("Object 'entered_list' must be list")
    for value in entered_list:
        if not isinstance(value, int):
            raise ValueError("All elements in 'entered_list' must be integers")


def check_path_value(path: str) -> None:
    if not isinstance(path, str):
        raise ValueError("Object 'path' must be of type str")
    if (not match(r"[C-G]:(/[a-zA-Z0-9_-]+)+\.[a-zA-Z]+", path) and
        not match(r"[C-G]:(\\[a-zA-Z0-9_-]+)+\.[a-zA-Z]+", path)):
        raise ValueError("Invalid path")


def print_list(entered_list: list[Any]) -> None:
    print("List:", *entered_list)


def print_list_of_integers(entered_list: list[int]) -> None:
    check_values_list_of_int(entered_list)
    print("List:", end=" ")
    for i in range(len(entered_list)):
        print(f"{entered_list[i]:4d}", end=" ")
    else:
        print()


def random_string(
    words: int,
    letters: str,
    space: str = " ",
    count_of_letters: int | None = None,
    mode: None | str = None
) -> str:
    string = ""
    for _ in range(words):
        if string and mode == "spaces":
            string += space * randint(2, 10)
        elif string: string += space
        if count_of_letters:
            count = count_of_letters
        else:
            count = randint(1, 10)
        for i in range(count):
             string += choice(letters)
    return string
