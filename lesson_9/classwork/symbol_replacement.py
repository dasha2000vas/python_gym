from string import ascii_lowercase, digits

from tools import random_string


def symbol_replacement(original_string: str, replace: str) -> str:
    """
    Replaces all entries of first symbol in string except first one.

    Args:
        original_string (str): Original string.
        replace (str): Substring to replace first symbol.

    Returns:
        updated_string (str): Updated string.
    """
    for string in (original_string, replace):
        if not isinstance(string, str):
            raise ValueError('Original string must of type str')
    first_symbol = original_string[0]
    updated_string = original_string[1:].replace(first_symbol, replace)
    return first_symbol + updated_string


if __name__ == '__main__':
    original_string = random_string(words=3, letters=ascii_lowercase)
    replace = random_string(words=1, letters=digits)
    print(f"Original string: {original_string}")
    print(f"Replaced string: {replace}")
    print(f"Updated string: {symbol_replacement(original_string, replace)}")
