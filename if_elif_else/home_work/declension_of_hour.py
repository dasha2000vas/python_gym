from random import randint


def declension_of_word_hour(num: int) -> str:
    """
    Defines declension of word hour after number.

    Args:
        num (int): Entered number

    Returns:
        str: Declension of word hour.
    """
    if num % 100 in (11, 12, 13, 14):
        hour = "часов"
    elif num % 10 == 1:
        hour = "час"
    elif num % 10 in (2, 3, 4):
        hour = "часа"
    else:
        hour = "часов"
    return hour


if __name__ == "__main__":
    num = randint(0, 200)
    print(f"{num} {declension_of_word_hour(num)}")
