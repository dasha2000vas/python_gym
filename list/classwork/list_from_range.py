from random import randint, choice


def check_values(start: int, stop: int, step: int) -> None:
    for value in (start, stop, step):
        if not isinstance(value, int):
            raise ValueError("All args must be of type int")
    if start < 0 or stop < 0:
        raise ValueError("Start and stop must be non-negative")
    if step == 0:
        raise ValueError("Step cannot be zero")


def get_list_of_even_numbers_from_range(start: int, stop: int, step: int = 1) -> list:
    check_values(start, stop, step)
    if step < 0:
        start, stop = max(start, stop), min(start, stop) - 1
    else:
        start, stop = min(start, stop), max(start, stop) + 1
    return [i for i in range(start, stop, step) if i % 2 == 0]


if __name__ == "__main__":
    start, stop, step = randint(0, 100), randint(0, 100), choice([i for i in range(-10, 11) if i != 0])
    print(f"start: {start}, stop: {stop}, step: {step}")
    print(f"Result: {get_list_of_even_numbers_from_range(start, stop, step)}")
