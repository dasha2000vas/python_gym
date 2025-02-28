from random import randint


def get_nth_fibonacci_number(number, first: int = 1, second: int = 1) -> str | int:
    try:
        for value in (number, first, second):
            if not isinstance(value, int):
                raise ValueError("All args must be integers")
        if first < 1 or second < 1:
            raise ValueError("Numbers first and second must be greater or equal to one")
        if number < 0:
            raise ValueError("Number cannot be negative")
        elif number == 0:
            return 0
        elif number == 2 or number == 1:
            return second
        return get_nth_fibonacci_number(number - 1, second, second + first)
    except ValueError as error:
        return error.args[0]


if __name__ == '__main__':
    number = randint(-10, 20)
    print(f"Number: {number}")
    result = get_nth_fibonacci_number(number)
    if isinstance(result, str):
        print(result)
    else:
        print(f"Fibonacci number: {get_nth_fibonacci_number(number)}")
