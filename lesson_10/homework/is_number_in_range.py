from random import randint


def is_number_in_range(num: int, start: int, end: int) -> bool:
    """
    Defines if number is in range.

    Args:
        num (int): Entered number.
        start (int): Start of range.
        end (int): End of range.

    Returns:
        bool: True if number is in range, else False.
    """
    for arg in (num, start, end):
        if not isinstance(arg, int):
            raise ValueError("All args must be integers")
    return start <= num <= end


if __name__ == '__main__':
    num, start, end = randint(-100, 100), randint(-100, 100), randint(-100, 100)
    if start > end:
        start, end = end, start
    print(f"{num} in ({start}, {end}) - {is_number_in_range(num, start, end)}")
