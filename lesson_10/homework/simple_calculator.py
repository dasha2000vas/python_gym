from random import randint, choice

OPERATIONS = "+-*/"


def simple_calculator(num1: int, num2: int, operation: str) -> int | float:
    """
    Calculates expression. Supports the
    following operations: +, -, *, /.

    Args:
        num1 (int): First number.
        num2 (int): Second number.
        operation (str): Operation.

    Returns:
        int|float:  Arithmetic expression result.
    """
    for num in (num1, num2):
        if not isinstance(num, int):
            raise ValueError("Numbers must be of type int")
    if not operation in OPERATIONS:
        raise ValueError("Operation must be one of: +, -, *, /")
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    return round(num1 / num2, 3)


if __name__ == '__main__':
    num1, num2 = randint(-100, 100), randint(-100, 100)
    operation = choice(OPERATIONS)
    print(f"{num1} {operation} {num2} = {simple_calculator(num1, num2, operation)}")
