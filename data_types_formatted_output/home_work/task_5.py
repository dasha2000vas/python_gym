from math import ceil


def find_number_of_packages(n: int, k: int) -> int:
    """
    Someone decided to hand over the empty bottles by packing them in bags.
    Data: number of bottles - n,
          the maximum number of bottles that can hold one package - k
    Task: find how many packages he needs
    """
    return ceil(n / k)


if __name__ == "__main__":
    n, k = int(input("Total bottles: ")), int(input("Package hold bottles: "))
    print("We need", find_number_of_packages(n, k), "packages")
