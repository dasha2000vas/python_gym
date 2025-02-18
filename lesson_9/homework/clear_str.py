from string import ascii_lowercase, ascii_uppercase, punctuation, digits

from tools import random_string


def clear_str(original_str: str) -> str:
    """
    Clears entered string. Reduces text
    to lowercase and removes all characters
    except the English alphabet and underscores.

    Args:
        original_str (str): Entered string.

    Returns:
        clear_str (str): Cleared string.
    """
    if not isinstance(original_str, str):
        raise ValueError("Original string must be of type str")
    original_str = original_str.lower()
    cleared_str = ""
    valid_char = ascii_lowercase + "_"
    for char in original_str:
        if char in valid_char:
            cleared_str += char
    return cleared_str


if __name__ == "__main__":
    original_str = random_string(
        words=3,
        letters=ascii_lowercase+ascii_uppercase+digits+punctuation
    )
    print(f"Original string: {original_str}")
    print(f"Cleared string: {clear_str(original_str)}")
