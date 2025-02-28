from re import sub, escape
from string import ascii_letters

from tools import random_string

AFTER = ".,:;?!)]}"
BEFORE = "([{"


def check_value(entered_string: str) -> None:
    if not isinstance(entered_string, str):
        raise ValueError("Object entered_string must be of type str")


def add_whitespaces(entered_string: str) -> str:
    """
    Adds whitespaces after symbols - .,:;?!)]}...
    and before symbols - ([{.

    Args:
        entered_string (str)

    Returns:
        str: Resulting string.
    """
    check_value(entered_string)
    new_string = entered_string
    for char in AFTER:
        new_string = new_string.replace(char + " ", char)
        new_string = new_string.replace(char, char + " ")
    new_string = new_string.replace(". . .", "...")
    for char in BEFORE:
        new_string = new_string.replace(" " + char, char)
        new_string = new_string.replace(char, " " + char)
    return new_string.strip()


def add_whitespaces_with_re(entered_string: str) -> str:
    check_value(entered_string)
    new_string = entered_string
    for char in AFTER:
        new_string = sub(escape(char) + r"(\s*)", char + " ", new_string)
    new_string = sub(r"\. \. \.", "...", new_string)
    for char in BEFORE:
        new_string = sub(r"(\s*)" + escape(char), " " + char, new_string)
    return new_string.strip()


if __name__ == '__main__':
    entered_string = random_string(words=5, letters=ascii_letters+AFTER+BEFORE)
    print(entered_string)
    print(add_whitespaces(entered_string))
    print(add_whitespaces_with_re(entered_string))
