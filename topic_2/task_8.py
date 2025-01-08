def calculate_time(n: int) -> tuple[int, int, int, int]:
    """
    Data: n seconds have passed since the beginning of the day (n is an integer)
    Task: find the number of full minutes, number of full hours,
          number of seconds that have passed since the beginning of the last minute,
          number of minutes that have passed since the beginning of the last hour
    """
    return  n // 60, n // 3600, n % 60, n % 3600 //60


if __name__ == "__main__":
    n = int(input("Enter a number of seconds: "))
    full_min, full_hr, remain_sec, remain_min = calculate_time(n)
    print("Full minutes since the beginning of the day:", full_min)
    print("Full hours since the beginning of the day:", full_hr)
    print("Seconds since the beginning of the last minute:", remain_sec)
    print("Minutes since the beginning of the last hour:", remain_min)
