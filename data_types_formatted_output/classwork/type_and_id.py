"""
Data: variables - a, b, c, d, f
Task: print the type of each variable and its ID
"""

if __name__ == "__main__":
    a = 15
    b = "Hello"
    c = 14.58
    d = (14, 66, 376)
    f = [14, 66, 376]

    print("a - ", type(a), ", id - ", id(a), sep='')
    print("b - ", type(b), ", id - ", id(b), sep='')
    print("c - ", type(c), ", id - ", id(c), sep='')
    print("d - ", type(d), ", id - ", id(d), sep='')
    print("f - ", type(f), ", id - ", id(f), sep='')
