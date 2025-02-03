import pytest
from pytest import mark, raises

from if_elif_else import (
    number_sign,
    type_of_triangle,
    get_season,
    calculate_y,
    will_closet_pass,
    declension_of_word_hour,
    make_decision,
    chocolate_slices,
    calculate_u,
    lend_money,
    get_day_of_delivery,
    are_events_cross,
    are_rectangles_cross,
    contains_two_rectangles,
    declension_of_words_rubles_and_pennies,
    orientation_of_locator,
    get_day_of_week,
)


@mark.parametrize(
    "num,result",
    [
        (100, "Sign of number 100 is plus"),
        (0, "Number is zero"),
        (-100, "Sign of number -100 is minus")],
)
def test_number_sign(num, result):
    assert number_sign(num) == result


@mark.parametrize(
    "angle1,angle2,criteria",
    [
        (50, 50, "is acute-angled and isosceles"),
        (60, 60, "is acute-angled and equilateral"),
        (55, 60, "is acute-angled and scalene"),
        (45, 45, "is right-angled and isosceles"),
        (30, 30, "is blunt-angled and isosceles"),
        (30, 40, "is blunt-angled and scalene"),
        (100, 100, "doesn't exist"),
    ]
)
def test_type_of_triangle(angle1, angle2, criteria):
    assert type_of_triangle(angle1, angle2) == criteria


@mark.parametrize(
    "month,season",
    [
        (12, "Winter"),
        (4, "Spring"),
        (8, "Summer"),
        (9, "Autumn"),
    ],
)
def test_season(month, season):
    assert get_season(month) == season


@mark.parametrize(
    "month,message",
    [
        (24, "Month must be between 1 and 12"),
        (1.11, "Month must be integer"),
    ],
)
def test_season_value_error(month, message):
    with raises(ValueError, match=message):
        get_season(month)


@mark.parametrize(
    "x, result",
    [
        (-50, -0.6),
        (57, 0.87),
        (0, "There is no solution"),
        (50, "There is no solution"),
    ]
)
def test_calculate_y(x, result):
    assert calculate_y(x) == result


@mark.parametrize(
    "a1,b1,a2,b2,result",
    [
        (100, 100, 50, 50, "Closet will pass"),
        (50, 50, 50, 50, "Closet will not pass"),
        (50, 50, 100, 100, "Closet will not pass")
    ],
)
def test_closet(a1,b1,a2,b2,result):
    assert will_closet_pass(a1,b1,a2,b2) == result


@mark.parametrize(
    "a1,b1,a2,b2",
    [
        (-100, 100, 50, 50),
        (100, 100, 50, -50),
        (-100, -100, -50, -50),
    ],
)
def test_closet_value_error(a1,b1,a2,b2):
    with raises(ValueError, match="All entered numbers must be positive."):
        will_closet_pass(a1,b1,a2,b2)


@mark.parametrize(
    "num,result",
    [(101, "час"),(102, "часа"),(112, "часов"), (120, "часов")]
)
def test_declension_of_hour(num, result):
    assert declension_of_word_hour(num) == result


@mark.parametrize(
    "temp_out, temp_body, weather, result",
    [
        (0, 36.6, "clear","Go outside"),
        (20, 35.5, "cloudy", "Go outside"),
        (-30, 36.0, "windy", "Stay home"),
    ],
)
def test_make_decision(temp_out, temp_body, weather, result):
    assert make_decision(temp_out, temp_body, weather) == result


@mark.parametrize(
    "temp_out,temp_body,weather,message",
    [
        (0, 36.6, "raining men", r"Weather .* is not in .*"),
        (-100, 36.6, "clear", "Temperature must be between -30 and 30."),
        (0, 100, "clear", "Temperature of body must be between 35 and 42.")
    ]
)
def test_make_decision_value_error(temp_out, temp_body, weather, message):
    with raises(ValueError, match=message):
        make_decision(temp_out, temp_body, weather)


@mark.parametrize(
    "a,b,slices,result",
    [(2, 4, 6, True), (5, 10, 15, True), (2, 4, 7, False)]
)
def test_chocolate_slices(a, b, slices, result):
    assert chocolate_slices(a, b, slices) == result


@mark.parametrize(
    "a,b,slices,message",
    [
        (2, 4, -6, "A, b and n must be positive."),
        (2, 4, 6.11, "A, b and n must be integers.")
    ]
)
def test_chocolate_slices_value_error(a, b, slices, message):
    with raises(ValueError, match=message):
        chocolate_slices(a, b, slices)


@mark.parametrize(
    "x,y,z,result",
    [
        (3.333, 4.444, 5.555, 4.0),
        (10.0, 20.0, 50.0, -3.0),
        (1.111, 2.222, 3.333, "There is no solution"),
    ],
)
def test_calculate_u(x, y, z, result):
    assert calculate_u(x, y, z) == result



@mark.parametrize(
    "x,y,z",
    [(1, 1, 1),(1, 1.0, 1.0),(1.0, 5.0, 10)],
)
def test_calculate_u_value_error(x, y, z):
    with raises(ValueError, match="x, y and z must be floats"):
        calculate_u(x, y, z)


@mark.parametrize(
    "you_have_money,is_drinker,returned_earlier,is_miser,decision",
    [
        (True, False, True, False, True),
        (False, False, True, False, False),
        (False, True, False, True, False),
    ]
)
def test_lend_money(you_have_money, is_drinker, returned_earlier, is_miser, decision):
    assert lend_money(you_have_money, is_drinker, returned_earlier, is_miser) == decision


@mark.parametrize(
    "you_have_money,is_drinker,returned_earlier,is_miser",
    [
        (True, False, True, "False"),
        (False, False, True, 0),
        (False, True, False, [True]),
    ]
)
def test_lend_money(you_have_money, is_drinker, returned_earlier, is_miser):
    with raises(ValueError, match=r"All criteria must be bool, not .*"):
        lend_money(you_have_money, is_drinker, returned_earlier, is_miser)


@mark.parametrize(
    "n,k,result",
    [(0, 3, 3), (0, 5, 0), (3, 10, 0), (3, 5, 1)]
)
def test_day_of_delivery(n, k, result):
    assert get_day_of_delivery(n, k) == result


@mark.parametrize(
    "n,k,message",
    [
        (0.5, 3, "n and k must be integers"),
        (20, 5, "n must be between 0 and 6"),
        (3, -10, "k must be positive"),
    ]
)
def test_day_of_delivery(n, k, message):
    with raises(ValueError, match=message):
        get_day_of_delivery(n, k)


@mark.parametrize(
    (
        "h_start_1,m_start_1,s_start_1,"
        "h_finish_1,m_finish_1,s_finish_1,"
        "h_start_2,m_start_2,s_start_2,"
        "h_finish_2,m_finish_2,s_finish_2,"
        "result"
    ),
    [
        (10, 10, 10, 14, 10, 10, 11, 0, 0, 12, 0, 0, True),
        (10, 10, 10, 14, 10, 10, 10, 20, 0, 14, 0, 0, True),
        (10, 10, 10, 14, 10, 10, 10, 10, 0, 14, 10, 0, True),
        (10, 10, 10, 14, 10, 10, 10, 10, 10, 14, 10, 10, True),
        (10, 10, 10, 14, 10, 10, 8, 20, 20, 12, 20, 20, True),
        (10, 10, 10, 14, 10, 10, 12, 20, 20, 18, 20, 20, True),
        (10, 10, 10, 14, 10, 10, 14, 50, 50, 18, 50, 50, False)
    ],
)
def test_cross_events(
    h_start_1, m_start_1, s_start_1,
    h_finish_1, m_finish_1, s_finish_1,
    h_start_2, m_start_2, s_start_2,
    h_finish_2, m_finish_2, s_finish_2,
    result
):
    assert are_events_cross(
        h_start_1, m_start_1, s_start_1,
        h_finish_1, m_finish_1, s_finish_1,
        h_start_2, m_start_2, s_start_2,
        h_finish_2, m_finish_2, s_finish_2,
    ) == result


@mark.parametrize(
    "x1,y1,a1,b1,x2,y2,a2,b2,result",
    [
        (1, 8, 8, 4, 4, 10, 2, 1, (4, 10, 6, 11)),
        (3, 1, 9, 5, 6, 5, 8, 6, (6, 5, 12, 6)),
        (1, 8, 4, 9, 4, 4, 9, 2, "Rectangles are not crossed"),
    ],
)
def test_cross_rectangles(x1, y1, a1, b1, x2, y2, a2, b2, result):
    assert are_rectangles_cross(x1, y1, a1, b1, x2, y2, a2, b2) == result


@mark.parametrize(
    "x1,y1,a1,b1,x2,y2,a2,b2,result",
    [
        (1, 8, 8, 4, 4, 10, 2, 1, (1, 8, 9, 12)),
        (3, 1, 9, 5, 6, 5, 8, 6, (3, 1, 14, 11)),
        (1, 8, 4, 9, 4, 4, 9, 2, (1, 4, 13, 17)),
    ],
)
def test_contains_two_rectangles(x1, y1, a1, b1, x2, y2, a2, b2, result):
    assert contains_two_rectangles(x1, y1, a1, b1, x2, y2, a2, b2) == result


@mark.parametrize(
    "cost_in_rubles,result",
    [
        (1.01, "1 рубль 1 копейка"),
        (23.24, "23 рубля 24 копейки"),
        (11.12, "11 рублей 12 копеек"),
        (25.30, "25 рублей 30 копеек"),
    ],
)
def test_declension_of_rubles_and_pennies(cost_in_rubles, result):
    assert declension_of_words_rubles_and_pennies(cost_in_rubles) == result


@mark.parametrize(
    "cost_in_rubles,message",
    [
        (-100, "Entered number must be between 0 and 100."),
        (10, "Entered number must be float."),
        (10.11111, "Entered number must have 2 digits after dot."),
    ]
)
def test_declension_of_rubles_and_pennies_value_error(cost_in_rubles, message):
    with raises(ValueError, match=message):
        declension_of_words_rubles_and_pennies(cost_in_rubles)



@mark.parametrize(
    "n1,n2,result",
    [
        (2, 2, "North"),
        (1, 1, "South"),
        (1, 2, "East"),
        (-1, 2, "West"),
    ],
)
def test_orientation_of_locator(n1, n2, result):
    assert orientation_of_locator(n1, n2) == result


@mark.parametrize(
    "n1,n2",
    [
        (3, 3),
        (1, 5),
        (-4, 1),
    ]
)
def test_orientation_of_locator_value_error(n1, n2):
    with raises(ValueError, match="Turns can be just -1, 1 or 2."):
        orientation_of_locator(n1, n2)


@mark.parametrize(
    "day_of_year, jan_1, day_of_weak",
    [
        (12, 5, 2),
        (124, 7, 4),
        (22, 7, 7),
    ]
)
def test_day_of_weak(day_of_year, jan_1, day_of_weak):
    assert get_day_of_week(day_of_year, jan_1) == day_of_weak



@mark.parametrize(
    "day_of_year,jan_1,message",
    [
        (400, 1, "Day of year must be between 1 and 365."),
        (200, 10, "Day of week number of 1 january must be between 1 and 7.")
    ]
)
def test_day_of_weak_value_error(day_of_year, jan_1, message):
    with raises(ValueError, match=message):
        assert get_day_of_week(day_of_year, jan_1)
