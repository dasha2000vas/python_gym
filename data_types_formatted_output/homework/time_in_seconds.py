from random import randint


def check_value(time_in_seconds: int) -> None:
    if not isinstance(time_in_seconds, int):
        raise ValueError('Object time_in_seconds must be integer')
    if 86400 < time_in_seconds or time_in_seconds < 0:
        raise ValueError('Number time_in_seconds must be between 0 and 86400 (inclusive)')


def translate_from_seconds(time_in_seconds: int) -> tuple[int, int, int, int]:
    """
    Calculates number of full minutes since the beginning of the day,
    number of full hours since the beginning of the day,
    number of seconds since the beginning of the last minute,
    number of minutes since the beginning of the last hour.

    Args:
        time_in_seconds (int): Number of seconds since the beginning of the day.

    Returns:
        tuple[int, int, int, int]: Resulting numbers.
    """
    check_value(time_in_seconds)
    return  (
        time_in_seconds // 60,
        time_in_seconds // 3600,
        time_in_seconds % 60,
        time_in_seconds % 3600 // 60
    )


if __name__ == "__main__":
    time_in_seconds = randint(0, 86400)
    print("Number of seconds:", time_in_seconds)
    full_min, full_hr, remain_sec, remain_min = translate_from_seconds(time_in_seconds)
    print("Full minutes since the beginning of the day:", full_min)
    print("Full hours since the beginning of the day:", full_hr)
    print("Seconds since the beginning of the last minute:", remain_sec)
    print("Minutes since the beginning of the last hour:", remain_min)
