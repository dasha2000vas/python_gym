from random import randint


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
