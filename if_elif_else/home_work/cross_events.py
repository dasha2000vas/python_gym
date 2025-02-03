from tools import random_time_event


def are_events_cross(
    h_start_1: int, m_start_1: int, s_start_1: int,
    h_finish_1: int, m_finish_1: int, s_finish_1: int,
    h_start_2: int, m_start_2: int, s_start_2: int,
    h_finish_2: int, m_finish_2: int, s_finish_2: int,
) -> bool:
    """
    Defines if two events are crossed.

    Args:
        h_start_1 (int): Start hour of first event.
        m_start_1 (int): Start minute of first event.
        s_start_1 (int): Start second of first event.
        h_finish_1 (int): Finish hour of first event.
        m_finish_1 (int): Finish minute of first event.
        s_finish_1 (int): Finish second of first event.
        h_start_2 (int): Start hour of second event.
        m_start_2 (int): Start minute of second event.
        s_start_2 (int): Start second of second event.
        h_finish_2 (int): Finish hour of second event.
        m_finish_2 (int): Finish minute of second event.
        s_finish_2 (int): Finish second of second event.

    Returns:
        bool: True if the two events are crossed, else False.
    """
    start_in_sec_1 = h_start_1 * 3600 + m_start_1 * 60 + s_start_1
    finish_in_sec_1 = h_finish_1 * 3600 + m_finish_1 * 60 + s_finish_1
    start_in_sec_2 = h_start_2 * 3600 + m_start_2 * 60 + s_start_2
    finish_in_sec_2 = h_finish_2 * 3600 + m_finish_2 * 60 + s_finish_2
    if (
        start_in_sec_1 <= start_in_sec_2 <= finish_in_sec_1 or
        start_in_sec_1 <= finish_in_sec_2 <= finish_in_sec_1
    ):
        return True
    return False


if __name__ == "__main__":
    h_start_1, m_start_1, s_start_1, h_finish_1, m_finish_1, s_finish_1 = random_time_event()
    h_start_2, m_start_2, s_start_2, h_finish_2, m_finish_2, s_finish_2 = random_time_event()
    print("First event:")
    print(f"start = {h_start_1}h{m_start_1}m{s_start_1}s")
    print(f"finish = {h_finish_1}h{m_finish_1}m{s_finish_1}")
    print("Second event:")
    print(f"start = {h_start_2}h{m_start_2}m{s_start_2}s")
    print(f"finish = {h_finish_2}h{m_finish_2}m{s_finish_2}")
    result = are_events_cross(
        h_start_1, m_start_1, s_start_1,
        h_finish_1, m_finish_1, s_finish_1,
        h_start_2, m_start_2, s_start_2,
        h_finish_2, m_finish_2, s_finish_2,
    )
    print(f"Events are crossed: {result}")
