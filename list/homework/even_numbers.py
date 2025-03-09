from tools import (
    generate_list_of_random_numbers,
    print_list_of_integers,
    check_values_list_of_int,
)


def add_first_even_number_to_all_even_numbers(entered_list: list[int]) -> None:
    check_values_list_of_int(entered_list)
    first_even = None
    for i in range(len(entered_list)):
        if entered_list[i] % 2 == 0:
            if first_even is None:
                first_even = entered_list[i]
            entered_list[i] += first_even


if __name__ == '__main__':
    entered_list = generate_list_of_random_numbers()
    print_list_of_integers(entered_list)
    add_first_even_number_to_all_even_numbers(entered_list)
    print_list_of_integers(entered_list)
