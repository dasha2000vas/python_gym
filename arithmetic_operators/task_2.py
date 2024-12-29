from math import sqrt


def find_perimeter_and_square(x1, x2, x3, y1, y2, y3):
    """
        Data: coordinates of the three vertices of the triangle
              point1 - (x1, y1), point2 - (x2, y2), point3 - (x3, y3)
        Task: find the perimeter and square of the triangle
    """
    AB = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    AC = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    BC = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    perimeter = round(AB + AC + BC, 2)
    square = abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)) / 2
    return perimeter, square


if __name__ == "__main__":
    x1 = int(input("x1 = "))
    x2 = int(input("x2 = "))
    x3 = int(input("x3 = "))
    y1 = int(input("y1 = "))
    y2 = int(input("y2 = "))
    y3 = int(input("y3 = "))
    perimeter, square = find_perimeter_and_square(x1, x2, x3, y1, y2, y3)
    print("Perimeter=", perimeter)
    print("Square=", square)
