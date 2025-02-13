from random import randint


def sum_of_digits_from_str(number: str) -> int:
    """
    Calculates sum of digits of number from string.

    Args:
        number (str): String containing natural number.

    Returns:
        sum_of_digits (int): Sum of digits of number.
    """
    if not isinstance(number, str):
        raise ValueError("Object with name number must be of type str")
    if not (number.isdigit() and int(number) > 0):
        raise ValueError("String with name number must containing natural number")
    sum_of_digits = 0
    for digit in number:
        sum_of_digits += int(digit)
    return sum_of_digits


if __name__ == "__main__":
    number = str(randint(0, 10000))
    print(f"Number = {number}")
    print(f"Sum of digits = {sum_of_digits_from_str(number)}")
