from random import randint


def count_of_local_max() -> tuple[int,int]:
    """
    Generates sequence of numbers between
    -10 and 10 that ends with zero. Defines
    count of local maximums.

    Returns:
       max_num (int): Local maximum.
       count (int): Count of local maximums.
    """
    sequence = []
    num = randint(-10, 10)
    while True:
        print(num, end = " ")
        sequence.append(num)
        if num == 0:
            break
        num = randint(-10, 10)
    return max(sequence), sequence.count(max(sequence))


if __name__ == '__main__':
    result = count_of_local_max()
    print(f"\nCount of local maximum {result[0]}: {result[1]}")
