from math import cos, radians, sin, tan
from random import randint


def calculate_sin_cos_tg_of_angle(
    degrees: int, minutes: int, seconds: int
) -> tuple[float, float, float, float]:
    """
    Converts the value from degrees, minutes, seconds to radians,
    calculate the sine, cosine and tangent of this angle.

    Args:
        degrees (int): The number of degrees.
        minutes (int): The number of minutes.
        seconds (int): The number of seconds.

    Returns:
        tuple[float, float, float, float]: Radians, sine, cosine, tangent of angle.
    """
    for number in (degrees, minutes, seconds):
        if not isinstance(number, int):
            raise ValueError("All args must be integers")
    if not 0 <= minutes <= 59 or not 0 <= seconds <= 59:
        raise ValueError("Minutes and seconds must be between 0 and 59")
    degrees = radians(degrees + minutes / 60 + seconds / 3600)
    return (
        round(degrees, 2),
        round(sin(degrees), 2),
        round(cos(degrees), 2),
        round(tan(degrees), 2)
    )


if __name__ == "__main__":
    degrees, minutes, seconds = randint(-360, 360), randint(0, 59), randint(0, 59)
    print("Degrees of the angle:", degrees, "\nMinutes of the angle:", minutes, "\nSeconds of the angle:", seconds)
    rad, sin, cos, tan = calculate_sin_cos_tg_of_angle(degrees, minutes, seconds)
    print("%d d %d ' %d '' = %.2f radians" %(degrees, minutes, seconds, rad))
    print("sin( %d d %d ' %d '' ) = %.2f" %(degrees, minutes, seconds, sin))
    print("cos( %d d %d ' %d '' ) = %.2f" %(degrees, minutes, seconds, cos))
    print("tan( %d d %d ' %d '' ) = %.2f" %(degrees, minutes, seconds, tan))
