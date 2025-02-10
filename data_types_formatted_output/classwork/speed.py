def find_speed_in_m_s(time: int, distance: int) -> float:
    """
    Calculates speed in m/s.

    Args:
        time (int): Time in hours.
        distance (int): Distance in km.

    Returns:
        float: Speed in m/s.
    """
    return (distance * 1000) / (time * 60 * 60)


if __name__ == "__main__":
    time = int(input("time in hours: "))
    distance = int(input("distance in km: "))
    speed = find_speed_in_m_s(time, distance)
    print("Answer: with time = %d h and distance = %d km, speed is %.3f m/s" % (time, distance, speed))
