"""
Applies following functions to numbers (a, b, c, d, f, g) -
int, round, trunc, ceil, floor. Outputs answer in form of  table.
Column names are functions, rows are entered numbers.
"""

from math import ceil, floor, trunc

if __name__ == "__main__":
    a, b, c, d, f, g = 5.49, 4.49, 5.51, 4.51, -4.4, -5.5
    print("         int     round    trunc    ceil     floor")
    print("%.2f %6d %8d %8d %8d %8d" %(a, int(a), round(a), trunc(a), ceil(a), floor(a)))
    print("%.2f %6d %8d %8d %8d %8d" %(b, int(b), round(b), trunc(b), ceil(b), floor(b)))
    print("%.2f %6d %8d %8d %8d %8d" %(c, int(c), round(c), trunc(c), ceil(c), floor(c)))
    print("%.2f %6d %8d %8d %8d %8d" %(d, int(d), round(d), trunc(d), ceil(d), floor(d)))
    print("%.1f %6d %8d %8d %8d %8d" %(f, int(f), round(f), trunc(f), ceil(f), floor(f)))
    print("%.1f %6d %8d %8d %8d %8d" %(g, int(g), round(g), trunc(g), ceil(g), floor(g)))
