from tools import (
    generate_list_of_random_numbers,
    print_list,
    check_values_list_of_int,
)


def is_list_non_decreasing_sequence(entered_list: list[int]) -> bool:
    check_values_list_of_int(entered_list)
    if len(entered_list) < 2: return True
    return entered_list != sorted(entered_list, reverse=True)


if __name__ == '__main__':
    entered_list = generate_list_of_random_numbers()
    print_list(entered_list)
    print(f"List is non-decreasing sequence: {is_list_non_decreasing_sequence(entered_list)}")
