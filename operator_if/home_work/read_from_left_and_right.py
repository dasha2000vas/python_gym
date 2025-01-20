def read_same_from_left_and_right(number: int) -> str:
    """
    Defines if number reads the same
    if you start from left or right end.

    Args:
        number (int): Four-digit number.

    Returns:
        str: Yes or No.
    """
    return (
        "Yes" if number // 1000 == number % 10 and
        number // 100 % 10 == number // 10 % 10 else "No"
    )


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(f"Is number read the same if you start from left or right end?")
    print(read_same_from_left_and_right(number))
