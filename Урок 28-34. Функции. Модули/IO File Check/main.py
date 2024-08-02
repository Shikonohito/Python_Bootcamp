from time import time
from os import remove
from os.path import isfile, exists


def timer(func):  # Декоратор
    def wrapper(*args, **kwargs):  # Обёртка
        start_time = time()
        func(*args, **kwargs)
        end_time = time()
        result = end_time - start_time
        return result
    return wrapper


def read_block(size):
    @timer
    def read_byte(input_file_path, output_file_path):
        with open(input_file_path, "r") as input_file:
            with open(output_file_path, "w") as output_file:
                content = input_file.read(size)
                while content:
                    output_file.write(content)
                    content = input_file.read(size)
    return read_byte


@timer
def read_line(input_file_path, output_file_path):
    with open(input_file_path, "r") as input_file:
        with open(output_file_path, "w") as output_file:
            line = input_file.readline()
            while line:
                output_file.write(line)
                line = input_file.readline()


@timer
def read_all(input_file_path, output_file_path):
    with open(input_file_path, "r") as file:
        content = file.read()

    with open(output_file_path, "w") as file:
        file.write(content)


def init_tbl(func_names: tuple, file_path="time.txt"):
    if isfile(file_path):
        remove(file_path)
    with open(file_path, "ab") as file_output:
        file_output.write("data_type,".encode("utf-8"))
        for i in range(len(func_names) - 1):
            file_output.write(f"{func_names[i]},".encode("utf-8"))
        file_output.write(f"{func_names[len(func_names) - 1]}".encode("utf-8"))


def start_check_func_time(funcs: dict, files: tuple, result_out: dict):
    for file_name in files:
        result_dict[file_name] = []
        print(f"File: {file_name}")
        for func_name, func_read in funcs.items():
            print(f"Func name: {str(func_name).ljust(25)}Time: ", end="")
            input_fp = f"Text files\\{file_name}"
            output_fp = f"Text files\\Output {file_name}"
            result_time = func_read(input_fp, output_fp)
            result_out[file_name].append(result_time)
            print(f"{str(result_time).ljust(18)} sec.")
            if exists(output_fp):
                remove(output_fp)
        print()


def write_to_txt(some_str: str, file_path="time.txt"):
    with open(file_path, "ab") as file_output:
        file_output.write(some_str.encode("utf-8"))


def dict_to_str(some_dict: dict):
    result = ""
    for key, item_list in some_dict.items():
        result += f"\n{key}," + ",".join(map(str, item_list))
    return result


WRITE_PATH = "time.txt"

read_funcs = {"read_block(1)": read_block(1),
              "read_line": read_line,
              "read_block(8192)": read_block(8192),
              "read_all": read_all}

files_txt = ("8KB.txt", "16KB.txt", "32KB.txt",
             "64KB.txt", "Newlines64KB.txt",
             "100KB.txt", "Newlines100KB.txt",
             "1MB.txt", "Newlines1MB.txt",
             "10MB.txt", "Newlines10MB.txt",
             "100MB.txt", "Newlines100MB.txt")

result_dict = dict()

start_check_func_time(read_funcs, files_txt, result_dict)
init_tbl(tuple(read_funcs.keys()), WRITE_PATH)
key_value_str = dict_to_str(result_dict)
write_to_txt(key_value_str, WRITE_PATH)


