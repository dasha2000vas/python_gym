from tools import (
    generate_list_of_random_numbers,
    check_values_list_of_int,
    print_list_of_integers,
)


def replace_signs_of_numbers(entered_list: list[int]) -> list[int]:
    check_values_list_of_int(entered_list)
    return [-i for i in entered_list]


if __name__ == '__main__':
    entered_list = generate_list_of_random_numbers()
    print_list_of_integers(entered_list)
    modified_list = replace_signs_of_numbers(entered_list)
    print_list_of_integers(modified_list)
