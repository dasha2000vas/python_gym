from random import randint


def find_greatest_number() -> tuple[int, int]:
    """
    Finds greatest number in random
    sequence that ends with zero.

    Returns:
         greatest_num (int): Greatest number.
         index_of_greatest_num (int): Index of greatest number.
    """
    index = 1
    greatest_num = num = randint(-10, 10)
    index_of_greatest_num = 1
    while True:
        print(f"{num}[{index}]", end=" ")
        if num > greatest_num:
            greatest_num = num
            index_of_greatest_num = index
        if num == 0:
            break
        num = randint(-10, 10)
        index += 1
    return greatest_num, index_of_greatest_num


if __name__ == "__main__":
    result = find_greatest_number()
    print(f"\nGreatest number in sequence: {result[0]}[{result[1]}]")
