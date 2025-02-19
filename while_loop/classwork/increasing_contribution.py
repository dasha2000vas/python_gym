from random import randint


def increasing_contribution(start_rubles: int, goal_rubles: int, percent: int) -> int:
    """
    Defines how many years you need for increasing
    contribution from start rubles to finish rubles.
    Note: after increasing decimal part of value discards.

    Args:
        start_rubles (int): Start amount of rubles.
        goal_rubles (int): Goal amount of rubles.
        percent (int): Percent of contribution (one time in year).

    Returns:
        count_of_years (int): Count of years.
    """
    for num in (start_rubles, goal_rubles, percent):
        if not isinstance(num, int):
            raise ValueError("All numbers must be integers")
        if num <= 0:
            raise ValueError("All numbers must be positive")
    count_of_years = 0
    current_rubles = start_rubles
    while current_rubles < goal_rubles:
        current_rubles += int(current_rubles * percent / 100)
        count_of_years += 1
    return count_of_years


if __name__ == "__main__":
    start_rubles, goal_rubles, percent = randint(1, 1000), randint(1001, 10000), randint(1, 20)
    print(f"start_rubles = {start_rubles}, goal_rubles = {goal_rubles}, percent = {percent}")
    count_of_years = increasing_contribution(start_rubles, goal_rubles, percent)
    print(f"You need {count_of_years} years")
