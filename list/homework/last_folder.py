from re import findall

from tools import  check_path_value


def get_last_folder_from_path_using_list(path: str) -> str:
    check_path_value(path)
    if "/" in path:
        split_by = "/"
    else:
        split_by = "\\"
    return path.split(split_by)[-2]


def get_last_folder_from_path_using_regex(path: str) -> str:
    check_path_value(path)
    return findall(r"[a-zA-Z0-9_-]+", path)[-3]


if __name__ == '__main__':
    path = r"C:\Users\dev\python_gym\list\homework\file_name.py"
    file_name1 = get_file_name_from_path_using_list(path)
    file_name2 = get_file_name_from_path_using_regex(path)
    print(f"Path: {path}")
    print(f"Get last folder using list: {file_name1}")
    print(f"Get last folder using regex: {file_name2}")
