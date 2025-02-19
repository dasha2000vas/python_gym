from random import randint


def define_fibonacci_number(number: int) -> tuple[int,int] | int | str:
    """
    Defines if entered number is fibonacci
    number. Returns its order number or message
    that it isn't fibonacci number.

    Args:
        number (int): Entered number.

    Returns:
        tuple[int]|int|str: Order number(s) or message.
    """
    if not isinstance(number, int):
        raise ValueError("Number must be integer")
    if number <= 0:
        raise ValueError("Number must be positive")
    if number == 1:
        return 1, 2
    a1 = 1
    a2 = 1
    n = 3
    while a2 <= number:
        a1, a2 = a2, a1 + a2
        if a2 == number:
            return n
        n += 1
    return f"Number {number} isn't fibonacci number"


if __name__ == "__main__":
    number = randint(1, 100)
    print(f"number = {number}")
    result = define_fibonacci_number(number)
    if isinstance(result, str):
        print(result)
    else:
        print(f"Order number(s): {result}")
