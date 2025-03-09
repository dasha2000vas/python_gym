"""
Performs operations with a list of strings.
"""

if __name__ == "__main__":
    list1 = ["cat", "dog", "fish", "snake", "mouse"]
    print(f"list1 = {list1} {len(list1)}")
    list2 = []
    print(f"list2 = {list2} {len(list2)}")
    list2 = list1
    print(f"list2 = {list2} {len(list2)}")
    list1[0] = "Very well!"
    list2[2] = "Excellently!"
    print(f"list1 = {list1}")
    print(f"list2 = {list2}")
