"""
Data: float number
Task: round this number with round()
      5, 3, 2, 1, 0 digits after dot
"""

from random import uniform

if __name__ == "__main__":
    a = uniform(1, 10)
    print("a =", a)
    print(round(a, 5))
    print(round(a, 3))
    print(round(a, 2))
    print(round(a, 1))
    print(round(a))
