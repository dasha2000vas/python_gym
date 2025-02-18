from string import ascii_letters, digits, punctuation

from tools import random_string


def remove_spaces(original_string: str) -> str:
    """
    Removes all symbols except letters,
    digits and punctuation from original string.

    Args:
        original_string (str): Entered string.

    Returns:
        result (str): Resulting string.
    """
    if not isinstance(original_string, str):
        raise ValueError('Original must be a string')
    symbols = ascii_letters + digits + punctuation
    result = ""
    for char in original_string:
        if char in symbols:
            result += char
    return result


if __name__ == '__main__':
    original_string = random_string(words=5, letters=ascii_letters + digits + punctuation)
    print(f"Original string: {original_string}")
    print(f"Resulting string: {remove_spaces(original_string)}")
