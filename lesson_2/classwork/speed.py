from random import randint


def find_speed_in_m_s(time: int, distance: int) -> float:
    """
    Calculates speed in m/s.

    Args:
        time (int): Time in hours.
        distance (int): Distance in km.

    Returns:
        float: Speed in m/s.
    """
    for number in (time, distance):
        if not isinstance(number, int):
            raise ValueError('All args must be integers')
        if number <= 0:
            raise ValueError('All numbers must be positive')
    return (distance * 1000) / (time * 60 * 60)


if __name__ == "__main__":
    time, distance = randint(1, 10), randint(1, 1000)
    print(f"Time in hours: {time} \nDistance: {distance}")
    speed = find_speed_in_m_s(time, distance)
    print("Answer: with time = %d h and distance = %d km, speed is %.3f m/s" % (time, distance, speed))
