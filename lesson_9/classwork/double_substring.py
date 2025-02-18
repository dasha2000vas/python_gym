from random import choice, randint
from string import ascii_letters

from tools import  random_string


def double_substring(original_string: str, substring: str) -> str:
    """
    Doubles every entry of substring in string.

    Args:
        original_string (str): Original string.
        substring (str): String to double.

    Returns:
        updated_string (str): Modified string.
    """
    for string in (original_string, substring):
        if not isinstance(string, str):
            raise ValueError('All args must be strings')
    if original_string.find(substring) != -1:
        updated_string = original_string.replace(substring, substring * 2)
        return updated_string
    return f"There are no entries of {substring} in string"


if __name__ == '__main__':
    original_string = random_string(words=4, letters=ascii_letters)
    substring = choice(ascii_letters)
    print(f"Original string: {original_string}")
    print(f"Substring: {substring}")
    result = double_substring(original_string, substring)
    if "There are no entries of" in result:
        print(result)
    else:
        print(f"Modified string: {result}")
