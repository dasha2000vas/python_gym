from random import randint
from string import ascii_lowercase

from tools import random_string


def write_string_n_times(entered_str: str, n: int) -> str:
    """
    Writes entered string n times.

    Args:
        entered_str (str): Entered string.
        n (int): Number of times to write.

    Returns:
        str: Resulting string.
    """
    if not isinstance(entered_str, str):
        raise ValueError('Entered string must be of type str')
    if not isinstance(n, int):
        raise ValueError('n must be of type int')
    if n <= 0:
        raise ValueError("n must be positive")
    return entered_str * n


if __name__ == '__main__':
    entered_str = random_string(words=1, letters=ascii_lowercase)
    n = randint(1, 10)
    print(f"Entered string: {entered_str}")
    print(f"Times: {n}")
    print(f"Result: {write_string_n_times(entered_str, n)}")
