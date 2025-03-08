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
    index = 0
    while index <= len(entered_string) - 1:
        if entered_string[index] in AFTER and entered_string[index - 1] == " ":
            entered_string = entered_string[:index - 1] + entered_string[index:]
            index -= 1
        elif entered_string[index] in BEFORE and entered_string[index - 1] != " ":
            entered_string = entered_string[:index] + " " + entered_string[index:]
            index += 1
        if (
            index != len(entered_string) - 1 and
            entered_string[index] in AFTER and
            entered_string[index + 1] != " " and
            entered_string[index + 1] not in AFTER
        ):
            entered_string = entered_string[:index + 1] + " " + entered_string[index + 1:]
            index += 1
        elif entered_string[index] in BEFORE and entered_string[index + 1] == " ":
            entered_string = entered_string[:index + 1] + entered_string[index + 2:]
            index -= 1
        index += 1
    return entered_string.strip()


def add_whitespaces_with_re(entered_string: str) -> str:
    check_value(entered_string)
    new_string = entered_string
    new_string = sub(r" ([.,:;?!)\]}])", r"\1", new_string)
    new_string = sub(r"([(\[{]) ", r"\1", new_string)
    new_string = sub(r"([.,:;?!)\]}]|\.\.\.)(\w|[(\[{])", r"\1 \2", new_string)
    new_string = sub(r"(\w)([(\[{])", r"\1 \2", new_string)
    return new_string.strip()


if __name__ == '__main__':
    entered_string = random_string(words=5, letters=ascii_letters+AFTER+BEFORE)
    print(entered_string)
    print(add_whitespaces(entered_string))
    print(add_whitespaces_with_re(entered_string))
