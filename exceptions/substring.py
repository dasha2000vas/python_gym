from random import choice


def check_values(entered_string: str, substring: str) -> int:
    for value in (entered_string, substring):
        if not isinstance(value, str):
            raise ValueError("All args must be strings")


def check_if_substring_in_string(entered_string: str, substring: str) -> int|str:
    try:
        check_values(entered_string, substring)
        try:
            return entered_string.index(substring)
        except ValueError:
            raise ValueError(f"There's no substring '{substring}' in entered string")
    except Exception as exp:
        return exp.args[0]


if __name__ == '__main__':
    entered_string, substring = "A snake sneaks to seek a snack.", choice(["ca", "sn", "ak", "ch"])
    print(f"Entered string: {entered_string} \nSubstring: {substring}")
    result = check_if_substring_in_string(entered_string, substring)
    if isinstance(result, int):
        print(f"Index: {result}")
    else:
        print(result)
