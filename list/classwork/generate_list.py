from random import randint


def check_values(number: int, times: int) -> None:
    for value in (number, times):
        if not isinstance(value, int):
            raise ValueError("Args 'number' and 'times' must be of type int")
        if value <= 0:
            raise ValueError("Number and times must be positive")


def generate_list_using_append(number: int, times: int, empty_list: list) -> list[int]:
    check_values(number, times)
    for _ in range(times):
        empty_list.append(randint(-number, number))
    return empty_list


def generate_list_using_list_comprehension(number: int, times: int) -> list[int]:
    check_values(number, times)
    return [randint(-number, number) for _ in range(times)]


if __name__ == "__main__":
    number, times = randint(1, 100), randint(1, 10)
    print(f"Number: {number}, times: {times}")
    empty_list = []
    list1 = generate_list_using_append(number, times, empty_list)
    list2 = generate_list_using_list_comprehension(number, times)
    print(*list1)
    print(*list2)
