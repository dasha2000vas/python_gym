from string import ascii_letters, punctuation, digits
from re import findall

from tools import random_string


def check_value(entered_string: str) -> None:
    if not isinstance(entered_string, str):
        raise ValueError("Object entered_string must be of type str")


def clean_string(entered_string: str) -> str:
    """
    Removes from string all symbols
    except letters and underlining.

    Args:
        entered_string (str)

    Returns:
        str: Resulting string.
    """
    check_value(entered_string)
    return "".join(findall(r"[a-zA-Z]|_", entered_string))


if __name__ == '__main__':
    entered_string = random_string(words=5, letters=ascii_letters+punctuation+digits, space="_")
    print(entered_string)
    print(clean_string(entered_string))
