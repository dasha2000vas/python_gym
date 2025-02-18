from random import choice


def shortening_word(word: str) -> str:
    """
    Shorts word if it has more than seven letters.

    Args:
        word (str): Entered word.

    Returns:
        str: Shortened word if letters > 7,
             else word without change.
    """
    if not isinstance(word, str):
        raise ValueError('Word must be of type str')
    if not word.isalpha():
        raise ValueError("Word must contain only letters")
    if not len(word) > 7:
        return word
    shortened_word = ""
    vowels = "aeiouy"
    consonant = "bcdfghjklmnpqrstvwxz"
    two_vowels = 0
    for i in range(len(word)):
        if word[i] in vowels:
            two_vowels += 1
        if word[i] in consonant and two_vowels == 2:
            shortened_word += word[:i+1] + "-"
            break
    for i in range(-1, -len(word), -1):
        if word[i] in consonant:
            shortened_word += word[i:]
            break
    return shortened_word


if __name__ == '__main__':
    words = [
        "biomechanical", "aesthetically",
        "antibacterial", "automatically",
        "collaboration", "decompression",
        "cat", "taco",
        "cheese", "sun",
        "dog", "like",
    ]
    word = choice(words)
    print(f"Word: {word}")
    print(f"Shortened word: {shortening_word(word)}")
