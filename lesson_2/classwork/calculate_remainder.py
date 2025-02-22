from random import randint

def calculate_remainder(n: int, k: int) -> int :
    """
    Writes number n thousand times, then
    finds remainder of division by k.

    Args:
        n (int): The first number.
        k (int): The divider.

    Returns:
        int: The resulting number.
    """
    for number in (n, k):
        if not isinstance(number, int):
            raise ValueError("All args must be integers")
        if number <= 0:
            raise ValueError("All numbers must be positive")
    return int(str(n) * 1000) % k


if __name__ == '__main__':
    n, k = randint(1, 999), randint(2, 50)
    print("n =", n, "\nk =", k)
    print("Remainder:", calculate_remainder(n, k))
