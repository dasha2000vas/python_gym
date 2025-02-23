from random import randint, random
from time import perf_counter


def find_members_of_sequence_iteratively(number: float, n: int) -> list[int|float]:
    """
    Finds all members of sequence
    up to n-th member iteratively.

    Args:
        number (float): Starting number (between 1 and 0).
        n (int): Number of members (>0).

    Returns:
        list[int|float]: List of members.
    """
    if not isinstance(number, float):
        raise ValueError('Starting number must be of type float')
    if number > 1 or number < 0:
        raise ValueError('Starting number must be between 1 and 0')
    if not isinstance(n, int):
        raise ValueError('N must be of type int')
    if n <= 0:
        raise ValueError('N must be greater than 0')
    result = [number]
    for i in range(1, n + 1):
        number = round((number + 1) / i, 3)
        result.append(number)
    return result


def recursive_calculation(number: float, n: int, divider: int = 1) -> list[int|float]:
    """
    Finds all members of sequence
    up to n-th member using recursion.

    Args:
        number (float): Starting number.
        n (int): Number of members.
        divider (int, optional): Divider. Defaults to 1.

    Returns:
        list[int|float]: List of members.
    """
    result = [number]
    if n == 0: return result
    result.extend(
        recursive_calculation(
            round((number + 1) / divider, 3),
            n - 1,
            divider + 1,
        )
    )
    return result


def find_members_of_sequence_recursively(number: float, n: int) -> list[int|float]:
    """
    Finds all members of sequence up to
    n-th member using recursive function.

    Args:
        number (float): Starting number (between 1 and 0).
        n (int): Number of members (>0).

    Returns:
        list[int|float]: List of members.
    """
    if not isinstance(number, float):
        raise ValueError('Starting number must be of type float')
    if number > 1 or number < 0:
        raise ValueError('Starting number must be between 1 and 0')
    if not isinstance(n, int):
        raise ValueError('N must be of type int')
    if n <= 0:
        raise ValueError('N must be greater than 0')
    if n > 996:
        raise ValueError("Recursion limit exceeded")
    return recursive_calculation(number, n)


if __name__ == '__main__':
    number, n = round(random(), 3), randint(1, 10)
    print(f"Number: {number}, n: {n}")
    time0 = perf_counter()
    result1 = find_members_of_sequence_iteratively(number, n)
    time_iteratively = perf_counter() - time0
    print(f"Result iteratively: {result1}. Time: {time_iteratively:.10f}")
    time0 = perf_counter()
    result2 = find_members_of_sequence_recursively(number, n)
    time_recursively = perf_counter() - time0
    print(f"Result recursively: {result2}. Time: {time_iteratively:.10f}")
