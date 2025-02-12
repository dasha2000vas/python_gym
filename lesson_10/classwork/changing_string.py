from string import ascii_letters

from tools import  random_string


def changing_string(original_string: str) -> str:
    """
    Modifies entered original string.
    Doubles symbols with even indexes,
    replaces symbols with odd indexes
    with their codes.

    Args:
        original_string (str): Original string.

    Returns:
        updated_string (str): Modified string.
    """
    updated_string = ""
    if not isinstance(original_string, str):
        raise ValueError('Original must be a string')
    for i in range(len(original_string)):
        if i % 2 == 0:
            updated_string += original_string[i] * 2
        else:
            updated_string += str(ord(original_string[i]))
    return updated_string


if __name__ == '__main__':
    # original_string = random_string(words=1, letters=ascii_letters)
    original_string = "bird"
    print(f"Original string: {original_string}")
    print(f"Modified string: {changing_string(original_string)}")
