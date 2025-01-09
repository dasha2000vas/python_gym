from math import ceil
from random import randint


def calculate_count_of_desks(class_a: int, class_b: int, class_c: int) -> int:
    """
    In some school, it was decided to create three new math classes and
    equip classrooms with new desks for the students. Two students can sit at each desk
        Data: number of students in each class - A, B, C
        Task: find the minimum number of desks that need to be purchased
    """
    return ceil(class_a / 2) + ceil(class_b / 2) + ceil(class_c / 2)


if __name__ == "__main__":
    class_a, class_b, class_c = randint(10, 30), randint(10, 30), randint(10, 30)
    print("Students in 1A:", class_a, "\nStudents in 1B:", class_b, "\nStudents in 1C:", class_c)
    print(f"You need {calculate_count_of_desks(class_a, class_b, class_c)} desks")
