from string import ascii_letters

from tools import random_string


def get_vowels_of_word(word: str) -> list[str]:
    """
    Gets vowels that occur in word.
    (case-insensitive).

    Args:
        word (str): Entered word.

    Returns:
       vowels_in_word (list[str]): List of vowels in word.
    """
    if not isinstance(word, str):
        raise ValueError('Word must be of type str')
    if not word.isalpha():
        raise ValueError("Word must contain only letters")
    word = word.lower()
    vowels_in_word = []
    vowels = "aeiouy"
    for letter in word:
        if letter in vowels and letter not in vowels_in_word:
            vowels_in_word.append(letter)
    return vowels_in_word


if __name__ == '__main__':
    word = random_string(words=1, letters=ascii_letters, count_of_letters=10)
    print(f"Word: {word}")
    print(f"Vowels in word: {get_vowels_of_word(word)}")
