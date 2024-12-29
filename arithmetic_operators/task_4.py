def  define_third_digit_from_end(integer):
    """
        Data: integer
        Task: define third digit from end
    """
    return integer // 100 % 10


if __name__ == "__main__":
    integer = int(input("Integer: "))
    print(f"Third digit from end:", define_third_digit_from_end(integer))
