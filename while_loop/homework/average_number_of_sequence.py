from random import randint


def average_number_of_sequence() -> float | str:
    """
    Generates sequence of numbers between
    -10 and 10 that ends with zero. Calculates
    the average value of this sequence.

    Returns:
       float|str: Average value of sequence or message
                  that sequence contains just 0.
    """
    sequence = []
    num = randint(-10, 10)
    while True:
        print(num, end = " ")
        sequence.append(num)
        if num == 0:
            break
        num = randint(-10, 10)
    if sequence != [0]:
        return round(sum(sequence) / len(sequence), 3)
    else:
        return "\nThere are no numbers except 0"


if __name__ == '__main__':
    result = average_number_of_sequence()
    if isinstance(result, str):
        print(result)
    else:
        print(f"\nAverage value: {result}")
