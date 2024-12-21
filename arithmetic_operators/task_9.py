def find_cost_in_rubles_and_kopeks(cost):
    return cost // 100, cost % 100


if __name__ == "__main__":
    cost = int(input("Введите стоимость в копейках: "))
    r, k = find_cost_in_rubles_and_kopeks(cost)
    print(r, "рублей")
    print(k, "копеек")
