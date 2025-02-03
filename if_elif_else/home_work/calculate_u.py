from random import uniform


def calculate_u(x: float, y: float, z: float) -> float|str:
    """
    Calculate value of expression.

    Args:
        x (float): First number.
        y (float): Second number.
        z (float): Third number.

    Returns:
        float|str: Resulting number or message what result doesn't exist.
    """
    if not isinstance(x, float) or not isinstance(y, float) or not isinstance(z, float):
        raise ValueError("x, y and z must be floats")
    if (divider := x + y - z) == 0:
        return "There is no solution"
    else:
        return round((max(x, y, z) + min(x, y, z)) / divider, 3)


if __name__ == "__main__":
    x, y, z = uniform(-100, 100), uniform(-100, 100), uniform(-100, 100)
    print(f"x = {x:.3f} \ny = {y:.3f} \nz = {z:.3f}")
    result = calculate_u(x, y, z)
    print(f"u = {result}" if isinstance(result, float) else result)
