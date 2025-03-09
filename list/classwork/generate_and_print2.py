"""
Generates list from random number
of integers between number and -number.
Prints this list using unpacking.
"""

from random import randint

if __name__ == '__main__':
    number, times = randint(1, 100), randint(1, 10)
    print(f"Number: {number}, times: {times}")
    list_of_numbers = [randint(-number, number) for _ in range(times)]
    print(*list_of_numbers)
