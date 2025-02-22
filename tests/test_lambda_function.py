from pytest import mark, raises

from lambda_function import (
    get_area_of_circle,
    get_areas_of_circles,
    is_string_number,
    contain_letter_and_digit,
    get_nth_fibonacci_number,
)


@mark.parametrize(
    "radius,result",
    [
        (68, 14526.724),
        (7, 153.938),
        (88.497, 24604.071),
    ]
)
def test_area_of_circle(radius, result):
    assert get_area_of_circle(radius) == result


@mark.parametrize(
    "radius,message",
    [
        ("1", 'Radius must be integer or float'),
        ([1], 'Radius must be integer or float'),
        (-1, 'Radius value must be positive'),
    ]
)
def test_area_of_circle_value_error(radius, message):
    with raises(ValueError, match=message):
        get_area_of_circle(radius)


@mark.parametrize(
    "start,end,result",
    [
        (1, 6, [3.142, 12.566, 28.274, 50.265, 78.54, 113.097]),
        (4, 8, [50.265, 78.54, 113.097, 153.938, 201.062]),
        (2, 6, [12.566, 28.274, 50.265, 78.54, 113.097]),
    ]
)
def test_areas_of_circles(start, end, result):
    assert get_areas_of_circles(start, end) == result


@mark.parametrize(
    "start,end,message",
    [
        ("1", 3, 'All args must be integers'),
        (1, -3, 'All numbers must be positive'),
    ]
)
def test__value_error(start, end, message):
    with raises(ValueError, match=message):
        get_areas_of_circles(start, end)


@mark.parametrize(
    "entered_str,result",
    [
        ("2", True),
        ("-2", True),
        ("2.0", True),
        ("-2.0", True),
        ("2.0.0", False),
        ("cat2", False),
    ]
)
def test_is_number(entered_str, result):
    assert is_string_number(entered_str) == result


@mark.parametrize(
    "entered_str",
    [
        2,
        ["2"],
        2.222,
    ]
)
def test_is_number_value_error(entered_str):
    with raises(ValueError, match="Object entered_str must be string"):
        is_string_number(entered_str)


@mark.parametrize(
    "entered_str,result",
    [
        ("AAbb11", True),
        ("AAbb", False),
        ("1234", False),
        ("AA123", False),
        ("abc12", False),
    ]
)
def test_contain_letter_and_digit(entered_str, result):
    assert contain_letter_and_digit(entered_str) == result


@mark.parametrize(
    "entered_str",
    [
        1234,
        1.111,
        ["abc123D"],
    ]
)
def test_contain_letter_and_digit_value_error(entered_str):
    with raises(ValueError, match="Object entered_str must be string"):
        contain_letter_and_digit(entered_str)


@mark.parametrize(
    "n,result",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (16, 987),
        (10, 55),
    ]
)
def test_nth_fibonacci_number(n, result):
    assert get_nth_fibonacci_number(n) == result


@mark.parametrize(
    "n,message",
    [
        ("1", 'Object n must be integer'),
        (1.111, 'Object n must be integer'),
        (-1, 'Number n cannot be negative'),
    ]
)
def test_nth_fibonacci_number_value_error(n, message):
    with raises(ValueError, match=message):
        get_nth_fibonacci_number(n)
