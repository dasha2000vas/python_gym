from random import randint


def calculate_time(n: int) -> tuple[int, int, int, int]:
    """
    Calculates number of full minutes since the beginning of the day,
    number of full hours since the beginning of the day,
    number of seconds since the beginning of the last minute,
    number of minutes since the beginning of the last hour.

    Args:
        n (int): The number of seconds.

    Returns:
        tuple[int, int, int, int]: Resulting numbers.
    """
    if not isinstance(n, int):
        raise ValueError('Object n must be integer')
    if not 0 <= n <= 86400:
        raise ValueError('Number n must be between 0 and 86400')
    return  (
        n // 60,
        n // 3600,
        n % 60,
        n % 3600 // 60
    )


if __name__ == "__main__":
    n = randint(0, 86400)
    print("Number of seconds:", n)
    full_min, full_hr, remain_sec, remain_min = calculate_time(n)
    print("Full minutes since the beginning of the day:", full_min)
    print("Full hours since the beginning of the day:", full_hr)
    print("Seconds since the beginning of the last minute:", remain_sec)
    print("Minutes since the beginning of the last hour:", remain_min)
