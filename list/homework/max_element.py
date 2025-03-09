from tools import (
    generate_list_of_random_numbers,
    print_list,
    check_values_list_of_int,
)


def get_max_element_and_its_count(entered_list: list[int]) -> tuple[int, int]:
    check_values_list_of_int(entered_list)
    count = 1
    max_element = entered_list[0]
    for i in range(1, len(entered_list)):
        if entered_list[i] > max_element:
            max_element = entered_list[i]
            count = 1
        elif entered_list[i] == max_element:
            count += 1
    return max_element, count


if __name__ == '__main__':
    entered_list = generate_list_of_random_numbers()
    print_list(entered_list)
    max_element, count = get_max_element_and_its_count(entered_list)
    print(f"Max element: {max_element}, count: {count}")
