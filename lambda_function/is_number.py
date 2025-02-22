from random import choice

is_number = lambda x: x.strip("-").replace(".", "", 1).isdigit()


def is_string_number(entered_str: str) -> bool:
    """
    Defines if entered_str is number (integer
    or float) or not using lambda function.

    Args:
        entered_str (str): Entered string.

    Returns:
        bool: True if entered_str is number, else False.
    """
    if not isinstance(entered_str, str):
        raise ValueError("Object entered_str must be string")
    return is_number(entered_str)


if __name__ == '__main__':
    example_strings = ["-2", "2", "2.0", "-2.2", "2.0.1", "cat", "a1", "10+1"]
    entered_str = choice(example_strings)
    print(f"Entered string: {entered_str}")
    print(f"Is number: {is_number(entered_str)}")
