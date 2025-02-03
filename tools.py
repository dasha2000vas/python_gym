from datetime import datetime
from random import randint

from operator_if.class_work.leap_year import is_year_leap

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


def max_day_of_month(year: int, month: int) -> int:
    if is_year_leap(year) == "is leap year" and month == 2:
        max_day = 29
    elif month == 2:
        max_day = 28
    elif month in (1, 3, 5, 7, 8, 10, 12):
        max_day = 31
    else:
        max_day = 30
    return max_day


def random_time_event(
    yr1=None, mon1=None, day1=None
) -> tuple[datetime, datetime]:
    if yr1 is None and mon1 is None and day1 is None:
        yr1, mon1, = randint(2000, 2025), randint(1, 12)
        day1 = randint(1, max_day_of_month(yr1, mon1))
    yr2, mon2, day2 = yr1, mon1, day1
    hr1, min1, sec1 = randint(0, 23), randint(0, 59), randint(0, 59)
    hr2 = randint(0, 23)
    min2 = min1 + randint(0, 59)
    sec2 = sec1 + randint(0, 59)
    if sec2 > 59:
        sec2 %= 60
        min2 += 1
    if min2 > 59:
        min2 %= 60
        hr2 +=1
    if hr2 > 23:
        hr2 %= 24
        day2 += 1
    elif hr2 < hr1:
        day2 += 1
    if day2 > max_day_of_month(yr2, mon2):
        day2 %= max_day_of_month(yr2, mon2)
        mon2 += 1
    if mon2 > 12:
        mon2 %= 12
        yr2 += 1
    return (
        datetime(yr1, mon1, day1, hr1, min1, sec1),
        datetime(yr2, mon2, day2, hr2, min2, sec2)
    )
