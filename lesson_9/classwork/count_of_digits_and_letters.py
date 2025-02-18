from string import ascii_letters, punctuation, digits, ascii_lowercase

from tools import random_string


def count_of_digits_and_letters(entered_str: str) -> tuple[int, int]:
    """
    Counts number of digits and low letters in string.

    Args:
        entered_str (str): Entered string.

    Returns:
        count_of_digits (int): Number of digits.
        count_of_low_letters (int): Number of low letters.
    """
    if not isinstance(entered_str, str):
        raise ValueError("Entered string must be of type str")
    count_of_digits = count_of_low_letters = 0
    for char in entered_str:
        if char.isdigit():
            count_of_digits += 1
        elif char in ascii_lowercase:
            count_of_low_letters += 1
    return count_of_digits, count_of_low_letters


if __name__ == '__main__':
    entered_str = random_string(words=3, letters=ascii_letters+punctuation+digits)
    print(f"String: {entered_str}")
    result = count_of_digits_and_letters(entered_str)
    print(f"Count of digits: {result[0]}, count of letters: {result[1]}")
