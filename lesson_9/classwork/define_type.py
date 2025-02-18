"""
Define type of object and print it in specific way.
"""
from random import  choice, randint, random
from string import ascii_letters

from tools import random_string

if __name__ == '__main__':
    entered_object = choice(
        [
            randint(1, 100),
            random(),
            random_string(words=2, letters=ascii_letters),
        ]
    )
    if isinstance(entered_object, int):
        print(f"{entered_object} is integer")
        print("{:.>20d}".format(entered_object))
    elif isinstance(entered_object, float):
        print(f"{entered_object} is float")
        print("{:_>20.2f}".format(entered_object))
    else:
        print(f"{entered_object} is string")
        print("{}".format(entered_object))
