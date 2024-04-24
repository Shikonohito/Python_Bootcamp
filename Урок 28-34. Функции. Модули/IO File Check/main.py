import os.path
from time import time
from os import path, remove


def timer(func):  # Декоратор
    def wrapper(*args, **kwargs):  # Обёртка
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Execution time: {end_time - start_time} seconds. File size: {path.getsize(args[0])} Bytes. File name: {args[0]}.")
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


read_funcs = {"read_block(1)": read_block(1),
              "read_line": read_line,
              "read_block(8192)": read_block(8192),
              "read_all": read_all}

files = ["8KB.txt", "16KB.txt", "32KB.txt",
         "64KB.txt", "Newlines64KB.txt",
         "100KB.txt", "Newlines100KB.txt",
         "1MB.txt", "Newlines1MB.txt",
         "10MB.txt", "Newlines10MB.txt",
         "100MB.txt", "Newlines100MB.txt"]

for func_name, func in read_funcs.items():
    print(func_name)
    for file_name in files:
        input_file_path = f"Text files\\{file_name}"
        output_file_path = f"Text files\\Output {file_name}"
        func(input_file_path, output_file_path)
        if os.path.exists(output_file_path):
            remove(output_file_path)
    print()