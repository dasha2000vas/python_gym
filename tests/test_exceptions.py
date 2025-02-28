from pytest import mark, raises

from exceptions import (
    check_if_expression_is_valid,
    check_if_number_is_greater_than_ten,
    get_nth_fibonacci_number,
    add_strings_and_integers,
    get_factorial_recursively,
    get_factorial_iteratively,
    check_if_substring_in_string,
)


@mark.parametrize(
    "number1,number2,result",
    [
        (4, 2, 1),
        (4, 0, "Number2 cannot be zero"),
        (-4, 2, "Number1 cannot be negative"),
    ]
)
def test_expression(number1, number2, result):
    assert check_if_expression_is_valid(number1, number2) == result


@mark.parametrize(
    "number1,number2",
    [
        ("a", 2),
        (4, "a"),
    ]
)
def test_expression_value_error(number1, number2):
    with raises(ValueError, match="All args must be integers"):
        check_if_expression_is_valid(number1, number2)


@mark.parametrize(
    "number,result",
    [
        (1, "Number must be greater than 10"),
        (20, "Number is greater than 10"),
        (10, "Number must be greater than 10"),
    ]
)
def test_number_greater_than_10(number, result):
    assert check_if_number_is_greater_than_ten(number) == result


@mark.parametrize(
    "number",
    [
        "a", 1.111, [1]
    ]
)
def test_number_greater_than_10_value_error(number):
    with raises(ValueError, match="Object number must be integer"):
        check_if_number_is_greater_than_ten(number)


@mark.parametrize(
    "number,first,second,result",
    [
        (11, 1, 1, 89),
        ("a", 1, 1, "All args must be integers"),
        (11, "a", 1, "All args must be integers"),
        (11, 1, "a", "All args must be integers"),
        (11, -1, 1, "Numbers first and second must be greater or equal to one"),
        (11, 1, 0, "Numbers first and second must be greater or equal to one"),
        (-1, 1, 1, "Number cannot be negative"),
    ]
)
def test_fibonacci_number(number, first, second, result):
    assert get_nth_fibonacci_number(number, first, second) == result


@mark.parametrize(
    "obj1,obj2,result",
    [
        (2, 2, 4),
        ("2", 2, 4),
        (2, "2", 4),
        ("2", "2", 4),
        ("a2", 2, "a22"),
        (2, "b2", "2b2"),
        ("abc", "1def", "abc1def"),
    ]
)
def test_addition(obj1, obj2, result):
    assert add_strings_and_integers(obj1, obj2) == result


@mark.parametrize(
    "obj1,obj2",
    [
        (2.222, 2),
        (2, [2]),
    ]
)
def test_addition_value_error(obj1, obj2):
    with raises(ValueError, match="All args must be of type str or int"):
        add_strings_and_integers(obj1, obj2)


@mark.parametrize(
    "number,result",
    [
        (5, 120),
        (10, 3628800),
        ("a", 'Number must be integer'),
        (-5, 'Number cannot be negative'),
        (1000, "Recursion limit exceeded")
    ]
)
def test_factorial(number, result):
    if result != "Recursion limit exceeded":
        assert get_factorial_iteratively(number) == result
    assert get_factorial_recursively(number) == result


@mark.parametrize(
    "entered_string,substring,result",
    [
        ("A snake sneaks to seek a snack.", "sn", 2),
        ("A snake sneaks to seek a snack.", "ak", 4),
        ("A snake sneaks to seek a snack.", "ca", "There's no substring 'ca' in entered string"),
        (1, "a", "All args must be strings"),
        ("a", 1, "All args must be strings"),
    ]
)
def test_substring(entered_string, substring, result):
    assert check_if_substring_in_string(entered_string, substring) == result
