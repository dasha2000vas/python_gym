from re import sub


def check_value(entered_string: str) -> None:
    if not isinstance(entered_string, str):
        raise ValueError("Object entered_string must be of type str")


def replace_substrings(entered_string: str) -> str:
    """
    Replaces all substrings of form XX:XX:
    1. if it's time -> XX:XX
    2. if it isn't time -> 00000.

    Args:
        entered_string (str)

    Returns:
        str: Resulting string.
    """
    check_value(entered_string)
    entered_string = sub(r"(2[0-3]|[0-1]\d):[0-5]\d", "XX:XX", entered_string)
    return sub(r"\d\d:\d\d", "00000", entered_string)


if __name__ == '__main__':
    entered_string = ("Valid time: 11:11, 22:22, 00:00. "
                      "Invalid time: 33:33, 44:44, 55:55.")
    print(entered_string)
    print(replace_substrings(entered_string))
