from re import findall

from tools import  check_path_value


def get_file_name_from_path_using_list(path: str) -> str:
    check_path_value(path)
    if "/" in path:
        split_by = "/"
    else:
        split_by = "\\"
    return path.split(split_by)[-1].split(".")[0]


def get_file_name_from_path_using_regex(path: str) -> str:
    check_path_value(path)
    return findall(r"[a-zA-Z0-9_-]+", path)[-2]


if __name__ == '__main__':
    path = r"C:\Users\dev\python_gym\list\homework\file_name.py"
    file_name1 = get_file_name_from_path_using_list(path)
    file_name2 = get_file_name_from_path_using_regex(path)
    print(f"Path: {path}")
    print(f"Get filename using list: {file_name1}")
    print(f"Get filename using regex: {file_name2}")
