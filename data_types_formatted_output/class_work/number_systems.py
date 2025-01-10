# Data: integer - a
# Task: print its value in binary, decimal, octal, and hexadecimal


if __name__ == "__main__":
    a = int(input("a = "))
    print(a, "in the binary system", bin(a))
    print(a, "in the decimal system", a)
    print(a, "in the octal system", oct(a))
    print(a, "in the hexadecimal system", hex(a))
