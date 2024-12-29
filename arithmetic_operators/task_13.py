from math import radians, e, sin


def calculate_1(a, x, in_degrees):
    """
        Data: numbers - a, x
        Task: calculate the value of the expression y = e ** a * (sin x) ** 2 - (|x - a|) / 7
              two ways: first - x in radians, second - x in degrees
    """
    if in_degrees.lower() == "y":
        x = radians(x)
    return round(e ** a * sin(x) ** 2 - abs(x - a) / 7, 3)


if __name__ == "__main__":
    a = int(input("a = "))
    x = int(input("x = "))
    is_degrees = input("x in degrees(y/n): ")
    print("Result:", calculate_1(a, x, is_degrees))
