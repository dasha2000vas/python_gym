from random import randint


def type_of_triangle(angle1: int, angle2: int) -> str:
    """
    Defines if triangle exist by its two angles.
    Also defines following criteria for triangle:
    1. right-angled, blunt-angled, acute-angled
    2. equilateral, isosceles, scalene

    Args:
        angle1 (int): First angle in degrees.
        angle2 (int): Second angle in degrees.

    Returns:
        criteria (str): Type of triangle or message what it doesn't exist.
    """
    criteria = ""
    angle3 = 180 - angle1 - angle2
    if angle3 <= 0 or angle1 <= 0 or angle2 <= 0:
        return "doesn't exist"
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        criteria += "is right-angled "
    elif angle1 > 90 or angle2 > 90 or angle3 > 90:
        criteria += "is blunt-angled "
    else:
        criteria += "is acute-angled "
    if angle1 == angle2 == angle3:
        criteria += "and equilateral"
    elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
        criteria += "and isosceles"
    else:
        criteria += "and scalene"
    return criteria


if __name__ == "__main__":
    angle1, angle2 = randint(0,180), randint(0,180)
    print(f"Triangle with angles {angle1} and {angle2} {type_of_triangle(angle1, angle2)}")
