from random import randint


def calculate_profit_indicators(first_profit: int | float, percent: int, years: int) -> float:
    """
    Calculate profit indicators for entered number of years.
    1. There is no profit in first year.
    2. In second year profit will be equal to value first_profit.
    3. In subsequent years, profit will increase by a percentage
    from the previous year.

    Args:
        first_profit (int|float): Second year's profit.
        percent (int): Percentage of profit increase.
        years (int): Number of years.

    Returns:
        float: Profit indicators.
    """
    for number in (percent, years):
        if not isinstance(number, int):
            raise ValueError("Percent and years value must be integers")
    if not isinstance(first_profit, (int, float)):
        raise ValueError("Second year's profit must be integer or float")
    for number in (first_profit, percent, years):
        if number <= 0:
            raise ValueError("All args must be positive")
    if years == 1: return 0
    if years == 2: return first_profit
    return round(calculate_profit_indicators(
        first_profit + first_profit / 100 * percent,
        percent,
        years - 1
    ), 3)


if __name__ == '__main__':
    first_profit, percent, years = randint(1,1000), randint(1,10), randint(1,10)
    print(f"First profit: {first_profit}, percent: {percent}, years: {years}")
    print(f"Result: {calculate_profit_indicators(first_profit, percent, years)}")
