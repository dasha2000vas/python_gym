from random import randint


def  define_third_digit_from_end(integer: int) -> int:
    """
        Data: integer - min three digits
        Task: define third digit from end
    """
    return integer // 100 % 10


if __name__ == "__main__":
    integer = randint(100, 999999)
    print("Integer:", integer)
    print(f"Third digit from end:", define_third_digit_from_end(integer))
