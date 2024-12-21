from math import trunc


def calculate_temperature_in_fahrenheit(TC):
    return trunc(TC * 9 / 5 + 32)


if __name__ == "__main__":
    TC = int(input("Температура по Цельсию: "))
    print("Температура по Фаренгейту: ", calculate_temperature_in_fahrenheit(TC))
