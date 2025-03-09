"""
Performs operations with a list of numbers.
"""

if __name__ == '__main__':
    list_of_numbers = [55, 4, 66, 12, 72, 1, 3]
    print(f"List: {list_of_numbers} {len(list_of_numbers)}")
    print(f"Member with index 0: {list_of_numbers[0]}")
    print(f"Member with index 3: {list_of_numbers[3]}")
    print(f"Member with index 5: {list_of_numbers[5]}")
    list_of_numbers[0] = "string"
    print(f"List after replacement: {list_of_numbers}")
    print(f"Length of first member: {len(list_of_numbers[0])}")
