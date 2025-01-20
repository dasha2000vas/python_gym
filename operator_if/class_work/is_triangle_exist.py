from random import randint


def is_triangle_exist(a: int, b: int, c: int) -> str:
    """
    Checks if triangle exists.

    Args:
        a (int): First side of the triangle.
        b (int): Second side of the triangle.
        c (int): Third side of the triangle.

    Returns:
        str: Says exists triangle or not.
    """
    return (
        "Triangle exists" if a + b > c and a + c > b and b + c > a
        else "Triangle does not exist"
    )


if __name__ == "__main__":
    a, b, c = randint(1, 100), randint(1, 100), randint(1, 100)
    print(f"Sides of the triangle: {a}, {b}, {c}")
    print(is_triangle_exist(a, b, c))
