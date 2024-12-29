def sum_of_digits(integer):
    """
       Data: а three-digit integer
       Task: find the sum of digits of the number using next operations: %, //
    """
    if len(str(integer)) != 3:
        raise ValueError("Integer must be 3 digits long!")
    return integer // 100 + integer // 10 % 10 + integer % 10


if __name__ == "__main__":
    integer = int(input("Integer: "))
    print("Sum of digits:", sum_of_digits(integer))
