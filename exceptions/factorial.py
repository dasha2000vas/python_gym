from random import randint


def check_values_iteratively(number: int) -> None:
    if not isinstance(number, int):
        raise ValueError('Number must be integer')
    if number < 0:
        raise ValueError('Number cannot be negative')


def get_factorial_iteratively(number: int) -> int|str:
    try:
        check_values_iteratively(number)
    except ValueError as error:
        return error.args[0]
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    return factorial


def check_values_recursively(number: int) -> None:
    if not isinstance(number, int):
        raise ValueError('Number must be integer')
    if number < 0:
        raise ValueError('Number cannot be negative')
    if number > 996:
        raise ValueError("Recursion limit exceeded")


def get_factorial_recursively(number: int) -> int|str:
    try:
        check_values_recursively(number)
    except ValueError as error:
        return error.args[0]
    if number == 0: return 1
    return number * get_factorial_recursively(number - 1)


if __name__ == '__main__':
    number = randint(-100, 100)
    print(f"Number: {number}")
    result1 = get_factorial_iteratively(number)
    print(f"Get factorial iteratively: {result1}")
    result2 = get_factorial_recursively(number)
    print(f"Get factorial recursively: {result2}")
