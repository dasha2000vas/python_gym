from random import randint


def generating_series() -> list[int]:
    """
    Generates a series of random numbers (0, 1, 2)
    with one number of twos and zeros.

    Returns:
        result (list[int]): List of numbers.
    """
    twos = 0
    zeros = 0
    result = []
    while twos != zeros or not twos or not zeros:
        number = randint(0, 2)
        result.append(number)
        if number == 0:
            zeros += 1
        elif number == 2:
            twos += 1
    return result


if __name__ == "__main__":
    print(generating_series())
