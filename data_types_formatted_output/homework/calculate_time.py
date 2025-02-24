from random import randint

from pydantic import BaseModel, Field


class TimeInSeconds(BaseModel):
    time_in_seconds: int = Field(ge=0, le=86400, description="Number of seconds.")


def calculate_time(value: TimeInSeconds) -> tuple[int, int, int, int]:
    """
    Calculates number of full minutes since the beginning of the day,
    number of full hours since the beginning of the day,
    number of seconds since the beginning of the last minute,
    number of minutes since the beginning of the last hour.

    Args:
        value (TimeInSeconds)

    Returns:
        tuple[int, int, int, int]: Resulting numbers.
    """
    return  (
        value.time_in_seconds // 60,
        value.time_in_seconds // 3600,
        value.time_in_seconds % 60,
        value.time_in_seconds % 3600 // 60
    )


if __name__ == "__main__":
    time_in_seconds = randint(0, 86400)
    print("Number of seconds:", time_in_seconds)
    full_min, full_hr, remain_sec, remain_min = calculate_time(
        TimeInSeconds(time_in_seconds=time_in_seconds)
    )
    print("Full minutes since the beginning of the day:", full_min)
    print("Full hours since the beginning of the day:", full_hr)
    print("Seconds since the beginning of the last minute:", remain_sec)
    print("Minutes since the beginning of the last hour:", remain_min)
