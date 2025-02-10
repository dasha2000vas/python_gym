from random import randint


def sequence_with_three_numbers_1() -> list[int]:
    """
    Writes sequence that contains three numbers 1.

    Returns:
        list[int]: Sequence with three numbers 1.
    """
    result = []
    count = 1
    while count <= 3:
        num = randint(1, 3)
        result.append(num)
        if num == 1:
            count += 1
    return result


if __name__ == "__main__":
    print(sequence_with_three_numbers_1())
