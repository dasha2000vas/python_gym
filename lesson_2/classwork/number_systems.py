"""
Prints value of number (a) in binary,
decimal, octal, and hexadecimal.
"""

from random import randint

if __name__ == "__main__":
    a = randint(-100, 100)
    print(a, "in the binary system", bin(a))
    print(a, "in the decimal system", a)
    print(a, "in the octal system", oct(a))
    print(a, "in the hexadecimal system", hex(a))
