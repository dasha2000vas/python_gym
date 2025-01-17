from pytest import mark

from logical_operators.home_work.b_between_a_and_c import b_between_a_and_c
from logical_operators.home_work.disparities import is_disparities_true
from logical_operators.home_work.even_numbers import are_even_numbers
from logical_operators.home_work.multiple_of_five import multiple_of_five
from logical_operators.home_work.odd_number import is_odd
from logical_operators.home_work.positive_number import is_positive


@mark.parametrize(
    "test_a,test_b,test_c,test_result",
    [(1, 50, 99, 1), (30, 29, 40, 0), (10, 10, 20, 0)],
)
def test_b_between_a_and_c(test_a, test_b, test_c, test_result):
    assert b_between_a_and_c(test_a, test_b, test_c) == test_result


@mark.parametrize(
    "test_a,test_b,test_result",
    [(10, 3, True), (2, 3, False), (10, 10, False)],
)
def test_disparities(test_a, test_b, test_result):
    assert is_disparities_true(test_a, test_b) == test_result


@mark.parametrize(
    "test_a,test_b,test_result",
    [(2, 10, True), (2, 7, False), (1, 10, False)],
)
def test_even_numbers(test_a, test_b, test_result):
    assert are_even_numbers(test_a, test_b) == test_result


@mark.parametrize(
    "test_a,test_b,test_result",
    [(1, 7, False), (5, 7, True), (1, 10, True)],
)
def test_multiple_of_five(test_a, test_b, test_result):
    assert multiple_of_five(test_a, test_b) == test_result


@mark.parametrize(
    "test_a,test_result",
    [(1, True), (2, False), (88, False)],
)
def test_odd_number(test_a, test_result):
    assert is_odd(test_a) == test_result


@mark.parametrize(
    "test_a,test_result",
    [(1, True), (0, False), (-1, False)],
)
def test_positive_number(test_a, test_result):
    assert is_positive(test_a) == test_result
