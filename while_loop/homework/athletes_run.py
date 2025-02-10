from random import randint


def increasing_athletes_run(first_day_distance: int, goal_distance: int) -> int:
    """
    Defines how many days athlete needs for increasing
    distance (km) from first day distance to goal distance.
    Note: Every day distance increases by 10%.

    Args:
        first_day_distance (int): First day distance in km.
        goal_distance (int): Goal distance in km.

    Returns:
        count_of_days (int): Count of days.
    """
    for num in (first_day_distance, goal_distance):
        if not isinstance(num, int):
            raise ValueError("All numbers must be integers")
        if num <= 0:
            raise ValueError("All numbers must be positive")
    count_of_days = 1
    current_distance = first_day_distance
    while current_distance < goal_distance:
        current_distance += current_distance * 0.1
        count_of_days += 1
    return count_of_days


if __name__ == "__main__":
    first_day_distance = randint(1, 10)
    goal_distance = randint(first_day_distance + 1, first_day_distance + 10)
    print(f"first_day_distance = {first_day_distance},", end=" ")
    print(f"goal_distance = {goal_distance}")
    count_of_days = increasing_athletes_run(first_day_distance, goal_distance)
    print(f"Athlete needs {count_of_days} days")
