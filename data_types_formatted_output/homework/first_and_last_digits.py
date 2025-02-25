from random import randint


def check_value(number: int) -> None:
    if not isinstance(number, int):
        raise ValueError('Object number must be integer')
    if 999 < number or number < 100:
        raise ValueError('Number must be between 100 and 999 (inclusive)')


def swap_first_and_last_digits(number: int) -> int:
    check_value(number)
    return number % 10 * 100 + number // 10 % 10 * 10 + number // 100


if __name__ == "__main__":
    number = randint(100, 999)
    print("Number:", number)
    print("Result:", swap_first_and_last_digits(number))
