def get_result_of_calculations(n: int, k: int, m: int) -> float:
    """
    Data: a three-digit integer - n,
          number of times - k,
          power - m
    Task: find the result of next calculations -
          raise a number n to the 10th power,
          record k times in a row,
          extract m-th root
    """
    return int(str(n ** 10) * k ) ** (1 / m)


if __name__ == "__main__":
    n, k, m = int(input("n = ")), int(input("k = ")), int(input("m = "))
    result = get_result_of_calculations(n, k, m)
    print("Result: %.3f" %result)
