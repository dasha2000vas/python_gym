from random import randint


def find_b_in_a(a: int, b: int) -> tuple[int, int]:
    """
        Data: positive integers - a, b (a > b)
        Task: find how many segments b fit into segments a
              find the length of the remaining part
    """
    return a // b, a % b


if __name__ == "__main__":
    a, b = randint(51, 100), randint(1, 50)
    print("a =", a, "\nb =", b)
    count, remain = find_b_in_a(a, b)
    print(count, "times b fit into a")
    print(remain, "- length of remaining part")
