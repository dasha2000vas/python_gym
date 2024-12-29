def  define_third_digit_from_end(number):
    """
        Data: integer
        Task: define third digit from end
    """
    return number // 100 % 10


if __name__ == "__main__":
    number = int(input("Число: "))
    print(f"Третья цифра с конца:", define_third_digit_from_end(number))
