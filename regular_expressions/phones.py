from re import findall


def check_value(phones_string: str) -> None:
    if not isinstance(phones_string, str):
        raise ValueError("Object phones_string must be of type str")


def get_phones_from_string(phones_string: str) -> list[str]:
    check_value(phones_string)
    return findall(r"(?:\+7|8).\d\d\d.\d\d\d.\d\d.\d\d", phones_string)


if __name__ == '__main__':
    phones_string = ("Valid phone numbers: 8-999-999-99-99, +7-999-999-99-99, "
                     "8 888 888 88 88, +7 888 888 88 88. Invalid phone numbers: "
                     "+71111111111, 85555555555, 9-999-999-99-99")
    print(phones_string)
    print(f"Phones: {get_phones_from_string(phones_string)}")
