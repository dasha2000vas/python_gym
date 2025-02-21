from random import uniform, choice


def get_roots_count(a: float, b: float, c: float) -> str:
    """
    Defines roots count of quadratic equation
    using .

    Args:
        a (float): First coefficient (!=0).
        b (float): Second coefficient.
        c (float): Third coefficient.

    Returns:
       str: Roots count or message
            that there are no roots.
    """
    for num in (a, b, c):
        if not isinstance(num, float):
            raise ValueError('All numbers must be float')
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return "Equation has no roots"
    if discriminant > 0:
        return "Equation has two roots"
    else:
        return "Equation has one root"


if __name__ == '__main__':
    a = choice([uniform(-10, -1), uniform(1, 10)])
    b, c = uniform(-10, 10), uniform(-10, 10)
    print(f"a = {a:.3f}, b = {b:.3f}, c = {c:.3f}")
    print(get_roots_count(a, b, c))
