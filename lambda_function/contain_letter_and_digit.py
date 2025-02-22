from random import randint, choice
from string import ascii_letters, digits, ascii_lowercase, ascii_uppercase

from tools import random_string

ALL = ascii_letters + digits

check = lambda x: x.lower() != x and x.upper() != x and bool(set(x) & set(digits))


def contain_letter_and_digit(entered_str: str) -> bool:
    """
    Defines if entered_str contains uppercase
    and lowercase letter aтd digit using lambda function.

    Args:
        entered_str (str): Entered string.

    Returns:
        bool: True if entered_str contains, else False.
    """
    if not isinstance(entered_str, str):
        raise ValueError("Object entered_str must be string")
    return check(entered_str)


if __name__ == '__main__':
    entered_str = random_string(words=1, letters=choice([ALL, digits, ascii_letters]))
    print(f"Entered string: {entered_str}")
    result = contain_letter_and_digit(entered_str)
    print(f"Contains uppercase and lowercase letter aтd digit: {result}")
