from math import radians, e, sin, sqrt


def calculate_2(a, b, c, d, x, in_degrees):
    """
        Data: numbers - a, b, c, d, x
        Task: calculate the value of the expression y = e ** a * (sin x) ** 2 - sqrt(|(c - b ** 2) / a|) + d
              two ways: first - x in radians, second - x in degrees
    """
    if in_degrees.lower() == "y":
        x = radians(x)
    return round(e ** a * sin(x) ** 2 - sqrt(abs((c - b ** 2) / a)) + d, 3)


if __name__ == "__main__":
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    d = int(input("d = "))
    x = int(input("x = "))
    in_degrees = input("x in degrees(y/n): ")
    print("Result:", calculate_2(a, b, c, d, x, in_degrees))
