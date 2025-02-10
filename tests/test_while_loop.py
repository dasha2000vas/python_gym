from pytest import mark, raises

from while_loop import (
    get_squares_of_natural_numbers,
    increasing_contribution,
    create_n_numbers,
    define_fibonacci_number,
    sum_of_local_min,
    generating_series,
    solving_equation,
    sequence_ends_with_positive_number,
    get_powers_of_2,
    define_power_of_2,
    increasing_athletes_run,
    get_lowest_simple_divider,
)


@mark.parametrize(
    "n,result",
    [
        (10, [1, 4, 9]),
        (50, [1, 4, 9, 16, 25, 36, 49]),
        (100, [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]),
    ]
)
def test_squares_of_natural_numbers(n, result):
    assert get_squares_of_natural_numbers(n) == result


@mark.parametrize(
    "n,message",
    [
        ("10", "n must be integer"),
        (10.111, "n must be integer"),
        (-10, "n must be natural number"),
    ]
)
def test_squares_of_natural_numbers(n, message):
    with raises(ValueError, match=message):
        get_squares_of_natural_numbers(n)


@mark.parametrize(
    "start_rubles,goal_rubles,percent,count_of_years",
    [
        (10, 20, 10, 10),
        (199, 9305, 16, 27),
        (775, 2431, 15, 9),
    ]
)
def test_increasing_contribution(start_rubles, goal_rubles, percent, count_of_years):
    assert increasing_contribution(start_rubles, goal_rubles, percent) == count_of_years


@mark.parametrize(
    "start_rubles,goal_rubles,percent,message",
    [
        (10, 20, "10", "All numbers must be integers"),
        (10, 20.222, 10, "All numbers must be integers"),
        (10, 20, -10, "All numbers must be positive"),
    ]
)
def test_increasing_contribution(start_rubles, goal_rubles, percent, message):
    with raises(ValueError, match=message):
        increasing_contribution(start_rubles, goal_rubles, percent)


@mark.parametrize(
    "n,message",
    [
        ("10", "n must be integer"),
        (10.111, "n must be integer"),
        (-10, "n must be positive"),
    ]
)
def test_n_numbers(n, message):
    with raises(ValueError, match=message):
        create_n_numbers(n)


@mark.parametrize(
    "number,result",
    [
        (1, (1, 2)),
        (8, 6),
        (55, 10),
        (18, "Number 18 isn't fibonacci number")
    ]
)
def test_define_fibonacci_number(number, result):
    assert define_fibonacci_number(number) == result


@mark.parametrize(
    "number,message",
    [
        ("1", "Number must be integer"),
        (1.111, "Number must be integer"),
        (-10, "Number must be positive"),
    ]
)
def test_define_fibonacci_number(number, message):
    with raises(ValueError, match=message):
        define_fibonacci_number(number)


@mark.parametrize(
    "numbers, result",
    [
        ([1, 2, 5, 10, 1, 1], 3),
        ([-7, -9, 9, -10, -3, -10, 8], -20),
        ([-8, -2, 8, -6], -8),
    ]
)
def test_sum_of_local_min(numbers, result):
    assert sum_of_local_min(numbers) == result


@mark.parametrize(
    "numbers,message",
    [
        ([1, 2, 3, "4"], "All numbers must be an integers"),
        ([1, 2, 3, 4.444], "All numbers must be an integers"),
        ([1, 2, 3, 0], "All numbers cannot be 0"),
    ]
)
def test_sum_of_local_min(numbers, message):
    with raises(ValueError, match=message):
        sum_of_local_min(numbers)


def test_generating_series():
    result = generating_series()
    twos = 0
    zeros = 0
    for number in result:
        if number == 0:
            zeros += 1
        elif number == 2:
            twos += 1
    assert zeros == twos


def test_solving_equation():
    assert solving_equation() == 0.33758544921875


def test_sequence_ends_with_positive_number():
    assert sequence_ends_with_positive_number()[-1] > 0


@mark.parametrize(
    "n,result",
    [
        (10, [1, 2, 3]),
        (100, [1, 2, 3, 4, 5, 6]),
        (300, [1, 2, 3, 4, 5, 6, 7, 8]),
    ]
)
def test_powers_of_2(n, result):
    assert get_powers_of_2(n) == result


@mark.parametrize(
    "n, message",
    [
        ("10", "n must be integer"),
        (10.111, "n must be integer"),
        (-10, "n must be positive"),
    ]
)
def test_powers_of_2(n, message):
    with raises(ValueError, match=message):
        get_powers_of_2(n)


@mark.parametrize(
    "n,result",
    [
        (7, 3),
        (8, 3),
        (9, 4),
    ]
)
def test_define_power_of_2(n, result):
    assert define_power_of_2(n) == result


@mark.parametrize(
    "n,message",
    [
        ("10", "n must be integer"),
        (10.111, "n must be integer"),
        (-10, "n must be positive"),
    ]
)
def test_define_power_of_2(n, message):
    with raises(ValueError, match=message):
        define_power_of_2(n)


@mark.parametrize(
    "first_day_distance,goal_distance,days",
    [
        (10, 19, 8),
        (5, 10, 9),
        (6, 12, 9),
    ]
)
def test_athletes_run(first_day_distance, goal_distance, days):
    assert increasing_athletes_run(first_day_distance, goal_distance) == days


@mark.parametrize(
    "first_day_distance,goal_distance,message",
    [
        (10, "19", "All numbers must be integers"),
        (10, 19.999, "All numbers must be integers"),
        (10, -19, "All numbers must be positive"),
    ]
)
def test_athletes_run(first_day_distance, goal_distance, message):
    with raises(ValueError, match=message):
        increasing_athletes_run(first_day_distance, goal_distance)


@mark.parametrize(
    "num,divider",
    [
        (79, 79),
        (77, 7),
        (14, 2),
    ]
)
def test_lowest_simple_divider(num,divider):
    assert get_lowest_simple_divider(num) == divider


@mark.parametrize(
    "num,message",
    [
        ("10", "num must be integer"),
        (10.111, "num must be integer"),
        (1, "num cannot be less than 2"),
    ]
)
def test_lowest_simple_divider(num, message):
    with raises(ValueError, match=message):
        get_lowest_simple_divider(num)
