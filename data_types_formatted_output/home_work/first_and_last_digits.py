from random import randint


def swap_first_and_last_digits(number: int) -> int:
    """
        Data: a three-digit integer
        Task: get a new number by swapping first and last digits
    """
    return number % 10 * 100 + number // 10 % 10 * 10 + number // 100


if __name__ == "__main__":
    number = randint(100, 999)
    print("Number:", number)
    print("Result:", swap_first_and_last_digits(number))
