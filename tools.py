from random import randint


def drop_fractional_part(number: float) -> int:
    """
    Drops fractional part of given number.

    Args:
        number (float): Float number.

    Returns:
        int: Dropped number.
    """
    return int(number)


def random_numbers_of_same_parity() -> tuple[int, int]:
    """
    Generates two random
    numbers of same parity.

    Returns:
        a (int): First number.
        b (int): Second number.
    """
    a = randint(1, 5)
    b = randint(15, 20)
    if not (a % 2 == 0 and b % 2 == 0) and not (a % 2 == 1 and b % 2 == 1):
        if a != 1:
            a -= 1
        else:
            a += 1
    return a, b


def random_time_for_winner_and_second() -> tuple[int, int, int, int, int, int]:
    """
    Generates random time for
    winner and second opponent.

    Returns:
        hr_1 (int): Hours of the winner.
        min_1 (int): Minutes of the winner.
        sec_1 (int): Seconds of the winner.
        hr_2 (int): Hours of the next opponent.
        min_2 (int): Minutes of the next opponent.
        sec_2 (int): Seconds of the next opponent.
    """
    hr_1, min_1, sec_1 = randint(1, 10), randint(1, 59), randint(1, 59)
    hr_2, min_2, sec_2 = hr_1, min_1, sec_1 + randint(1, 59)
    if sec_2 % 60:
        min_2 += sec_2 // 60
        sec_2 = sec_2 % 60
    return hr_1, min_1, sec_1, hr_2, min_2, sec_2
