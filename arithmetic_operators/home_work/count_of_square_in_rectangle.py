from random import randint


def find_count_of_square_in_rectangle(a: int, b: int, c: int) -> tuple[int, int]:
    """
        Data: rectangle with sides - a, b
              square with side - c
        Task: find the number of squares that can fit in the rectangle
              find the area of the remaining part
    """
    count = (a // c) * (b // c)
    return count, a * b - c * c * count


if __name__ == '__main__':
    a, b, c = randint(11, 20), randint(21, 30), randint(1, 10)
    print("a =", a, "\nb =", b, "\nc =", c)
    count, remain = find_count_of_square_in_rectangle(a, b, c)
    print(count, "times")
    print(remain, "- area of the remaining part")
