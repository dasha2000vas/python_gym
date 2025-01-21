from math import ceil
from random import randint


def calculate_count_of_desks(class_a: int, class_b: int, class_c: int) -> int:
    """
    Calculates how many desks need to be purchased
    to equip classrooms for three new math classes.
    Note: Two students can sit at one desk.

    Args:
        class_a (int): Count of students in class A.
        class_b (int): Count of students in class B.
        class_c (int): Count of students in class C.

    Returns:
        int: The minimum number of desks.
    """
    return ceil(class_a / 2) + ceil(class_b / 2) + ceil(class_c / 2)


if __name__ == "__main__":
    class_a, class_b, class_c = randint(10, 30), randint(10, 30), randint(10, 30)
    print("Students in 1A:", class_a, "\nStudents in 1B:", class_b, "\nStudents in 1C:", class_c)
    print(f"You need {calculate_count_of_desks(class_a, class_b, class_c)} desks")
