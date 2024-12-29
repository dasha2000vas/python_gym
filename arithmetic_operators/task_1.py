from math import trunc


def calculate_temperature_in_fahrenheit(TC):
    """
        Data: temperature value in degrees Celsius - TC
        Task: find its temperature value in degrees Fahrenheit -TF
    """
    return trunc(TC * 9 / 5 + 32)


if __name__ == "__main__":
    TC = int(input("TC: "))
    print("TF: ", calculate_temperature_in_fahrenheit(TC))
