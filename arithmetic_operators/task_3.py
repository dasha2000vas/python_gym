def move_leftmost_digit_to_right_end(number):
    """
        Data: а three-digit number
        Task: move the leftmost digit to the right end of the number
    """
    last_digit = number // 100
    return number % 100 * 10 + last_digit


if __name__ == "__main__":
    number = int(input("Number: "))
    print("Result: ", move_leftmost_digit_to_right_end(number))
