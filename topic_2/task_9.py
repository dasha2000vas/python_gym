from math import cos, radians, sin, tan


def calculate_sin_cos_tg_of_angle(d: int, min: int, sec: int) -> tuple[float, float, float, float]:
    """
    Data: angle value (in degrees, minutes, seconds)
    Task: convert the value to radians,
          calculate the sine, cosine and tangent of this angle
    """
    d = radians(d + min / 60 + sec / 3600)
    return d, sin(d), cos(d), tan(d)


if __name__ == "__main__":
    d = int(input("Enter the degrees of the angle: "))
    min = int(input("Enter the minutes of the angle: "))
    sec = int(input("Enter the seconds of the angle: "))
    rad, sin, cos, tan = calculate_sin_cos_tg_of_angle(d, min, sec)
    print("%d d %d ' %d '' = %.2f radians" %(d, min, sec, rad))
    print("sin( %d d %d ' %d '' ) = %.2f" %(d, min, sec, sin))
    print("cos( %d d %d ' %d '' ) = %.2f" %(d, min, sec, cos))
    print("tan( %d d %d ' %d '' ) = %.2f" %(d, min, sec, tan))
