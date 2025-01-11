from random import randint

from tools import drop_fractional_part


def calculate_temperature_in_fahrenheit(temp_in_celsius: int) -> int:
    """
    Converts temperature from degrees Celsius to degrees Fahrenheit
    and returns the result.

    Args:
        temp_in_celsius (int): Temperature in degrees Celsius.

    Returns:
          int: Temperature in degrees Fahrenheit.
    """
    return drop_fractional_part(temp_in_celsius * 9 / 5 + 32)


if __name__ == "__main__":
    temp_in_celsius = randint(-100, 100)
    print("tc =", temp_in_celsius)
    print("tf =", calculate_temperature_in_fahrenheit(temp_in_celsius))
