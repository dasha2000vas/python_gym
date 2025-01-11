from random import randint


def find_b_in_a(a: int, b: int) -> tuple[int, int]:
    """
    Calculates how many segments b fit into segments a,
    finds the length of the remaining part and returns the result.
    Note: a must be greater than b.

    Args:
        a (int): The first positive number.
        b (int): The second positive number.

    Returns:
        tuple[int, int]: The resulting numbers.
    """
    return a // b, a % b


if __name__ == "__main__":
    a, b = randint(51, 100), randint(1, 50)
    print("a =", a, "\nb =", b)
    count, remain = find_b_in_a(a, b)
    print(count, "times b fit into a")
    print(remain, "- length of remaining part")
