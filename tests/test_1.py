from arithmetic_operators.task_1 import calculate_temperature_in_fahrenheit
from arithmetic_operators.task_2 import find_perimeter_and_square
from arithmetic_operators.task_3 import move_leftmost_digit_to_right_end
from arithmetic_operators.task_4 import define_third_digit_from_end
from arithmetic_operators.task_5 import glue_numbers
from arithmetic_operators.task_6 import sum_of_digits
from arithmetic_operators.task_7 import find_count_of_square_in_rectangle
from arithmetic_operators.task_8 import find_b_in_a
from arithmetic_operators.task_9 import find_cost_in_rubles_and_kopecks
from arithmetic_operators.task_10 import count_value
from arithmetic_operators.task_11 import count_of_cabins
from arithmetic_operators.task_12 import calculate_count_of_desks
from arithmetic_operators.task_13 import calculate_1
from arithmetic_operators.task_14 import calculate_2


def test_task_1():
    assert calculate_temperature_in_fahrenheit(25) == 77
    assert calculate_temperature_in_fahrenheit(40) == 104
    assert calculate_temperature_in_fahrenheit(60) == 140


def test_task_2():
    perimeter, square = find_perimeter_and_square(2, 3, 6, 1, 4, 8)
    assert perimeter == 16.22
    assert square == 2.5
    perimeter, square = find_perimeter_and_square(1, 4, 7, 3, 5, 10)
    assert perimeter == 18.66
    assert square == 4.5
    perimeter, square = find_perimeter_and_square(1, 5, 9, 1, 5, 7)
    assert perimeter == 20.13
    assert square == 4


def test_task_3():
    assert move_leftmost_digit_to_right_end(237) == 372
    assert move_leftmost_digit_to_right_end(340) == 403
    assert move_leftmost_digit_to_right_end(572) == 725


def test_task_4():
    assert define_third_digit_from_end(130985) == 9
    assert define_third_digit_from_end(24024057) == 0
    assert define_third_digit_from_end(321) == 3


def test_task_5():
    assert glue_numbers(100, 500) == 100500
    assert glue_numbers(123, 456) == 123456
    assert glue_numbers(987, 654) == 987654


def test_task_6():
    assert sum_of_digits(111) == 3
    assert sum_of_digits(123) == 6
    assert sum_of_digits(999) == 27


def test_task_7():
    count, remain = find_count_of_square_in_rectangle(11, 7, 3)
    assert count == 6
    assert remain == 23
    count, remain = find_count_of_square_in_rectangle(9, 16, 4)
    assert count == 8
    assert remain == 16
    count, remain = find_count_of_square_in_rectangle(21, 24, 20)
    assert count == 1
    assert remain == 104



def test_task_8():
    count, remain = find_b_in_a(20, 3)
    assert count == 6
    assert remain == 2
    count, remain = find_b_in_a(123, 4)
    assert count == 30
    assert remain == 3
    count, remain = find_b_in_a(987, 56)
    assert count == 17
    assert remain == 35



def test_task_9():
    r, k = find_cost_in_rubles_and_kopecks(453)
    assert r == 4
    assert k == 53
    r, k = find_cost_in_rubles_and_kopecks(3483)
    assert r == 34
    assert k == 83
    r, k = find_cost_in_rubles_and_kopecks(98765)
    assert r == 987
    assert k == 65


def test_task_10():
    assert count_value(3, 5, 33, 77) == 44.998
    assert count_value(2, 3, 4, 5) == 17.8
    assert count_value(6, 7, 11, 22) == 125.983


def test_task_11():
    assert count_of_cabins(8, 20) == 24
    assert count_of_cabins(1, 5) == 8
    assert count_of_cabins(4, 22) == 36


def test_task_12():
    assert calculate_count_of_desks(21, 19, 17) == 30
    assert calculate_count_of_desks(11, 15, 23) == 26
    assert calculate_count_of_desks(19, 25, 22) == 34


def test_task_13():
    assert calculate_1(12, 45, "n") == 117835.745
    assert calculate_1(12, 45, "y") == 81375.794
    assert calculate_1(5, 20, "n") == 121.555
    assert calculate_1(5, 20, "y") == 16.697
    assert calculate_1(2, 30, "n") == 3.213
    assert calculate_1(2, 30, "y") == 1.636


def test_task_14():
    assert calculate_2(22, 1, 44, 27, 30, "n") == 3499615212.824
    assert calculate_2(22, 1, 44, 27, 30, "y") == 896228237.135
    assert calculate_2(2, 3, 4, 5, 6, "n") == 3.996
    assert calculate_2(2, 3, 4, 5, 6, "y") == 3.5
    assert calculate_2(11, 12, 13, 14, 15, "n") == 25329.783
    assert calculate_2(11, 12, 13, 14, 15, "y") == 4021.356
