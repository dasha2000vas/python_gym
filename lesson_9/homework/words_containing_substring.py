from random import choice
from string import ascii_lowercase

from tools import  random_string


def count_words_containing_substring(entered_string: str, substring: str) -> int:
    """
    Counts number of words containing substring.

    Args:
        entered_string (string): Entered string.
        substring (string): Substring.

    Returns:
        count (int): Number of words containing substring.
    """
    for string in (entered_string, substring):
        if not isinstance(string, str):
            raise ValueError('All args must be strings')
    for word in entered_string.split():
        if not word.isalpha():
            raise ValueError("Entered string must contain only letters and whitespaces")
    if not substring.isalpha():
        raise ValueError("Substring must contain only letters")
    count = 0
    for word in entered_string.split():
        if word.find(substring) != -1:
            count += 1
    return count


if __name__ == '__main__':
    entered_string = random_string(words=5, letters=ascii_lowercase)
    substring = choice(ascii_lowercase)
    print(f"Entered string: {entered_string}")
    print(f"Substring: {substring}")
    print(f"Count of words with substring: {count_words_containing_substring(entered_string, substring)}")
