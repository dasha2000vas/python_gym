from math import radians, sin, tan
from random import randint

from pydantic import BaseModel, Field, model_validator


class ExpressionValues(BaseModel):
    angle_value: int | float = Field(description="Angle value.")
    in_degrees: bool = Field(
        default=False,
        description="True if angle_value is in degrees,"
                    "False if angle_value is in radians.",
    )

    @model_validator(mode="after")
    def translate_in_radians(self):
        if self.in_degrees:
            self.angle_value = radians(self.angle_value)
        return self


def calculate_expression1(values: ExpressionValues) -> float:
    return round(tan(values.angle_value) - sin(values.angle_value), 5)


if __name__ == '__main__':
    angle_value = randint(-100, 100)
    print("a =", angle_value)
    values1 = ExpressionValues(angle_value=angle_value)
    result1 = calculate_expression1(values1)
    print("Result if a in radians: %10.5f" % result1)
    values2 = ExpressionValues(angle_value=angle_value, in_degrees=True)
    result2 = calculate_expression1(values2)
    print("Result if a in degrees: %10.5f" % result2)
