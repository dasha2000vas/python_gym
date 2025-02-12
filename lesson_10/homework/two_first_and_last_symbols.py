from string import ascii_letters

from tools import random_string


def two_first_and_last_symbols(original_string: str) -> str:
    """
    Forms string from first and
    last symbols of original string.
    Note: if string length is less
    than 2, it returns empty string.

    Args:
        original_string (str): Entered string.

    Returns:
        str: Resulting string.
    """
    if not isinstance(original_string, str):
        raise ValueError('Original must be a string')
    if len(original_string) < 2:
        return ""
    return original_string[0:2] + original_string[-2:]


if __name__ == '__main__':
    original_string = random_string(words=1, letters=ascii_letters)
    print(f"Original string: {original_string}")
    print(f"Updated string: {two_first_and_last_symbols(original_string)}")
