from pytest import mark

from data_types_formatted_output.class_work.calculate_f_1 import calculate_f_1
from data_types_formatted_output.class_work.calculate_f_2 import calculate_f_2
from data_types_formatted_output.class_work.calculate_remainder import calculate_remainder
from data_types_formatted_output.class_work.speed import find_speed_in_m_s
from data_types_formatted_output.home_work.first_and_last_digits import swap_first_and_last_digits
from data_types_formatted_output.home_work.glue_numbers_without_last_digits import glue_numbers_without_last_digits
from data_types_formatted_output.home_work.result_of_calculations import get_result_of_calculations
from data_types_formatted_output.home_work.lag_time import find_lag_time
from data_types_formatted_output.home_work.packages_for_bottles import find_number_of_packages
from data_types_formatted_output.home_work.probability_2_white_balls import probability_of_two_white_balls
from data_types_formatted_output.home_work.calculate_time import calculate_time
from data_types_formatted_output.home_work.sin_cos_tg_of_angle import calculate_sin_cos_tg_of_angle


@mark.parametrize(
    "test_input,test_result_if_a_in_radians,test_result_if_a_in_degrees",
    [(3, -0.28367, 0.00007), (10, 1.19238, 0.00268), (100, -0.08085, -6.65609)]
)
def test_calculate_f_1(test_input, test_result_if_a_in_radians, test_result_if_a_in_degrees):
    assert calculate_f_1(test_input) == test_result_if_a_in_radians
    assert calculate_f_1(test_input, True) == test_result_if_a_in_degrees


@mark.parametrize(
    "test_input,test_result",
    [((472, 15), 7), ((100, 3), 1), ((999, 25), 24)],
)
def test_calculate_remainder(test_input, test_result):
    assert calculate_remainder(*test_input) == test_result


@mark.parametrize(
    "test_input,test_result",
    [((1, 60), 16.667), ((5, 237), 13.167), ((10, 543), 15.083)],
)
def test_speed_in_m_s(test_input, test_result):
    assert round(find_speed_in_m_s(*test_input), 3) == test_result


@mark.parametrize(
    "test_input,test_result",
    [(45, 0.534), (-100, 4.848), (360, 0.135)],
)
def test_calculate_f_2(test_input, test_result):
    assert round(calculate_f_2(test_input), 3) == test_result


@mark.parametrize(
    "test_input,test_result",
    [(123, 321), (450, 54), (987, 789)],
)
def test_first_and_last_digits(test_input, test_result):
    assert swap_first_and_last_digits(test_input) == test_result


@mark.parametrize(
    "test_input,test_result",
    [((123, 456), 1245), ((100, 200), 1020), ((999, 707), 9970)],
)
def test_glue_numbers_without_last_digits(test_input, test_result):
    assert glue_numbers_without_last_digits(*test_input) == test_result


@mark.parametrize(
    "test_input,test_result",
    [((234, 3, 12), 942641.483), ((100, 2, 5), 158489319.246), ((999, 2, 20), 999.500)],
)
def test_result_of_calculations(test_input, test_result):
    assert round(get_result_of_calculations(*test_input), 3) == test_result


@mark.parametrize(
    "test_input,test_result",
    [((2, 33, 14, 2, 34, 15), 61), ((1, 17, 31, 2, 18, 24), 3653), ((4, 27, 44, 4, 28, 13), 29)],
)
def test_lag_time(test_input, test_result):
    assert find_lag_time(*test_input) == test_result


@mark.parametrize(
    "test_input,test_result",
    [((16, 5), 4), ((22, 4), 6), ((35, 7), 5)],
)
def test_packages_for_bottles(test_input, test_result):
    assert find_number_of_packages(*test_input) == test_result


@mark.parametrize(
    "test_input,test_result",
    [((7, 10), 15.44), ((22, 30), 17.42), ((5, 2), 47.62)]
)
def test_probability_2_white_balls(test_input, test_result):
    assert round(probability_of_two_white_balls(*test_input), 2) == test_result


@mark.parametrize(
    "test_input,test_result",
    [(3665,( 61, 1, 5, 1)), (86400, (1440, 24, 0, 0)), (3500, (58, 0, 20, 58))]
)
def test_calculate_time(test_input, test_result):
    assert calculate_time(test_input) == test_result


@mark.parametrize(
    "test_input,test_result",
    [
        ((68, 56, 6), (1.20, 0.93, 0.36, 2.60)),
        ((-100, 30, 30), (-1.74, -0.99, -0.16, 5.98)),
        ((360, 59, 59), (6.30, 0.02, 1.00, 0.02)),
    ],
)
def test_sin_cos_tg_of_angle(test_input, test_result):
    assert calculate_sin_cos_tg_of_angle(*test_input) == test_result
