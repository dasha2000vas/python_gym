from pytest import mark

from arithmetic_operators.home_work.celsius_to_fahrenheit import calculate_temperature_in_fahrenheit
from arithmetic_operators.home_work.perimeter_and_square_of_triangle import find_perimeter_and_square
from arithmetic_operators.home_work.leftmost_digit_to_right_end import move_leftmost_digit_to_right_end
from arithmetic_operators.home_work.third_digit_from_end import define_third_digit_from_end
from arithmetic_operators.home_work.glue_numbers import glue_numbers
from arithmetic_operators.home_work.sum_of_digits import sum_of_digits
from arithmetic_operators.home_work.count_of_square_in_rectangle import find_count_of_squares_in_rectangle
from arithmetic_operators.home_work.find_b_in_a import find_b_in_a
from arithmetic_operators.home_work.cost_in_rubles_and_pennies import find_cost_in_rubles_and_pennies
from arithmetic_operators.home_work.count_value import count_value
from arithmetic_operators.home_work.count_of_cabins import count_of_cabins
from arithmetic_operators.home_work.count_of_desks import calculate_count_of_desks
from arithmetic_operators.home_work.calculate_y_from_a_and_angle_x import calculate_y_from_a_and_angle_x
from arithmetic_operators.home_work.calculate_y_from_a_b_c_d_and_angle_x import calculate_y_from_a_b_c_d_and_angle_x


@mark.parametrize("test_temp_in_celsius,test_temp_in_fahrenheit", [(25, 77), (40, 104), (60, 140)])
def test_celsius_to_fahrenheit(test_temp_in_celsius, test_temp_in_fahrenheit):
    assert calculate_temperature_in_fahrenheit(test_temp_in_celsius) == test_temp_in_fahrenheit


@mark.parametrize(
    "test_x1,test_x2,test_x3,test_y1,test_y2,test_y3,test_perimeter,test_square",
    [
        (2, 3, 6, 1, 4, 8, 16.22, 2.5),
        (1, 4, 7, 3, 5, 10, 18.66, 4.5),
        (1, 5, 9, 1, 5, 7, 20.13, 4)
    ]
)
def test_perimeter_and_square_of_triangle(
        test_x1, test_x2, test_x3, test_y1, test_y2, test_y3, test_perimeter, test_square
):
    assert find_perimeter_and_square(
        test_x1, test_x2, test_x3, test_y1, test_y2, test_y3
    ) == (test_perimeter, test_square)


@mark.parametrize("test_number,test_result", [(237, 372), (340, 403), (572, 725)])
def test_leftmost_digit_to_right_end(test_number, test_result):
    assert move_leftmost_digit_to_right_end(test_number) == test_result


@mark.parametrize("test_number,test_result", [(130985, 9), (24024057, 0), (321, 3)])
def test_third_digit_from_end(test_number, test_result):
    assert define_third_digit_from_end(test_number) == test_result


@mark.parametrize(
    "test_a,test_b,test_result",
    [(100, 500, 100500), (123, 456, 123456 ), (987, 654, 987654)]
)
def test_glue_numbers(test_a, test_b, test_result):
    assert glue_numbers(test_a, test_b) == test_result


@mark.parametrize("test_number,test_sum", [(111, 3), (123, 6), (999, 27)])
def test_sum_of_digits(test_number, test_sum):
    assert sum_of_digits(test_number) == test_sum


@mark.parametrize(
    "test_a,test_b,test_c,test_count,test_remain",
    [(11, 7, 3, 6, 23), (9, 16, 4, 8,16), (21, 24, 20, 1, 104)]
)
def test_count_of_squares_in_rectangle(test_a, test_b, test_c, test_count, test_remain):
    assert find_count_of_squares_in_rectangle(test_a, test_b, test_c) == (test_count, test_remain)


@mark.parametrize(
    "test_a,test_b,test_count,test_remain",
    [(20, 3, 6, 2), (123, 4, 30, 3), (987, 56, 17, 35)]
)
def test_find_b_in_a(test_a, test_b, test_count, test_remain):
    assert find_b_in_a(test_a, test_b) == (test_count, test_remain)


@mark.parametrize(
    "test_cost_in_pennies,test_rubles,test_pennies",
    [(453, 4, 53), (3483, 34, 83), (98765, 987, 65)]
)
def test_cost_in_rubles_and_pennies(test_cost_in_pennies, test_rubles, test_pennies):
    assert find_cost_in_rubles_and_pennies(test_cost_in_pennies) == (test_rubles, test_pennies)


@mark.parametrize(
    "test_a,test_b,test_c,test_d,test_result",
    [(3, 5, 33, 77, 44.998), (2, 3, 4, 5, 17.8), (6, 7, 11, 22, 125.983)]
)
def test_count_value(test_a, test_b, test_c, test_d, test_result):
    assert count_value(test_a, test_b, test_c, test_d) == test_result


@mark.parametrize("test_a,test_b,test_count", [(8, 20, 24), (1, 5, 8), (4, 22, 36)])
def test_count_of_cabins(test_a, test_b, test_count):
    assert count_of_cabins(test_a, test_b) == test_count


@mark.parametrize(
    "test_class_a,test_class_b,test_class_c,test_count",
    [(21, 19, 17, 30), (11, 15, 23, 26), (19, 25, 22, 34)]
)
def test_count_of_desks(test_class_a, test_class_b, test_class_c, test_count):
    assert calculate_count_of_desks(test_class_a, test_class_b, test_class_c) == test_count


@mark.parametrize(
    "test_a,test_x,test_result_if_x_in_radians,test_result_if_x_in_degrees",
    [
        (12, 45, 117835.745, 81375.794),
        (5, 20, 121.555, 16.697),
        (2, 30, 3.213, 1.636),
    ]
)
def test_calculate_y_from_a_and_angle_x(test_a, test_x, test_result_if_x_in_radians, test_result_if_x_in_degrees):
    assert calculate_y_from_a_and_angle_x(test_a, test_x) == test_result_if_x_in_radians
    assert calculate_y_from_a_and_angle_x(test_a, test_x, True) == test_result_if_x_in_degrees


@mark.parametrize(
    "test_a,test_b,test_c,test_d,test_x,test_result_if_x_in_radians,test_result_if_x_in_degrees",
    [
        (22, 1, 44, 27, 30, 3499615212.824, 896228237.135),
        (2, 3, 4, 5, 6, 3.996, 3.5),
        (11, 12, 13, 14, 15, 25329.783, 4021.356),
    ]
)
def test_calculate_y_from_a_b_c_d_and_angle_x(
        test_a,
        test_b,
        test_c,
        test_d,
        test_x,
        test_result_if_x_in_radians,
        test_result_if_x_in_degrees
):
    assert calculate_y_from_a_b_c_d_and_angle_x(
        test_a,
        test_b,
        test_c,
        test_d,
        test_x,
    ) == test_result_if_x_in_radians
    assert calculate_y_from_a_b_c_d_and_angle_x(
        test_a,
        test_b,
        test_c,
        test_d,
        test_x,
        True
    ) == test_result_if_x_in_degrees
