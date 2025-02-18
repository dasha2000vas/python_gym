from pytest import mark, raises

from lesson_9 import (
    check_same_digits,
    double_substring,
    add_string_after_symbol,
    count_of_digits_and_letters,
    make_lower,
    make_initials_second_way,
    make_initials_first_way,
    from_str_to_number,
    is_palindrome,
    symbol_replacement,
    shortening_word,
    clear_str,
    remove_last_match,
    count_words_containing_substring,
    count_of_matching_letters,
    remove_spaces,
    arithmetic_expression_in_string,
    get_longest_word,
    form_paragraphs,
    get_vowels_of_word,
)


@mark.parametrize(
    "num,result",
    [
        (604, False),
        (111, True),
        (255, True),
    ]
)
def test_check_same_digits(num, result):
    assert check_same_digits(num) == result


@mark.parametrize(
    "num",
    [
        ("11"),
        (11.111),
        ([11]),
    ]
)
def test_check_same_digits_value_error(num):
    with raises(ValueError, match="Number must be integer"):
        check_same_digits(num)


@mark.parametrize(
    "original_string,substring,updated_string",
    [
        ("snow, snake", "sn", "snsnow, snsnake"),
        ("take, make, fake", "ake", "takeake, makeake, fakeake"),
        ("cat, bad, sad", "a", "caat, baad, saad"),
        ("house, bird, street", "q", "There are no entries of q in string")
    ]
)
def test_double_substring(original_string, substring, updated_string):
    assert double_substring(original_string, substring) == updated_string


@mark.parametrize(
    "original_string,substring",
    [
        (10, "a"),
        ("a", 10),
        (10.111, "a"),
    ]
)
def test_double_substring_value_error(original_string, substring):
    with raises(ValueError, match="All args must be strings"):
        double_substring(original_string, substring)


@mark.parametrize(
    "original_string,add_string,symbol,result",
    [
        ("snow, snake", "la", "n", "snlaow, snlaake"),
        ("take, make, fake", "yes", "k", "takyese, makyese, fakyese"),
        ("cat, bad, sad", "  ", "a", "ca  t, ba  d, sa  d"),
        ("house, bird, street", "", "q", "There are no entries of q in string"),
    ]
)
def test_add_string_after_symbol(original_string, add_string, symbol, result):
    assert add_string_after_symbol(original_string, add_string, symbol) == result


@mark.parametrize(
    "original_string,add_string,symbol",
    [
        (10, "a", "a"),
        ("a", 10, "a"),
        ("a", "a", 10.111),
    ]
)
def test_add_string_after_symbol_value_error(original_string, add_string, symbol):
    with raises(ValueError, match="All args must be strings"):
        add_string_after_symbol(original_string, add_string, symbol)


@mark.parametrize(
    "entered_str,count_of_digits,count_of_low_letters",
    [
        ("We have 2 CATS", 1, 5),
        ("It's RAINY outside", 0, 9),
        ("1, 2, 3, 4, 5, I start SEEK", 5, 5),
    ]
)
def test_count_of_digits_and_letters(entered_str, count_of_digits, count_of_low_letters):
    assert count_of_digits_and_letters(entered_str) == (count_of_digits, count_of_low_letters)


@mark.parametrize(
    "entered_str",
    [
        (11),
        (11.111),
        ([11]),
    ]
)
def test_count_of_digits_and_letters_value_error(entered_str):
    with raises(ValueError, match="Entered string must be of type str"):
        count_of_digits_and_letters(entered_str)


@mark.parametrize(
    "original_str,result",
    [
        ("WE HAVE 2 CATS", "we have 2 cats"),
        ("It'S rAiNy OuTsIdE", "it's rainy outside"),
        ("Flowers Are Nice", "flowers are nice"),
    ]
)
def test_make_lower(original_str, result):
    assert make_lower(original_str) == result


@mark.parametrize(
    "original_str",
    [
        (11),
        (11.111),
        ([11]),
    ]
)
def test_make_lower_value_error(original_str):
    with raises(ValueError, match="Original string must be of type str"):
        make_lower(original_str)


@mark.parametrize(
    "full_name,initial",
    [
        ("Dasha Alexandrovna Vasilevskaya", "D. A. Vasilevskaya"),
        ("Ann Cook", "A. Cook"),
        ("Rose Mary Keat", "R. M. Keat"),
    ]
)
def test_make_initials_first_way(full_name, initial):
    assert make_initials_first_way(full_name) == initial
    assert make_initials_second_way(full_name) == initial


@mark.parametrize(
    "full_name, message",
    [
        (11, "Full name must be of type str"),
        (11.111, "Full name must be of type str"),
        ("Ann", "Name must be full"),
    ]
)
def test_make_initials_first_way_value_error(full_name, message):
    with raises(ValueError, match=message):
        make_initials_first_way(full_name)
    with raises(ValueError, match=message):
        make_initials_second_way(full_name)


@mark.parametrize(
    "entered_str,result",
    [
        ("10", 10),
        ("10.111", 10.111),
        ("10,111", 10.111),
        ("1.0.0.1", "Cannot convert to number"),
        ("a123", "Cannot convert to number"),
    ]
)
def test_from_str_to_number(entered_str, result):
    assert from_str_to_number(entered_str) == result


@mark.parametrize(
    "entered_str",
    [
        (10),
        (10.111),
        (["10"]),
    ]
)
def test_from_str_to_number_value_error(entered_str):
    with raises(ValueError, match="Entered string must be of type str"):
        from_str_to_number(entered_str)


@mark.parametrize(
    "word,result",
    [
        ("level", True),
        ("eye", True),
        ("cat", False),
    ]
)
def test_is_palindrome(word, result):
    assert is_palindrome(word) == result


@mark.parametrize(
    "word,message",
    [
        (10, "Word must be string"),
        ("10", "Word must contain only letters"),
        ("l.e.v.e.l", "Word must contain only letters"),
    ]
)
def test_is_palindrome_value_error(word, message):
    with raises(ValueError, match=message):
        is_palindrome(word)


@mark.parametrize(
    "original_string,replace,updated_string",
    [
        ("rural ruler", "__", "ru__al __ule__"),
        ("black back bat", "111", "black 111ack 111at"),
        ("good blood, bad blood", "010", "good blood, bad blood"),
    ]
)
def test_symbol_replacement(original_string,replace,updated_string):
    assert symbol_replacement(original_string, replace) == updated_string


@mark.parametrize(
    "original_string,replace",
    [
        (10, "11"),
        ("11", 10.111),
        (["10"], "11"),
    ]
)
def test_symbol_replacement_value_error(original_string,replace):
    with raises(ValueError, match='Original string must of type str'):
        symbol_replacement(original_string,replace)


@mark.parametrize(
    "word,shortened_word",
    [
        ("biomechanical", "biom-l"),
        ("automatically", "aut-ly"),
        ("cat", "cat"),
    ]
)
def test_shortening_words(word, shortened_word):
    assert shortening_word(word) == shortened_word


@mark.parametrize(
    "word,message",
    [
        (10, "Word must be of type str"),
        (["cat"], "Word must be of type str"),
        ("10", "Word must contain only letters"),
        ("c.a.t", "Word must contain only letters"),
    ]
)
def test_shortening_words_value_error(word, message):
    with raises(ValueError, match=message):
        shortening_word(word)


@mark.parametrize(
    "original_str,cleared_str",
    [
        ("C9)_$&a_/.>t", "c_a_t"),
        ("d!+0O=g__", "dog__"),
        ("S8*^U_-(n@}5", "su_n"),
        ("flower", "flower"),
    ]
)
def test_clear_str(original_str, cleared_str):
    assert clear_str(original_str) == cleared_str


@mark.parametrize(
    "original_str",
    [
        (10),
        (10.111),
        (["cat"]),
    ]
)
def test_clear_str_value_error(original_str):
    with raises(ValueError, match="Original string must be of type str"):
        clear_str(original_str)


@mark.parametrize(
    "original_string,substring,result",
    [
        ("rural ruler", "ru", "rural ler"),
        ("black back bat", "ack", "black b bat"),
        ("good blood, bad blood", "ood", "good blood, bad bl"),
    ]
)
def test_remove_last_match(original_string, substring, result):
    assert remove_last_match(original_string, substring) == result


@mark.parametrize(
    "original_string,substring",
    [
        (10, "a"),
        ("a", 10),
        (10.111, "a"),
    ]
)
def test_remove_last_match_value_error(original_string, substring):
    with raises(ValueError, match="All args must be strings"):
        remove_last_match(original_string, substring)


@mark.parametrize(
    "entered_string,substring,count",
    [
        ("rural ruler", "r", 2),
        ("thin sticks thick bricks", "ick", 3),
        ("black back bat", "cat", 0),
    ]
)
def test_words_containing_substring(entered_string, substring, count):
    assert count_words_containing_substring(entered_string, substring) == count


@mark.parametrize(
    "entered_string,substring,message",
    [
        (10, "a", "All args must be strings"),
        ("a", 10, "All args must be strings"),
        ("123", "a", "Entered string must contain only letters and whitespaces"),
        ("a a a", "1", "Substring must contain only letters"),
    ]
)
def test_words_containing_substring_value_error(entered_string, substring, message):
    with raises(ValueError, match=message):
        count_words_containing_substring(entered_string, substring)


@mark.parametrize(
    "word1, word2, count",
    [
        ("karma", "paint", 1),
        ("honor", "robot", 2),
        ("bonus", "cheek", 0),
    ]
)
def test_count_of_matching_letters(word1, word2, count):
    assert count_of_matching_letters(word1, word2) == count


@mark.parametrize(
    "word1, word2, message",
    [
        (10, "a", "All args must be strings"),
        ("a", 10, "All args must be strings"),
        ("10", "a", "All args must contain only letters"),
        ("a", "10", "All args must contain only letters"),
        ("cat", "flower", "Args must have same length"),
    ]
)
def test_count_of_matching_letters_value_error(word1, word2, message):
    with raises(ValueError, match=message):
        count_of_matching_letters(word1, word2)


@mark.parametrize(
    "original_string,result",
    [
        ("Good blood, bad blood.", "Goodblood,badblood."),
        ("2 * 2 = 4", "2*2=4"),
        ("We have 2 cats!", "Wehave2cats!"),
    ]
)
def test_remove_spaces(original_string, result):
    assert remove_spaces(original_string) == result


@mark.parametrize(
    "original_string",
    [
        (10),
        (10.111),
        (["cat"]),
    ]
)
def test_remove_spaces_value_error(original_string):
    with raises(ValueError, match="Original must be a string"):
        remove_spaces(original_string)


@mark.parametrize(
    "expression,result",
    [
        ("1+2+3+4", 10),
        ("2+2-5", -1),
        ("9-4-5-6", -6),
    ]
)
def test_arithmetic_expression_in_string(expression, result):
    assert arithmetic_expression_in_string(expression) == result


@mark.parametrize(
    "expression,message",
    [
        (10, "Expression must be of type str"),
        ("1+2+a3+7a", "Expression must contain only digits and signs of subtraction and addition"),
        ("1+42+-3+7", r"Expression must have following format:"),
    ]
)
def test_arithmetic_expression_in_string_value_error(expression, message):
    with raises(ValueError, match=message):
        arithmetic_expression_in_string(expression)


@mark.parametrize(
    "entered_str,target_word",
    [
        ("Stupid superstition.", "superstition"),
        ("A snake sneaks to seek a snack.", "sneaks"),
        ("Thin sticks, thick bricks.", "sticks"),
    ]
)
def test_get_longest_word(entered_str, target_word):
    assert get_longest_word(entered_str) == target_word


@mark.parametrize(
    "entered_str, message",
    [
        (10, "Entered string must be of type str"),
        ("10", "Entered string must contain only letters and and whitespaces"),
    ]
)
def test_get_longest_word_value_error(entered_str, message):
    with raises(ValueError, match=message):
        get_longest_word(entered_str)


@mark.parametrize(
    "entered_str,list_of_strings",
    [
        (
            ("At the Zoo we can see many wild animals: "
             "elephants and giraffes, lions and tigers, "
             "monkeys and crocodiles, wolves and foxes, "
             "bears and hares. We can see many fine birds."
             "$As for me, I like monkeys. They are very "
             "clever and funny. They like to jump, run, and play."),
            [
                "    At the Zoo we can see many wild animals:",
                "elephants and giraffes, lions and tigers,",
                "monkeys and crocodiles, wolves and foxes,",
                "bears and hares. We can see many fine birds.",
                "    As for me, I like monkeys. They are very",
                "clever and funny. They like to jump, run, and",
                "play.",
            ],
        ),
        (
            ("I have two pets. They are a dog and a cat. "
             "Look at my dog! Its name is Jay. It is white and black. "
             "Its eyes are black and ears are long. Its tail is short. "
             "Its feet are short too. It is very clever and kind. Joy likes "
             "to play with a ball.$And that is my cat. Its name is Willy. "
             "It’s gray. Its eyes are green and very clever. It likes milk "
             "and meat. Willy likes to jump, run and play with a ball. "
             "$Joy and Willy are good friends. They like to play together. "
             "When I come home from school, I like to play with my pets."),
            [
                "    I have two pets. They are a dog and a cat.",
                "Look at my dog! Its name is Jay. It is white",
                "and black. Its eyes are black and ears are",
                "long. Its tail is short. Its feet are short",
                "too. It is very clever and kind. Joy likes to",
                "play with a ball.",
                "    And that is my cat. Its name is Willy.",
                "It’s gray. Its eyes are green and very clever.",
                "It likes milk and meat. Willy likes to jump,",
                "run and play with a ball.",
                "    Joy and Willy are good friends. They like",
                "to play together. When I come home from",
                "school, I like to play with my pets.",
            ],
        ),
    ]
)
def test_form_paragraphs(entered_str, list_of_strings):
    assert form_paragraphs(entered_str) == list_of_strings


@mark.parametrize(
    "entered_str",
    [
        (10),
        (10.111),
        (["cat"])
    ]
)
def test_form_paragraphs_value_error(entered_str):
    with raises(ValueError, match="Entered string must be of type str"):
        form_paragraphs(entered_str)


@mark.parametrize(
    "word,vowels_in_word",
    [
        ("biomechanical", ["i", "o", "e", "a"]),
        ("cat", ["a"]),
        ("swEEt", ["e"]),
    ]
)
def test_get_vowels_of_word(word, vowels_in_word):
    assert get_vowels_of_word(word) == vowels_in_word


@mark.parametrize(
    "word,message",
    [
        (10, "Word must be of type str"),
        (["cat"], "Word must be of type str"),
        ("10", "Word must contain only letters"),
        ("c.a.t", "Word must contain only letters"),
    ]
)
def test_get_vowels_of_word_value_error(word, message):
    with raises(ValueError, match=message):
        get_vowels_of_word(word)
