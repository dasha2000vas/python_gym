"""
Generates two integers (number1, number2) and
formats output with operator %.
"""

from random import randint

if __name__ == "__main__":
    number1, number2 = randint(-100, 100), randint(-100, 100)
    print("number1 =", number1, "\nnumber2 =", number2)
    quotient = number1 / number2

    print("%d / %d = %.1f" % (number1, number2, quotient))
    print("%d / %d = %.2f" % (number1, number2, quotient))
    print("%d / %d = %.3f" % (number1, number2, quotient))

    print("%d / %d = %10.1f" % (number1, number2, quotient))
    print("%d / %d = %10.2f" % (number1, number2, quotient))
    print("%d / %d = %10.3f" % (number1, number2, quotient))
