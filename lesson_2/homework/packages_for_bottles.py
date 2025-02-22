from math import ceil
from random import randint


def find_number_of_packages(n: int, k: int) -> int:
    """
    Calculates how many packages we need to pack n bottles
    if one package can hold maximum k bottles.

    Args:
        n (int): Number of bottles.
        k (int): Max number of bottles that can hold one package.

    Returns:
        int: Number of packages.
    """
    for number in (n, k):
        if not isinstance(number, int):
            raise ValueError('All args must be integers')
        if number <= 0:
            raise ValueError('All numbers must be positive')
    return ceil(n / k)


if __name__ == "__main__":
    n, k = randint(1, 100), randint(5, 20)
    print("Total bottles:", n, "\nPackage hold bottles:", k)
    print("We need", find_number_of_packages(n, k), "packages")
