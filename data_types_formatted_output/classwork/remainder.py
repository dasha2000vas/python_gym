from random import randint


def check_values(number: int, divider: int) -> None:
    for value in (number, divider):
        if not isinstance(value, int):
            raise ValueError("All args must be integers")
        if value <= 0:
            raise ValueError("All numbers must be positive")


def calculate_remainder(number: int, divider: int) -> int :
    """
    Writes number thousand times, then finds
    remainder of division by divider.

    Args:
        number (int): The first number.
        divider (int): The divider.

    Returns:
        int: The resulting number.
    """
    check_values(number, divider)
    return int(str(number) * 1000) % divider


if __name__ == '__main__':
    number, divider = randint(1, 999), randint(2, 50)
    print("Number:", number, "\nDivider:", divider)
    result = calculate_remainder(number, divider)
    print("Remainder:", result)
