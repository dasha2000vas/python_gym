from random import randint


def is_number_equal_to_its_sum_of_cubes_of_digits(num: int) -> bool:
    """
    Defines if number is equal to
    its sum of cubes of its digits.

    Args:
        num (int): Entered number.

    Returns:
        bool: True if equal, else False.
    """
    if not isinstance(num, int):
        raise ValueError('Number must be of type int')
    if num <= 0:
        raise ValueError('Number must be positive')
    a = [int(i) ** 2 for i in str(num)]
    return num == sum([int(i) ** 3 for i in str(num)])


if __name__ == '__main__':
    num = randint(1, 1000)
    print(f"Number: {num}")
    result = is_number_equal_to_its_sum_of_cubes_of_digits(num)
    print(f"Is number equal to its sum of cubes of digits: {result}")
