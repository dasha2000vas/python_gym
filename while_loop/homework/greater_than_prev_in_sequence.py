from random import randint


def greater_than_prev_in_sequence() -> int:
    """
    Generates sequence of numbers between
    -10 and 10 that ends with zero. Defines
    count of elements that are greater than
    previous.

    Returns:
       count (int): Count of elements.
    """
    sequence = []
    count = 0
    num2 = num1 = randint(-10, 10)
    while True:
        print(num2, end = " ")
        sequence.append(num2)
        if num2 == 0:
            break
        if num2 > num1:
            count += 1
        num1 = num2
        num2 = randint(-10, 10)
    return count


if __name__ == "__main__":
    print(f"\nCount of elements that are greater than previous: {greater_than_prev_in_sequence()}")
