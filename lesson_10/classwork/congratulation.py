from random import randint
from string import ascii_lowercase

from tools import random_string

def congratulation(name: str, n: int) -> str:
    """
    Inserts name in greeting and congratulation.
    Writes result n times.

    Args:
        name (str): Name of person.
        n (int): Number of times.

    Returns:
        str: Greeting and congratulation.
    """
    if not isinstance(name, str):
        raise ValueError('Name must be of type str')
    if not name.isalpha():
        raise ValueError("Name must contain only letters")
    if not isinstance(n, int):
        raise ValueError('n must be of type int')
    if n <= 0:
        raise ValueError("n must be positive")
    return f"Hi, {name.title()}! Happy New Year!\n" * n


if __name__ == '__main__':
    name = random_string(words=1, letters=ascii_lowercase)
    n = randint(1, 10)
    print(congratulation(name, n))
