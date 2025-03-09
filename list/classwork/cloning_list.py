from random import choice
from typing import Any


def check_values(values_list: list[list[Any]]) -> None:
    for value in values_list:
        if not isinstance(value, list):
            raise ValueError("Value must be of type list")


def clone_list_using_list_comprehension(entered_list: list[Any]) -> list[Any]:
    check_values([entered_list])
    return [obj for obj in entered_list]


def clone_list_using_cut(entered_list: list[Any]) -> list[Any]:
    check_values([entered_list])
    return entered_list[:]


def are_lists_identical(list1: list[Any], list2: list[Any]) -> list[Any]:
    check_values([list1, list2])
    return [list1 == list2, list1 is list2]


def term_in_list(entered_list: list[Any], obj: Any) -> str:
    check_values([entered_list])
    if obj in entered_list:
        return f"There is {obj} in entered list"
    return f"There is no {obj} in entered list"


if __name__ == '__main__':
     animals = ["cat", "dog", "snake", "mouse", "hamster"]
     animals_cloned1 = clone_list_using_list_comprehension(animals)
     animals_cloned2 = clone_list_using_cut(animals)
     print(f"Original: {animals}")
     print(f"Clone1: {animals_cloned1}")
     print(f"Clone2: {animals_cloned2}")
     equal1, same_id1 = are_lists_identical(animals_cloned1, animals)
     print(f"Original and clone1 equal: {equal1}, have same id: {same_id1}")
     equal2, same_id2 = are_lists_identical(animals_cloned2, animals)
     print(f"Original and clone2 equal: {equal2}, have same id: {same_id2}")
     obj = choice(animals + [1, 2, 3, "cow", "elefant", "monkey"])
     print(term_in_list(animals, obj))
