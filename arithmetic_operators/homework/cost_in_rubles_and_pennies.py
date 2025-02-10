from random import randint


def find_cost_in_rubles_and_pennies(cost_in_pennies: int) -> tuple[int, int]:
    """
    Calculates how many rubles and pennies are in the cost.

    Args:
        cost_in_pennies (int): The cost of pennies.

    Returns:
        rubles (int): Full rubles in the cost.
        pennies (int): Remaining pennies in the cost.
    """
    return cost_in_pennies // 100, cost_in_pennies % 100


if __name__ == "__main__":
    cost_in_pennies = randint(100, 999999)
    print("Cost in pennies:", cost_in_pennies)
    rubles, pennies = find_cost_in_rubles_and_pennies(cost_in_pennies)
    print(rubles, "rubles")
    print(pennies, "pennies")
