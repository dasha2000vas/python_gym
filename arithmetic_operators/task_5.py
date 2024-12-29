def glue_numbers(a, b):
    """
        Data: two three-digit numbers - a, b
        Task: glue those numbers
    """
    if len(str(a)) != 3 or len(str(b)) != 3:
        raise ValueError("a and b must be 3 digits long!")
    return a * 1000 + b


if __name__ == '__main__':
    a = int(input("a = "))
    b = int(input("b = "))
    print("Result:", glue_numbers(a, b))
