from random import choice, randint
from string import ascii_letters

from tools import  random_string


def add_string_after_symbol(original_string: str, add_string: str, symbol: str ) -> str:
    """
    Adds add_string after every entry of symbol in string.

    Args:
        original_string (str): Original string.
        add_string (str): String to add.
        symbol (str): Symbol to find.

    Returns:
        updated_string (str): Modified string.
    """
    for string in (original_string, add_string, symbol):
        if not isinstance(string, str):
            raise ValueError('All args must be strings')
    if original_string.find(symbol) != -1:
        updated_string = original_string.replace(symbol, symbol + add_string)
        return updated_string
    return f"There are no entries of {symbol} in string"


if __name__ == '__main__':
    original_string = random_string(words=4, letters=ascii_letters)
    add_string = random_string(words=1, letters=ascii_letters)
    symbol = choice(ascii_letters)
    print(f"Original string: {original_string}")
    print(f"Add string: {add_string}")
    print(f"Symbol: {symbol}")
    result = add_string_after_symbol(original_string, add_string, symbol)
    if "There are no entries of" in result:
        print(result)
    else:
        print(f"Modified string: {result}")
