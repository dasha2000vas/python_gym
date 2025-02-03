from datetime import datetime

from tools import random_time_event


def are_events_cross(
    start1: datetime, finish1: datetime, start2: datetime, finish2: datetime
) -> bool:
    """
    Defines if two events are crossed.

    Args:
        start1 (datetime): Start datetime of first event.
        finish1 (datetime): Finish datetime of first event.
        start2 (datetime): Start datetime of second event.
        finish2 (datetime): Finish datetime of second event.

    Returns:
        bool: True if the two events are crossed, else False.
    """
    for dt in [start1, finish1, start2, finish2]:
        if not isinstance(dt, datetime):
            raise ValueError("Both start and finish datetime must be of type datetime.")
    start1_sec = start1.timestamp()
    finish1_sec = finish1.timestamp()
    start2_sec = start2.timestamp()
    finish2_sec = finish2.timestamp()
    if (
        start1_sec <= start2_sec <= finish1_sec or
        start1_sec <= finish2_sec <= finish1_sec
    ) or (
            start2_sec < start1_sec and finish2_sec > finish1_sec
    ):
        return True
    return False


if __name__ == "__main__":
    start1, finish1 = random_time_event()
    start2, finish2 = random_time_event(start1.year, start1.month, start1.day)
    print("First event:")
    print(f"start = {start1}")
    print(f"finish = {finish1}")
    print("Second event:")
    print(f"start = {start2}")
    print(f"finish = {finish2}")
    result = are_events_cross(
        start1, finish1, start2, finish2
    )
    print(f"Events are crossed: {result}")
