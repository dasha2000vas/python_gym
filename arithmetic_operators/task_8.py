def find_b_in_a(a, b):
    if a < b:
        raise ValueError("A не может быть меньше B")
    return a // b, a % b


if __name__ == "__main__":
    print("Введите два целых положительных числа - A и B (A > B)")
    a = int(input("A = "))
    b = int(input("B = "))
    count, remain = find_b_in_a(a, b)
    print(f"В отрезке A вмещается {count} B, {remain} - длина оставшейся части")
