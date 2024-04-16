# ==============================================LESSON21==============================================
# Понятие коллекции
# Неизменяемая упорядоченная коллекция символов, которая может содержать повторяющиеся элементы
# Сложение строк и умножение строки на число
# Позиция каждого символа
# Str - immutable (неизменяемый)
# len()


# my_str = "Monty Python"
# print(my_str[11])


# my_str_1 = "Hello"
# my_str_2 = "World"
# print(my_str_1 + my_str_2)
# print(my_str_1 * 5)


# my_str = "Hello"
# print(my_str[0], my_str[1], my_str[2], my_str[3], my_str[4])  # Вывод по индексу
# print(my_str[-1], my_str[-2], my_str[-3], my_str[-4], my_str[-5])  # Использование отрицательных индексов
# print(my_str[5])  # Ошибка Out of Range - выход за границу памяти


# Иммутабельность (неизменяемость элементов)
# my_str = "Hello"
# my_str[0] = "B"  # Ошибка - объект иммутабелен, не может быть изменён
# print(my_str[0], my_str[1], my_str[2], my_str[3], my_str[4], sep="\t\t\t\t")


# my_str = "Hello"
# len_text = len(my_str)
# print(len_text)
#
# my_str = "Hello"
# len_text = 0
# for symbol in my_str:
#     len_text += 1
# print(len_text)


# my_str = "Hello"
# for symbol in my_str:
#     print(symbol)

# my_str = "Hello"
# len_text = len(my_str)
# for i in range(len_text):
#     print(my_str[i])
#
# my_str = "Hello"
# len_text = 0
# for symbol in my_str:
#     len_text += 1
#
# i = 0
# while i < len_text:
#     print(my_str[i], end=" ")
#     i += 1


# my_str = input("Введите слово: ")
# len_text = len(my_str)
# for i in range(len_text):
#     print(my_str[i], end="\t")


# ====================================================================================================
# ПЗ 21.1 - 21.10
# ====================================================================================================


# ==============================================LESSON22==============================================
# Срезы
# Экранированные последовательности \
# Raw strings - сырые строки
# .format()
# Где лучше применять


# my_str = "HelloWorld"
# my_str_1 = my_str[0:5]
# my_str_2 = my_str[5:]
# my_str_3 = my_str[0:5:2]
# my_str_4 = my_str[::-1]
#
# print(my_str_1)
# print(my_str_2)
# print(my_str_3)
# print(my_str_4)

# my_str = "Monty Python"
# result = my_str[6:10]
# print(result)
# print(my_str[-12:-7])

# my_str = "HelloWorld"
# my_str_1 = my_str[:5] + " " + my_str[5:]
# print(my_str_1)

# ====================================================================================================
# ПЗ 22.1
# ====================================================================================================

# file_path = "C:\new folder\trade.py"
# print(file_path)
#
# file_path = "C:\\new folder\\trade.py"
# print(file_path)
#
# text = r"aaa\t\t\tbbb\t\t\tccc\nddd\t\t\teee\t\t\tfff"
# print(text)
#
# text = 'It\'s "me"!'
# print(text)
#
# text = '''Some
# big\t\ttext'''
# print(text)


# name = "Teston"
# age = 25
# height_m = 1.79
# weight_kg = 86.5
#
# print("Name:", name, "\t|\tAge:", age, "\t|\tHeight:", height_m, "meters\t|\tWeight:", weight_kg, "kg")
#
# result_str = "Name: {0}\t|\tAge: {1} \t|\tHeight: {2} meters\t|\tWeight: {3} kg"
# print(result_str.format(name, age, height_m, weight_kg))
#
# result_str = "Name: {n}\t|\tAge: {a} \t|\tHeight: {h} meters\t|\tWeight: {w} kg"
# print(result_str.format(n=name, a=age, h=height_m, w=weight_kg))
#
# result_str = f"Name: {name}\t|\tAge: {age} \t|\tHeight: {height_m} meters\t|\tWeight: {weight_kg} kg"
# print(result_str)


# obj = "text"
# print("Some " + obj)

# obj = 5
# print("Some {0}".format(obj))


# ====================================================================================================
# ПЗ 22.2 - 22.5
# ====================================================================================================


# ==============================================LESSON23==============================================
# Разбор задач:
# 1. Определение наличия символа в строке
# 2. Определение индекса первого вхождения символа
# 3. Определение индексов первого вхождения символа из набора в строке
# 4. Подсчёт количество символов из набора символов в строке
# 5. Определение наличия только указанных символов
# 6. Удаление указанного символа из строки
# 7. Замена больших букв на маленькие буквы для русских букв
# 8. Замена символа на другой символ


# 1.
# my_str = "Hello World One Two"
# to_find = "o"
# len_text = len(my_str)
# is_find = False
#
# i = 0
# while i < len_text:
#     if my_str[i] == to_find:
#         is_find = True
#         break
#     i += 1
#
# if is_find:
#     print("Found!")
# else:
#     print("Not found!")

# ====================================================================================================

# 2.
# my_str = "Hello World One Two"
# to_find = "o"
# len_text = len(my_str)
# found_index = -1
#
# i = 0
# while i < len_text:
#     if my_str[i] == to_find:
#         found_index = i
#         break
#     i += 1
#
# print(found_index)

# ====================================================================================================

# 3.
# my_str = "Hello 5 World9"
# to_find = "0123456789"
# len_text = len(my_str)
# len_find = len(to_find)
# found_index = -1
#
# is_find = False
# i = 0  # С какого символа искать
# while i < len_text:
#     j = 0  # Для прохода по набору символов
#     while j < len_find:
#         if my_str[i] == to_find[j]:
#             found_index = i
#             is_find = True
#             break
#         j += 1
#
#     if is_find:
#         break
#     i += 1
#
# print(found_index)

# ====================================================================================================

# 4.
# my_str = "Hello 5 World9"
# to_find = "0123456789"
# len_text = len(my_str)
# len_find = len(to_find)
# found_count = 0
#
# i = 0  # С какого символа искать
# while i < len_text:
#     j = 0  # Для прохода по набору символов
#     while j < len_find:
#         if my_str[i] == to_find[j]:
#             found_count += 1
#             break
#         j += 1
#     i += 1
# print(found_count)

# ====================================================================================================

# 5.
# my_str = "59"
# to_find = "0123456789"
# len_text = len(my_str)
# len_find = len(to_find)
# is_num = False
#
# i = 0  # С какого символа искать
# while i < len_text:
#     j = 0  # Для прохода по набору символов
#     is_num = False
#     while j < len_find:
#         if my_str[i] == to_find[j]:
#             is_num = True
#             break
#         j += 1
#     if not is_num:
#         break
#     i += 1
#
# if is_num:
#     print("Only nums")
# else:
#     print("Not only nums")

# ====================================================================================================

# 6.
# my_str = "А буду я у дуба"
# to_delete = " "
# result = ""
# len_text = len(my_str)
#
# i = 0
# while i < len_text:
#     if my_str[i] != to_delete:
#         result += my_str[i]
#     i += 1
#
# print(result)

# ====================================================================================================

# 7.
# my_str = "А Буду Я У Дуба"
# ru_big = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
# ru_small = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# result = ""
# len_text = len(my_str)
# len_big = len(ru_big)
#
# i = 0
# while i < len_text:
#     is_changed = False
#     j = 0
#     while j < len_big:
#         if my_str[i] == ru_big[j]:
#             result += ru_small[j]
#             is_changed = True
#             break
#         j += 1
#     if not is_changed:
#         result += my_str[i]
#     i += 1
#
# print(result)

# ====================================================================================================

# 8.
# my_str = "abcabcdabc abcd"
# symb_find = "d"
# symb_change = "x"
# len_text = len(my_str)
# result = ""
#
# i = 0
# while i < len_text:
#     if my_str[i] != symb_find:
#         result += my_str[i]
#     else:
#         result += symb_change
#     i += 1
# print(result)

# ==============================================LESSON24==============================================
# Методы строк
# 9. Поиск последовательности символов
# 10. Замена последовательности символов на другую последовательность символов


# text = "SoMe teXt"
# text_upper = text.upper()
# text_lower = text.lower()
# text_title = text.title()
# text_swap_case = text.swapcase()
#
# print(text_upper, text_lower, text_title, text_swap_case, sep="\n")


# my_str = "Какой-то большой текст с несколькими словами и несколькими буквами"
# count_symb = my_str.count("о", 0, len(my_str))
# print(count_symb)

# my_str = "Какой-то большой текст с несколькими словами и несколькими буквами"
# find_symb_index = my_str.find("о", 0, len(my_str))
# print(find_symb_index)

# my_str = "Какой-то большой текст с несколькими словами и несколькими буквами"
# find_symb_index = my_str.find("о", 0, len(my_str))
# while find_symb_index != -1:
#     print(find_symb_index)
#     find_symb_index = my_str.find("о", find_symb_index + 1, len(my_str))

# my_str = "Какой-то большой текст с несколькими словами и несколькими буквами"
# find_symb = my_str.index("о", 0, len(my_str))
# while find_symb != -1:
#     print(find_symb)
#     find_symb = my_str.index("о", find_symb + 1, len(my_str))

# my_str = "text5"
# if my_str.isalnum():
#     print("YES")
# else:
#     print("NO")

# my_str = "text"
# if my_str.isalpha():
#     print("YES")
# else:
#     print("NO")

# my_str = "666"
# if my_str.isdigit():
#     print("YES")
# else:
#     print("NO")

# my_str = "TEXT"
# if my_str.isupper():
#     print("YES")
# else:
#     print("NO")

# my_str = "text"
# if my_str.islower():
#     print("YES")
# else:
#     print("NO")


# import string
# print(string.digits)


# ====================================================================================================

# 9.
# text = "abcabcdabc abcd"
# to_find = "abcd"
#
# len_text = len(text)
# len_find = len(to_find)
# found_index = -1
#
# i = 0
# while i < len_text:
#     is_find = True
#     j = 0
#     while j < len_find:
#         if i + j < len_text and text[i + j] != to_find[j]:
#             is_find = False
#             break
#         j += 1
#     if is_find and i + j <= len_text:
#         found_index = i
#         break
#     i += 1
#
# print(found_index)

# ====================================================================================================
# 10.
# text = "abcabcdabc abcd"
# to_find = "abcd"
# to_change = "xx"
# len_text = len(text)
# len_find = len(to_find)
# result = ""
#
# i = 0
# while i < len_text:
#     is_find = True
#     j = 0
#     while j < len_find:
#         if i + j < len_text and text[i + j] != to_find[j]:
#             is_find = False
#             break
#         j += 1
#     if is_find and i + j <= len_text:
#         result += to_change
#         i += len_find
#     else:
#         result += text[i]
#         i += 1
#
# print(result)

# ====================================================================================================

# ==============================================LESSON25==============================================
# Понятие массива
# Изменяемая упорядоченная коллекция, которая может содержать повторяющиеся элементы
# Создание списков - list(), []
# Индексация списков
# Как хранится в памяти
# Ввод списка в одной строке - split()
# Вывод списка - print(), for elem in list, for i in range()
# Поиск элемента
# Сумма всех элементов

# my_list_1 = list()
# my_list_2 = []

# my_list_3 = list([26, 15, 27, 9, 10])
# my_list_4 = [26, True, "Text", 9.5]

# print(my_list_4)


# my_list = [26, True, "Text", 9.5]
# print(my_list[0], my_list[1], my_list[2], my_list[3])
# print(my_list[4])  # Ошибка Out of Range
#
# my_list[2] = 25
# print(my_list)


# my_list = [100, 200, 300, 400]
# my_list.append("Teston")
# my_list.insert(2, "Teston")
# print(my_list)
# print(my_list[0], my_list[1], my_list[2], my_list[3], my_list[4])


# my_list = input("Введите последовательность чисел: ").split()
# len_list = len(my_list)
# for i in range(len_list):
#     my_list[i] = int(my_list[i])
#
# print(my_list)


# my_list = [10, True, "Text", 5.5]
# print(my_list)

# print(*my_list)

# for item in my_list:
#     print(item, end=" ")
# print()

# len_list = len(my_list)
# for i in range(len_list):
#     print(my_list[i], end=" ")


# ====================================================================================================
# ПЗ 25.1 - 25.3
# ====================================================================================================


# ==============================================LESSON26==============================================
# Операции со списками - добавление, объединение, удаление, изменение, принадлежность
# Срезы списков


# my_list = list()
# my_list.append(25)
# my_list.append("Text")
# my_list.append(True)
# my_list.insert(0, 1.33)
# print(my_list)


# my_list_1 = [1, 2, 3]
# my_list_2 = ["a", "b", "c"]
# my_list_3 = my_list_1 + my_list_2
# print(my_list_3)

# print(my_list_1)
# my_list_1.extend(my_list_2)
# print(my_list_1)


# my_list = ["Bob", "Jim", "Teston", "Kid", "Arthur", "Kate", "Lisa", "Teston"]
# my_list[1] = 47
# print(my_list)

# del my_list[2]
# print(my_list)
#
# del my_list[4]
# print(my_list)

# my_list.remove("Teston")
# print(my_list)
#
# elem = my_list.pop(2)
# print(elem)
# print(my_list)


# my_list = ["Jake", "Teston", "Bob", "Jim"]
# to_find = "Jake"
# is_find = False
# for elem in my_list:
#     if elem == to_find:
#         is_find = True
#         break
# if is_find:
#     print("YES")
# else:
#     print("NO")

# my_list = ["Teston", "Bob", "Jim", "Jake"]
# to_find = "Jake"
# found_index = -1
# len_my_list = len(my_list)
# for i in range(len_my_list):
#     if my_list[i] == to_find:
#         found_index = i
#         break
# if found_index == -1:
#     print("Not found")
# else:
#     print(found_index)


# my_list = ["Teston", "Bob", "Jim", "Teston", "Kid"]
# print(my_list.index("Teston"))
# print(my_list.count("Teston"))
# print(my_list[1::2])


# ====================================================================================================
# ПЗ 26.1
# ====================================================================================================


# ==============================================LESSON27==============================================
# Копирование списков
# Матрицы
# Где лучше применять


# start = 0
# end = start
# start = 10
#
# print(start, end)


# my_list_1 = ["a", "b", "c"]
# my_list_2 = my_list_1
# print(my_list_1, my_list_2, sep="\t\t\t")
#
# my_list_1[0] = 25
# print(my_list_1, my_list_2, sep="\t\t\t")


# my_list_1 = ["a", "b", "c", [100, 200]]
# len_list = len(my_list_1)
#
# my_list_2 = list()
# for i in range(len_list):
#     my_list_2.append(my_list_1[i])
#
# print(my_list_1, my_list_2, sep="\t\t\t")
#
# my_list_1[0] = 25
# print(my_list_1, my_list_2, sep="\t\t\t")


# my_list_1 = ["a", "b", "c"]
# # my_list_2 = list(my_list_1)
# my_list_2 = my_list_1.copy()
# print(my_list_1, my_list_2, sep="\t\t\t", end=" ")
# print()
# my_list_1[0] = 25
# print(my_list_1, my_list_2, sep="\t\t\t", end=" ")


# my_list = ["a", "b", [100, [2001, 2002], 300]]
# print(my_list[2][1][0])


# name_list = ["Bob", "Tom", "Jim"]
# date_list = ["27.06.2023", "12.06.2023", "22.04.2023"]
# grade_list = [12, 11, 12]
# my_table = [name_list, date_list, grade_list]

# my_table = [["Bob", "Tom", "Jim"], ["27.06.2023", "12.06.2023", "22.04.2023"], [12, 11, 12]]

# print(my_table)

# for row in my_table:
#     print(row)

# for li in my_table:
#     for elem in li:
#         print(elem, end="\t\t\t")
#     print()

# for i in range(len(my_table)):
#     for j in range(len(my_table[i])):
#         print(my_table[j][i], end="\t\t")
#     print()


# my_matrix_1 = [["00", "01", "02"], ["10", "11"], 30]
# my_matrix_2 = my_matrix_1
# print(my_matrix_1, my_matrix_2, sep="\n", end="\n\n")
#
# my_matrix_2[0] = 100
# print(my_matrix_1, my_matrix_2, sep="\n")


# my_matrix_1 = [["00", "01", "02"], ["10", "11"], 30]
# my_matrix_2 = list(my_matrix_1)
# my_matrix_2 = my_matrix_1.copy()
# print(my_matrix_1, my_matrix_2, sep="\n", end="\n\n")
#
# my_matrix_2[0][1] = 100
# print(my_matrix_1, my_matrix_2, sep="\n")


# import copy
# my_matrix_1 = [["00", "01", "02"], ["10", "11"], 30]
# my_matrix_2 = copy.deepcopy(my_matrix_1)
# print(my_matrix_1, my_matrix_2, sep="\n", end="\n\n")
#
# my_matrix_2[0][1] = 100
# print(my_matrix_1, my_matrix_2, sep="\n")

# ====================================================================================================
# Задание 30 - дан список
#              my_list = [155, 255, [True, False], ["Tom", [12, "RU", ["Python", "C#"]]], 68]
#              Вывести в консоль число 68 из этого списка.
#              Вывести в консоль "RU" из этого списка.
#              Вывести в консоль "Python" из этого списка.

# Задание 31 - дан список
#              my_list = ["weather", [[12, 39.4, "windy"], [13, 39.2, "sunny"]]]
#              Вывести в консоль "sunny" из этого списка.

# Задание 32 - дан список
#              my_list = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#              используйте .append() или .insert(), чтобы получился список
#              1. [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
#              2. [10, 20, [300, 400, [5000, 6000], 500, 600], 30, 40]
#              3. [10, 20, [300, 400, [5000, 6000], 450, 500], 30, 40]
#              4. [10, 20, [300, 400, [5000, 6000], 500], 30, 35, 40]
#              5. [10, 20, [300, 400, [5000, 6000], 500], 30, 40, [800, 900]]

# Задание 33 - программа должна найти в следующем списке максимальный среди всех элемент, а также
#              максимальный элемент в каждом списке.
#              my_list = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
#              Из максимальных элементов нужно составить отдельный список.

# Задание 34 - пользователь вводит число n. Потом n раз вводит через пробел Имя, Возраст, пол М или Ж.
#              Оформить эти данные в виде вложенного списка. Реализовать меню:
#              1. Поиск данных
#              2. Добавить данные
#              3. Удалить данные
#              4. Завершить программу
# ====================================================================================================