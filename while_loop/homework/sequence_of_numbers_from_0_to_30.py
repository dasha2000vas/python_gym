from random import randint

from Homework1.squares_in_a_rectangle import result


def sequence_of_numbers_from_0_to_30() -> tuple[list[int],int]:
    """
    Generates sequence of numbers from 0 to 30
    that ends with zero. Defines value of
    second-largest element in sequence.
    Note: there are at least two elements in sequence.

    Returns:
       result (list[int]): Sequence of numbers.
       second_number (int): Second-largest element in sequence.
    """
    result = [randint(1, 30), randint(1, 30)]
    while num := randint(0, 30):
        result.append(num)
    else:
        result.append(num)
    max_number = max(result)
    second_number = 0
    for num in result:
        if second_number < num < max_number:
            second_number = num
    return result, second_number


if __name__ == "__main__":
    result = sequence_of_numbers_from_0_to_30()
    print(f"{result[0]} \nSecond-largest element in sequence: {result[1]}")
