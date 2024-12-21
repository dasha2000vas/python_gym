def find_x(result):
    last_number = result // 100
    return result % 100 * 10 + last_number


if __name__ == "__main__":
    result = int(input("Результат вычисления: "))
    print("Искомое число:", find_x(result))
