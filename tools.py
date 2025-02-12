from random import randint, choice
from string import ascii_letters, digits

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


def random_string(words: int, letters, mode: None | str = None) -> str:
    string = ""
    for _ in range(words):
        if string and mode == "spaces":
            string += " " * randint(2, 10)
        elif string: string += " "
        for i in range(randint(1, 10)):
             string += choice(letters)
    return string
