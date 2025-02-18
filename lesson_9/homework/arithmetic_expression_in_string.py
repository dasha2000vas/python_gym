from random import randint, choice
from string import digits

SIGNS = "+-"


def arithmetic_expression_in_string(expression: str) -> int:
    """
    Calculates result of arithmetic
    expression obtained from string.
    Note: expression have view like this:
    <digit> +- <digit> +- ... +- <digit>.

    Args:
        expression (str): Expression to calculate.

    Returns:
        result (int): Resulting number.
    """
    if not isinstance(expression, str):
        raise ValueError("Expression must be of type str")
    for char in expression:
        if char not in SIGNS + digits:
            raise ValueError(
                "Expression must contain only digits and signs of subtraction and addition"
            )
    for i in range(0, len(expression) + 1, 2):
        if i != 0 and expression[i - 1] not in SIGNS or not expression[i].isdigit():
            raise ValueError(
                "Expression must have following format: <digit> +- <digit> +- ... +- <digit>"
            )
    result = 0
    for i in range(0, len(expression) + 1, 2):
        if i != 0 and expression[i - 1] == "-":
            result -= int(expression[i])
        else:
            result += int(expression[i])
    return result


if __name__ == '__main__':
    expression = str(randint(1, 9))
    for _ in range(randint(1, 9)):
        expression += choice(SIGNS) + str(randint(1, 9))
    print(f"Arithmetic expression: {expression}")
    print(f"Result: {arithmetic_expression_in_string(expression)}")
