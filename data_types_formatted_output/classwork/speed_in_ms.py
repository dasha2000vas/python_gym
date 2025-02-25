from random import randint


def check_values(time_in_hr: int, distance_in_km: int) -> None:
    for value in (time_in_hr, distance_in_km):
        if not isinstance(value, int):
            raise ValueError("All args must be integers")
        if value <= 0:
            raise ValueError("All numbers must be positive")


def get_speed_in_ms(time_in_hr: int, distance_in_km: int) -> float:
    check_values(time_in_hr, distance_in_km)
    return (distance_in_km * 1000) / (time_in_hr * 60 * 60)


if __name__ == "__main__":
    time_in_hr, distance_in_km = randint(1, 10), randint(1, 1000)
    print(f"Time in hours: {time_in_hr} \nDistance in km: {distance_in_km}")
    speed = get_speed_in_ms(time_in_hr, distance_in_km)
    print("Answer: with time = %d h and distance = %d km, speed is %.3f m/s" % (time_in_hr, distance_in_km, speed))
