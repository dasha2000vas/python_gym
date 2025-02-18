from random import choice


def is_palindrome(word: str) -> bool:
    """
    Defines if word is a palindrome.

    Args:
        word (str): Word to check.

    Returns:
        bool: True if word is a palindrome, else False.
    """
    if not isinstance(word, str):
        raise ValueError("Word must be string")
    if not word.isalpha():
        raise ValueError("Word must contain only letters")
    return word.lower() == word.lower()[::-1]


if __name__ == '__main__':
    words = ["dad", "eye", "level", "noon", "cat", "flower", "bird", "tree"]
    word = choice(words)
    print(f"Word: {word}")
    print(f"Is palindrome: {is_palindrome(word)}")
