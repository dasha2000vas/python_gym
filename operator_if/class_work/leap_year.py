from random import randint


def is_year_leap(year: int) -> str:
    """
    Defines if year is leap.

    Args:
        year (int): Year value.

    Returns:
        str: Says year is leap or not.
    """
    return (
        "is leap year" if not year % 4 and
        (year % 100 or not year % 400)
        else "is ordinary year"
    )


if __name__ == "__main__":
    year = randint(400, 2050)
    print(f"{year} {is_year_leap(year)} ")
