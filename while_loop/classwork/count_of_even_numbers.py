from random import randint, choice


def count_of_even_numbers() -> int:
    """
    Counts number of even numbers in
    random sequence that ends with zero.

    Returns:
         count (int): Count of even numbers.
    """
    count = 0
    while num := randint(-10, 10):
        print(num, end = " ")
        if num % 2 == 0:
            count += 1
    return count


if __name__ == "__main__":
    print(f"\nCount = {count_of_even_numbers()}")
