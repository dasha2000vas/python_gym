from random import choice
from string import ascii_lowercase

from tools import random_string


def remove_last_match(original_string: str, substring: str) -> str:
    """
    Removes last match of substring in original string.
    If there are no matches, returns original string.

    Args:
        original_string (str): Original string.
        substring (str): Substring to remove.

    Returns:
        str: Resulting string.
    """
    for string in (original_string, substring):
        if not isinstance(string, str):
            raise ValueError('All args must be strings')
    return "".join(original_string.rsplit(substring, 1))


if __name__ == '__main__':
    original_string = random_string(words=5,letters=ascii_lowercase)
    substring = choice(ascii_lowercase)
    print(f"Original string: {original_string}")
    print(f"Substring: {substring}")
    print(f"Resulting string: {remove_last_match(original_string, substring)}")
