from string import ascii_letters

from tools import random_string


def get_longest_word(entered_str: str) -> str:
    """
    Defines longest word in entered string.

    Args:
        entered_str (str): Entered string.

    Returns:
        target_word (str): Longest word.
    """
    if not isinstance(entered_str, str):
        raise ValueError("Entered string must be of type str")
    entered_str = entered_str.strip(".?!")
    entered_str = entered_str.replace(",", "")
    for word in entered_str.split():
        if not word.isalpha():
            raise ValueError(
                'Entered string must contain only letters and and whitespaces'
            )
    length = 0
    target_word = ""
    for word in entered_str.split():
        if len(word) > length:
            length = len(word)
            target_word = word
    return target_word


if __name__ == '__main__':
    entered_str = random_string(words=5, letters=ascii_letters)
    print(f"Entered string: {entered_str}")
    print(f"Longest word: {get_longest_word(entered_str)}")
