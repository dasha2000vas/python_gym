from math import cos, radians, sin, tan
from random import randint


def calculate_sin_cos_tg_of_angle(d: int, min: int, sec: int) -> tuple[float, float, float, float]:
    """
    Converts the value from degrees, minutes, seconds to radians,
    calculate the sine, cosine and tangent of this angle.

    Args:
        d (int): The number of degrees.
        min (int): The number of minutes.
        sec (int): The number of seconds.

    Returns:
        tuple[float, float, float, float]: Radians, sine, cosine, tangent of angle.
    """
    d = radians(d + min / 60 + sec / 3600)
    return round(d, 2), round(sin(d), 2), round(cos(d), 2), round(tan(d), 2)


if __name__ == "__main__":
    d, min, sec = randint(-360, 360), randint(0, 59), randint(0, 59)
    print("Degrees of the angle:", d, "\nMinutes of the angle:", min, "\nSeconds of the angle:", sec)
    rad, sin, cos, tan = calculate_sin_cos_tg_of_angle(d, min, sec)
    print("%d d %d ' %d '' = %.2f radians" %(d, min, sec, rad))
    print("sin( %d d %d ' %d '' ) = %.2f" %(d, min, sec, sin))
    print("cos( %d d %d ' %d '' ) = %.2f" %(d, min, sec, cos))
    print("tan( %d d %d ' %d '' ) = %.2f" %(d, min, sec, tan))
