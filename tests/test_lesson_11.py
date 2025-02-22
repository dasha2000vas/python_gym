from pytest import mark, raises


from lesson_11 import (
    get_sum_from_1_to_n,
    raise_number_to_power_of_n,
    get_factorial_iteratively,
    get_factorial_recursively,
    calculate_profit_indicators,
    find_members_of_sequence_recursively,
    find_members_of_sequence_iteratively,
    sum_of_series_recursively,
    sum_of_series_iteratively,
)


@mark.parametrize(
    "n,result",
    [
        (3, 6),
        (4, 10),
        (8, 36),
    ]
)
def test_sum_from_1_to_n(n, result):
    assert get_sum_from_1_to_n(n) == result


@mark.parametrize(
    "n,message",
    [
        ("1", "N must be integer"),
        (1.111, "N must be integer"),
        (-1, "N must be positive"),
    ]
)
def test_sum_from_1_to_n_value_error(n, message):
    with raises(ValueError, match=message):
        get_sum_from_1_to_n(n)


@mark.parametrize(
    "number,power,result",
    [
        (2, 10, 1024),
        (3, 5, 243),
        (7, 3, 343),
    ]
)
def test_number_to_power_of_n(number, power, result):
    assert raise_number_to_power_of_n(number, power) == result


@mark.parametrize(
    "number,power,message",
    [
        ("2", 2, "Number must be integer or float"),
        (2, "2", "Power must be integer"),
        (2, -2, "Power must be positive"),
    ]
)
def test_number_to_power_of_n_value_error(number, power, message):
    with raises(ValueError, match=message):
        raise_number_to_power_of_n(number, power)


@mark.parametrize(
    "number,result",
    [
        (4, 24),
        (8, 40320),
        (10, 3628800),
    ]
)
def test_factorial_of_number(number, result):
    assert get_factorial_iteratively(number) == result
    assert get_factorial_recursively(number) == result


@mark.parametrize(
    "number,message",
    [
        ("1", 'Number must be integer'),
        (-1, 'Number cannot be negative'),
        (1000, "Recursion limit exceeded"),
    ]
)
def test_factorial_of_number_value_error(number, message):
    with raises(ValueError, match=message):
        if message != "Recursion limit exceeded":
            get_factorial_iteratively(number)
        get_factorial_recursively(number)


@mark.parametrize(
    "first_profit,percent,years,result",
    [
        (100, 10, 5, 133.1),
        (163, 3, 9, 200.469),
        (492, 3, 10, 623.251),
    ]
)
def test_business_plan(first_profit, percent, years, result):
    assert calculate_profit_indicators(first_profit, percent, years) == result


@mark.parametrize(
    "first_profit,percent,years,message",
    [
        (10, "10", 10, "Percent and years value must be integers"),
        (10, 10, "10", "Percent and years value must be integers"),
        ("10", 10, 10, "Second year's profit must be integer or float"),
        (-10, 10, 10, "All args must be positive"),
        (10, -10, 10, "All args must be positive"),
        (10, 10, -10, "All args must be positive"),
    ]
)
def test_business_plan_value_error(first_profit, percent, years, message):
    with raises(ValueError, match=message):
        calculate_profit_indicators(first_profit, percent, years)


@mark.parametrize(
    "number,n,result",
    [
        (0.5, 5, [0.5, 1.5, 1.25, 0.75, 0.438, 0.288]),
        (0.222, 3, [0.222, 1.222, 1.111, 0.704]),
        (0.648, 1, [0.648, 1.648]),
    ]
)
def test_members_of_sequence(number, n, result):
    assert find_members_of_sequence_iteratively(number, n) == result
    assert find_members_of_sequence_recursively(number, n) == result


@mark.parametrize(
    "number,n,message",
    [
        (1, 1, "Starting number must be of type float"),
        (1.5, 1, 'Starting number must be between 1 and 0'),
        (0.5, "1", 'N must be of type int'),
        (0.5, 0, 'N must be greater than 0'),
        (0.5, 1000, "Recursion limit exceeded"),
    ]
)
def test_members_of_sequence_value_error(number, n, message):
    with raises(ValueError, match=message):
        if message != "Recursion limit exceeded":
            find_members_of_sequence_iteratively(number, n)
        find_members_of_sequence_recursively(number, n)


@mark.parametrize(
    "number,n,result",
    [
        (2, 3, 12),
        (19, 94, 84835),
        (5, 11, 330),
    ]
)
def test_sum_of_series(number, n, result):
    assert sum_of_series_iteratively(number, n) == result
    assert sum_of_series_recursively(number, n) == result


@mark.parametrize(
    "number,n,message",
    [
        ("10", 10, 'All args must be integers'),
        (10, "10", "All args must be integers"),
        (-100, 10, 'All args must be between 0 and 100'),
        (10, 200, 'All args must be between 0 and 100'),
    ]
)
def test_sum_of_series_value_error(number, n, message):
    with raises(ValueError, match=message):
        sum_of_series_iteratively(number, n)
        sum_of_series_recursively(number, n)
