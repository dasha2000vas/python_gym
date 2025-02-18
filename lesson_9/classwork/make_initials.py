from string import ascii_letters
from random import randint

from tools import random_string


def make_initials_first_way(full_name):
    """
    Makes string with initial
    and surname from full name.
    First way to make it.

    Args:
        full_name (str): Full name of person.

    Returns:
        initial (str): String with initial and surname.
    """
    if not isinstance(full_name, str):
        raise ValueError("Full name must be of type str")
    if full_name.count(" ") == 0:
        raise ValueError("Name must be full")
    initial = full_name
    start_index = 0
    for i in range(full_name.count(" ")):
        end_index = full_name.find(" ", start_index)
        name = full_name[start_index:end_index]
        initial = initial.replace(name, name[0] + ".")
        start_index = end_index + 1
    return initial.title()


def make_initials_second_way(full_name):
    """
    Makes string with initial
    and surname from full name.
    Second way to make it.

    Args:
        full_name (str): Full name of person.

    Returns:
         str: String with initial and surname.
    """
    if not isinstance(full_name, str):
        raise ValueError("Full name must be of type str")
    if full_name.count(" ") == 0:
        raise ValueError("Name must be full")
    word_list = full_name.split()
    for i in range(len(word_list) - 1):
        word_list[i] = word_list[i][0] + "."
    return " ".join(word_list).title()



if __name__ == '__main__':
    full_name = random_string(words=randint(2,5), letters=ascii_letters)
    print(f"Full name: {full_name}")
    print("Initial and surname:")
    print(f"first way: {make_initials_first_way(full_name)}")
    print(f"second way: {make_initials_second_way(full_name)}")
