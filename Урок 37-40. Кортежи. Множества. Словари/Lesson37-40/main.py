# ==============================================LESSON37==============================================
# Кортеж - неизменяемая, упорядоченная коллекция элементов, которая может содержать повторяющиеся элементы
# Хранение в памяти как списки, только последовательно в куче.
# Создание
# Индексация
# Проход по кортежам
# Приведение кортежа к списку и наоборот
# Операции
# Где использовать - мало памяти, быстрое обращение к элементам, неизменяемый.


# my_tuple_1 = tuple()
# my_tuple_2 = ()


# user_types = tuple(("admin", "teacher", "student"))

# my_tuple_1 = (25, True, "Text", 29.5, [1, 2])
#
# print(my_tuple_1[4])
# my_tuple_1[4] = list()
# my_tuple_1[4][0] = 5
# print(my_tuple_1[4])


# my_tuple_2 = ("admin",)
# print(type(my_tuple_2), my_tuple_2)


# user_types = ("admin", "teacher", "student")
# print(user_types[0], user_types[1], user_types[2])
# print(user_types)
# print(user_types[3])  # Ошибка IndexError


# user_names = ("Tom", "Bob", "Kid", "Jake")
# for name in user_names:
#     print(name, end=" ")
# print()
#
# len_tuple = len(user_names)
# for i in range(len_tuple):
#     print(user_names[i], end=" ")
# print()


# user_names = ("Tom", "Bob", "Kid", "Jake")
# user_names[1] = 25  # Ошибка TypeError

# user_names = ("Tom", "Bob", "Kid", "Jake")
# list_user_name = list(user_names)
# list_user_name[1] = 25
# user_names = tuple(list_user_name)
# print(user_names)


# some_list = [1, 2, 3]
# my_tuple = (10, 20, some_list)
# print(my_tuple)
#
# some_list[0] = 100
# print(my_tuple)
#
# my_tuple[2][0] = 200
# print(my_tuple)
#
# my_tuple[2] = [100, 200, 300]
# print(my_tuple)


# user_types = ("admin", "moderator", "teacher", "student")
# user_1, user_2, user_3, user_4 = user_types
# print(user_1, user_2, user_3, user_4)
#
# user_1, *other_users, user_3 = user_types
# print(user_1, other_users, user_3)


# user_types_1 = ("admin", "moderator")
# user_types_2 = ("teacher", "student")
# all_users = user_types_1 + user_types_2
# print(all_users)
#
# some_types = user_types_1 * 2
# print(some_types)


# ====================================================================================================
# Множество - неизменяемая, неупорядоченная коллекция элементов, которая содержит только уникальные элементы
# Создание
# Проход по множеству
# Добавление, удаление элементов
# Объединение, пересечение, вычитание через добавление и удаление
# Где использовать - быстрое обращение, уникальные элементы, но много памяти
#                    (около х2-х4 по сравнению со списками)

# my_set_1 = set()
# my_set_2 = set(("Bob", "Kate", "Jack", "Kate"))
# my_set_3 = {"Bob", "Kate", "Jack", "Kate"}
# my_set_4 = {"Bob", "Kate", ["Student", "Teacher"]}  # Ошибка TypeError


# my_set_4 = set(["Kate", "Kate", "Kate", "Bob", "Bob", "Kate"])
# print(my_set_4)


# my_set = {"Bob", "Kate", "Jack", "Kate"}
# print(my_set)
#
# for name in my_set:
#     print(name, end=" ")


# name_set = {"Bob", "Kate", "Jack"}
# to_find = "Kate"
# is_find = False
#
# for name in name_set:
#     if to_find == name:
#         is_find = True
#         break
#
# if is_find:
#     print("YES")
# else:
#     print("NO")


# my_set_1 = {1, 2, 3}
# my_set_2 = {3, 1, 2}
# print(my_set_1 == my_set_2)


# name_set = {"Bob", "Tom"}
# name_set.add("Jack")
# print(name_set)
# name_set.add("Jack")
# name_set.add("Jack")
# name_set.add("Jack")
# print(name_set)

# name_set.update(("Bob", "Tom", "Kate"))
# print(name_set)


# name_set = {"Bob", "Tom", "Jack", "Kate"}
# print(name_set)
# name_set.discard("Tom")
# print(name_set)
# name_set.discard("Tom")
# print(name_set)


# name_set = {"Bob", "Tom", "Jack", "Kate"}
# name_set.remove("Kate")
# print(name_set)
# name_set.remove("Kate")
# print(name_set)


# name_set_1 = {"Bob", "Jack", "Kate"}
# name_set_2 = {"Kate", "Tom"}
#
# name_set_result = name_set_1 | name_set_2
# print(name_set_result)
# name_set_result = name_set_1 & name_set_2
# print(name_set_result)
# name_set_result = name_set_1 - name_set_2
# print(name_set_result)


# name_list = ["Tom", "Tom", "Tom", "Tom", "Tom", "Tom"]
# name_set = set(name_list)
#
# import sys
# print("SIZE (bytes)")
# print(f"SET: {sys.getsizeof(name_set)}\tLIST: {sys.getsizeof(name_list)}")
# name_set.add("Kate")
# name_list.append("Kate")
# print(f"SET: {sys.getsizeof(name_set)}\tLIST: {sys.getsizeof(name_list)}")
#
# print(f"{name_set}\t\t{name_list}")
# name_list = list(name_set)

# print(f"\n{name_set}\t\t{name_list}")
# print(f"SET: {sys.getsizeof(name_set)}\tLIST: {sys.getsizeof(name_list)}")


# from sys import getsizeof
# my_tuple = tuple()
# my_set = set()
# my_list = list()
# my_str = str()
#
# print(type(my_tuple), type(my_set), type(my_str), type(my_list), sep="\t")
# print(getsizeof(my_tuple), getsizeof(my_set), getsizeof(my_str), getsizeof(my_list),
#       sep=" bytes\t\t", end=" bytes\n")
#
# my_tuple = tuple(("Tom",))
# my_set = set({"Tom"})
# my_list = list("Tom")
# my_str = str("Tom")
#
# print(getsizeof(my_tuple), getsizeof(my_set), getsizeof(my_str), getsizeof(my_list),
#       sep=" bytes\t\t", end=" bytes\n")


# from sys import getsizeof
# my_set = {"Tom"}
# print(f"{getsizeof(my_set)} bytes\t\t{my_set}")
# my_set.add("Kate")
# print(f"{getsizeof(my_set)} bytes\t\t{my_set}")
# my_set.add("Bob")
# print(f"{getsizeof(my_set)} bytes\t\t{my_set}")
# my_set.add("Jack")
# print(f"{getsizeof(my_set)} bytes\t\t{my_set}")
# my_set.add("Arthur")
# print(f"{getsizeof(my_set)} bytes\t\t{my_set}")


# ====================================================================================================
# ПЗ 37.1 - 37.4

# ПЗ 37.1
# from datetime import datetime
# date_str = "28/04/2028"
# date_format = "%d/%m/%Y"
# expiration_date  = datetime.strptime(date_str, date_format).date()
# current_date = datetime.now().date()
#
# if current_date > expiration_date:
#     print("Просрочено")
# else:
#     print(f"Осталось {(expiration_date - current_date).days} дней до истечения срока")
# ====================================================================================================


# ==============================================LESSON38==============================================
# Ассоциативный массив или словарь
# Изменяемая, упорядоченная коллекция пар {ключ: значение}. Значение могут повторяться, изменяться, ключи - нет.
# Хранение в памяти - ключ хешируется (превращается в адрес) и по этому адресу находится элемент.
# Создание
# Индексация
# Проход по словарю
# Операции и действия над словарями
# Перевод словаря в список
# Где использовать - быстрое обращение и добавление, но много памяти.


# my_dict_1 = dict()
# my_dict_2 = {}
# book = {"author": "Eric Matthes", "title": "Python Crash Course", "price": 14.43, "reading age": "12 years and up", "language": "English"}
# print(book)


# book = {"author": "Eric Matthes",
#         "title": "Python Crash Course",
#         "price": 14.43,
#         "reading age": "12 years and up",
#         "language": "English"}
#
# print(book["author"])
# print(book.get("author"))
# print(book["number of pages"])
# print(book.get("number of pages"))


# book = {"author": "Eric Matthes",
#         "title": "Python Crash Course",
#         "price": 14.43,
#         "reading age": "12 years and up",
#         "language": "English"}
#
# for key in book:
#     print(f"{key}: {book[key]}", end="\t")
#
# print()
# for key in book.keys():
#     print(f"{key}: {book[key]}", end="\t")
#
# print()
# for key, value in book.items():
#     print(f"{key}: {value}", end="\t")
#
# print()
# for value in book.values():
#     print(f"{value}", end="\t")


# book = {"author": "Eric Matthes",
#         "title": "Python Crash Course",
#         "price": 14.43,
#         "reading age": "12 years and up",
#         "language": "English"}
#
# for key in book:
#     print(f"{key}: {book[key]}", end="\t")
#
# book["language"] = "Russian"
#
# print()
# for key in book:
#     print(f"{key}: {book[key]}", end="\t")
#
# book["number of pages"] = 378
#
# print()
# for key in book:
#     print(f"{key}: {book[key]}", end="\t")
#
# del book["number of pages"]
#
# print()
# for key in book:
#     print(f"{key}: {book[key]}", end="\t")


# book = {"author": "Eric Matthes",
#         "title": "Python Crash Course",
#         "price": 14.43,
#         "reading age": "12 years and up",
#         "language": "English"}
#
# some_key = "language"
#
# if some_key in book:
#     del book[some_key]
# else:
#     print("Ключ отсутствует.")
#
# for key in book:
#     print(f"{key}: {book[key]}", end="\t")


# student_grade_1 = {"Tom": 65, "Kate": 15}
# student_grade_2 = {"Jack": 20, "Bob": 40, "Kate": 25}
# student_grade_1.update(student_grade_2)
# for key in student_grade_1:
#     print(f"{key}: {student_grade_1[key]}", end="\t\t")


# student_grade_1 = {"Tom": 65, "Kate": 15}
# student_grade_2 = {"Jack": 20, "Bob": 40, "Kate": 25}
# all_grades = dict()
# all_grades.update(student_grade_1)
# all_grades.update(student_grade_2)
#
# for key in student_grade_1:
#     print(f"{key}: {student_grade_1[key]}", end="\t\t")
# print()
# for key in student_grade_2:
#     print(f"{key}: {student_grade_2[key]}", end="\t\t")
# print()
# for key in all_grades:
#     print(f"{key}: {all_grades[key]}", end="\t\t")


# students = {"Jack": 20, "Bob": 40, "Kate": 25}
# print(students.keys())
# print(students.values())
# some_list = list(students)
# print(some_list)


# student_grade = {"Jack": 20, "Bob": 40, "Kate": 25}
# print(student_grade)
#
# key_tuple = ("Jack", "Bob", "Kate")
# value_list = [20, 40, 25]
# some_dict = dict()
#
# for i in range(len(key_tuple)):
#     some_dict[key_tuple[i]] = value_list[i]
#
# print(some_dict)


# my_tuple = (1, 2, 3)
# my_dict = {my_tuple: "TEXT"}  # хешированный тип ключа
# print(my_dict)

# my_tuple = (1, 2, [100, 200, 300])
# my_dict = {my_tuple: "TEXT"}  # НЕ хешированый тип ключа
# print(my_dict)

# my_set = {1, 2, 3}
# my_dict = {my_set: "TEXT"}  # НЕ хешированый тип ключа
# print(my_dict)


# from sys import getsizeof
#
# some_tuple = tuple()
# some_set = set()
# some_dict = dict()
# some_str = str()
# some_list = list()
#
# print(type(some_tuple), type(some_set), type(some_dict), type(some_str), type(some_list), sep="\t")
# print(getsizeof(some_tuple), getsizeof(some_set), getsizeof(some_dict), getsizeof(some_str),
#       getsizeof(some_list), sep=" bytes\t\t", end=" bytes\n")
#
# some_tuple = tuple(["key_1", 5])
# some_set = {"key_1", 5}
# some_dict = {"key_1": 5}
# some_str = "key_1 5"
# some_list = ["key_1", 5]
#
# print(getsizeof(some_tuple), getsizeof(some_set), getsizeof(some_dict), getsizeof(some_str),
#       getsizeof(some_list), sep=" bytes\t\t", end=" bytes\n")


# ====================================================================================================
# ПЗ 38.1 - 38.2
# ====================================================================================================


# ==============================================LESSON39-40==============================================
# Работа со вложенными словарями


# ====================================================================================================
# ДЗ 40.1
# ====================================================================================================
