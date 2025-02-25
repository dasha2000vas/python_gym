"""
Applies following functions to numbers (1-6) -
int, round, trunc, ceil, floor. Outputs answer in form of table.
Column names are functions, rows are entered numbers.
"""

from math import ceil, floor, trunc

if __name__ == "__main__":
    number1, number2, number3, number4, number5, number6 = (
        5.49, 4.49, 5.51, 4.51, -4.4, -5.5
    )
    print("         int     round    trunc    ceil     floor")
    print("%.2f %6d %8d %8d %8d %8d" %(
        number1, int(number1), round(number1),
        trunc(number1), ceil(number1), floor(number1)
    ))
    print("%.2f %6d %8d %8d %8d %8d" %(
        number2, int(number2), round(number2),
        trunc(number2), ceil(number2), floor(number2)
    ))
    print("%.2f %6d %8d %8d %8d %8d" %(
        number3, int(number3), round(number3),
        trunc(number3), ceil(number3), floor(number3)
    ))
    print("%.2f %6d %8d %8d %8d %8d" %(
        number4, int(number4), round(number4),
        trunc(number4), ceil(number4), floor(number4)
    ))
    print("%.1f %6d %8d %8d %8d %8d" %(
        number5, int(number5), round(number5),
        trunc(number5), ceil(number5), floor(number5)
    ))
    print("%.1f %6d %8d %8d %8d %8d" %(
        number6, int(number6), round(number6),
        trunc(number6), ceil(number6), floor(number6)
    ))
