from string import ascii_lowercase, digits

from tools import random_string


def swap_first_and_last_symbol(original_string: str) -> str:
    """
    Swaps first and last symbol of entered string.

    Args:
        original_string (str): Entered string.

    Returns:
        str: Updated string.
    """
    if not isinstance(original_string, str):
        raise ValueError('Original must be a string')
    return original_string[-1] + original_string[1:-1] + original_string[0]


if __name__ == '__main__':
    original_string = random_string(words=1, letters=ascii_lowercase)
    print(f"Original string: {original_string}")
    print(f"Updated string: {swap_first_and_last_symbol(original_string)}")
