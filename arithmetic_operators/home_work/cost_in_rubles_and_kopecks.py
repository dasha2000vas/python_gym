from random import randint


def find_cost_in_rubles_and_kopecks(cost: int) -> tuple[int, int]:
    """
       Data: cost of the product in kopecks
       Task: find cost in rubles and kopecks
    """
    return cost // 100, cost % 100


if __name__ == "__main__":
    cost = randint(100, 999999)
    print("Cost in kopecks:", cost)
    r, k = find_cost_in_rubles_and_kopecks(cost)
    print(r, "rubles")
    print(k, "kopecks")
