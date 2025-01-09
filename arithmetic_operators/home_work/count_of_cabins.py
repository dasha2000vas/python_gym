from tools import random_numbers_of_same_parity


def count_of_cabins(a: int, b: int) -> int:
    """
     There is a Ferris wheel with an even number of cabins in the amusement park.
     When cabin №A is at the bottom, cabin №B is at the top (A < B, A and B have the same parity)
        Data: number of cabins - A, B
        Task: find the count of cabins on the Ferris wheel
    """
    return 2 * b - 2 * a


if __name__ == "__main__":
    a, b = random_numbers_of_same_parity()
    print("№A =", a, "\n№B =", b)
    print(count_of_cabins(a, b), "cabins")
