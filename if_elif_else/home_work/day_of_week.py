from random import randint


def get_day_of_week(day_of_year: int, jan1: int) -> int:
    """
    Defines day of week number.

    Args:
        day_of_year (int): Day of year (1-365).
        jan1 (int): Day of week number of 1 january (1-7).

    Returns:
        int: Day of week number.
    """
    if not 1 <= day_of_year <= 365:
        raise ValueError("Day of year must be between 1 and 365.")
    if not 1 <= jan1 <= 7:
        raise ValueError("Day of week number of 1 january must be between 1 and 7.")
    day_of_week = jan1 + day_of_year % 7 - 1
    if 1 <= day_of_week <= 7:
        return day_of_week
    else:
        return day_of_week % 7


if __name__ == "__main__":
    day_of_year, jan1 = randint(1, 365), randint(1, 7)
    print(f"Day of year: {day_of_year} \nDay of week number of 1 january: {jan1}")
    print(f"Day of week number: {get_day_of_week(day_of_year, jan1)}")
