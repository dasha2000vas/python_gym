from tools import random_time_for_winner_and_second

from pydantic import BaseModel, Field, model_validator


class TimeValues(BaseModel):
    hr_1: int = Field(ge=0, description="Hours of winner.")
    min_1: int = Field(ge=0, le=59, description="Minutes of winner.")
    sec_1: int = Field(ge=0, le=59, description="Seconds of winner.")
    hr_2: int = Field(ge=0, description="Hours of next opponent.")
    min_2: int = Field(ge=0, le=59, description="Minutes of next opponent.")
    sec_2: int = Field(ge=0, le=59, description="Seconds of next opponent.")

    @property
    def seconds_of_winner(self) -> int:
        return self.hr_1 * 3600 + self.min_1 * 60 + self.sec_1

    @property
    def seconds_of_next_opponent(self) -> int:
        return self.hr_2 * 3600 + self.min_2 * 60 + self.sec_2

    @model_validator(mode="after")
    def validate_time(self) -> "TimeValues":
        if self.seconds_of_winner > self.seconds_of_next_opponent:
            raise ValueError("Time of winner cannot be greater than time of next opponent")
        return self


def find_lag_time(values: TimeValues) -> int:
    return values.seconds_of_next_opponent - values.seconds_of_winner


if __name__ == "__main__":
    hr_1, min_1, sec_1, hr_2, min_2, sec_2 = random_time_for_winner_and_second()
    print("Hr of the winner:", hr_1, "\nMin of the winner:", min_1, "\nSec of the winner:", sec_1)
    print("Hr of the second:", hr_2, "\nMin of the second:", min_2, "\nSec of the second:", sec_2)
    lag_time = find_lag_time(TimeValues(
        hr_1=hr_1, min_1=min_1, sec_1=sec_1,
        hr_2=hr_2, min_2=min_2, sec_2=sec_2
    ))
    print("Seconds lag:", lag_time)
