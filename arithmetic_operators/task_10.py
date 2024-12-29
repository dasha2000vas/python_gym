def count_value(a, b, c, d):
    """
       Data: integers not equal to zero - A, B, C, D
       Task: calculate the value of the expression y = 3ab - 4 / (cd)
    """
    if a == 0 or b == 0 or c == 0 or d == 0:
        raise ValueError("Числа a, b, c, d не должны быть равны нулю")
    return round(3 * a * b - 4 / (c * d), 3)


if __name__ == "__main__":
    print("Введите четыре целых числа, не равных нулю")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    d = int(input("d = "))
    print("Ответ:", count_value(a, b, c, d))
