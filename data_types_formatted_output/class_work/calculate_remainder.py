from random import randint

def calculate_remainder(n: int, k: int) -> int :
    """
        Data: integers - n, k
        Task: write down the number n a thousand times
              find the remainder of the division by k
    """
    return int(str(n) * 1000) % k


if __name__ == '__main__':
    n, k = randint(1, 999), randint(2, 50)
    print("n =", n, "\nk =", k)
    print("Remainder:", calculate_remainder(n, k))
