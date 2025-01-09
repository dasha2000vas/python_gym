from random import choice


def count_value(a: int, b: int, c: int, d: int) -> float:
    """
       Data: integers not equal to zero - a, b, c, d
             if a=0 or b=0 the value will always be negative
             if c=0 or d=0 there will be division by zero
       Task: calculate the value of the expression y = 3ab - 4 / (cd)
    """
    return round(3 * a * b - 4 / (c * d), 3)


if __name__ == "__main__":
    numbers = [i for i in range(-50, 50) if i != 0]
    a, b, c, d = choice(numbers), choice(numbers), choice(numbers), choice(numbers)
    print("a =", a, "\nb =", b, "\nc =", c, "\nd =", d)
    print("Result:", count_value(a, b, c, d))
