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
from arithmetic_operators.home_work.calculate_value import calculate_value
from arithmetic_operators.home_work.count_of_cabins import count_of_cabins
from arithmetic_operators.home_work.count_of_desks import calculate_count_of_desks
from arithmetic_operators.home_work.calculate_y_from_a_and_angle_x import calculate_y_from_a_and_angle_x
from arithmetic_operators.home_work.calculate_y_from_a_b_c_d_and_angle_x import calculate_y_from_a_b_c_d_and_angle_x


@mark.parametrize("temp_in_celsius,temp_in_fahrenheit", [(25, 77), (40, 104), (60, 140)])
def test_celsius_to_fahrenheit(temp_in_celsius, temp_in_fahrenheit):
    assert calculate_temperature_in_fahrenheit(temp_in_celsius) == temp_in_fahrenheit


@mark.parametrize(
    "x1,x2,x3,y1,y2,y3,perimeter,square",
    [
        (2, 3, 6, 1, 4, 8, 16.22, 2.5),
        (1, 4, 7, 3, 5, 10, 18.66, 4.5),
        (1, 5, 9, 1, 5, 7, 20.13, 4)
    ]
)
def test_perimeter_and_square_of_triangle(
        x1, x2, x3, y1, y2, y3, perimeter, square
):
    assert find_perimeter_and_square(
        x1, x2, x3, y1, y2, y3
    ) == (perimeter, square)


@mark.parametrize("number,result", [(237, 372), (340, 403), (572, 725)])
def test_leftmost_digit_to_right_end(number, result):
    assert move_leftmost_digit_to_right_end(number) == result


@mark.parametrize("number,result", [(130985, 9), (24024057, 0), (321, 3)])
def test_third_digit_from_end(number, result):
    assert define_third_digit_from_end(number) == result


@mark.parametrize(
    "a,b,result",
    [(100, 500, 100500), (123, 456, 123456 ), (987, 654, 987654)]
)
def test_glue_numbers(a, b, result):
    assert glue_numbers(a, b) == result


@mark.parametrize("number,sum", [(111, 3), (123, 6), (999, 27)])
def test_sum_of_digits(number, sum):
    assert sum_of_digits(number) == sum


@mark.parametrize(
    "a,b,c,count,remain",
    [(11, 7, 3, 6, 23), (9, 16, 4, 8,16), (21, 24, 20, 1, 104)]
)
def test_count_of_squares_in_rectangle(a, b, c, count, remain):
    assert find_count_of_squares_in_rectangle(a, b, c) == (count, remain)


@mark.parametrize(
    "a,b,count,remain",
    [(20, 3, 6, 2), (123, 4, 30, 3), (987, 56, 17, 35)]
)
def test_find_b_in_a(a, b, count, remain):
    assert find_b_in_a(a, b) == (count, remain)


@mark.parametrize(
    "cost_in_pennies,rubles,pennies",
    [(453, 4, 53), (3483, 34, 83), (98765, 987, 65)]
)
def test_cost_in_rubles_and_pennies(cost_in_pennies, rubles, pennies):
    assert find_cost_in_rubles_and_pennies(cost_in_pennies) == (rubles, pennies)


@mark.parametrize(
    "a,b,c,d,result",
    [(3, 5, 33, 77, 44.998), (2, 3, 4, 5, 17.8), (6, 7, 11, 22, 125.983)]
)
def test_calculate_value(a, b, c, d, result):
    assert calculate_value(a, b, c, d) == result


@mark.parametrize("a,b,count", [(8, 20, 24), (1, 5, 8), (4, 22, 36)])
def test_count_of_cabins(a, b, count):
    assert count_of_cabins(a, b) == count


@mark.parametrize(
    "class_a,class_b,class_c,count",
    [(21, 19, 17, 30), (11, 15, 23, 26), (19, 25, 22, 34)]
)
def test_count_of_desks(class_a, class_b, class_c, count):
    assert calculate_count_of_desks(class_a, class_b, class_c) == count


@mark.parametrize(
    "a,x,result_if_x_in_radians,result_if_x_in_degrees",
    [
        (12, 45, 117835.745, 81375.794),
        (5, 20, 121.555, 16.697),
        (2, 30, 3.213, 1.636),
    ]
)
def test_calculate_y_from_a_and_angle_x(a, x, result_if_x_in_radians, result_if_x_in_degrees):
    assert calculate_y_from_a_and_angle_x(a, x) == result_if_x_in_radians
    assert calculate_y_from_a_and_angle_x(a, x, True) == result_if_x_in_degrees


@mark.parametrize(
    "a,b,c,d,x,result_if_x_in_radians,result_if_x_in_degrees",
    [
        (22, 1, 44, 27, 30, 3499615212.824, 896228237.135),
        (2, 3, 4, 5, 6, 3.996, 3.5),
        (11, 12, 13, 14, 15, 25329.783, 4021.356),
    ]
)
def test_calculate_y_from_a_b_c_d_and_angle_x(
        a, b, c, d, x, result_if_x_in_radians, result_if_x_in_degrees
):
    assert calculate_y_from_a_b_c_d_and_angle_x(
        a, b, c, d, x,
    ) == result_if_x_in_radians
    assert calculate_y_from_a_b_c_d_and_angle_x(
        a, b, c, d, x,
        True
    ) == result_if_x_in_degrees
