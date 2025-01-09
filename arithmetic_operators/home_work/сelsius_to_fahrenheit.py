from random import randint

from tools import drop_fractional_part


def calculate_temperature_in_fahrenheit(tc: int) -> int:
    """
        Data: temperature value in degrees Celsius - tc
        Task: find its temperature value in degrees Fahrenheit -tf
    """
    return drop_fractional_part(tc * 9 / 5 + 32)


if __name__ == "__main__":
    tc = randint(-100, 100)
    print("tc =", tc)
    print("tf =", calculate_temperature_in_fahrenheit(tc))
