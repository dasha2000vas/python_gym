def glue_numbers(a, b):
    """
        Data: two three-digit numbers (a, b)
        Task: glue those numbers
    """
    if len(str(a)) != 3 or len(str(b)) != 3:
        raise ValueError("Числа a и b должны быть трёхзначными!")
    return a * 1000 + b


if __name__ == '__main__':
    print("Введите два трёхзначных числа")
    a = int(input("a = "))
    b = int(input("b = "))
    print("Ответ:", glue_numbers(a, b))
