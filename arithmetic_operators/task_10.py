def count_value(a, b, c, d):
    """
       Data: integers not equal to zero - a, b, c, d
       Task: calculate the value of the expression y = 3ab - 4 / (cd)
    """
    if a == 0 or b == 0 or c == 0 or d == 0:
        raise ValueError("a, b, c, and d cannot be zero")
    return round(3 * a * b - 4 / (c * d), 3)


if __name__ == "__main__":
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    d = int(input("d = "))
    print("Result:", count_value(a, b, c, d))
