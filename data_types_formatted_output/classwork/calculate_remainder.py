from random import randint

from pydantic import BaseModel, Field


class ValuesForCalculatingRemainder(BaseModel):
    number: int = Field(gt=0, description="First number.")
    divider: int = Field(gt=0, description="Divider.")


def calculate_remainder(values: ValuesForCalculatingRemainder) -> int :
    """
    Writes number thousand times, then finds
    remainder of division by divider number.

    Args:
        values (ValuesForCalculation)

    Returns:
        int: The resulting number.
    """
    return int(str(values.number) * 1000) % values.divider


if __name__ == '__main__':
    number, divider = randint(1, 999), randint(2, 50)
    print("Number:", number, "\nDivider:", divider)
    result = calculate_remainder(ValuesForCalculatingRemainder(number=number, divider=divider))
    print("Remainder:", result)
