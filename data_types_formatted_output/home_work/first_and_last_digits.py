from random import randint


def get_first_and_last_digits(number: int) -> int:
    """
        Data: a three-digit integer
        Task: get a new number made up of the first and last digits
    """
    return number // 100 * 10 + number % 10


if __name__ == "__main__":
    number = randint(100, 999)
    print("Number:", number)
    print("Result:", get_first_and_last_digits(number))
