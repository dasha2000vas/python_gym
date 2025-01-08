def find_lag_time(hr_1: int, min_1: int, sec_1: int, hr_2: int, min_2: int, sec_2: int) -> int:
    """
    Data: the finish time of the winner and the next opponent -
          hours, minutes, seconds
    Task: find the lag time in seconds
    """
    return (hr_2 - hr_1) * 3600 + (min_2 - min_1) * 60 + (sec_2 - sec_1)


if __name__ == "__main__":
    hr_1, min_1, sec_1 = (
        int(input("Hr of the winner: ")),
        int(input("Min of the winner: ")),
        int(input("Sec of the winner: "))
    )
    hr_2, min_2, sec_2 = (
        int(input("Hr of the second: ")),
        int(input("Min of the second: ")),
        int(input("Sec of the second: "))
    )
    print("Seconds lag:", find_lag_time(hr_1, min_1, sec_1, hr_2, min_2, sec_2))
