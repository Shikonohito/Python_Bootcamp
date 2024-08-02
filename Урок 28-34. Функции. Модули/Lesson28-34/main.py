# ==============================================LESSON28==============================================
# Примеры встроенных функций - abs, sum, max
# Примеры модулей random (randInt, choice), math (ceil, floor)
# Создание функции без аргументов и его использование
# Создание функции с аргументами и его использование. Понятие параметра
# Возвращение значений в функциях. Несколько return


# num = -5
# temp = abs(num)
# print(temp)

# my_list = [1, 2, 3, 4, 5]
# sum_list = sum(my_list)
# print(sum_list)

# my_list = [5, 6, 3, 100, 2]
# max_elem = max(my_list)
# print(max_elem)


# from random import randint, choice
#
# for i in range(5):
#     num = randint(1, 100)
#     print(num, end="\t")
#
#
# my_list = ["Bob", "Tom", "Jim", "Kid"]
# for i in range(5):
#     selected = choice(my_list)
#     print(selected, end="\t")


# from math import ceil, floor
#
# my_list = [26, 12, 14, 3, 1]
# sum_list = sum(my_list)
# size_list = len(my_list)
# result = sum_list / size_list
# result_ceil = ceil(result)
# result_floor = floor(result)
# print(result, result_ceil, result_floor)


# def print_welcome():
#     print("Добро пожаловать в программу!")
#     print("Эта программа выводит текст")
#
#
# print_welcome()


# def draw_square():
#     for i in range(5):
#         print("*" * 5)
#
#
# draw_square()


# def calculate(num_1, num_2):
#     print(f"{num_1} + {num_2} = {num_1 + num_2}")
#     print(f"{num_1} - {num_2} = {num_1 - num_2}")
#     print(f"{num_1} * {num_2} = {num_1 * num_2}")
#     print(f"{num_1} / {num_2} = {num_1 / num_2}")
#     print(f"{num_1} % {num_2} = {num_1 % num_2}")
#     print(f"{num_1} // {num_2} = {num_1 // num_2}")
#     print(f"{num_1} ** {num_2} = {num_1 ** num_2}")
#     print()
#
#
# first_num = 2
# second_num = 4
# calculate(first_num, second_num)
# calculate(2, 6)
# calculate(10, 10)


# ====================================================================================================
# ПЗ 28.1 - 28.2
# ====================================================================================================


# def max_num(num_1, num_2):
#     if num_1 > num_2:
#         result = num_1
#     else:
#         result = num_2
#     return result
#
# maximum = max_num(1, 5)
# print(maximum)
#


# ====================================================================================================
# ПЗ 28.3 - 28.7
# ====================================================================================================


# ==============================================LESSON29==============================================
# Сигнатура функции. Аннотации Python 3.5.
# Упаковка - передача нескольких аргументов в один параметр
# Распаковка аргументов перед их передачей
# Аргументы по умолчанию
# Передача аргументов по ключам
# Расположение обязательных, упаковки, необязательных параметров


# def print_hello() -> None:
#     print("Hello")


# def print_msg(message: str) -> None:
#     print("Your message is \"{0}\"".format(message))


# def print_msg_to(message: str, name: str) -> None:
#     print("This message for {1}:\n{0}".format(message, name))


# def code_to_message(code: int) -> str:
#     if code == 200:
#         msg = "OK"
#     elif code == 404:
#         msg = "Not Found"
#     elif code == 408:
#         msg = "Request Timeout"
#     elif code == 503:
#         msg = "Service Unavailable"
#     else:
#         msg = "Unknown Code"
#     return msg


# print_hello()
# print_msg("Some text")
# print_msg_to("Жду от тебя ответа", "Джим")
#
# message = code_to_message(404)
# print(message)

# ====================================================================================================

# def total_sum(nums):
#     num_sum = 0
#     for num in nums:
#         num_sum += num
#     return num_sum
#
#
# num_list = [10, 20, 30, 40, 50]
# result = total_sum(num_list)
# print(result)


# def total_sum(*nums):
#     num_sum = 0
#     for num in nums:
#         num_sum += num
#     return num_sum
#
#
# result = total_sum(10, 20, 30, 40, 50)
# print(result)
#
# num_list = [10, 20, 30, 40, 50]
# result = total_sum(*num_list)
# print(result)

# ====================================================================================================

# def show_data(name: str, age=0, group="Unknown") -> None:
#     print(f"Name: {name}\t\tAge: {age}\t\tGroup: {group}")
#
#
# show_data("Tom", 18, "233BC_Python")
# # show_data()
# show_data("Jacob")
# show_data("Jim", 25)
# show_data(age=15, group="Python", name="Tom")


# def show_data(name: str, *groups: str, work="No") -> None:
#     print("Name: {}".format(name))
#     print("Groups:")
#     for group in groups:
#         print("\t{}".format(group))
#     print("Work: {}".format(work))
#
#
# show_data("Tom", "Python 10:00", "Python 13:00", "Python 19:00", work="QA Tester")


# ====================================================================================================
# ПЗ 29.1 - 29.4
# ====================================================================================================


# ==============================================LESSON30==============================================
# Local, Enclosing, Global, Built-In - LEGB
# Локальные и глобальные переменные


# Local
# def func(num):
#     num += 10
#     print(num)
#
# func(5)


# Global
# glob_num_1 = 10
# glob_num_2 = 20
# glob_list = list()
# def func():
#     num = 1
#     print(glob_num_1 + num)
#
#     global glob_num_2
#     glob_num_2 += num
#
#     glob_list.append("TEST")
#
#
# func()
# print(glob_num_1, glob_num_2, glob_list)


# Enclosing
# def outer_function(num_2):
#     num_1 = 1  # Enclosing область для func
#
#     def func(num):  # Closure/Замыкание
#         print(num_1, end="\t")
#
#         nonlocal num_2
#         num_2 += num
#         print(num_2)
#
#     return func
#
#
# inner_func = outer_function(2)  # Closure object
# inner_func(10)
# inner_func(10)
# inner_func(10)


# Built-in
# print("global:", len("Hello World"))
# def outer_function():
#     print("outer_function:", len("Hello World"))
#
#     def func():
#         print("func:", len("Hello World"))
#
#     func()
#
#
# outer_function()


# ====================================================================================================
# ПЗ 30.1 - 30.3
# ====================================================================================================


# ==============================================LESSON31==============================================
# Объекты первого класса или динамически созданные объекты
# Передача и возвращение функций как объектов - функции высших порядков


# Пример объектов первого класса
# def hello(msg) -> None:
#     print("Hello", msg)
#
#
# def goodbye(msg) -> None:
#     print("Goodbye", msg)
#
#
# say = hello
# say()
#
# say = goodbye
# say()
#
# print_smthg = [hello, goodbye]
#
# for func in print_smthg:
#     func("Teston")


# Пример функций высшего порядка
# def default_indexes(obj_list: list):
#     return range(0, len(obj_list), 1)  # range(0, 10, 1) -> (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
#
#
# def reverse_indexes(obj_list: list):
#     return range(len(obj_list) - 1, -1, -1)
#
#
# def even_indexes(obj_list: list):
#     return range(0, len(obj_list), 2)  # (0, 2, 4, 6, 8)
#
#
# def odd_indexes(obj_list: list):
#     return range(1, len(obj_list), 2)
#
#
# def print_list(obj_list: list, order):  # Функция высшего порядка, т.к. принимает функцию
#     for i in order(obj_list):
#         print(obj_list[i], end=" ")
#     print()
#
#
# nums = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
# print_list(nums, default_indexes)
# print_list(nums, reverse_indexes)
# print_list(nums, even_indexes)
# print_list(nums, odd_indexes)


# def oper_sum(num_1, num_2):
#     return num_1 + num_2
#
#
# def oper_dif(num_1, num_2):
#     return num_1 - num_2
#
#
# def oper_prod(num_1, num_2):
#     return num_1 * num_2
#
#
# def oper_choice(oper):  # Функция высшего порядка, т.к. возвращает функцию
#     choice = None
#     if oper == "+":
#         choice = oper_sum
#     elif oper == "-":
#         choice = oper_dif
#     elif oper == "*":
#         choice = oper_prod
#     return choice
#
#
# first = 20
# second = 15
# for operation_symbol in ["+", "-", "*"]:
#     operation = oper_choice(operation_symbol)
#     result = operation(first, second)
#     print(result)


# ====================================================================================================
# ПЗ 31.1 - 31.2
# ====================================================================================================


# ==============================================LESSON32==============================================
# Рекурсия
# Функциональное программирование


# def func(count):
#     if count <= 0:
#         print("END")
#     else:
#         print(count)
#         func(count - 1)
#
#
# func(5)


# ====================================================================================================
# ПЗ 32.1 - 32.5
# ====================================================================================================


# def my_greeting1():
#     print("Good morning! Have a nice day!")
#
#
# def my_greeting2():
#     print("Good day! Nice to see you!")
#
#
# def my_greeting3():
#     print("Hey! Long-time no see.")
#
#
# def my_greeting4():
#     print("Good night! See you tomorrow.")
#
#
# def greeting_recipient(greet_function):
#     print("Dear,", input("Your name: "))
#     greet_function()
#     print()
#
#
# for my_greeting in (my_greeting1, my_greeting2, my_greeting3, my_greeting4):
#     greeting_recipient(my_greeting)


# ==============================================LESSON33==============================================
# Карринг
# Декораторы
# Лямбда-выражения и анонимные функции
# map, filter, sorted


# def send_hi(user_to, msg_txt):
#     print(f"Dear {user_to}, welcome to the Python! {msg_txt}")
#
#
# def send_goodbye(user_to, msg_txt):
#     print(f"Goodbye, {user_to}! {msg_txt}")
#
#
# def send_msg(msg_type, user_to, msg_txt):
#     print(f"Message type: {msg_type}\nDear {user_to}, {msg_txt}")
#
# # def type_of_send_msg(msg_type):  # Каррированный
# #     def send_msg(user_to, msg_txt):
# #         print(f"Message type: {msg_type}\nDear {user_to}, {msg_txt}")
# #     return send_msg
#
#
# users = ["Teston", "Jim", "Kate"]
# msgs = ["Nice to see you.", "Hope to see you soon.", "The deadline has been extended by 30 days."]
# msg_selected_type = "Information"
# funcs = [send_hi, send_goodbye, send_msg]
#
# for i in range(len(funcs)):
#     funcs[i](users[i], msgs[i])
#     print()

# ====================================================================================================

# def simple_decorator(func):  # Декоратор
#     def simple_wrapper():  # Обёртка
#         print("simple_wrapper: BEFORE MAIN FUNC")
#         func()
#         print("simple_wrapper: AFTER MAIN FUNC")
#
#     return simple_wrapper
#
#
# def print_message():
#     print("print_message: Hello")
#
#
# show_message = simple_decorator(print_message)
# show_message()


# def simple_decorator(func):  # Декоратор
#     def simple_wrapper():  # Обёртка
#         print("simple_wrapper: BEFORE MAIN FUNC")
#         func()
#         print("simple_wrapper: AFTER MAIN FUNC")
#
#     return simple_wrapper
#
#
# @simple_decorator  # Применение декоратора
# def print_message():
#     print("print_message: Hello")
#
#
# print_message()


# import math
#
# print(math.sin(1.6))
#
#
# def sin_decorator(func):  # Декоратор
#     def sin_degrees(x_degrees):  # Обёртка
#         x_radians = math.radians(x_degrees)
#         return func(x_radians)
#     return sin_degrees
#
#
# sinus = sin_decorator(math.sin)
# print(sinus(90))

# ====================================================================================================

# def num_prod_two(x):
#     return x * 2
#
#
# nums = [10, 15, 20, 25, 30]
# for i in range(len(nums)):
#     print((lambda x: x * 2)(nums[i]), end=" ")  # Анонимная функция
# print()
# print(nums)


# nums = [10, 15, 20, 25, 30]
# some_lambda = lambda x: x * 2  # НЕ анонимная функция
# for i in range(len(nums)):
#     print(some_lambda(nums[i]), end=" ")
# print()
# print(nums)


# def str_num_to_int(x):
#     return int(x)
#
#
# nums = ["10", "15", "20", "25", "30"]
# print(nums)
# nums = list(map(lambda x: int(x), nums))
# print(nums)


# nums = [10, 15, 20, 25, 30]
# nums = list(filter(lambda x: x % 2 == 0, nums))  # filter требует предикат
# print(nums)

# nums = [20, 15, 10, 30, 25]
# nums = sorted(nums, key=lambda x: x)
# print(nums)

# students = [["Tom", 20], ["Jim", 15], ["Kate", 10], ["Bob", 30], ["Arthur", 25]]
# students = sorted(students, key=lambda x: x[1])
# print(students)


# num_1 = 10
# num_2 = 20
# print((lambda x, y: x * y)(num_1, num_2))

# ==============================================LESSON34==============================================
# Решение задач с использованием своих функций


# ====================================================================================================
# ДЗ34
# ====================================================================================================
