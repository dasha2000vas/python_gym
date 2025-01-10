def find_speed_in_m_s(t: int, d: int) -> float:
    """
        Data: time in hours - t
              distance in km - d
        Task: find speed in m/s
              output in format 00.000
    """
    return (d * 1000) / (t * 60 * 60)


if __name__ == "__main__":
    t = int(input("time in hours: "))
    d = int(input("distance in km: "))
    s = find_speed_in_m_s(t, d)
    print("Answer: with time = %d h and distance = %d km, speed is %.3f m/s" % (t, d, s))
