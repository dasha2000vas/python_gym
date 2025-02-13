from string import ascii_letters

from tools import random_string


def add_html_tags_around_word(word: str) -> str:
    """
    Adds html tags around word.

    Args:
        word (str): Entered string.

    Returns:
        str: Resulting string.
    """
    if not isinstance(word, str):
        raise ValueError('Word must be a string')
    return f'<{word}>'


if __name__ == '__main__':
    word = random_string(words=1, letters=ascii_letters)
    print(f"Entered word: {word}")
    print(f"Add html tags: {add_html_tags_around_word(word)}")
