from math import factorial


def probability_of_two_white_balls(n: int, m: int) -> float:
    """
    There are n white and m black balls in the basket. Two balls are pulled out of it
    Data: number of white balls - n,
          number of black balls - m
    Task: find the percentage probability that two balls pulled out
          of the basket will turn out to be white
    """
    probability_n = factorial(n) / (factorial(n - 2) * 2)
    probability_m = factorial(m) / (factorial(m - 0) * 1)
    probability_all = factorial(m + n) / (factorial(m + n - 2) * 2)
    return probability_n * probability_m / probability_all * 100


if __name__ == '__main__':
    n, m = int(input("Number of white balls: ")), int(input("Number of black balls: "))
    result = probability_of_two_white_balls(n, m)
    print("Probability: %.2f percent" %result)
