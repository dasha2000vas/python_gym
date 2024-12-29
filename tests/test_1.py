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
    TF = calculate_temperature_in_fahrenheit(40)
    assert TF == 104


def test_task_2():
    perimeter, square = find_perimeter_and_square(2, 3, 6, 1, 4, 8)
    assert perimeter == 16.22
    assert square == 2.5


def test_task_3():
    assert move_leftmost_digit_to_right_end(237) == 372


def test_task_4():
    assert define_third_digit_from_end(130985) == 9


def test_task_5():
    assert glue_numbers(100, 500) == 100500


def test_task_6():
    assert sum_of_digits(235) == 10


def test_task_7():
    count, remain = find_count_of_square_in_rectangle(11, 7, 3)
    assert count == 6
    assert remain == 23


def test_task_8():
    count, remain = find_b_in_a(20, 3)
    assert count == 6
    assert remain == 2


def test_task_9():
    r, k = find_cost_in_rubles_and_kopecks(453)
    assert r == 4
    assert k == 53


def test_task_10():
    assert count_value(3, 5, 33, 77) == 44.998


def test_task_11():
    assert count_of_cabins(8, 20) == 24


def test_task_12():
    assert calculate_count_of_desks(21, 19, 17) == 30


def test_task_13():
    assert calculate_1(12, 45, "n") == 117835.745
    assert calculate_1(12, 45, "y") == 81375.794


def test_task_14():
    assert calculate_2(22, 1, 44, 27, 30, "n") == 3499615212.824
    assert calculate_2(22, 1, 44, 27, 30, "y") == 896228237.135
