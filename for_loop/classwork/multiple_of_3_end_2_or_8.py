from random import randint


def multiple_of_3_end_2_or_8(a: int, b: int) -> tuple[list[int], int]:
    """
    Calculates summ of multiple of 3 end with 2 or 8
    numbers that belong to range (a, b)

    Args:
        a (int): Start positive number.
        b (int): End positive number.

    Returns:
        target_numbers (list[int]): List of target numbers.
        sum_of_target_numbers (int): Sum of target numbers.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("a and b must be integers")
    if a <= 0 or b <= 0:
        raise ValueError("a and b must be positive")
    if b <= a:
        raise ValueError("b must be greater than a")
    target_numbers = []
    sum_of_target_numbers = 0
    for i in range(a, b):
        if i % 3 == 0 and (i % 10 == 2 or i % 10 == 8):
            target_numbers.append(i)
            sum_of_target_numbers += i
    return target_numbers, sum_of_target_numbers


if __name__ == "__main__":
    a, b = randint(1, 50), randint(51, 100)
    print(f"a = {a}, b = {b}")
    target_numbers, sum_of_target_numbers = multiple_of_3_end_2_or_8(a, b)
    print(f"Target numbers = {target_numbers}")
    print(f"Sum of target numbers = {sum_of_target_numbers}")
