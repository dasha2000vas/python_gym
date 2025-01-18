from tools import random_numbers_of_same_parity


def count_of_cabins(a: int, b: int) -> int:
    """
    Calculates count of cabins on the Ferris
    wheel if the number of cabins is even.
    Note: a < b, a and b have the same parity.

    Args:
        a (int): The bottom cabin.
        b (int): The top cabin.

    Returns:
        int: The count of cabins on the Ferris wheel.
    """
    return 2 * b - 2 * a


if __name__ == "__main__":
    a, b = random_numbers_of_same_parity()
    print("№A =", a, "\n№B =", b)
    print(count_of_cabins(a, b), "cabins")
