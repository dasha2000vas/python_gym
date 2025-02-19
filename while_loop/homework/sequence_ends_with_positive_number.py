from random import randint


def sequence_ends_with_positive_number() -> list[int]:
    """
    Generates sequence of numbers
    that ends with positive number.

    Returns:
       result (list[int]): Sequence of numbers.
    """
    result = []
    while (num := randint(-10, 10)) <= 0:
        result.append(num)
    else:
        result.append(num)
    return result


if __name__ == "__main__":
    print(sequence_ends_with_positive_number())
