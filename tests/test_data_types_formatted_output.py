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


def test_calculate_f_1():
    assert calculate_f_1(3) == -0.28367
    assert calculate_f_1(3, True) == 0.00007
    assert calculate_f_1(10) == 1.19238
    assert calculate_f_1(10, True) == 0.00268
    assert calculate_f_1(100) == -0.08085
    assert calculate_f_1(100, True) == -6.65609


def test_calculate_remainder():
    assert calculate_remainder(472, 15) == 7
    assert calculate_remainder(100, 3) == 1
    assert calculate_remainder(999, 25) == 24


def test_speed_in_m_s():
    assert round(find_speed_in_m_s(1, 60), 3) == 16.667
    assert round(find_speed_in_m_s(5, 237), 3) == 13.167
    assert round(find_speed_in_m_s(10, 543), 3) == 15.083


def test_calculate_f_2():
    assert round(calculate_f_2(45), 3) == 0.534
    assert round(calculate_f_2(-100), 3) == 4.848
    assert round(calculate_f_2(360), 3) == 0.135


def test_first_and_last_digits():
    assert swap_first_and_last_digits(123) == 321
    assert swap_first_and_last_digits(450) == 54
    assert swap_first_and_last_digits(987) == 789


def test_glue_numbers_without_last_digits():
    assert glue_numbers_without_last_digits(123, 456) == 1245
    assert glue_numbers_without_last_digits(100, 200) == 1020
    assert glue_numbers_without_last_digits(999, 707) == 9970


def test_result_of_calculations():
    assert round(get_result_of_calculations(234, 3, 12), 3) == 942641.483
    assert round(get_result_of_calculations(100, 2, 5), 3) == 158489319.246
    assert round(get_result_of_calculations(999, 2, 20), 3) == 999.500


def test_lag_time():
    assert find_lag_time(2, 33, 14, 2, 34, 15) == 61
    assert find_lag_time(1, 17, 31, 2, 18, 24) == 3653
    assert find_lag_time(4, 27, 44, 4, 28, 13) == 29


def test_packages_for_bottles():
    assert find_number_of_packages(16, 5) == 4
    assert find_number_of_packages(22, 4) == 6
    assert find_number_of_packages(35,7) == 5


def test_probability_2_white_balls():
    assert round(probability_of_two_white_balls(7, 10), 2) == 15.44
    assert round(probability_of_two_white_balls(22, 30), 2) == 17.42
    assert round(probability_of_two_white_balls(5, 2), 2) == 47.62


def test_calculate_time():
    assert calculate_time(3665) == (61, 1, 5, 1)
    assert calculate_time(86400) == (1440, 24, 0, 0)
    assert calculate_time(3500) == (58, 0, 20, 58)


def test_sin_cos_tg_of_angle():
    assert calculate_sin_cos_tg_of_angle(68, 56, 6) == (1.20, 0.93, 0.36, 2.60)
    assert calculate_sin_cos_tg_of_angle(-100, 30, 30) == (-1.74, -0.99, -0.16, 5.98)
    assert calculate_sin_cos_tg_of_angle(360, 59, 59) == (6.30, 0.02, 1.00, 0.02)
