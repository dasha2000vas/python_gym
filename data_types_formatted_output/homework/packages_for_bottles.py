from random import randint

from pydantic import BaseModel, Field

from tools import drop_fractional_part


class BottleValues(BaseModel):
    number_of_bottles: int = Field(gt=0, description='Number of bottles')
    one_package_hold: int = Field(gt=0, description='Max number of bottles that can hold one package.')


def find_number_of_packages(values: BottleValues) -> int:
    result = values.number_of_bottles / values.one_package_hold
    if str(result).split(".")[-1] == "0":
        return drop_fractional_part(result)
    return drop_fractional_part(result) + 1


if __name__ == "__main__":
    number_of_bottles, one_package_hold = randint(1, 100), randint(5, 20)
    print("Total bottles:", number_of_bottles, "\nPackage hold bottles:", one_package_hold)
    result = find_number_of_packages(BottleValues(
        number_of_bottles=number_of_bottles, one_package_hold=one_package_hold
    ))
    print("We need", result, "packages")
