from math import log10, factorial
from decimal import Decimal
from os.path import isfile
from os import remove


CPU_HZ = 4.8 * 1_000_000_000
N_LIST = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]


def convert_seconds(seconds: float):
    time = dict()

    time["seconds"] = seconds % 60

    minutes = seconds // 60
    time["minutes"] = minutes % 60

    hours = minutes // 60
    time["hours"] = hours % 24

    days = hours // 24
    time["days"] = days % 365

    years = days // 365
    time["years"] = years

    return time


def get_time_const(n, frequency):
    time = Decimal(100) / Decimal(frequency)
    return float(time)


def get_time_logn(n, frequency):
    time = Decimal(log10(n)) / Decimal(frequency)
    return float(time)


def get_time_n(n, frequency):
    time = Decimal(n) / Decimal(frequency)
    return float(time)


def get_time_nlogn(n, frequency):
    time = Decimal(n * log10(n)) / Decimal(frequency)
    return float(time)


def get_time_nn(n, frequency):
    time = Decimal(n * n) / Decimal(frequency)
    return float(time)


def get_time_2pown(n, frequency):
    if n <= 1_000:
        time = Decimal(pow(2, n)) / Decimal(frequency)
    else:
        time = 0
    return float(time)


def get_time_nfact(n, frequency):
    if n <= 100:
        time = Decimal(factorial(n)) / Decimal(frequency)
    else:
        time = 0
    return float(time)


def time_to_str(time: dict):
    result_str = ""
    if time["years"] != 0:
        result_str += f"{time["years"]:.0f} лет "
    if time["days"] != 0:
        result_str += f"{time["days"]:.0f} дней "
    if time["hours"] != 0:
        result_str += f"{time["hours"]:.0f} часов "
    if time["minutes"] != 0:
        result_str += f"{time["minutes"]:.0f} минут "
    if time["years"] != 0 or time["days"] != 0 or time["hours"] != 0 or time["minutes"] != 0:
        result_str += f"{time["seconds"]:.0f} секунд"
    elif time["seconds"] != 0:
        result_str += f"{time["seconds"]:.12f} секунд"
    else:
        result_str = "inf"
    return result_str


func_list = [get_time_const, get_time_logn, get_time_n, get_time_nlogn,
             get_time_nn, get_time_2pown, get_time_nfact]

file_path = "time.txt"
if isfile(file_path):
    remove(file_path)

with open(file_path, "ab") as file_output:
    file_output.write("n,Время O(1),Время O(log n),Время O(n),Время O(n log n),Время O(n^2),Время O(2^n),Время O(n!)".encode("utf-8"))
    for n in N_LIST:
        file_output.write(f"\n{n}".encode("utf-8"))
        for func in func_list:
            time_seconds = round(func(n, CPU_HZ), 12)
            time_dict = convert_seconds(time_seconds)
            time_str = time_to_str(time_dict)
            file_output.write(f",{time_str}".encode("utf-8"))
