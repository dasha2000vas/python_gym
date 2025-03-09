from tools import (
    generate_list_of_random_numbers,
    print_list_of_integers,
    check_values_list_of_int,
)


def add_first_odd_number_to_all_even_numbers(entered_list: list[int]) -> None:
    check_values_list_of_int(entered_list)
    first_odd = 0
    for number in entered_list:
        if first_odd == 0 and number % 2 == 1:
            first_odd = number
    for i in range(len(entered_list)):
        if entered_list[i] % 2 == 0:
            entered_list[i] += first_odd


if __name__ == '__main__':
    entered_list = generate_list_of_random_numbers()
    print_list_of_integers(entered_list)
    add_first_odd_number_to_all_even_numbers(entered_list)
    print_list_of_integers(entered_list)
