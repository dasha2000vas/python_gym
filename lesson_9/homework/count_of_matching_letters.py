from string import ascii_lowercase
from random import randint

from tools import random_string


def count_of_matching_letters(word1: str, word2: str) -> int:
    """
    Counts number of matching letters in word1 and word2.

    Args:
        word1 (str): First word.
        word2 (str): Second word.

    Returns:
        count (int): Number of matching letters.
    """
    for word in (word1, word2):
        if not isinstance(word, str):
            raise ValueError('All args must be strings')
        if not word.isalpha():
            raise ValueError('All args must contain only letters')
    if len(word1) != len(word2):
        raise ValueError('Args must have same length')
    count = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            count += 1
    return count


if __name__ == '__main__':
    count_of_letters = randint(1, 20)
    word1 = random_string(words=1, letters=ascii_lowercase, count_of_letters=count_of_letters)
    word2 = random_string(words=1, letters=ascii_lowercase, count_of_letters=count_of_letters)
    print(f"Word1: {word1}\nWord2: {word2}")
    print(f"Number of matching letters: {count_of_matching_letters(word1, word2)}")
