from pytest import raises, mark

from lesson_10 import (
    write_string_n_times,
    congratulation,
    get_hypotenuse,
    is_number_equal_to_its_sum_of_cubes_of_digits,
    get_cylinder_area,
    get_roots_count,
    get_sum_of_series,
    get_sum_of_series2,
    get_sum_of_harmonic_series,
    max_number_of_two,
    max_number_of_four,
    max_number_of_three,
    find_num_which_fact_is_less_than_n,
    get_max_digit_in_number,
    is_number_in_range,
    simple_calculator,
)


@mark.parametrize(
    "entered_str,n,result",
    [
        ("cat", 3, "catcatcat"),
        ("taco", 5, "tacotacotacotacotaco"),
        ("1->2", 2, "1->21->2"),
    ]
)
def test_write_string_n_times(entered_str, n, result):
    assert write_string_n_times(entered_str, n) == result


@mark.parametrize(
    "entered_str,n,message",
    [
        (10, 2, "Entered string must be of type str"),
        (["10"], 2, "Entered string must be of type str"),
        ("10", "2", "n must be of type int"),
        ("10", -2, "n must be positive"),
    ]
)
def test_write_string_n_times_value_error(entered_str, n, message):
    with raises(ValueError, match=message):
        write_string_n_times(entered_str, n)


@mark.parametrize(
    "name,n,result",
    [
        ("dasha", 1, "Hi, Dasha! Happy New Year!\n"),
        (
            "rONY",
            2,
            ("Hi, Rony! Happy New Year!\n"
             "Hi, Rony! Happy New Year!\n")
        ),
        (
            "TrIxIe",
            3,
            ("Hi, Trixie! Happy New Year!\n"
             "Hi, Trixie! Happy New Year!\n"
             "Hi, Trixie! Happy New Year!\n")
        ),
    ]
)
def test_congratulation(name, n, result):
    assert congratulation(name, n) == result


@mark.parametrize(
    "name,n,message",
    [
        (10, 2,'Name must be of type str'),
        ("dasha123", 2, "Name must contain only letters"),
        ("dasha", "2", 'n must be of type int'),
        ("dasha", -2, "n must be positive"),
    ]
)
def test_congratulation_value_error(name, n, message):
    with raises(ValueError, match=message):
        congratulation(name, n)


@mark.parametrize(
    "leg1,leg2,hypotenuse",
    [
        (66, 88, 110.0),
        (32, 71, 77.878),
        (17, 53, 55.66),
    ]
)
def test_get_hypotenuse(leg1, leg2, hypotenuse):
    assert get_hypotenuse(leg1, leg2) == hypotenuse


@mark.parametrize(
    "leg1,leg2,message",
    [
        ("10", 10, "Legs must be integers"),
        (10, "10", "Legs must be integers"),
        (-10, 10, "Legs must be positive"),
        (10, -10, "Legs must be positive")
    ]
)
def test_get_hypotenuse_value_error(leg1, leg2, message):
    with raises(ValueError, match=message):
        get_hypotenuse(leg1, leg2)


@mark.parametrize(
    "num,result",
    [
        (153, True),
        (370, True),
        (424, False),
    ]
)
def test_sum_of_cubes_of_digits(num, result):
    assert is_number_equal_to_its_sum_of_cubes_of_digits(num) == result


@mark.parametrize(
    "num,message",
    [
        ("10", 'Number must be of type int'),
        (10.111, 'Number must be of type int'),
        (-10, 'Number must be positive'),
    ]
)
def test_sum_of_cubes_of_digits_value_error(num, message):
    with raises(ValueError, match=message):
        is_number_equal_to_its_sum_of_cubes_of_digits(num)


@mark.parametrize(
    "height,radius,mode,area",
    [
        (5, 2, "", None),
        (5, 2, "side", "Side surface area is 62.832"),
        (5, 2, "all", "Area of entire surface is 87.965"),
    ]
)
def test_get_cylinder_area(height, radius, mode, area):
    assert get_cylinder_area(height, radius, mode) == area


@mark.parametrize(
    "height,radius,mode,message",
    [
        ("5", 2, "", "Height and radius must be of type int"),
        (5, "2", "", "Height and radius must be of type int"),
        (-5, 2, "", "Height and radius must be greater than zero"),
        (5, -2, "", "Height and radius must be greater than zero"),
        (5, 2, "abracadabra", "Invalid mode. Modes are")
    ]
)
def test_get_cylinder_area_value_error(height, radius, mode, message):
    with raises(ValueError, match=message):
        get_cylinder_area(height, radius, mode)


@mark.parametrize(
    "a,b,c,result",
    [
        (4.420, 8.507, 0.385, "Equation has two roots"),
        (7.817, -5.320, 4.160, "Equation has no roots"),
        (16.0, 8.0, 1.0, "Equation has one root"),
    ]
)
def test_get_roots_count(a, b, c, result):
    assert get_roots_count(a, b, c) == result


@mark.parametrize(
    "a,b,c,message",
    [
        (1, 1.0, 1.0, 'All numbers must be float'),
        (1.0, "1.0", 1.0, 'All numbers must be float'),
        (1.0, 1.0, [1.0], 'All numbers must be float'),
        (0.0, 1.0, 1.0, "a cannot be zero")
    ]
)
def test_get_roots_count_value_error(a, b, c, message):
    with raises(ValueError, match=message):
        get_roots_count(a, b, c)


@mark.parametrize(
    "n,h,result",
    [
        (5, 2, 6.267),
        (2, 1, 1.5),
        (8, 10, 7329.841),
    ]
)
def test_sum_of_series(n, h, result):
    assert get_sum_of_series(n, h) == result


@mark.parametrize(
    "n,h,message",
    [
        ("1", 1, "All args must be integers"),
        (1, "1", "All args must be integers"),
        (-1, 1, 'n must be positive'),
        (1, 0, 'h cannot be zero'),
    ]
)
def test_sum_of_series_value_error(n, h, message):
    with raises(ValueError, match=message):
        get_sum_of_series(n, h)


@mark.parametrize(
    "n,h,x,result",
    [
        (7, 2, 1, 0.135),
        (6, -6, 1, -42.195),
        (5, 3, 14, -0.052),
    ]
)
def test_sum_of_series2(n, h, x, result):
    assert get_sum_of_series2(n, h, x) == result


@mark.parametrize(
    "n,h,x,message",
    [
        ("1", 1, 1, 'All args must be integers'),
        (1, 1.111, 1, 'All args must be integers'),
        (1, 1, [1], 'All args must be integers'),
        (-1, 1, 1, 'n must be positive'),
        (1, 0, 1, 'h cannot be zero')
    ]
)
def test_sum_of_series2_value_error(n, h, x, message):
    with raises(ValueError, match=message):
        get_sum_of_series2(n, h, x)


@mark.parametrize(
    "n,result",
    [
        (4, 2.083),
        (81, 4.978),
        (11, 3.02),
    ]
)
def test_sum_of_harmonic_series(n, result):
    assert get_sum_of_harmonic_series(n) == result


@mark.parametrize(
    "n,message",
    [
        ("2", 'n must be integer'),
        (1, 'n must grater than 1'),
        (-10, 'n must grater than 1'),
    ]
)
def test_sum_of_harmonic_series_value_error(n, message):
    with raises(ValueError, match=message):
        get_sum_of_harmonic_series(n)


@mark.parametrize(
    "num1,num2,max_num",
    [
        (69, -95, 69),
        (-27, 63, 63),
        (40, 40, 40),
    ]
)
def test_max_number_of_two(num1, num2, max_num):
    assert max_number_of_two(num1, num2) == max_num


@mark.parametrize(
    "num1,num2",
    [
        ("1", 1),
        (1, "1"),
    ]
)
def test_max_number_of_two_value_error(num1, num2):
    with raises(ValueError, match="All args must be integers"):
        max_number_of_two(num1, num2)


@mark.parametrize(
    "num1,num2,num3,max_num",
    [
        (69, -95, 85, 85),
        (-27, 63, 69, 69),
        (40, 40, 30, 40),
    ]
)
def test_max_number_of_three(num1, num2, num3, max_num):
    assert max_number_of_three(num1, num2, num3) == max_num


@mark.parametrize(
    "num1,num2,num3",
    [
        ("1", 1, 1),
        (1, "1", 1),
        (1, 1, "1"),
    ]
)
def test_max_number_of_three_value_error(num1, num2, num3):
    with raises(ValueError, match="All args must be integers"):
        max_number_of_three(num1, num2, num3)


@mark.parametrize(
    "num1,num2,num3,num4,max_num",
    [
        (69, -95, 85, 98, 98),
        (-27, 63, 69, -67, 69),
        (40, 40, 30, 30, 40),
    ]
)
def test_max_number_of_four(num1, num2, num3, num4, max_num):
    assert max_number_of_four(num1, num2, num3, num4) == max_num


@mark.parametrize(
    "num1,num2,num3,num4",
    [
        ("1", 1, 1, 1),
        (1, "1", 1, 1),
        (1, 1, "1", 1),
        (1, 1, 1, "1"),
    ]
)
def test_max_number_of_four_value_error(num1, num2, num3, num4):
    with raises(ValueError, match="All args must be integers"):
        max_number_of_four(num1, num2, num3, num4)


@mark.parametrize(
    "n,result",
    [
        (16, [0, 1, 2, 3]),
        (98, [0, 1, 2, 3, 4]),
        (190, [0, 1, 2, 3, 4, 5]),
    ]
)
def test_num_which_fact_is_less_than_n(n, result):
    assert find_num_which_fact_is_less_than_n(n) == result


@mark.parametrize(
    "n,message",
    [
        ("1", "n must be integer"),
        (0, 'n must be greater than 0'),
        (-1, 'n must be greater than 0'),
    ]
)
def test_num_which_fact_is_less_than_n_value_error(n, message):
    with raises(ValueError, match=message):
        find_num_which_fact_is_less_than_n(n)


@mark.parametrize(
    "num,max_digit",
    [
        (6415, 6),
        (1731, 7),
        (2995, 9),
    ]
)
def test_max_digit_in_number(num, max_digit):
    assert get_max_digit_in_number(num) == max_digit


@mark.parametrize(
    "num,message",
    [
        ("1", "num must be integer"),
        (0, 'num must be positive'),
        (-10, 'num must be positive'),
    ]
)
def test_max_digit_in_number_value_error(num, message):
    with raises(ValueError, match=message):
        get_max_digit_in_number(num)


@mark.parametrize(
    "num,start,end,result",
    [
        (-25, -69, 56, True),
        (-92, -86, -10, False),
        (-9, -23, 67, True),
    ]
)
def test_is_number_in_range(num, start, end, result):
    assert is_number_in_range(num, start, end) == result


@mark.parametrize(
    "num,start,end",
    [
        ("1", 1, 1),
        (1, "1", 1),
        (1, 1, "1"),
    ]
)
def test_is_number_in_range_value_error(num, start, end):
    with raises(ValueError, match="All args must be integers"):
        is_number_in_range(num, start, end)


@mark.parametrize(
    "num1,num2,operation,result",
    [
        (10, 10, "+", 20),
        (10, 10, "-", 0),
        (10, 2, "*", 20),
        (10, 5, "/", 2)
    ]
)
def test_simple_calculator(num1, num2, operation, result):
    assert simple_calculator(num1, num2, operation) == result


@mark.parametrize(
    "num1,num2,operation,message",
    [
        ("10", 10, "-", "Numbers must be of type int"),
        (10, "10", "-", "Numbers must be of type int"),
        (10, 10, "&", "Operation must be one of"),
    ]
)
def test_simple_calculator_value_error(num1, num2, operation, message):
    with raises(ValueError, match=message):
        simple_calculator(num1, num2, operation)
