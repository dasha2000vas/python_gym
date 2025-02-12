from string import ascii_letters, digits

from tools import random_string


def leave_one_space(original_string: str) -> str:
    """
    Leaves one space between each word in string.

    Args:
        original_string (str): String with multiple spaces.

    Returns:
        str: Updated string.
    """
    if not isinstance(original_string, str):
        raise ValueError('Original must be a string')
    return " ".join(original_string.split())


if __name__ == '__main__':
    original_string = random_string(words=3, letters=ascii_letters + digits, mode="spaces")
    print(f"Original string: {original_string}")
    print(f"Updated string: {leave_one_space(original_string)}")
