def find_count_of_square_in_rectangle(a, b, c):
    count = (a // c) * (b // c)
    return count, a * b - c * c * count


if __name__ == '__main__':
    print("Введите числа a и b (стороны прямоугольника), с (сторона квадрата)")
    a = int(input("A = "))
    b = int(input("B = "))
    c = int(input("C = "))
    count, square = find_count_of_square_in_rectangle(a, b, c)
    print(count, "квадратиков")
    print(square, "- площадь оставшейся части")
