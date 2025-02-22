from math import factorial
from random import randint


def probability_of_two_white_balls(n: int, m: int) -> float:
    """
    Calculates the percentage probability that two balls
    pulled out of the basket will turn out to be white.

    Args:
        n (int): Number of white balls.
        m (int): Number of black balls.

    Returns:
        float: The percentage probability.
    """
    for number in (n, m):
        if not isinstance(number, int):
            raise ValueError("All args must be integers")
    if n < 2:
        raise ValueError("Number n must be greater or equal 2")
    if m < 0:
        raise ValueError("Number m must be greater or equal 0")
    probability_n = factorial(n) / (factorial(n - 2) * 2)
    probability_all = factorial(m + n) / (factorial(m + n - 2) * 2)
    return probability_n / probability_all * 100


if __name__ == '__main__':
    n, m = randint(2, 100), randint(1, 100)
    print("Number of white balls:", n, "\nNumber of black balls:", m)
    result = probability_of_two_white_balls(n, m)
    print("Probability: %.2f percent" %result)
