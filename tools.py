from random import randint, choice


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


def random_string(
    words: int,
    letters: str,
    count_of_letters: int | None = None,
    mode: None | str = None
) -> str:
    string = ""
    for _ in range(words):
        if string and mode == "spaces":
            string += " " * randint(2, 10)
        elif string: string += " "
        if count_of_letters:
            count = count_of_letters
        else:
            count = randint(1, 10)
        for i in range(count):
             string += choice(letters)
    return string
