from math import ceil

def calculate_count_of_desks(class_a, class_b, class_c):
    """
    In some school, it was decided to create three new math classes and
    equip classrooms with new desks for the students. Two students can sit at each desk
       Data: number of students in each class - A, B, C
       Task: find the minimum number of desks that need to be purchased
    """
    return ceil(class_a / 2) + ceil(class_b / 2) + ceil(class_c / 2)


if __name__ == "__main__":
    class_a = int(input("Кол-во учеников в 1A: "))
    class_b = int(input("Кол-во учеников в 1B: "))
    class_c = int(input("Кол-во учеников в 1C: "))
    print(f"Требуется {calculate_count_of_desks(class_a, class_b, class_c)} парт")
