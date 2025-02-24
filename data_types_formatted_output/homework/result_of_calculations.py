from random import randint

from pydantic import BaseModel, Field


class ValuesForCalculation(BaseModel):
    number: int = Field(ge=100, le=999, description="Three-digit number.")
    count_of_times: int = Field(gt=0, description="Number of times to record number.")
    power: int = Field(gt=0, description="Power factor.")


def get_result_of_calculations(values: ValuesForCalculation) -> float:
    """
    Raises the number to the 10th power,
    records times (count_of_times) in a
    row and extracts root of power (power).

    Args:
        values (ValuesForCalculation)

    Returns:
        float: The resulting number.
    """
    return int(str(values.number ** 10) * values.count_of_times) ** (1 / values.power)


if __name__ == "__main__":
    number, count_of_times, power = randint(100, 999), randint(1, 10), randint(1, 50)
    print("Number =", number, "\nCount of times =", count_of_times, "\nPower =", power)
    result = get_result_of_calculations(
        ValuesForCalculation(number=number, count_of_times=count_of_times, power=power)
    )
    print("Result: %.3f" %result)
