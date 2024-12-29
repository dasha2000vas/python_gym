from math import trunc


def calculate_temperature_in_fahrenheit(TC):
    """
        Data: temperature value in degrees Celsius
        Task: find its temperature value in degrees Fahrenheit
    """
    return trunc(TC * 9 / 5 + 32)


if __name__ == "__main__":
    TC = int(input("Температура по Цельсию: "))
    print("Температура по Фаренгейту: ", calculate_temperature_in_fahrenheit(TC))
