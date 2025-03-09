from pytest import mark, raises

from list import (
    get_list_of_even_numbers_from_range,
    get_square_roots,
    clone_list_using_cut,
    clone_list_using_list_comprehension,
    are_lists_identical,
    term_in_list,
    get_sum_of_positive_numbers,
    get_count_of_negative_numbers,
    replace_signs_of_numbers,
    get_max_element_and_its_count,
    add_first_even_number_to_all_even_numbers,
    add_first_odd_number_to_all_even_numbers,
    is_list_non_decreasing_sequence,
    get_longest_word_from_str,
    get_file_name_from_path_using_list,
    get_file_name_from_path_using_regex,
    get_last_folder_from_path_using_list,
    get_last_folder_from_path_using_regex,
)


@mark.parametrize(
    "start,stop,step,result",
    [
        (0, 0, 1, [0]),
        (0, 10, 1, [0, 2, 4, 6, 8, 10]),
        (63, 24, -3, [60, 54, 48, 42, 36, 30, 24]),
        (73, 30, 4, [30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70]),
    ]
)
def test_list_from_range(start, stop, step, result):
    assert get_list_of_even_numbers_from_range(start, stop, step) == result


@mark.parametrize(
    "start,stop,step,message",
    [
        ("a", 1, 1, "All args must be of type int"),
        (1, "a", 1, "All args must be of type int"),
        (1, 1, "a", "All args must be of type int"),
        (-1, 1, 1, "Start and stop must be non-negative"),
        (1, -1, 1, "Start and stop must be non-negative"),
        (1, 1, 0, "Step cannot be zero"),
    ]
)
def test_list_from_range_value_error(start, stop, step, message):
    with raises(ValueError, match=message):
        get_list_of_even_numbers_from_range(start, stop, step)


@mark.parametrize(
    "first,last,result",
    [
        (1, 10, [1.0, 1.414, 1.732, 2.0, 2.236, 2.449, 2.646, 2.828, 3.0, 3.162]),
        (20, 25, [4.472, 4.583, 4.69, 4.796, 4.899, 5.0]),
        (30, 40, [5.477, 5.568, 5.657, 5.745, 5.831, 5.916, 6.0, 6.083, 6.164, 6.245, 6.325]),
    ]
)
def test_square_root(first, last, result):
    assert get_square_roots(first, last) == result


@mark.parametrize(
    "first,last,message",
    [
        ("a", 1, "All args must be of type int"),
        (1, "a", "All args must be of type int"),
        (-1, 1, "Numbers cannot be negative"),
        (1, -1, "Numbers cannot be negative"),
    ]
)
def test_square_root_value_error(first, last, message):
    with raises(ValueError, match=message):
        get_square_roots(first, last)


@mark.parametrize(
    "entered_list",
    [
        ["cat", "dog", "snake", "mouse", "hamster"],
        [1, 2, 3, 4, 5],
        ["cat", 1, 1.111, ["dog"]],
    ]
)
def test_cloning_list(entered_list):
    clone1 = clone_list_using_list_comprehension(entered_list)
    clone2 = clone_list_using_cut(entered_list)
    assert are_lists_identical(entered_list, clone1) == [True, False]
    assert are_lists_identical(entered_list, clone2) == [True, False]


@mark.parametrize(
    "obj,result",
    [
        ( "cat" , "There is cat in entered list"),
        ("tiger", "There is no tiger in entered list"),
        (1, "There is no 1 in entered list"),
    ]
)
def test_clone_list(obj, result):
    assert term_in_list(["cat", "dog", "snake", "mouse", "hamster"], obj) == result


@mark.parametrize(
    "entered_list",
    [
        "cat",
        1,
        1.111,
    ]
)
def test_cloning_list_value_error(entered_list):
    with raises(ValueError, match="Value must be of type list"):
        clone_list_using_list_comprehension(entered_list)
        clone_list_using_cut(entered_list)
        are_lists_identical(entered_list, entered_list)
        term_in_list(entered_list, "cat")


@mark.parametrize(
    "entered_list,sum_of_positive,count_of_negative",
    [
        ([1, 2, 3, -1, -2, -3], 6, 3),
        ([4, 6, 5, 5, 10], 30, 0),
        ([-1, -2, -3, -4, -5], 0, 5),
    ]
)
def test_list_elements(entered_list, sum_of_positive, count_of_negative):
    assert get_sum_of_positive_numbers(entered_list) == sum_of_positive
    assert get_count_of_negative_numbers(entered_list) == count_of_negative


@mark.parametrize(
    "entered_list,message",
    [
        ((1, 2, 3), "Object 'entered_list' must be list"),
        ([1, 2, 3, "a"], "All elements in 'entered_list' must be integers"),
        ([1, 2, 3, 4.444], "All elements in 'entered_list' must be integers"),
    ]
)
def test_list_elements_value_error(entered_list, message):
    with raises(ValueError, match=message):
        get_sum_of_positive_numbers(entered_list)
        get_count_of_negative_numbers(entered_list)


@mark.parametrize(
    "entered_list,result",
    [
        ([1, 2, 3, -4, -5, -6], [-1, -2, -3, 4, 5, 6]),
        ([1, 2, 3], [-1, -2, -3]),
        ([-1, -2, -3], [1, 2, 3]),
    ]
)
def test_sign_replacing(entered_list, result):
    assert replace_signs_of_numbers(entered_list) == result


@mark.parametrize(
    "entered_list,message",
    [
        ((1, 2, 3), "Object 'entered_list' must be list"),
        ([1, 2, 3, "a"], "All elements in 'entered_list' must be integers"),
        ([1, 2, 3, 4.444], "All elements in 'entered_list' must be integers"),
    ]
)
def test_sign_replacing_value_error(entered_list, message):
    with raises(ValueError, match=message):
        replace_signs_of_numbers(entered_list)


@mark.parametrize(
    "entered_list,max_element,count",
    [
        ([1, 1, 2, 2, 3, 3], 3, 2),
        ([6, 3, 6, 4, 2, 6, 0, 3], 6, 3),
        ([3, 4, 7, 2, 6, 1], 7, 1),
    ]
)
def test_max_element(entered_list, max_element, count):
    assert get_max_element_and_its_count(entered_list) == (max_element, count)


@mark.parametrize(
    "entered_list,message",
    [
        ((1, 2, 3), "Object 'entered_list' must be list"),
        ([1, 2, 3, "a"], "All elements in 'entered_list' must be integers"),
        ([1, 2, 3, 4.444], "All elements in 'entered_list' must be integers"),
    ]
)
def test_max_element_value_error(entered_list, message):
    with raises(ValueError, match=message):
        get_max_element_and_its_count(entered_list)


@mark.parametrize(
    "entered_list,result",
    [
        ([1, 2, 3, 4, 5, 6], [1, 4, 3, 6, 5, 8]),
        ([6, 4, 2, 6, 8], [12, 10, 8, 12, 14]),
        ([1, 3, 5, 7, 9], [1, 3, 5, 7, 9]),
    ]
)
def test_even_numbers(entered_list, result):
    add_first_even_number_to_all_even_numbers(entered_list)
    assert entered_list == result


@mark.parametrize(
    "entered_list,message",
    [
        ((1, 2, 3), "Object 'entered_list' must be list"),
        ([1, 2, 3, "a"], "All elements in 'entered_list' must be integers"),
        ([1, 2, 3, 4.444], "All elements in 'entered_list' must be integers"),
    ]
)
def test_even_numbers_value_error(entered_list, message):
    with raises(ValueError, match=message):
        add_first_even_number_to_all_even_numbers(entered_list)


@mark.parametrize(
    "entered_list,result",
    [
        ([1, 2, 3, 4, 5, 6], [1, 3, 3, 5, 5, 7]),
        ([2, 4, 6, 8, 0, 1], [3, 5, 7, 9, 1, 1]),
        ([1, 3, 5, 7, 9], [1, 3, 5, 7, 9]),
        ([2, 4, 6, 8], [2, 4, 6, 8]),
    ]
)
def test_odd_number(entered_list, result):
    add_first_odd_number_to_all_even_numbers(entered_list)
    assert entered_list == result


@mark.parametrize(
    "entered_list,message",
    [
        ((1, 2, 3), "Object 'entered_list' must be list"),
        ([1, 2, 3, "a"], "All elements in 'entered_list' must be integers"),
        ([1, 2, 3, 4.444], "All elements in 'entered_list' must be integers"),
    ]
)
def test_odd_number_value_error(entered_list, message):
    with raises(ValueError, match=message):
        add_first_odd_number_to_all_even_numbers(entered_list)


@mark.parametrize(
    "entered_list,result",
    [
        ([1, 2, 3, 4, 5], True),
        ([2, 7, 3, 8, 1], True),
        ([5, 4, 3, 2, 1], False),
    ]
)
def test_non_decreasing_sequence(entered_list,result):
    assert is_list_non_decreasing_sequence(entered_list) == result


@mark.parametrize(
    "entered_list,message",
    [
        ((1, 2, 3), "Object 'entered_list' must be list"),
        ([1, 2, 3, "a"], "All elements in 'entered_list' must be integers"),
        ([1, 2, 3, 4.444], "All elements in 'entered_list' must be integers"),
    ]
)
def test_non_decreasing_sequence_value_error(entered_list, message):
    with raises(ValueError, match=message):
        is_list_non_decreasing_sequence(entered_list)


@mark.parametrize(
    "entered_str,longest_word",
    [
        ("hello world python", "python"),
        ("programming", "programming"),
        ("cat dog bat", "cat"),
        (" hello  world ", "hello"),
        ("hello, world!", "hello"),
    ]
)
def test_longest_word(entered_str, longest_word):
    assert get_longest_word_from_str(entered_str) == longest_word


@mark.parametrize(
    "entered_str,message",
    [
        (1, "Object 'entered_str' must be of type str"),
        ("hello 111 world", 'Entered string must contain only letters, whitespaces and punctuation'),
        ("", "Entered string must contain at least one letter"),
        ("   ", "Entered string must contain at least one letter"),
    ]
)
def test_longest_word_value_error(entered_str, message):
    with raises(ValueError, match=message):
        get_longest_word_from_str(entered_str)


@mark.parametrize(
    "path,file_name",
    [
        (r"C:\Users\dev\python_gym\list\homework\file_name.py", "file_name"),
        ("D:/Users/dev/python_gym/list/classwork/cloning_list.py", "cloning_list"),
        ("E:/111/111/111/111/cat123.txt", "cat123"),
    ]
)
def test_file_name(path, file_name):
    assert get_file_name_from_path_using_list(path) == file_name
    assert get_file_name_from_path_using_regex(path) == file_name


@mark.parametrize(
    "path,message",
    [
        (1, "Object 'path' must be of type str"),
        ("K:/111/111/111/111/cat123.txt", "Invalid path"),
        (r"E:/111/111\111/111/cat123.txt", "Invalid path"),
        (r"E:\111\\\\111\111\111\cat123.txt", "Invalid path"),
    ]
)
def test_file_name_value_error(path, message):
    with raises(ValueError, match=message):
        get_file_name_from_path_using_list(path)
        get_file_name_from_path_using_regex(path)


@mark.parametrize(
    "path,last_folder",
    [
        (r"C:\Users\dev\python_gym\list\homework\file_name.py", "homework"),
        ("D:/Users/dev/python_gym/list/classwork/cloning_list.py", "classwork"),
        ("E:/111/222/333/444/cat123.txt", "444"),
    ]
)
def test_last_folder(path, last_folder):
    assert get_last_folder_from_path_using_list(path) == last_folder
    assert get_last_folder_from_path_using_regex(path) == last_folder


@mark.parametrize(
    "path,message",
    [
        (1, "Object 'path' must be of type str"),
        ("K:/111/111/111/111/cat123.txt", "Invalid path"),
        (r"E:/111/111\111/111/cat123.txt", "Invalid path"),
        (r"E:\111\\\\111\111\111\cat123.txt", "Invalid path"),
    ]
)
def test_last_folder_value_error(path, message):
    with raises(ValueError, match=message):
        get_last_folder_from_path_using_list(path)
        get_last_folder_from_path_using_regex(path)
