def find_cost_in_rubles_and_kopecks(cost):
    """
       Data: cost of the product in kopecks
       Task: find cost in rubles and kopecks
    """
    return cost // 100, cost % 100


if __name__ == "__main__":
    cost = int(input("Cost in kopecks: "))
    r, k = find_cost_in_rubles_and_kopecks(cost)
    print(r, "rubles")
    print(k, "kopecks")
