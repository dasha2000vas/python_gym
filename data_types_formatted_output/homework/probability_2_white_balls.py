from math import factorial
from random import randint

from pydantic import BaseModel, Field


class BallsValues(BaseModel):
    count_of_white_balls: int = Field(ge=2, description="Number of white balls.")
    count_of_black_balls: int = Field(ge=0, description="Number of black balls.")


def probability_of_two_white_balls(values: BallsValues) -> float:
    """
    Calculates the percentage probability that two balls
    pulled out of the basket will turn out to be white.
    Uses formulas: reducing number of combinations
    (probability_white, probability_all),
    hypergeometric distribution in probability calculation
    (result).

    Args:
        values(BallsValues)

    Returns:
        float: The percentage probability.
    """
    white, black = values.count_of_white_balls, values.count_of_black_balls
    probability_white = factorial(white) / (factorial(white - 2) * 2)
    probability_all = factorial(black + white) / (factorial(black + white - 2) * 2)
    return probability_white / probability_all * 100


if __name__ == '__main__':
    count_of_white_balls, count_of_black_balls = randint(2, 100), randint(1, 100)
    print("Number of white balls:", count_of_white_balls)
    print("Number of black balls:", count_of_black_balls)
    result = probability_of_two_white_balls(BallsValues(
        count_of_white_balls=count_of_white_balls,
        count_of_black_balls=count_of_black_balls
    ))
    print("Probability: %.2f percent" %result)
