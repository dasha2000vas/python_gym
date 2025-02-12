from pytest import mark, raises

from lesson_10 import (
    sum_of_digits_from_str,
    calculation_of_years,
    changing_string,
    leave_one_space,
    swap_first_and_last_symbol,
    two_first_and_last_symbols,
    add_html_tags_around_word,
    remove_vowel_letters,
    remove_all_symbols,
)

@mark.parametrize(
    "number,sum_of_digits",
    [
        ("4021", 7),
        ("2850", 15),
        ("1876", 22),
    ]
)
def test_sum_of_digits_from_str(number, sum_of_digits):
    assert sum_of_digits_from_str(number) == sum_of_digits


@mark.parametrize(
    "number,message",
    [
        (1234, "Object with name number must be of type str"),
        ("-1234", "String with name number must containing natural number"),
        ("1234.123", "String with name number must containing natural number"),
    ]
)
def test_sum_of_digits_from_str_value_error(number, message):
    with raises(ValueError, match=message):
        sum_of_digits_from_str(number)


@mark.parametrize(
    "name,age,years",
    [
        ("Dasha Vasilevskaya", 24, 1.412),
        ("Roni Cat", 4, 0.571),
        ("Trixie Cat", 1, 0.111),
    ]
)
def test_calculation_of_years(name, age, years):
    assert calculation_of_years(name, age) == years


@mark.parametrize(
    "name,age,message",
    [
        (10, 10, 'Name must be a string'),
        ("10", 10, "Name must contain only letters"),
        ("Kate Daw", "30", "Age must be integer"),
        ("Kate Daw", 30.333, "Age must be integer"),
        ("Kate Daw", -30, "Age must be between 1 and 130"),
        ("Kate Daw", 200, "Age must be between 1 and 130"),
    ]
)
def test_calculation_of_years_value_error(name, age, message):
    with raises(ValueError, match=message):
        calculation_of_years(name, age)


@mark.parametrize(
    "original,update",
    [
        ("cat", "cc97tt"),
        ("flower", "ff108oo119ee114"),
        ("bird", "bb105rr100"),
    ]
)
def test_changing_string(original, update):
    assert changing_string(original) == update


@mark.parametrize(
    "original,message",
    [
        (10, "Original must be a string"),
        (10.111, "Original must be a string"),
        ([10], "Original must be a string"),
    ]
)
def test_changing_string_value_error(original, message):
    with raises(ValueError, match=message):
        changing_string(original)


@mark.parametrize(
    "original_string,updated_string",
    [
        ("   I    have    two    cats   ", "I have two cats"),
        ("  Flowers     are       nice  ", "Flowers are nice"),
        ("   Let's     have     some     tee ", "Let's have some tee"),
    ]
)
def test_leave_one_space(original_string, updated_string):
    assert leave_one_space(original_string) == updated_string


@mark.parametrize(
    "original_string,message",
    [
        (10, "Original must be a string"),
        (10.111, "Original must be a string"),
        ([10], "Original must be a string"),
    ]
)
def test_leave_one_space_value_error(original_string, message):
    with raises(ValueError, match=message):
        leave_one_space(original_string)



@mark.parametrize(
    "original_string,updated_string",
    [
        ("cat", "tac"),
        ("flower", "rlowef"),
        ("sky", "yks"),
    ]
)
def test_swap_first_and_last_symbol(original_string, updated_string):
    assert swap_first_and_last_symbol(original_string) == updated_string


@mark.parametrize(
    "original_string,message",
    [
        (10, "Original must be a string"),
        (10.111, "Original must be a string"),
        ([10], "Original must be a string"),
    ]
)
def test_swap_first_and_last_symbol_value_error(original_string, message):
    with raises(ValueError, match=message):
        swap_first_and_last_symbol(original_string)


@mark.parametrize(
    "original_string,updated_string",
    [
        ("cat", "caat"),
        ("flower", "fler"),
        ("I", ""),
    ]
)
def test_two_first_and_last_symbols(original_string, updated_string):
    assert two_first_and_last_symbols(original_string) == updated_string


@mark.parametrize(
    "original_string,message",
    [
        (10, "Original must be a string"),
        (10.111, "Original must be a string"),
        ([10], "Original must be a string"),
    ]
)
def test_two_first_and_last_symbols_value_error(original_string, message):
    with raises(ValueError, match=message):
        two_first_and_last_symbols(original_string)


@mark.parametrize(
    "word,result",
    [
        ("text", "<text>"),
        ("image", "<image>"),
        ("break", "<break>"),
    ]
)
def test_html_tags_around_word(word, result):
    assert add_html_tags_around_word(word) == result


@mark.parametrize(
    "word,message",
    [
        (10, "Word must be a string"),
        (10.111, "Word must be a string"),
        ([10], "Word must be a string"),
    ]
)
def test_html_tags_around_word_value_error(word, message):
    with raises(ValueError, match=message):
        add_html_tags_around_word(word)

@mark.parametrize(
    "original_string, result",
    [
        ("cat", "ct"),
        ("flower", "flwr"),
        ("I have two cats", "hv tw cts"),
    ]
)
def test_remove_vowel_letters(original_string, result):
    assert remove_vowel_letters(original_string) == result


@mark.parametrize(
    "original_string,message",
    [
        (10, "Original must be a string"),
        (10.111, "Original must be a string"),
        ([10], "Original must be a string"),
    ]
)
def test_remove_vowel_letters_value_error(original_string, message):
    with raises(ValueError, match=message):
        remove_vowel_letters(original_string)


@mark.parametrize(
    "original_string,result",
    [
        ("I have two cats", "   "),
        ("Flowers are nice", "  "),
        ("Let's have some tee!^-^", "   "),
    ]
)
def test_remove_all_symbols(original_string, result):
    assert remove_all_symbols(original_string) == result


@mark.parametrize(
    "original_string,message",
    [
        (10, "Original must be a string"),
        (10.111, "Original must be a string"),
        ([10], "Original must be a string"),
    ]
)
def test_remove_all_symbols_value_error(original_string, message):
    with raises(ValueError, match=message):
        remove_all_symbols(original_string)
