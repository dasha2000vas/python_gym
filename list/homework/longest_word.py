from string import ascii_letters, punctuation
from re import sub, escape

from tools import random_string


def check_value(entered_str: str) -> str:
    if not isinstance(entered_str, str):
        raise ValueError("Object 'entered_str' must be of type str")
    entered_str = sub(r"([" + escape(punctuation) + r"])", "", entered_str)
    if entered_str.strip() == "":
        raise ValueError("Entered string must contain at least one letter")
    for word in entered_str.split():
        if not word.isalpha():
            raise ValueError(
                'Entered string must contain only letters, whitespaces and punctuation'
            )
    return entered_str


def get_longest_word_from_str(entered_str: str) -> str:
    entered_str = check_value(entered_str)
    longest_word = ""
    for word in entered_str.split():
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


if __name__ == '__main__':
    entered_str = random_string(words=10, letters=ascii_letters+punctuation)
    print(f"Entered string: {entered_str}")
    longest_word = get_longest_word_from_str(entered_str)
    print(f"Longest word: {longest_word}")
