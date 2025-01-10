from math import ceil
from random import randint


def find_number_of_packages(n: int, k: int) -> int:
    """
    Someone decided to hand over the empty bottles by packing them in packages.
        Data: number of bottles - n,
              the maximum number of bottles that can hold one package - k
        Task: find how many packages he needs
    """
    return ceil(n / k)


if __name__ == "__main__":
    n, k = randint(1, 100), randint(5, 20)
    print("Total bottles:", n, "\nPackage hold bottles:", k)
    print("We need", find_number_of_packages(n, k), "packages")
