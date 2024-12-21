from math import radians, e, sin, sqrt


def calculate_2(a, b, c, d, x, is_degrees):
    if is_degrees.lower() == "да":
        x = radians(x)
    return round(e ** a * sin(x) ** 2 - sqrt(abs((c - b ** 2) / a)) + d, 3)


if __name__ == "__main__":
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    d = int(input("d = "))
    x = int(input("x = "))
    is_degrees = input("x в градусах(да/нет): ")
    print("Ответ: ", calculate_2(a, b, c, d, x, is_degrees))
