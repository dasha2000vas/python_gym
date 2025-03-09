"""
Generates list from random number
of integers between first to last.
Prints this list using while cycle.
"""

from random import randint

if __name__ == '__main__':
    first, last, times = randint(1, 100), randint(1, 100), randint(1, 10)
    if first > last:
        first, last = last, first
    print(f"first: {first}, last: {last}, times: {times}")
    list_of_numbers = [randint(first, last) for _ in range(times)]
    index = 0
    while index < len(list_of_numbers):
        print(list_of_numbers[index], end=" ")
        index += 1
