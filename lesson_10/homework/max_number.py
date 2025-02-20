from random import randint


def max_number_of_two(num1: int, num2: int) -> int:
    """
    Finds maximum number of two numbers.

    Args:
        num1 (int): First number.
        num2 (int): Second number.

    Returns:
        int: Maximum number of two numbers.
    """
    for num in (num1, num2):
        if not isinstance(num, int):
            raise ValueError("All args must be integers")
    if num1 >= num2:
        return num1
    return num2


def max_number_of_three(num1: int, num2: int, num3: int) -> int:
    """
    Finds maximum number of three numbers.

    Args:
        num1 (int): First number.
        num2 (int): Second number.
        num3 (int): Third number.

    Returns:
        int: Maximum number of three numbers.
    """
    for num in (num1, num2, num3):
        if not isinstance(num, int):
            raise ValueError("All args must be integers")
    max1 = max_number_of_two(num1, num2)
    max2 = max_number_of_two(num2, num3)
    if max1 >= max2:
        return max1
    return max2


def max_number_of_four(num1: int, num2: int, num3: int, num4: int) -> int:
    """
    Finds maximum number of four numbers.

    Args:
        num1 (int): First number.
        num2 (int): Second number.
        num3 (int): Third number.
        num4 (int): Fourth number.

    Returns:
        int: Maximum number of four numbers.
    """
    for num in (num1, num2, num3, num4):
        if not isinstance(num, int):
            raise ValueError("All args must be integers")
    max1 = max_number_of_two(num1, num2)
    max2 = max_number_of_two(num3, num4)
    if max1 >= max2:
        return max1
    return max2


if __name__ == '__main__':
    num1, num2 = randint(-100, 100), randint(-100, 100)
    num3, num4 = randint(-100, 100), randint(-100, 100)
    print(f"Numbers: {num1}, {num2}. Max = {max_number_of_two(num1, num2)}")
    print(f"Numbers: {num1}, {num2}, {num3}. Max = {max_number_of_three(num1, num2, num3)}")
    print(f"Numbers: {num1}, {num2}, {num3}, {num4}. Max = {max_number_of_four(num1, num2, num3, num4)}")
