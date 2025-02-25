from random import randint

from tools import drop_fractional_part


def check_values(number_of_bottles: int, one_package_hold: int) -> None:
    for value in (number_of_bottles, one_package_hold):
        if not isinstance(value, int):
            raise ValueError("All args must be integers")
        if value <= 0:
            raise ValueError("All numbers must be positive")


def find_number_of_packages(number_of_bottles: int, one_package_hold: int) -> int:
    check_values(number_of_bottles, one_package_hold)
    result = number_of_bottles / one_package_hold
    if str(result).split(".")[-1] == "0":
        return drop_fractional_part(result)
    return drop_fractional_part(result) + 1


if __name__ == "__main__":
    number_of_bottles, one_package_hold = randint(1, 100), randint(5, 20)
    print("Total bottles:", number_of_bottles, "\nPackage hold bottles:", one_package_hold)
    result = find_number_of_packages(number_of_bottles, one_package_hold)
    print("We need", result, "packages")
