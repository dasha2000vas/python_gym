from random import randint
from time import perf_counter


def get_factorial_iteratively(number: int) -> int:
    """
    Calculates factorial of number iteratively.

    Args:
        number (int): Entered number.

    Returns:
        factorial (int): Factorial of n.
    """
    if not isinstance(number, int):
        raise ValueError('Number must be integer')
    if number < 0:
        raise ValueError('Number cannot be negative')
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    return factorial


def get_factorial_recursively(number: int) -> int:
    """
    Calculates factorial of number using recursion.

    Args:
        number (int): Entered number.

    Returns:
        int: Factorial of n.
    """
    if not isinstance(number, int):
        raise ValueError('Number must be integer')
    if number < 0:
        raise ValueError('Number cannot be negative')
    if number > 996:
        raise ValueError("Recursion limit exceeded")
    if number == 0: return 1
    return number * get_factorial_recursively(number - 1)


if __name__ == '__main__':
    number = randint(1, 100)
    print(f"Number: {number}")
    time0 = perf_counter()
    result1 = get_factorial_iteratively(number)
    time_iteratively = perf_counter() - time0
    print(f"Get factorial iteratively: {result1}. Time: {time_iteratively:.10f}")
    time0 = perf_counter()
    result2 = get_factorial_recursively(number)
    time_recursively = perf_counter() - time0
    print(f"Get factorial recursively: {result2}. Time: {time_recursively:.10f}")
