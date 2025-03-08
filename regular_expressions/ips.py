from re import findall


def check_value(entered_string: str) -> None:
    if not isinstance(entered_string, str):
        raise ValueError("Object entered_string must be of type str")


def find_ip_in_string(entered_string):
    check_value(entered_string)
    regex = r"(\d{3}\.\d{3}\.\d{2}\.\d{3}|(?:[0-9a-fA-F]{4}:){7}[0-9a-fA-F]{4})"
    ips = findall(regex, entered_string)
    return ips


if __name__ == '__main__':
    entered_string = ("Valid ips: 3002:0bd6:0000:0000:0000:ee00:0033:6778, "
                      "3001:0da8:75a3:0000:0000:8a2e:0370:7334, "
                      "3003:aaaa:aaaa:0000:0000:0000:1111:1111. "
                      "Invalid ips: 3003:aaua:aaaa:0000:0000:0000:1111:1111, "
                      "3003:aaa:aaaa:0000:0000:0000:1111:1111, "
                      "3003:aaaa:aaaa:00000000:0000:1111:1111.")
    print(entered_string)
    print(f"IPs: {find_ip_in_string(entered_string)}")
