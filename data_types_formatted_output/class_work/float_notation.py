# Data: numbers in mathematical and exponential notation
# Task: write those numbers in another notation


if __name__ == "__main__":
    print("mathematical notation     exponential notation")
    print("----------------------------------------------")
    print("%21s %24s" %("308.14 * 10 ** -3", "3.0814e-1"))
    print("%21s %24s" %("11 * 10 ** 6", "1.1e+7"))
    print("%21s %24s" %("10.4 * 10 ** -5", "1.04e-4"))
    print("%21s %24s" %("256.2585", "2.562585e+2"))
    print("%21s %24s" %("0.0008009", "8.009e-4"))
    print()
    print("exponential notation          decimal fraction")
    print("----------------------------------------------")
    print("%20s %25s" %("2.44e+4", "24400.0"))
    print("%20s %25s" %("-1.7e-3", "-0.0017"))
    print("%20s %25s" %("3.12e-4", "0.000312"))
    print("%20s %25s" %("-1.99e3", "-1990.0"))
    print("%20s %25s" %("4.8e-1", "0.48"))
