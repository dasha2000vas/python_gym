from tools import random_time_for_winner_and_second


def find_lag_time(hr_1: int, min_1: int, sec_1: int, hr_2: int, min_2: int, sec_2: int) -> int:
    """
    Calculates the lag time from the finish
    time of the winner and the next opponent.

    Args:
        hr_1 (int): Hours of the winner.
        min_1 (int): Minutes of the winner.
        sec_1 (int): Seconds of the winner.
        hr_2 (int): Hours of the next opponent.
        min_2 (int): Minutes of the next opponent.
        sec_2 (int): Seconds of the next opponent.

    Returns:
        int: Lag time in seconds.
    """
    return (hr_2 - hr_1) * 3600 + (min_2 - min_1) * 60 + (sec_2 - sec_1)


if __name__ == "__main__":
    hr_1, min_1, sec_1, hr_2, min_2, sec_2 = random_time_for_winner_and_second()
    print("Hr of the winner:", hr_1, "\nMin of the winner:", min_1, "\nSec of the winner:", sec_1)
    print("Hr of the second:", hr_2, "\nMin of the second:", min_2, "\nSec of the second:", sec_2)
    print("Seconds lag:", find_lag_time(hr_1, min_1, sec_1, hr_2, min_2, sec_2))
