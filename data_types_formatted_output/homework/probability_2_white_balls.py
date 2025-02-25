from math import factorial
from random import randint


def check_values(count_of_white_balls: int, count_of_black_balls: int):
    for value in (count_of_white_balls, count_of_black_balls):
        if not isinstance(value, int):
            raise ValueError("All args must be integers")
    if count_of_white_balls < 2:
        raise ValueError("Number count_of_white_balls must be greater or equal 2")
    if count_of_black_balls < 0:
         raise ValueError("Number count_of_black_balls must be greater or equal 0")


def get_probability_of_two_white_balls(
    count_of_white_balls: int, count_of_black_balls: int
) -> float:
    """
    Calculates the percentage probability that two balls
    pulled out of the basket will turn out to be white.
    Uses formulas: reducing number of combinations
    (probability_white, probability_all),
    hypergeometric distribution in probability calculation
    (result).

    Args:
        count_of_white_balls (int): Number of white balls.
        count_of_black_balls (int): Number of black balls.

    Returns:
        float: The percentage probability.
    """
    white, black = count_of_white_balls, count_of_black_balls
    check_values(white, black)
    probability_white = factorial(white) / (factorial(white - 2) * 2)
    probability_all = factorial(black + white) / (factorial(black + white - 2) * 2)
    return probability_white / probability_all * 100


if __name__ == '__main__':
    count_of_white_balls, count_of_black_balls = randint(2, 100), randint(1, 100)
    print("Number of white balls:", count_of_white_balls)
    print("Number of black balls:", count_of_black_balls)
    result = get_probability_of_two_white_balls(
        count_of_white_balls, count_of_black_balls
    )
    print("Probability: %.2f percent" %result)
