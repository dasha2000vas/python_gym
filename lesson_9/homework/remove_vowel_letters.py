from string import ascii_letters

from tools import random_string


def remove_vowel_letters(original_string: str) -> str:
    """
    Removes vowel letters from string.

    Args:
        original_string (str): Original string.

    Returns:
        result (str): Resulting string.
    """
    vowel_letters = "AEIOUYaeiouy"
    if not isinstance(original_string, str):
        raise ValueError('Original must be a string')
    result = ""
    for char in original_string:
        if char not in vowel_letters:
            result += char
    return result.strip(" ")


if __name__ == '__main__':
    original_string = random_string(words=3, letters=ascii_letters)
    print(f"Original string: {original_string}")
    result = remove_vowel_letters(original_string)
    print(f"String with no vowel letters: {result}")
