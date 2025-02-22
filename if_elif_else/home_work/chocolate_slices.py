from random import randint


def chocolate_slices(a: int, b: int, n: int) -> bool:
    """
    Defines if it is possible to break
    off n slices from chocolate bar (a, b).
    Note: it can be broken in straight line just once.

    Args:
        a (int): First side of chocolate bar.
        b (int): Second side of chocolate bar.
        n (int): Count of chocolate slices.

    Returns:
       bool: True if it is possible, else False.
    """
    for num in (a, b, n):
        if num <= 0:
            raise ValueError("A, b and n must be positive.")
        if not isinstance(num, int):
            raise ValueError("A, b and n must be integers.")
    if (not n % a or not n % b) and n < a * b:
        return True
    return False


if __name__ == "__main__":
    a, b, n = randint(1, 5), randint(5, 10), randint(1, 10)
    print(f"a = {a}, b = {b} \nn = {n}")
    print(f"It is possible to break off n slices from chocolate bar: {chocolate_slices(a, b, n)}")
