"""
Generates float number. Rounds
this number with round() function:
5, 3, 2, 1, 0 digits after dot.
"""

from random import uniform

if __name__ == "__main__":
    number = uniform(1, 10)
    print("number =", number)
    print(round(number, 5))
    print(round(number, 3))
    print(round(number, 2))
    print(round(number, 1))
    print(round(number))
