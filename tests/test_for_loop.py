from pytest import mark, raises

from for_loop import (
    range_up_to_n,
    range_from_a_to_b,
    sum_of_series_up_to_nth_term,
    are_all_numbers_even,
    multiple_of_3_end_2_or_8,
    sum_of_series_signs_rotate,
    get_factorial_of_number,
    are_there_even_numbers,
    get_simple_numbers,
    numbers_equal_to_its_sum_of_cubes_of_digits,
    count_of_right_angled_triangles,
    count_of_coin_sets,
    nth_fibonacci_number,
    sum_of_series,
    get_perfect_numbers,
)


@mark.parametrize(
    "n,result",
    [
        (11, "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10"),
        (12, "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11"),
        (15, "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14"),
    ],
)
def test_range_up_to_n(n, result):
    assert range_up_to_n(n) == result


@mark.parametrize(
    "n,message",
    [
        (1, "n must be greater than 10"),
        (-10, "n must be greater than 10"),
        (11.111, "n must be integer"),
    ]
)
def test_range_up_to_n_value_error(n, message):
    with raises(ValueError, match=message):
        range_up_to_n(n)


@mark.parametrize(
    "a,b,s,result",
    [
        (34, 71, 10, "34, 44, 54, 64"),
        (13, 87, 8, "13, 21, 29, 37, 45, 53, 61, 69, 77, 85"),
        (41, 80, 4, "41, 45, 49, 53, 57, 61, 65, 69, 73, 77"),

    ]
)
def test_range_from_a_to_b(a, b, s, result):
    assert range_from_a_to_b(a, b, s) == result


@mark.parametrize(
    "a,b,s,message",
    [
        (-10, -5, 2, "a, b and s must be positive"),
        (5, 10, 2.222, "a, b and s must be integers"),
        (5, 10, "2", "a, b and s must be integers"),
        (10, 5, 2, "b must be greater than a"),
    ]
)
def test_range_from_a_to_b_value_error(a, b, s, message):
    with raises(ValueError, match=message):
        range_from_a_to_b(a, b, s)


@mark.parametrize(
    "n,result",
    [
        (7, 2.593),
        (67, 4.789),
        (45, 4.395),
    ]
)
def test_sum_of_series_up_to_nth_term(n, result):
    assert sum_of_series_up_to_nth_term(n) == result


@mark.parametrize(
    "n,message",
    [
        (3.333, "n must be integer"),
        ("3", "n must be integer"),
        (-10, "n must be positive")
    ]
)
def test_sum_of_series_up_to_nth_term_value_error(n, message):
    with raises(ValueError, match=message):
        sum_of_series_up_to_nth_term(n)


@mark.parametrize(
    "numbers,result",
    [
        ([2, 26, 14], "All numbers are even"),
        ([2, 26, 13], "There are odd numbers"),
        ([1, 25, 13], "There are odd numbers"),
    ]
)
def test_even_numbers(numbers, result):
    assert are_all_numbers_even(numbers) == result


@mark.parametrize(
    "numbers, message",
    [
        (2, "Numbers is not a list"),
        ("2", "Numbers is not a list"),
        ([2, 26, 14.444], "Items of list numbers must be integers"),
        ([2, "26", 14], "Items of list numbers must be integers"),
        ([[2], 26, 14], "Items of list numbers must be integers")
    ]
)
def test_even_numbers_value_error(numbers, message):
    with raises(ValueError, match=message):
        are_all_numbers_even(numbers)


@mark.parametrize(
    "a,b,target_numbers,sum_of_target_numbers",
    [
        (2, 50,[12, 18, 42, 48], 120),
        (38, 73, [42, 48, 72], 162),
        (2, 76, [12, 18, 42, 48, 72], 192),
    ]
)
def test_multiple_of_3_end_2_or_8(a, b, target_numbers, sum_of_target_numbers):
    assert multiple_of_3_end_2_or_8(a, b) == (target_numbers, sum_of_target_numbers)


@mark.parametrize(
    "a,b,message",
    [
        (2, -10, "a and b must be positive"),
        (2.222, 10, "a and b must be integers"),
        ("2", 10, "a and b must be integers"),
        (10, 2, "b must be greater than a"),
    ]
)
def test_multiple_of_3_end_2_or_8_value_error(a, b, message):
    with raises(ValueError, match=message):
        multiple_of_3_end_2_or_8(a, b)


@mark.parametrize(
    "n,result",
    [
        (7, 0.76),
        (48, 0.68),
        (25, 0.71),
    ]
)
def test_sum_of_series_signs_rotate(n, result):
    assert sum_of_series_signs_rotate(n) == result


@mark.parametrize(
    "n,message",
    [
        ("7", "n must be integer"),
        (48.48, "n must be integer"),
        (-25, "n must be positive"),
    ]
)
def test_sum_of_series_signs_rotate_value_error(n, message):
    with raises(ValueError, match=message):
         sum_of_series_signs_rotate(n)


@mark.parametrize(
    "n,result",
    [
        (0, 1),
        (5, 120),
        (10, 3628800),
    ]
)
def test_factorial_of_number(n, result):
    assert get_factorial_of_number(n) == result


@mark.parametrize(
    "n,message",
    [
        ("0", "n must be integer"),
        (0.222, "n must be integer"),
        (-10, "n can't be negative"),
    ]
)
def test_factorial_of_number_value_error(n, message):
    with raises(ValueError, match=message):
        get_factorial_of_number(n)


@mark.parametrize(
    "numbers,result",
    [
        ([1, 2, 3], "There are at least one even number"),
        ([2, 4, 6], "There are at least one even number"),
        ([1, 3, 5], "There are no even numbers"),
    ]
)
def test_is_there_even_numbers(numbers, result):
    assert are_there_even_numbers(numbers) == result


@mark.parametrize(
    "numbers, message",
    [
        (1, "Numbers is not a list"),
        ("1", "Numbers is not a list"),
        ([1.111, 2, 3], "Items of list numbers must be integers"),
        (["1", 2, 3], "Items of list numbers must be integers"),
        ([[1], 2, 3], "Items of list numbers must be integers"),
    ]
)
def test_is_there_even_numbers_value_error(numbers, message):
    with raises(ValueError, match=message):
        are_there_even_numbers(numbers)



@mark.parametrize(
    "a,b,result",
    [
        (0, 5, [2, 3, 5]),
        (10, 40, [11, 13, 17, 19, 23, 29, 31, 37]),
        (50, 70, [53, 59, 61, 67]),
    ]
)
def test_simple_numbers(a, b, result):
    assert get_simple_numbers(a, b) == result


@mark.parametrize(
    "a,b,message",
    [
        (0, "10", "a and b must be integers"),
        (0, 10.111, "a and b must be integers"),
        (0, -10, "a and b mustn't be negative"),
        (10, 0, "b must be greater than a"),
    ],
)
def test_simple_numbers_value_error(a, b, message):
    with raises(ValueError, match=message):
        get_simple_numbers(a, b)


def test_sum_of_cubes_of_digits():
    assert numbers_equal_to_its_sum_of_cubes_of_digits() == [153, 370, 371, 407]


@mark.parametrize(
    "min_side, max_side,result",
    [
        (1, 100, 50),
        (44, 93, 6),
        (20, 69, 15),
    ]
)
def test_count_of_right_angled_triangles(min_side, max_side, result):
    assert count_of_right_angled_triangles(min_side, max_side) == result


@mark.parametrize(
    "min_side,max_side,message",
    [
        (1, "100", "min_side and max_side must be integers"),
        (1.111, 100, "min_side and max_side must be integers"),
        (-10, 100, "min_side and max_side must be positive"),
        (100, 1, "max_side must be greater than min_side"),
    ]
)
def test_count_of_right_angled_triangles_value_error(min_side, max_side, message):
    with raises(ValueError, match=message):
        count_of_right_angled_triangles(min_side, max_side)


@mark.parametrize(
    "a1,a2,a5,a10,target_sum,result",
    [
        (4, 3, 5, 2, 34, 9),
        (2, 8, 1, 4, 43, 5),
        (3, 1, 8, 1, 22, 4),
    ]
)
def test_count_of_coin_sets(a1, a2, a5, a10, target_sum, result):
    assert count_of_coin_sets(a1, a2, a5, a10, target_sum) == result


@mark.parametrize(
    "a1,a2,a5,a10,target_sum,message",
    [
        (4, 3, 5, 2, "34", "All numbers must be integers"),
        (4, 3, 5.555, 2, 34, "All numbers must be integers"),
        (4, 3, 5, -2, 34, "All numbers must be positive"),
    ]
)
def test_count_of_coin_sets_value_error(a1, a2, a5, a10, target_sum, message):
    with raises(ValueError, match=message):
        count_of_coin_sets(a1, a2, a5, a10, target_sum)


@mark.parametrize(
    "n,result",
    [
        (6, 8),
        (9, 34),
        (20, 6765),
    ]
)
def test_nth_fibonacci_number(n, result):
    assert nth_fibonacci_number(n) == result


@mark.parametrize(
    "n,message",
    [
        ("6", "n must be integer"),
        (5.555, "n must be integer"),
        (-6, "n must be positive"),
    ]
)
def test_nth_fibonacci_number_value_error(n, message):
    with raises(ValueError, match=message):
        nth_fibonacci_number(n)


@mark.parametrize(
    "n,result",
    [
        (4, 7106),
        (6, 4149986),
        (10, 6867491336546),
    ]
)
def test_sum_of_series(n, result):
    assert sum_of_series(n) == result


@mark.parametrize(
    "n,message",
    [
        ("6", "n must be integer"),
        (5.555, "n must be integer"),
        (-6, "n must be positive"),
    ]
)
def test_sum_of_series_value_error(n, message):
    with raises(ValueError, match=message):
        sum_of_series(n)


@mark.parametrize(
    "n,result",
    [
        (30, [6, 28]),
        (500, [6, 28, 496]),
        (9000, [6, 28, 496, 8128]),
    ]
)
def test_perfect_numbers(n, result):
    assert get_perfect_numbers(n) == result


@mark.parametrize(
    "n,message",
    [
        ("500", "n must be integer"),
        (500.555, "n must be integer"),
        (-500, "n must be positive"),
    ]
)
def test_perfect_numbers_value_error(n, message):
    with raises(ValueError, match=message):
        get_perfect_numbers(n)
