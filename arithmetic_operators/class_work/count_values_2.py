# Data: two numbers - a, b
# Task: find the function values and display them on the screen,
#       round the result to two digits after the dot

from math import cos, sin
from random import randint

if __name__ == "__main__":
    a, b = randint(0, 50), randint(0, 50)
    print("a =", a, "\nb =", b)

    f = (a ** b) ** 0.5
    g = f - sin(a ** 3.5)
    s = g * f + cos(a - 2 * b) ** 2

    print(round(f, 2))
    print(round(g, 2))
    print(round(s, 2))
