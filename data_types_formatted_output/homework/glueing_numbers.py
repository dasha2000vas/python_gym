from random import randint


def check_values(number1: int, number2: int):
    for value in (number1, number2):
        if not isinstance(value, int):
            raise ValueError('All args must be integers')
        if 999 < value or value < 100:
            raise ValueError('All numbers must be between 100 and 999 (inclusive)')


def glue_numbers_without_last_digits(number1: int, number2: int) -> int:
    check_values(number1, number2)
    return number1 // 10 * 100 + number2 // 10


if __name__ == "__main__":
    number1, number2 = randint(100, 999), randint(100, 999)
    print("number1 =", number1, "\nnumber2 =", number2)
    result = glue_numbers_without_last_digits(number1, number2)
    print("Result:", result)
