from string import digits

from tools import random_string


def from_str_to_number(entered_str: str) -> float | int | str:
    """
    Converts string to integer or float.

    Args:
        entered_str (str): Entered string.

    Returns:
        int|float|str: Number or message that string
                       cannot be converted to number.
    """
    if not isinstance(entered_str, str):
        raise ValueError('Entered string must be of type str')
    entered_str = entered_str.replace(',', '.')
    if entered_str.isdigit():
        return int(entered_str)
    elif (
        "." in entered_str and
        entered_str.count('.') == 1 and
        entered_str.replace('.', '').isdigit()
    ):
        return float(entered_str)
    else:
        return "Cannot convert to number"


if __name__ == '__main__':
    entered_str = random_string(words=1, letters=digits + ".," + "abc")
    print(f"Entered string: {entered_str}")
    result = from_str_to_number(entered_str)
    if isinstance(result, str):
        print(result)
    else:
        print(f"Number: {result}")
