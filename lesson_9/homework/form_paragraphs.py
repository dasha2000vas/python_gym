from string import ascii_lowercase
from random import  randint

from tools import random_string


def form_paragraphs(entered_str: str) -> list[str]:
    """
    Forms paragraphs with length 45 for
    every string from entered string.

    Args:
        entered_str (str): Entered string.

    Returns:
        list_of_strings (list[str]): List of strings.
    """
    if not isinstance(entered_str, str):
        raise ValueError("Entered string must be of type str")
    list_of_strings = []
    for paragraphs in entered_str.split("$"):
        form_str = "    "
        for word in paragraphs.split():
            if len(form_str + word) <= 45:
                if form_str == "    ":
                    form_str += word
                else:
                    form_str += " " + word
            else:
                list_of_strings.append(form_str)
                form_str = word
        if len(form_str) > 1:
            list_of_strings.append(form_str)
    return list_of_strings


if __name__ == '__main__':
    entered_str = random_string(words=randint(1, 10), letters=ascii_lowercase)
    for _ in range(randint(1, 10)):
        entered_str += "$" + random_string(words=randint(1, 20), letters=ascii_lowercase)
    print(f"Entered string: {entered_str}")
    print(f"Output:")
    for form_str in form_paragraphs(entered_str):
        print(form_str)
