from math import radians, sin, tan
from random import randint


def check_value(angle_value_in_degrees: int) -> None:
    if not isinstance(angle_value_in_degrees, int):
        raise ValueError('Object angle_value_in_degrees must be integer')


def calculate_expression2(angle_value_in_degrees: int) -> float:
    check_value(angle_value_in_degrees)
    angle_value_in_degrees = radians(angle_value_in_degrees)
    return tan(angle_value_in_degrees) - sin(angle_value_in_degrees ** 3)


if __name__ == "__main__":
     angle_value_in_degrees = randint(-360, 360)
     print("Angle value in degrees:", angle_value_in_degrees)
     result = calculate_expression2(angle_value_in_degrees)
     print("Result: %.3f" %result)
