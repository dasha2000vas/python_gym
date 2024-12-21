from math import radians, e, sin


def calculate_1(a, x, is_degrees):
    if is_degrees.lower() == "да":
        x = radians(x)
    return round(e ** a * sin(x) ** 2 - abs(x - a) / 7, 3)


if __name__ == "__main__":
    a = int(input("a = "))
    x = int(input("x = "))
    is_degrees = input("x в градусах(да/нет): ")
    print("Ответ: ", calculate_1(a, x, is_degrees))
