"""
Data: integers - a, b
Task: format output with operator %
"""

from random import randint

if __name__ == "__main__":
    a, b = randint(-100, 100), randint(-100, 100)
    print("a =", a, "\nb =", b)
    x = a / b

    print("%d / %d = %.1f" % (a, b, x))
    print("%d / %d = %.2f" % (a, b, x))
    print("%d / %d = %.3f" % (a, b, x))

    print("%d / %d = %10.1f" % (a, b, x))
    print("%d / %d = %10.2f" % (a, b, x))
    print("%d / %d = %10.3f" % (a, b, x))
