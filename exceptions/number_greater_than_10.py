from random import randint


def check_value(number: int) -> None:
    if not isinstance(number, int):
        raise ValueError("Object number must be integer")


def check_if_number_is_greater_than_ten(number: int) -> str:
    check_value(number)
    try:
        if number <= 10:
            raise ValueError("Number must be greater than 10")
    except ValueError as error:
        return error.args[0]
    else:
        return "Number is greater than 10"


if __name__ == '__main__':
    number = randint(1, 20)
    print(f"Number: {number}")
    print(check_if_number_is_greater_than_ten(number))
