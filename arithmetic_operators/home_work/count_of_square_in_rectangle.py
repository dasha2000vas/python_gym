from random import randint


def find_count_of_squares_in_rectangle(a: int, b: int, c: int) -> tuple[int, int]:
    """
    Calculates the count of squares in a rectangle, the area of the remaining part
    and returns the result.

    Args:
        a (int): The side of the rectangle.
        b (int): Other side of the rectangle.
        c (int): The side of the square.

    Returns:
        tuple[int, int]: The resulting numbers.
    """
    count = (a // c) * (b // c)
    return count, a * b - c * c * count


if __name__ == '__main__':
    a, b, c = randint(11, 20), randint(21, 30), randint(1, 10)
    print("a =", a, "\nb =", b, "\nc =", c)
    count, remain = find_count_of_squares_in_rectangle(a, b, c)
    print(count, "times")
    print(remain, "- area of the remaining part")
