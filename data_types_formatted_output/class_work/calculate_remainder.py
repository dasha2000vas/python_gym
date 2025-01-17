from random import randint

def calculate_remainder(n: int, k: int) -> int :
    """
    Writes number n thousand times, then
    finds remainder of division by k.

    Args:
        n (int): The first number.
        k (int): The second number

    Returns:
        int: The resulting number.
    """
    return int(str(n) * 1000) % k


if __name__ == '__main__':
    n, k = randint(1, 999), randint(2, 50)
    print("n =", n, "\nk =", k)
    print("Remainder:", calculate_remainder(n, k))
