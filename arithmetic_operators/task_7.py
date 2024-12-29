def find_count_of_square_in_rectangle(a, b, c):
    """
        Data: rectangle with sides - a, b
              square with side - c
        Task: find the number of squares that can fit in the rectangle
              find the area of the remaining part
    """
    count = (a // c) * (b // c)
    return count, a * b - c * c * count


if __name__ == '__main__':
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    count, remain = find_count_of_square_in_rectangle(a, b, c)
    print(count, "squares")
    print(remain, "- area of the remaining part")
