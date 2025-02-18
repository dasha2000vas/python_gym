from string import ascii_letters, digits

from tools import random_string


def make_lower(original_str):
    """
    Makes all letters lowercase.

    Args:
        original_str (str): Original string.

    Returns:
        str: Lower string.
    """
    if not isinstance(original_str, str):
        raise ValueError("Original string must be of type str")
    return original_str.lower()


if __name__ == '__main__':
    original_str = random_string(words=3, letters=ascii_letters+digits)
    print(f"Original string: {original_str}")
    print(f"Updated string: {make_lower(original_str)}")
