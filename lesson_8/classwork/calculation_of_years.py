from string import ascii_letters
from random import randint

from tools import random_string


def calculation_of_years(name: str, age: int) -> float:
    """
    Calculates how many years user has
    lived for each letter of his name
    (space is not taken into account).

    Args:
        name (string): Name and surname of user.
        age (int): Age of user.

    Returns:
        years (float): Resulting number.
    """
    if not isinstance(name, str):
        raise ValueError('Name must be a string')
    name = name.replace(" ", "")
    if not name.isalpha():
        raise ValueError('Name must contain only letters')
    if not isinstance(age, int):
        raise ValueError('Age must be integer')
    if age <= 0 or age > 130:
        raise ValueError('Age must be between 1 and 130')
    return round(age / len(name), 3)


if __name__ == '__main__':
    name, age = random_string(words=2, letters=ascii_letters), randint(1, 130)
    print(f"Name: {name}")
    print(f"Age: {age}")
    years = calculation_of_years(name, age)
    print(f"You have lived for {years} years for every letter of your first and last name")
