def count_of_cabins(a, b):
    """
     There is a Ferris wheel with an even number of cabins in the amusement park.
     When cabin №A is at the bottom, cabin №B is at the top (A < B, A and B have the same parity)
       Data: number of cabins - A, B
       Task: find the count of cabins on the Ferris wheel
    """
    if a > b:
        raise ValueError("A must be less than B")
    if not (a % 2 == 0 and b % 2 == 0) and not (a % 2 == 1 and b % 2 == 1):
        raise ValueError("A and B have the same parity")
    return 2 * b - 2 * a


if __name__ == "__main__":
    a = int(input("№A = "))
    b = int(input("№B = "))
    print(count_of_cabins(a, b), "cabins")
