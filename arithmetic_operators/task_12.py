from math import ceil

def calculate_count_of_desks(class_a, class_b, class_c):
    return ceil(class_a / 2) + ceil(class_b / 2) + ceil(class_c / 2)


if __name__ == "__main__":
    class_a = int(input("Кол-во учеников в 1A: "))
    class_b = int(input("Кол-во учеников в 1B: "))
    class_c = int(input("Кол-во учеников в 1C: "))
    print(f"Требуется {calculate_count_of_desks(class_a, class_b, class_c)} парт")
