from pytest import mark, raises

from regular_expressions import (
    get_phones_from_string,
    replace_substrings,
    clean_string,
    add_whitespaces,
    add_whitespaces_with_re,
    find_ip_in_string,
)


@mark.parametrize(
    "phones_string,result",
    [
        (
            ("Phone numbers: 8 888 888 88 88,"
            "9 999 999 99 99, 1 111 111 11 11,"
            "+7 777 777 77 77, 7 777 777 77 77."),
            ["8 888 888 88 88", "+7 777 777 77 77"]
        ),
        (
            ("Here's phone numbers: 8-000-000-00-00,"
             "+7-000-000-00-00, +5-000-000-00-00,"
             "1-000-000-00-00, 9-000-000-00-00"),
            ["8-000-000-00-00", "+7-000-000-00-00"]
        ),
        (
            ("Valid phone numbers: 8-999-999-99-99, +7-999-999-99-99, "
             "8 888 888 88 88, +7 888 888 88 88. Invalid phone numbers: "
             "+71111111111, 85555555555, 9-999-999-99-99"),
            ['8-999-999-99-99', '+7-999-999-99-99',
             '8 888 888 88 88', '+7 888 888 88 88'],
        ),
    ]
)
def test_phones(phones_string, result):
    assert get_phones_from_string(phones_string) == result


@mark.parametrize(
    "phones_string",
    [
        1, 1.111, ["a"],
    ]
)
def test_phones_value_error(phones_string):
    with raises(ValueError, match="Object phones_string must be of type str"):
        get_phones_from_string(phones_string)


@mark.parametrize(
    "entered_string,result",
    [
        (
            ("Valid time: 11:11, 22:22, 00:00. "
             "Invalid time: 33:33, 44:44, 55:55."),
            ("Valid time: XX:XX, XX:XX, XX:XX. "
             "Invalid time: 00000, 00000, 00000."),
        ),
        (
            "In 11:00 go to park. In 13:00 start to clean room.",
            "In XX:XX go to park. In XX:XX start to clean room."
        ),
        (
            "90:90 80:30 11:11 30:20 12:12",
            "00000 00000 XX:XX 00000 XX:XX"
        ),
    ]
)
def test_substrings(entered_string, result):
    assert replace_substrings(entered_string) == result


@mark.parametrize(
    "entered_string",
    [
        1, 1.111, ["a"],
    ]
)
def test_substrings_value_error(entered_string):
    with raises(ValueError, match="Object entered_string must be of type str"):
        replace_substrings(entered_string)


@mark.parametrize(
    "entered_string,result",
    [
        (
            "23We5%_h,@a>v#e_,tw<o_c./at!s",
            "We_have_two_cats",
        ),
        (
            "Wh!e?2-=t.h+er_i<s_ni>,ce",
            "Whether_is_nice",
        ),
        (
            "S1u@?n2_>_i-+s_^:_/66*bri8g+=ht",
            "Sun__is__bright",
        ),
    ]
)
def test_cleaning(entered_string, result):
    assert clean_string(entered_string) == result


@mark.parametrize(
    "entered_string",
    [
        1, 1.111, ["a"],
    ]
)
def test_cleaning_value_error(entered_string):
    with raises(ValueError, match="Object entered_string must be of type str"):
        clean_string(entered_string)


@mark.parametrize(
    "entered_string,result",
    [
        (
            "Hello,world!How are you?",
            "Hello, world! How are you?",
        ),
        (
            "Hello, world! How are you?",
            "Hello, world! How are you?"
        ),
        (
            "Hello,(world)!How[are]you?",
            "Hello, (world)! How [are] you?",
        ),
        (
            "This is a test",
            "This is a test",
        ),
        (
            "Wait...What?",
             "Wait... What?"
        ),
        (
            "Enter( string ) :I'm in( bad )mood . . .Why ?",
            "Enter (string): I'm in (bad) mood... Why?"
        )
    ]
)
def test_whitespaces(entered_string, result):
    assert add_whitespaces(entered_string) == result
    assert add_whitespaces_with_re(entered_string) == result


@mark.parametrize(
    "entered_string",
    [
        1, 1.111, ["a"]
    ]
)
def test_whitespaces_value_error(entered_string):
    with raises(ValueError, match="Object entered_string must be of type str"):
        add_whitespaces(entered_string)
        add_whitespaces_with_re(entered_string)


@mark.parametrize(
    "entered_string,result",
    [
        (
            ("Valid ips: 192.168.10.150, 111.111.11.111, 222.222.22.222. "
             "Invalid ips: 192.168.101.50, 1111.11.11.111, 222.22a.22.222."),
            [
                "192.168.10.150", "111.111.11.111", "222.222.22.222",
            ]
        ),
        (
            ("Valid ips: 3002:0bd6:0000:0000:0000:ee00:0033:6778, "
             "3001:0da8:75a3:0000:0000:8a2e:0370:7334, "
             "3003:aaaa:aaaa:0000:0000:0000:1111:1111. "
             "Invalid ips: 3003:aaua:aaaa:0000:0000:0000:1111:1111, "
             "3003:aaa:aaaa:0000:0000:0000:1111:1111, "
             "3003:aaaa:aaaa:00000000:0000:1111:1111."),
            [
                "3002:0bd6:0000:0000:0000:ee00:0033:6778",
                "3001:0da8:75a3:0000:0000:8a2e:0370:7334",
                "3003:aaaa:aaaa:0000:0000:0000:1111:1111"
            ]
        ),
        (
            ("Ips: 192.168.10.150, 3002:0bd6:0000:0000:0000:ee00:0033:6778, "
             "1111.11.11.111, 3003:aaaa:aaaa:00000000:0000:1111:1111."),
            ["192.168.10.150", "3002:0bd6:0000:0000:0000:ee00:0033:6778"]
        ),
    ]
)
def test_ip(entered_string, result):
    assert find_ip_in_string(entered_string) == result


@mark.parametrize(
    "entered_string",
    [
        1, 1.111, ["a"]
    ]
)
def test_ip_value_error(entered_string):
    with raises(ValueError, match="Object entered_string must be of type str"):
        find_ip_in_string(entered_string)
