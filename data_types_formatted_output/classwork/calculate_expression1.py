from math import radians, sin, tan
from random import randint

from pydantic import BaseModel, Field


class ExpressionValues1(BaseModel):
    angle_value: int = Field(description="Angle value.")
    in_degrees: bool = Field(
        default=False,
        description="True if angle_value is in degrees,"
                    "False if angle_value is in radians.",
    )


def calculate_expression1(values: ExpressionValues1) -> float:
    if values.in_degrees:
        values.angle_value = radians(values.angle_value)
    return round(tan(values.angle_value) - sin(values.angle_value), 5)


if __name__ == '__main__':
    angle_value = randint(-100, 100)
    print("a =", angle_value)
    result1 = calculate_expression1(ExpressionValues1(angle_value=angle_value))
    print("Result if a in radians: %10.5f" % result1)
    result2 = calculate_expression1(ExpressionValues1(angle_value=angle_value, in_degrees="a"))
    print("Result if a in degrees: %10.5f" % result2)
