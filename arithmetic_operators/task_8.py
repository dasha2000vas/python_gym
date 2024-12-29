def find_b_in_a(a, b):
    """
        Data: positive integers - a, b (a > b)
        Task: find how many segments b fit into segments a
              find the length of the remaining part
    """
    if a < b:
        raise ValueError("a must be greater than b")
    return a // b, a % b


if __name__ == "__main__":
    a = int(input("a = "))
    b = int(input("b = "))
    count, remain = find_b_in_a(a, b)
    print(count, "times b fit into a")
    print(remain, "- length of remaining part")
