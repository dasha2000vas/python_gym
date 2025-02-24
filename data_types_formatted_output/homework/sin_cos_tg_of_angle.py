from math import cos, radians, sin, tan
from random import randint

from pydantic import BaseModel, Field

class DegreeValues(BaseModel):
    degrees: int = Field(description="Number of degrees")
    minutes: int = Field(ge=0, le=59, description="Number of minutes")
    seconds: int = Field(ge=0, le=59, description="Number of seconds")


def calculate_sin_cos_tg_of_angle(
    values: DegreeValues,
) -> tuple[float, float, float, float]:
    value_in_radians = radians(values.degrees + values.minutes / 60 + values.seconds / 3600)
    return (
        round(value_in_radians, 2),
        round(sin(value_in_radians), 2),
        round(cos(value_in_radians), 2),
        round(tan(value_in_radians), 2)
    )


if __name__ == "__main__":
    degrees, minutes, seconds = randint(-360, 360), randint(0, 59), randint(0, 59)
    print("Degrees of the angle:", degrees, "\nMinutes of the angle:", minutes, "\nSeconds of the angle:", seconds)
    rad, sin, cos, tan = calculate_sin_cos_tg_of_angle(
        DegreeValues(degrees=degrees, minutes=minutes, seconds=seconds)
    )
    print("%d d %d ' %d '' = %.2f radians" %(degrees, minutes, seconds, rad))
    print("sin( %d d %d ' %d '' ) = %.2f" %(degrees, minutes, seconds, sin))
    print("cos( %d d %d ' %d '' ) = %.2f" %(degrees, minutes, seconds, cos))
    print("tan( %d d %d ' %d '' ) = %.2f" %(degrees, minutes, seconds, tan))
