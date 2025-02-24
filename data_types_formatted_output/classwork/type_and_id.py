"""
Prints type of each object and its ID.
"""

if __name__ == "__main__":
    example_number = 15
    example_string = "Hello"
    example_float = 14.58
    example_list = (14, 66, 376)
    example_tuple = [14, 66, 376]

    print("example_number - ", type(example_number), ", id - ", id(example_number), sep='')
    print("example_string - ", type(example_string), ", id - ", id(example_string), sep='')
    print("example_float - ", type(example_float), ", id - ", id(example_float), sep='')
    print("example_list - ", type(example_list), ", id - ", id(example_list), sep='')
    print("example_tuple - ", type(example_tuple), ", id - ", id(example_tuple), sep='')
