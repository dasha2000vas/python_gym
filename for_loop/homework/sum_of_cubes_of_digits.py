def numbers_equal_to_its_sum_of_cubes_of_digits() -> list[int]:
    """
    Finds three-digit numbers that
    equal to its sum of its digits.

    Returns:
       result (list[int]): Resulting list.
    """
    result = []
    for i in range(100, 1000):
        if (i // 100) ** 3 + (i // 10 % 10) ** 3 + (i % 10) ** 3 == i:
            result.append(i)
    return result


if __name__ == "__main__":
    print("Three-digit numbers that equal to its sum of its digits:")
    result = numbers_equal_to_its_sum_of_cubes_of_digits()
    for number in result:
        print(number)
