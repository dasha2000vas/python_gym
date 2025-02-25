"""
Prints value of number in binary,
decimal, octal, and hexadecimal.
"""

from random import randint

if __name__ == "__main__":
    number = randint(-100, 100)
    print(number, "in the binary system", bin(number))
    print(number, "in the decimal system", number)
    print(number, "in the octal system", oct(number))
    print(number, "in the hexadecimal system", hex(number))
