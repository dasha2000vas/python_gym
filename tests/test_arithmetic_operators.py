from arithmetic_operators.home_work.сelsius_to_fahrenheit import calculate_temperature_in_fahrenheit
from arithmetic_operators.home_work.perimeter_and_square_of_triangle import find_perimeter_and_square
from arithmetic_operators.home_work.leftmost_digit_to_right_end import move_leftmost_digit_to_right_end
from arithmetic_operators.home_work.third_digit_from_end import define_third_digit_from_end
from arithmetic_operators.home_work.glue_numbers import glue_numbers
from arithmetic_operators.home_work.sum_of_digits import sum_of_digits
from arithmetic_operators.home_work.count_of_square_in_rectangle import find_count_of_square_in_rectangle
from arithmetic_operators.home_work.find_b_in_a import find_b_in_a
from arithmetic_operators.home_work.cost_in_rubles_and_kopecks import find_cost_in_rubles_and_kopecks
from arithmetic_operators.home_work.count_value import count_value
from arithmetic_operators.home_work.count_of_cabins import count_of_cabins
from arithmetic_operators.home_work.count_of_desks import calculate_count_of_desks
from arithmetic_operators.home_work.calculate_1 import calculate_1
from arithmetic_operators.home_work.calculate_2 import calculate_2


def test_сelsius_to_fahrenheit():
    assert calculate_temperature_in_fahrenheit(25) == 77
    assert calculate_temperature_in_fahrenheit(40) == 104
    assert calculate_temperature_in_fahrenheit(60) == 140


def test_perimeter_and_square_of_triangle():
    perimeter, square = find_perimeter_and_square(2, 3, 6, 1, 4, 8)
    assert perimeter == 16.22
    assert square == 2.5
    perimeter, square = find_perimeter_and_square(1, 4, 7, 3, 5, 10)
    assert perimeter == 18.66
    assert square == 4.5
    perimeter, square = find_perimeter_and_square(1, 5, 9, 1, 5, 7)
    assert perimeter == 20.13
    assert square == 4


def test_leftmost_digit_to_right_end():
    assert move_leftmost_digit_to_right_end(237) == 372
    assert move_leftmost_digit_to_right_end(340) == 403
    assert move_leftmost_digit_to_right_end(572) == 725


def test_third_digit_from_end():
    assert define_third_digit_from_end(130985) == 9
    assert define_third_digit_from_end(24024057) == 0
    assert define_third_digit_from_end(321) == 3


def test_glue_numbers():
    assert glue_numbers(100, 500) == 100500
    assert glue_numbers(123, 456) == 123456
    assert glue_numbers(987, 654) == 987654


def test_sum_of_digits():
    assert sum_of_digits(111) == 3
    assert sum_of_digits(123) == 6
    assert sum_of_digits(999) == 27


def test_count_of_square_in_rectangle():
    count, remain = find_count_of_square_in_rectangle(11, 7, 3)
    assert count == 6
    assert remain == 23
    count, remain = find_count_of_square_in_rectangle(9, 16, 4)
    assert count == 8
    assert remain == 16
    count, remain = find_count_of_square_in_rectangle(21, 24, 20)
    assert count == 1
    assert remain == 104



def test_find_b_in_a():
    count, remain = find_b_in_a(20, 3)
    assert count == 6
    assert remain == 2
    count, remain = find_b_in_a(123, 4)
    assert count == 30
    assert remain == 3
    count, remain = find_b_in_a(987, 56)
    assert count == 17
    assert remain == 35



def test_cost_in_rubles_and_kopecks():
    r, k = find_cost_in_rubles_and_kopecks(453)
    assert r == 4
    assert k == 53
    r, k = find_cost_in_rubles_and_kopecks(3483)
    assert r == 34
    assert k == 83
    r, k = find_cost_in_rubles_and_kopecks(98765)
    assert r == 987
    assert k == 65


def test_count_value():
    assert count_value(3, 5, 33, 77) == 44.998
    assert count_value(2, 3, 4, 5) == 17.8
    assert count_value(6, 7, 11, 22) == 125.983


def test_count_of_cabins():
    assert count_of_cabins(8, 20) == 24
    assert count_of_cabins(1, 5) == 8
    assert count_of_cabins(4, 22) == 36


def test_count_of_desks():
    assert calculate_count_of_desks(21, 19, 17) == 30
    assert calculate_count_of_desks(11, 15, 23) == 26
    assert calculate_count_of_desks(19, 25, 22) == 34


def test_calculate_1():
    assert calculate_1(12, 45) == 117835.745
    assert calculate_1(12, 45, True) == 81375.794
    assert calculate_1(5, 20) == 121.555
    assert calculate_1(5, 20, True) == 16.697
    assert calculate_1(2, 30) == 3.213
    assert calculate_1(2, 30, True) == 1.636


def test_calculate_2():
    assert calculate_2(22, 1, 44, 27, 30) == 3499615212.824
    assert calculate_2(22, 1, 44, 27, 30, True) == 896228237.135
    assert calculate_2(2, 3, 4, 5, 6) == 3.996
    assert calculate_2(2, 3, 4, 5, 6, True) == 3.5
    assert calculate_2(11, 12, 13, 14, 15) == 25329.783
    assert calculate_2(11, 12, 13, 14, 15, True) == 4021.356
