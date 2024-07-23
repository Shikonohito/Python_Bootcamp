from os.path import isfile
from os import remove
from random import randint


def read_from_txt(path: str) -> str:
    content = ""
    with open(path, "r", encoding="utf-8") as input_file:
        content = input_file.read()
    return content


def names_str_to_names_list(names: str) -> list:
    return names.split('\n')


def init_txt(path: str) -> None:
    if isfile(path):
        remove(path)
    with open(path, "w") as file:
        file.write("")


def get_random_id_str() -> str:
    num = randint(1, 999999)
    num_str = str(num)
    return ("0" * (6 - len(num_str))) + num_str


def has_id(names: dict, some_id: str) -> bool:
    return some_id in names


def get_unique_id(names: dict) -> str:
    while True:
        name_id = get_random_id_str()
        if not has_id(names, name_id):
            break
    return name_id


def names_list_to_dict(names: list) -> dict:
    result_dict = dict()
    for name in names:
        name_id = get_unique_id(result_dict)
        result_dict["№" + name_id] = name
    return result_dict


def names_dict_to_str(names: dict, size: int) -> str:
    pairs_list = [f"{name}    {id_}" for id_, name in names.items()]
    blocks_list = [pairs_list[i:i + size] for i in range(0, len(pairs_list), size)]
    block_strings = ['\n'.join(block) for block in blocks_list]
    result_str = '\n\n'.join(block_strings)
    return result_str


def save_to_txt(path: str, data_str: str) -> None:
    with open(path, "a", encoding="utf-8") as file:
        file.write(data_str)


LOAD_NAMES_PATH = "names.txt"
names_str = read_from_txt(LOAD_NAMES_PATH)
names_list = names_str_to_names_list(names_str)
names_dict = names_list_to_dict(names_list)
names_str = names_dict_to_str(names_dict, 27)

SAVE_NAMES_PATH = "saved_names.txt"
init_txt(SAVE_NAMES_PATH)
save_to_txt(SAVE_NAMES_PATH, names_str)
