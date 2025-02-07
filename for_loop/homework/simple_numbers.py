from random import  randint

def get_simple_numbers(a: int, b: int) -> list[int]:
    """
    Finds all simple numbers between a and b.

    Args:
        a (int): Start of range.
        b (int): End of range.

    Returns:
        result (list[int]): List of simple numbers.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("a and b must be integers")
    if a < 0 or b < 0:
        raise ValueError("a and b mustn't be negative")
    if b <= a:
        raise ValueError("b must be greater than a")
    result = []
    for i in range(a, b + 1):
        simple = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                simple = False
        if simple and i not in (0, 1):
            result.append(i)
    return result


if __name__ == "__main__":
    a, b = randint(0, 50), randint(51, 100)
    print(f"a = {a}, b = {b}")
    print(f"Simple numbers: {get_simple_numbers(a, b)}")
