from math import radians, sin, tan
from random import randint

from pydantic import BaseModel, Field


class ExpressionValue(BaseModel):
    angle_value: int = Field(description="Angle value in degrees.")


def calculate_expression2(value: ExpressionValue) -> float:
    value.angle_value = radians(value.angle_value)
    return tan(value.angle_value) - sin(value.angle_value ** 3)


if __name__ == "__main__":
     angle_value = randint(-360, 360)
     print("a =", angle_value)
     result = calculate_expression2(ExpressionValue(angle_value=angle_value))
     print("Result: %.3f" %result)
