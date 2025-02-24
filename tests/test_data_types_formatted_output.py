from pytest import mark, raises

from data_types_formatted_output import (
    calculate_time,
    calculate_remainder,
    calculate_expression1,
    ExpressionValues1,
    calculate_expression2,
    ExpressionValue,
    calculate_sin_cos_tg_of_angle,
    find_lag_time,
    get_speed_in_ms,
    find_number_of_packages,
    swap_first_and_last_digits,
    get_result_of_calculations,
    probability_of_two_white_balls,
    glue_numbers_without_last_digits,
    ValuesForCalculatingRemainder,
    ValuesForFindingSpeed,
    TimeInSeconds,
    ThreeDigitNumber,
    ThreeDigitNumbers,
    TimeValues,
    BottleValues,
    BallsValues,
    ValuesForCalculation,
    DegreeValues,
)


@mark.parametrize(
    "angle_value,result_if_a_in_radians,result_if_a_in_degrees",


    [(3, -0.28367, 0.00007), (10, 1.19238, 0.00268), (100, -0.08085, -6.65609)]
)
def test_calculate_expression1(angle_value, result_if_a_in_radians, result_if_a_in_degrees):
    assert calculate_expression1(
        ExpressionValues1(angle_value=angle_value)
    ) == result_if_a_in_radians
    assert calculate_expression1(
        ExpressionValues1(angle_value=angle_value, in_degrees=True)
    ) == result_if_a_in_degrees


@mark.parametrize(
    "angle_value,in_degrees,message",
    [
        ("a", True, '\nangle_value\n  Input should be a valid integer'),
        (1.111, True, '\nangle_value\n  Input should be a valid integer'),
        (1, "a", '\nin_degrees\n  Input should be a valid boolean'),
    ]
)
def test_calculate_expression1_value_error(angle_value, in_degrees, message):
    with raises(ValueError, match=message):
        ExpressionValues1(angle_value=angle_value, in_degrees=in_degrees)


@mark.parametrize(
    "number,divider,result",
    [(472, 15, 7), (100, 3, 1), (999, 25, 24)],
)
def test_calculate_remainder(number, divider, result):
    assert calculate_remainder(
        ValuesForCalculatingRemainder(number=number, divider=divider)
    ) == result


@mark.parametrize(
    "number,divider,message",
    [
        ("a", 2, '\nnumber\n  Input should be a valid integer'),
        (2, "a", '\ndivider\n  Input should be a valid integer'),
        (0, 2, "\nnumber\n  Input should be greater than 0"),
        (2, -2, "\ndivider\n  Input should be greater than 0"),
    ]
)
def test_calculate_remainder_value_error(number, divider, message):
    with raises(ValueError, match=message):
        ValuesForCalculatingRemainder(number=number, divider=divider)


@mark.parametrize(
    "time,distance,speed",
    [(1, 60, 16.667), (5, 237, 13.167), (10, 543, 15.083)],
)
def test_speed_in_m_s(time, distance, speed):
    assert round(get_speed_in_ms(
        ValuesForFindingSpeed(time=time, distance=distance)
    ), 3) == speed


@mark.parametrize(
    "time,distance,message",
    [
        ("a", 10, '\ntime\n  Input should be a valid integer'),
        (1, "a", '\ndistance\n  Input should be a valid integer'),
        (0, 10, "\ntime\n  Input should be greater than 0"),
        (1, -10, "\ndistance\n  Input should be greater than 0"),
    ]
)
def test_speed_in_m_s_value_error(time, distance, message):
    with raises(ValueError, match=message):
        ValuesForFindingSpeed(time=time, distance=distance)


@mark.parametrize(
    "angle_value,result",
    [(45, 0.534), (-100, 4.848), (360, -0.135)],
)
def test_calculate_expression2(angle_value, result):
    assert round(calculate_expression2(
        ExpressionValue(angle_value=angle_value)
    ), 3) == result


@mark.parametrize(
    "angle_value,message",
    [
        ("a", '\nangle_value\n  Input should be a valid integer'),
        (1.111, '\nangle_value\n  Input should be a valid integer'),
        ([1], '\nangle_value\n  Input should be a valid integer'),
    ]
)
def test_calculate_expression2_value_error(angle_value, message):
    with raises(ValueError, match=message):
        ExpressionValue(angle_value=angle_value)


@mark.parametrize(
    "number,result",
    [(123, 321), (450, 54), (987, 789)],
)
def test_first_and_last_digits(number, result):
    assert swap_first_and_last_digits(
        ThreeDigitNumber(number=number)
    ) == result


@mark.parametrize(
    "number,message",
    [
        ("a", '\nnumber\n  Input should be a valid integer'),
        (100.111, '\nnumber\n  Input should be a valid integer'),
        (99, '\nnumber\n  Input should be greater than or equal to 100'),
        (1000, '\nnumber\n  Input should be less than or equal to 999')
    ]
)
def test_first_and_last_digits_value_error(number, message):
    with raises(ValueError, match=message):
        ThreeDigitNumber(number=number)


@mark.parametrize(
    "number1,number2,result",
    [(123, 456, 1245), (100, 200, 1020), (999, 707, 9970)],
)
def test_glue_numbers_without_last_digits(number1, number2, result):
    assert glue_numbers_without_last_digits(
        ThreeDigitNumbers(number1=number1, number2=number2)
    ) == result


@mark.parametrize(
    "number1,number2,message",
    [
        ("a", 100, '\nnumber1\n  Input should be a valid integer'),
        (100, 100.111, '\nnumber2\n  Input should be a valid integer'),
        (99, 100, '\nnumber1\n  Input should be greater than or equal to 100'),
        (100, 1000, '\nnumber2\n  Input should be less than or equal to 999')
    ]
)
def test_glue_numbers_without_last_digits_value_error(number1, number2, message):
    with raises(ValueError, match=message):
        ThreeDigitNumbers(number1=number1, number2=number2)


@mark.parametrize(
    "number,count_of_times,power,result",
    [(234, 3, 12, 942641.483), (100, 2, 5, 158489319.246), (999, 2, 20, 999.500)],
)
def test_result_of_calculations(number, count_of_times, power, result):
    assert round(get_result_of_calculations(
        ValuesForCalculation(number=number, count_of_times=count_of_times, power=power)
    ), 3) == result


@mark.parametrize(
    "number,count_of_times,power,message",
    [
        ("a", 1, 1, "\nnumber\n  Input should be a valid integer"),
        (100, "a", 1, "\ncount_of_times\n  Input should be a valid integer"),
        (100, 1, "a", "\npower\n  Input should be a valid integer"),
        (10, 1, 1, "\nnumber\n  Input should be greater than or equal to 100"),
        (1000, 1, 1, "\nnumber\n  Input should be less than or equal to 999"),
        (100, -1, 1, "\ncount_of_times\n  Input should be greater than 0"),
        (100, 1, -1, "\npower\n  Input should be greater than 0"),
    ]
)
def test_result_of_calculations_value_error(number, count_of_times, power, message):
    with raises(ValueError, match=message):
        ValuesForCalculation(number=number, count_of_times=count_of_times, power=power)


@mark.parametrize(
    "hr_1,min_1,sec_1,hr_2,min_2,sec_2,lag_time",
    [(2, 33, 14, 2, 34, 15, 61), (1, 17, 31, 2, 18, 24, 3653), (4, 27, 44, 4, 28, 13, 29)],
)
def test_lag_time(hr_1, min_1, sec_1, hr_2, min_2, sec_2, lag_time):
    assert find_lag_time(
        TimeValues(
            hr_1=hr_1, min_1=min_1, sec_1=sec_1,
            hr_2=hr_2, min_2=min_2, sec_2=sec_2
        )
    ) == lag_time


@mark.parametrize(
    "hr_1,min_1,sec_1,hr_2,min_2,sec_2,message",
    [
        (1, 1, 1, "a", 1, 1, '\nhr_2\n  Input should be a valid integer'),
        (1, 1, -1, 1, 1, 1, "\nsec_1\n  Input should be greater than or equal to 0"),
        (1, 1, 1, 1, 1, 90, "\nsec_2\n  Input should be less than or equal to 59"),
        (1, 1, 3, 1, 1, 1, "Time of winner cannot be greater than time of next opponent"),
    ]
)
def test_lag_time_value_error(hr_1, min_1, sec_1, hr_2, min_2, sec_2, message):
    with raises(ValueError, match=message):
        TimeValues(
            hr_1=hr_1, min_1=min_1, sec_1=sec_1,
            hr_2=hr_2, min_2=min_2, sec_2=sec_2
        )


@mark.parametrize(
    "number_of_bottles,one_package_hold,result",
    [(16, 5, 4), (22, 4, 6), (35, 7, 5)],
)
def test_packages_for_bottles(number_of_bottles, one_package_hold, result):
    assert find_number_of_packages(
        BottleValues(number_of_bottles=number_of_bottles, one_package_hold=one_package_hold)
    ) == result


@mark.parametrize(
    "number_of_bottles,one_package_hold,message",
    [
        ("a", 10, '\nnumber_of_bottles\n  Input should be a valid integer'),
        (20, 10.111, '\none_package_hold\n  Input should be a valid integer'),
        (0, 100, '\nnumber_of_bottles\n  Input should be greater than 0'),
        (20, -10, '\none_package_hold\n  Input should be greater than 0')
    ]
)
def test_packages_for_bottles_value_error(number_of_bottles, one_package_hold, message):
    with raises(ValueError, match=message):
        BottleValues(number_of_bottles=number_of_bottles, one_package_hold=one_package_hold)


@mark.parametrize(
    "count_of_white_balls,count_of_black_balls,result",
    [(7, 10, 15.44), (22, 30, 17.42), (5, 2, 47.62)]
)
def test_probability_2_white_balls(count_of_white_balls, count_of_black_balls, result):
    assert round(probability_of_two_white_balls(
        BallsValues(
            count_of_white_balls=count_of_white_balls,
            count_of_black_balls=count_of_black_balls
        )
    ), 2) == result


@mark.parametrize(
    "count_of_white_balls,count_of_black_balls,message",
    [
        ("a", 1, "\ncount_of_white_balls\n  Input should be a valid integer"),
        (2, 1.111, "\ncount_of_black_balls\n  Input should be a valid integer"),
        (1, 1, "\ncount_of_white_balls\n  Input should be greater than or equal to 2"),
        (2, -1, "\ncount_of_black_balls\n  Input should be greater than or equal to 0")
    ]
)
def test_probability_2_white_balls_value_error(count_of_white_balls, count_of_black_balls, message):
    with raises(ValueError, match=message):
        BallsValues(
            count_of_white_balls=count_of_white_balls,
            count_of_black_balls=count_of_black_balls
        )


@mark.parametrize(
    "time_in_seconds,full_min,full_hr,remain_sec,remain_min",
    [(3665, 61, 1, 5, 1), (86400, 1440, 24, 0, 0), (3500, 58, 0, 20, 58)]
)
def test_calculate_time(time_in_seconds, full_min, full_hr, remain_sec, remain_min):
    assert calculate_time(
        TimeInSeconds(time_in_seconds=time_in_seconds)
    ) == (full_min, full_hr, remain_sec, remain_min)


@mark.parametrize(
    "time_in_seconds,message",
    [
        ("a", '\ntime_in_seconds\n  Input should be a valid integer'),
        (1.111, '\ntime_in_seconds\n  Input should be a valid integer'),
        (-1, '\ntime_in_seconds\n  Input should be greater than or equal to 0'),
        (87400, '\ntime_in_seconds\n  Input should be less than or equal to 86400')
    ]
)
def test_calculate_time_value_error(time_in_seconds, message):
    with raises(ValueError, match=message):
        TimeInSeconds(time_in_seconds=time_in_seconds)


@mark.parametrize(
    "degrees,minutes,seconds,rad,sin,cos,tan",
    [
        (68, 56, 6, 1.20, 0.93, 0.36, 2.60),
        (-100, 30, 30, -1.74, -0.99, -0.16, 5.98),
        (360, 59, 59, 6.30, 0.02, 1.00, 0.02),
    ],
)
def test_sin_cos_tg_of_angle(degrees, minutes, seconds, rad, sin, cos, tan):
    assert calculate_sin_cos_tg_of_angle(
        DegreeValues(degrees=degrees, minutes=minutes, seconds=seconds)
    ) == (rad, sin, cos, tan)


@mark.parametrize(
    "degrees,minutes,seconds,message",
    [
        (100, "a", 10, "\nminutes\n  Input should be a valid integer"),
        (100, 100, 10, "\nminutes\n  Input should be less than or equal to 59"),
        (100, 10, -10, "\nseconds\n  Input should be greater than or equal to 0"),
    ]
)
def test_sin_cos_tg_of_angle_value_error(degrees, minutes, seconds, message):
    with raises(ValueError, match=message):
        DegreeValues(degrees=degrees, minutes=minutes, seconds=seconds)
