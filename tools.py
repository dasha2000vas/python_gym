from random import randint


def random_time_for_winner_and_second() -> tuple[int, int, int, int, int, int]:
    hr_1, min_1, sec_1 = randint(1, 10), randint(1, 59), randint(1, 59)
    hr_2, min_2, sec_2 = hr_1, min_1, sec_1 + randint(1, 59)
    if sec_2 % 60:
        min_2 += sec_2 // 60
        sec_2 = sec_2 % 60
    return hr_1, min_1, sec_1, hr_2, min_2, sec_2
