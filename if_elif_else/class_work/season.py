from random import randint


def get_season(month: int) -> str:
    """
    Defines if month exist and gets its season.

    Args:
        month (int): The month number.

    Returns:
        str: Season of month.
    """
    if not 1 <= month <= 12:
        raise ValueError("Month must be between 1 and 12")
    if not isinstance(month, int):
        raise ValueError("Month must be integer")
    match month:
        case 12 | 1 | 2:
            return "Winter"
        case 3 | 4 | 5:
            return "Spring"
        case 6 | 7 | 8:
            return "Summer"
        case 9 | 10 | 11:
            return "Autumn"


if __name__ == "__main__":
    month = randint(1, 20)
    season = get_season(month)
    if "There" in season:
        print(f"{season} {month}")
    else:
        print(f"Season of month {month} is {get_season(month)}")
