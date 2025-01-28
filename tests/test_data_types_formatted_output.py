from pytest import mark

from data_types_formatted_output import *


@mark.parametrize(
    "a,result_if_a_in_radians,result_if_a_in_degrees",
    [(3, -0.28367, 0.00007), (10, 1.19238, 0.00268), (100, -0.08085, -6.65609)]
)
def test_calculate_f1(a, result_if_a_in_radians, result_if_a_in_degrees):
    assert calculate_f1(a) == result_if_a_in_radians
    assert calculate_f1(a, True) == result_if_a_in_degrees


@mark.parametrize(
    "n,k,result",
    [(472, 15, 7), (100, 3, 1), (999, 25, 24)],
)
def test_calculate_remainder(n, k, result):
    assert calculate_remainder(n, k) == result


@mark.parametrize(
    "time, distance,speed",
    [(1, 60, 16.667), (5, 237, 13.167), (10, 543, 15.083)],
)
def test_speed_in_m_s(time, distance, speed):
    assert round(find_speed_in_m_s(time, distance), 3) == speed


@mark.parametrize(
    "a,result",
    [(45, 0.534), (-100, 4.848), (360, 0.135)],
)
def test_calculate_f2(a, result):
    assert round(calculate_f2(a), 3) == result


@mark.parametrize(
    "number,result",
    [(123, 321), (450, 54), (987, 789)],
)
def test_first_and_last_digits(number, result):
    assert swap_first_and_last_digits(number) == result


@mark.parametrize(
    "a,b,result",
    [(123, 456, 1245), (100, 200, 1020), (999, 707, 9970)],
)
def test_glue_numbers_without_last_digits(a, b, result):
    assert glue_numbers_without_last_digits(a, b) == result


@mark.parametrize(
    "n,k,m,result",
    [(234, 3, 12, 942641.483), (100, 2, 5, 158489319.246), (999, 2, 20, 999.500)],
)
def test_result_of_calculations(n, k, m, result):
    assert round(get_result_of_calculations(n, k, m), 3) == result


@mark.parametrize(
    "hr_1,min_1,sec_1,hr_2,min_2,sec_2,lag_time",
    [(2, 33, 14, 2, 34, 15, 61), (1, 17, 31, 2, 18, 24, 3653), (4, 27, 44, 4, 28, 13, 29)],
)
def test_lag_time(hr_1, min_1, sec_1, hr_2, min_2, sec_2, lag_time):
    assert find_lag_time(hr_1, min_1, sec_1, hr_2, min_2, sec_2) == lag_time


@mark.parametrize(
    "n,k,result",
    [(16, 5, 4), (22, 4, 6), (35, 7, 5)],
)
def test_packages_for_bottles(n, k, result):
    assert find_number_of_packages(n, k) == result


@mark.parametrize(
    "n,m,result",
    [(7, 10, 15.44), (22, 30, 17.42), (5, 2, 47.62)]
)
def test_probability_2_white_balls(n, m, result):
    assert round(probability_of_two_white_balls(n, m), 2) == result


@mark.parametrize(
    "n,full_min,full_hr,remain_sec,remain_min",
    [(3665, 61, 1, 5, 1), (86400, 1440, 24, 0, 0), (3500, 58, 0, 20, 58)]
)
def test_calculate_time(n, full_min, full_hr, remain_sec, remain_min):
    assert calculate_time(n) == (full_min, full_hr, remain_sec, remain_min)


@mark.parametrize(
    "d,min,sec,rad, sin, cos, tan",
    [
        (68, 56, 6, 1.20, 0.93, 0.36, 2.60),
        (-100, 30, 30, -1.74, -0.99, -0.16, 5.98),
        (360, 59, 59, 6.30, 0.02, 1.00, 0.02),
    ],
)
def test_sin_cos_tg_of_angle(d, min, sec, rad, sin, cos, tan):
    assert calculate_sin_cos_tg_of_angle(d, min, sec) == (rad, sin, cos, tan)
