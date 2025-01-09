from random import randint


def sum_of_digits(integer: int) -> int:
    """
        Data: а three-digit integer
        Task: find the sum of digits of the number using next operations: %, //
    """
    return integer // 100 + integer // 10 % 10 + integer % 10


if __name__ == "__main__":
    integer = randint(100, 999)
    print("Integer:", integer)
    print("Sum of digits:", sum_of_digits(integer))
