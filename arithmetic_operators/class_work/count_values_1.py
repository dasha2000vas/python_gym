# Data: two numbers - a, b
# Task: find the values of expressions - a + b + a / b,
#       2a - a / (3b), sqrt(3a) / (2b)
#       display values on the screen

from random import randint

if __name__ == "__main__":
    a, b = randint(0, 50), randint(0, 50)
    print("a =", a, "\nb =", b)

    print(a + b + a / b)
    print(2 * a - a / (3 * b))
    print((3 * a) ** 0.5 / (2 * b))
