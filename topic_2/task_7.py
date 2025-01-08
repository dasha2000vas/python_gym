# Data: real numbers - A, B, C, D, F, G
# Task: apply the following functions to these numbers - int, round, trunc, ceil, floor
#       output the answer in the form of a table
#       column names are functions, rows are entered numbers

from math import ceil, floor, trunc

if __name__ == "__main__":
    A, B, C, D, F, G = 5.49, 4.49, 5.51, 4.51, -4.4, -5.5
    print("         int     round    trunc    ceil     floor")
    print("%.2f %6d %8d %8d %8d %8d" %(A, int(A), round(A), trunc(A), ceil(A), floor(A)))
    print("%.2f %6d %8d %8d %8d %8d" %(B, int(B), round(B), trunc(B), ceil(B), floor(B)))
    print("%.2f %6d %8d %8d %8d %8d" %(C, int(C), round(C), trunc(C), ceil(C), floor(C)))
    print("%.2f %6d %8d %8d %8d %8d" %(D, int(D), round(D), trunc(D), ceil(D), floor(D)))
    print("%.1f %6d %8d %8d %8d %8d" %(F, int(F), round(F), trunc(F), ceil(F), floor(F)))
    print("%.1f %6d %8d %8d %8d %8d" %(G, int(G), round(G), trunc(G), ceil(G), floor(G)))
