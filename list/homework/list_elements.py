from tools import (
    generate_list_of_random_numbers,
    print_list,
    check_values_list_of_int
)


def get_sum_of_positive_numbers(entered_list: list[int]) -> int:
    check_values_list_of_int(entered_list)
    sum_of_positive = 0
    for number in entered_list:
        if number > 0:
            sum_of_positive += number
    return sum_of_positive


def get_count_of_negative_numbers(entered_list: list[int]) -> int:
    check_values_list_of_int(entered_list)
    count_of_negative = 0
    for number in entered_list:
        if number < 0:
            count_of_negative += 1
    return count_of_negative


if __name__ == '__main__':
    list_of_numbers = generate_list_of_random_numbers()
    print_list(list_of_numbers)
    sum_of_positive = get_sum_of_positive_numbers(list_of_numbers)
    count_of_negative = get_count_of_negative_numbers(list_of_numbers)
    print(f"Sum of positive numbers: {sum_of_positive}")
    print(f"Count of negative numbers: {count_of_negative}")
