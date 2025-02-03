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


def random_time_event() -> tuple[int, int, int, int, int, int,]:
    year1, month1, day1
    hr1, min1, sec1 = randint(0, 23), randint(0, 59), randint(0, 59)
    hr2 = randint(hr1, 23)
    min2 = min1 + randint(0, 59)
    sec2 = sec1 + randint(0, 59)
    if sec2 > 59:
        sec2 %= 60
        min2 += 1
    if min2 > 59:
        min2 %= 60
        hr2 +=1
    if hr2 > 23:
        hr2 = 23
    return hr1, min1, sec1, hr2, min2, sec2

