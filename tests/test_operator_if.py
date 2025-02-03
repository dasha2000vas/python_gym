from pytest import mark

from operator_if import *


@mark.parametrize(
    "num1,num2,num3,count",
    [(-5, -10, -15, 3), (-5, 0, 5, 1), (5, 10, 15, 0)]
)
def test_count_of_negative_and_multiples_of_5(num1, num2, num3, count):
    assert count_of_negative_and_multiples_of_five(num1, num2, num3) == count


@mark.parametrize(
    "a,b,c,result",
    [
        (4, 4, 4, "Triangle exists"),
        (3, 5, 7, "Triangle exists"),
        (3, 5, 10, "Triangle does not exist")
    ]
)
def test_is_triangle_exist(a, b, c, result):
    assert is_triangle_exist(a, b, c) == result


@mark.parametrize(
    "year,result",
    [(2000, "is leap year"), (2024, "is leap year"), (1900, "is ordinary year")]
)
def test_leap_year(year, result):
    assert is_year_leap(year) == result


@mark.parametrize(
    "num1,num2,num3,min_num",
    [(1, 2, 3, 1), (5, -5, 4, -5), (2, 1, 0, 0)],
)
def test_min_number(num1, num2, num3, min_num):
    assert find_min_number(num1, num2, num3) == min_num


@mark.parametrize(
    "num1,num2,result",
    [
        (2, -2, "There are positive even numbers"),
        (1, 4, "There are positive even numbers"),
        (1, 5, "There are no positive even numbers"),
    ]
)
def test_positive_even_number(num1, num2, result):
    assert is_there_positive_even_number(num1, num2) == result


@mark.parametrize(
    "num1,num2,num3,result",
    [(6, 12, 18, 30), (0, 9, 18, 18), (15, 21, 27, 0)]
)
def test_sum_of_even_two_digit_multiples_of_3(num1, num2, num3, result):
    assert sum_of_even_two_digit_multiples_of_three(num1, num2, num3) == result


@mark.parametrize(
    "num1,num2,num3,result",
    [(1, 2, 3, 6), (-1, 0, 1, 1), (-2, -1, 0, 0)]
)
def test_sum_of_positive_numbers(num1, num2, num3, result):
    assert sum_of_positive_numbers(num1, num2, num3) == result


@mark.parametrize(
    "num1,num2,num3,result_for_one,result_for_all",
    [
        (1, 111, 222, True, False),
        (111, 222, 333, True, True),
        (1, 2, 3, False, False)
    ]
)
def test_three_digit_numbers(num1, num2, num3, result_for_one, result_for_all):
    assert one_three_digit_number(num1, num2, num3) == result_for_one
    assert all_three_digit_numbers(num1, num2, num3) == result_for_all


@mark.parametrize(
    "num1,num2,result",
    [(111, 221, True), (11, 111, False), (11, 21, False)]
)
def test_three_digit_with_end_1(num1, num2, result):
    assert three_digit_with_end_one(num1, num2) == result


@mark.parametrize(
    "num1,num2,result",
    [(107, 207, True), (107, 10, True), (17, 27, False)]
)
def test_three_digit_with_end_7(num1, num2, result):
    assert three_digit_with_end_seven(num1, num2) == result


@mark.parametrize(
    "number,result",
    [(10, 10), (-10, 10), (0, 0)]
)
def test_absolute_value(number, result):
    assert get_absolute_value(number) == result


@mark.parametrize(
    "x,y,area",
    [
        (0, 0, "origin of coordinates"),
        (0, 10, "y-axis"),
        (10, 0, "x-axis"),
        (10, 10, "first quarter"),
        (-10, 10, "second quarter"),
        (-10, -10, "third quarter"),
        (10, -10, "fourth quarter"),
    ]
)
def test_area_with_dot(x, y, area):
    assert get_area_with_dot(x, y) == area


@mark.parametrize(
    "x1,y1,x2,y2,result",
    [(3, 2, 6, 5, True), (6, 2, 3, 5, True), (2, 2, 4, 7, False)]
)
def test_bishop_move(x1, y1, x2, y2, result):
    assert is_enough_one_bishop_move(x1, y1, x2, y2) == result


@mark.parametrize(
    "x,y,color",
    [(1, 1, "black"), (2, 2, "black"), (2, 3, "white"), (3, 6, "white")]
)
def test_cell_color(x, y, color):
    assert get_cell_color(x, y) == color


@mark.parametrize(
    "name,result",
    [("Dasha", "Welcome, Dasha"), ("Ilya", "Welcome, Ilya"), ("", "Please log in")],
)
def test_greeting(name, result):
    assert greeting(name) == result


@mark.parametrize(
    "num1,num2,num3,result",
    [(-1, 0, 1, "Hooray!"), (3, -3, 10, ""), (6, 8, 10, "")],
)
def test_hooray(num1, num2, num3, result):
    assert belong_to_range(num1, num2, num3) == result


@mark.parametrize(
    "num1,num2,num3,result",
    [(2, 4, 6, True), (-2, 2, 1, True), (-1, 0, 1, False)],
)
def test_positive_even_number(num1, num2, num3, result):
    assert one_positive_even_number(num1, num2, num3) == result


@mark.parametrize(
    "number,result",
    [(1001, "Yes"), (7777, "Yes"), (1234, "No")],
)
def test_read_from_left_and_right(number, result):
    assert read_same_from_left_and_right(number) == result


@mark.parametrize(
    "x1,y1,x2,y2,result",
    [(3, 2, 3, 7, True), (8, 5, 3, 5, True), (7, 2, 2, 5, False)],
)
def test_rook_move(x1, y1, x2, y2, result):
    assert is_enough_one_rook_move(x1, y1, x2, y2) == result


@mark.parametrize(
    "number,result",
    [(100, True), (500, True), (999, False)],
)
def test_three_digit_even_number(number, result):
    assert is_three_digit_even(number) == result
