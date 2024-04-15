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



# Множество - неизменяемая, неупорядоченная коллекция элементов, которая содержит только уникальные элементы
# Создание
# Проход по множеству
# Добавление, удаление элементов
# Объединение, пересечение, вычитание через добавление и удаление
# Где использовать - быстрое обращение, уникальные элементы, но много памяти
#                    (около х2-х4 по отношению к спискам)

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
# name_set.discard("Tom")
# print(name_set)
# name_set.discard("Tom")
# print(name_set)

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
# name_set.add("Kate")
# print(sys.getsizeof(name_set), sys.getsizeof(name_list))


# print(name_list)
# print(name_set)
#
# name_list = list(name_set)
# print(name_list)


# import sys
# my_tuple = tuple()
# my_set = set()
# my_list = list()
# my_str = str()
#
# print(sys.getsizeof(my_tuple), sys.getsizeof(my_set), sys.getsizeof(my_list), sys.getsizeof(my_str))

# ====================================================================================================
# Задание 1 - пользователь вводит Имя, Фамилию, Год рождения, Пол на отдельных строках.
#             Нужно сформировать из этих данных кортеж.

# Задание 2 - пользователь вводит Имя, Фамилию, Год рождения, Пол на отдельных строках. Из них
#             формируется кортеж. Далее программа предлагает пользователю снова ввести новые
#             данные или закончить программу. Требуется сформировать список из кортежей.
#             Выполнить задание, создав свою функцию ввода данных и свою функцию меню.

# Задание 3 - есть кортеж с названиями производителей автомобилей. Пользователь вводит название, которое
#             хочет поменять, и название, на которое хочет поменять. Программа должна заменить все найденные
#             названия. Совпадение должно быть полным.

# Задание 4 - есть кортеж с числами от 0 до 9999 включительно. Требуется вывести статистику
#             по количеству цифр в числах. Например:
#             (5869, 123, 1588)
#             Одна цифра - 0
#             Две цифры - 0
#             Три цифры - 1
#             Четыре цифры - 2

# Задание 5 - пользователь вводит числа через пробел. Нужно вывести только уникальные числа.

# Задание 6 - пользователь вводит на первой строке слово, затем на второй строке тоже слово.
#             программа должна определить, является ли второе слово анаграммой первого.
#             Например из слова "night" можно анаграммой получить слово "thing" (одинаковые буквы и количество).
# ====================================================================================================


# ==============================================LESSON38==============================================
# Ассоциативный массив или словарь
# Изменяемая, упорядоченная коллекция пар {ключ : значение}. Значение могут повторяться, изменяться, ключи - нет.
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

# print(book["author"])
# print(book.get("author"))
# print(book["number of pages"])
# print(book.get("number of pages"))

# for key in book:
#     print(f"{key}: {book[key]}")

# for key in book.keys():
#     print("{}: {}".format(key, book[key]))

# for value in book.values():
#     print("{}".format(value))

# for key, value in book.items():
#     print("{}: {}".format(key, value))


# book = {"author": "Eric Matthes",
#         "title": "Python Crash Course",
#         "price": 14.43,
#         "reading age": "12 years and up",
#         "language": "English",
#         "number of pages": 319}


# for key in book:
#     print("{}: {}".format(key, book[key]))

# book["language"] = "Russian"  # Изменение значения по ключу
# for key in book:
#     print("{}: {}".format(key, book[key]))

# book["number of pages"] = 378  # Добавление пары "ключ: значение".
# for key in book:
#     print("{}: {}".format(key, book[key]))

# del book["number of pages"]  # Удаление пары "ключ: значение".
# for key in book:
#     print("{}: {}".format(key, book[key]))


# student_grade_1 = {"Tom": 65, "Kate": 15}
# student_grade_2 = {"Jack": 20, "Bob": 40, "Kate": 25}
# student_grade_1.update(student_grade_2)
# for key in student_grade_1:
#     print("{}: {}".format(key, student_grade_1[key]))


# student_grade_1 = {"Tom": 65, "Kate": 15}
# student_grade_2 = {"Jack": 20, "Bob": 40, "Kate": 25}
# all_grades = dict()
# all_grades.update(student_grade_1)
# all_grades.update(student_grade_2)
#
# for key in student_grade_1:
#     print("{}: {}".format(key, student_grade_1[key]), end="    ")
# print()
# for key in student_grade_2:
#     print("{}: {}".format(key, student_grade_2[key]), end="    ")
# print()
# for key in all_grades:
#     print("{}: {}".format(key, all_grades[key]), end="    ")


# student_grade = {"Jack": 20, "Bob": 40, "Kate": 25}
# print(student_grade.keys())
# print(student_grade.values())
# my_list = list(student_grade)
# print(my_list)


# student_grade = {"Jack": 20, "Bob": 40, "Kate": 25}
# key_tuple = ("Jack", "Bob", "Kate")
# value_list = [20, 40, 25]
#
# student_grade = {}
#
# for i in range(len(key_tuple)):
#     student_grade[key_tuple[i]] = value_list[i]
#
# print(student_grade)


# my_tuple = (1, 2, 3)
# my_dict = {my_tuple: "TEXT"}  # хешированный тип ключа
# print(my_dict)

# my_tuple = (1, 2, [100, 200, 300])
# my_dict = {my_tuple: "TEXT"}  # НЕ хешированый тип ключа
# print(my_dict)

# my_set = {1, 2, 3}
# my_dict = {my_set: "TEXT"}  # НЕ хешированый тип ключа
# print(my_dict)


# import sys
#
# some_tuple = tuple()
# some_set = set()
# some_dict = dict()
# some_str = str()
# some_list = list()
#
# print(type(some_tuple), type(some_set), type(some_dict), type(some_str), type(some_list), sep="\t")
# print(sys.getsizeof(some_tuple), sys.getsizeof(some_set),
#       sys.getsizeof(some_dict), sys.getsizeof(some_str), sys.getsizeof(some_list), sep="\t\t\t\t")


# some_tuple = tuple(["key_1", 5])
# some_set = {"key_1", 5}
# some_dict = {"key_1": 5}
# some_str = "key_1 5"
# some_list = ["key_1", 5]
#
# print(sys.getsizeof(some_tuple), sys.getsizeof(some_set),
#       sys.getsizeof(some_dict), sys.getsizeof(some_str), sys.getsizeof(some_list), sep="\t\t\t\t")


# ====================================================================================================
# Задание 7 - реализовать следующее меню:
#             1. Показать данные пользователей
#             2. Зарегистрировать пользователя
#             3. Удалить пользователя
#             4. Изменить пароль пользователя
#             Для регистрации пользователя нужно указать логин и пароль.
#             Изначально словарь пустой. Заполнять словарь по формату {"логин": "пароль"}.

# Задание 8 - реализовать следюущее меню:
#             1. Показать данные студента
#             2. Изменить ФИО
#             3. Изменить возраст
#             4. Изменить группу
#             5. Добавить оценку
#             Изначально данные студента следующего вида:
#             {"f_name": "Unknown", "l_name": "Unknown", "m_name": "Unknown",
#              "age": 0, "grades": []}


# Задание 9 - реализовать следующее меню:
#             1. Показать данные всех пользователей
#             2. Добавить нового пользователя
#             3. Найти пользователя по логину
#             4. Изменить информацию по логину
#             5. Удалить пользователя по логину
#             6. Завершить программу
#             Пользователь это словарь с ключами "login", "password", "l_name", "f_name", "birth_date".
#             Все пользователи должны храниться в списке. Изначально список пользователей пустой.
#             Для пункта 2 сделайте так, чтобы невозможно было добавить пользователя, login которого
#             уже есть в списке пользователей.
#             Для пункта 4 сделайте так, чтобы программа показывала меню:
#             1. Изменить логин
#             2. Изменить пароль
#             3. Изменить фамилию
#             4. Изменить имя
#             5. Изменить дату рождения
#             6. Вернуться в главное меню
#             В этом случае для пункта 1 сделайте так, чтобы невозможно было изменить логин пользователя
#             на тот, который уже используется для какого-либо пользователя в списке.
# ====================================================================================================


# ==============================================LESSON39==============================================
# Работа со вложенными словарями


# user = {"id": "1234ABC",
#         "full_name": {"l_name": "Jackson", "f_name": "Tom"},
#         "birth_date": {"day": 10, "month": 2, "year": 1994},
#         "bank_cards": [{"id": "1234123412341234",
#                         "f_name": "Tom", "l_name": "Jackson",
#                         "month": 10, "year": 2026, "balance": 1500},
#                        {"id": "5869586958695869",
#                         "f_name": "Kate", "l_name": "Jackson",
#                         "month": 2, "year": 2025, "balance": 1050}]}


user_full_name_1 = {"l_name": "Jackson", "f_name": "Tom"}
user_birth_date_1 = {"day": 10, "month": 2, "year": 1994}
card_1 = {"id": "1234123412341234", "f_name": "Tom", "l_name": "Jackson",
          "month": 10, "year": 2026, "balance": 1500}
card_2 = {"id": "5869586958695869", "f_name": "Kate", "l_name": "Jackson",
          "month": 2, "year": 2025, "balance": 1050}
user_bank_cards_1 = [card_1, card_2]
user_1 = {"id": "1234ABC",
        "full_name": user_full_name_1,
        "birth_date": user_birth_date_1,
        "bank_cards": user_bank_cards_1}


user_full_name_2 = {"l_name": "Morgan", "f_name": "Arthur"}
user_birth_date_2 = {"day": 6, "month": 12, "year": 1988}
user_bank_cards_2 = []
user_2 = {"id": "QWE1234",
          "full_name": user_full_name_2,
          "birth_date": user_birth_date_2,
          "bank_cards": user_bank_cards_2}


def get_user_data_by_id(some_list: list, some_id: str) -> str:
    user_str_data = ""
    for user in some_list:
        if user["id"] == some_id:
            user_str_data = f'ID: {user["id"]}\nFull name: {user["full_name"]["f_name"]} {user["full_name"]["l_name"]}'
            user_str_data += f'\nBirth date: {user["birth_date"]["day"]}.{user["birth_date"]["month"]}.{user["birth_date"]["year"]}'
            user_str_data += f'\nBank cards:'
            for card in user["bank_cards"]:
                user_str_data += "\n\n"
                user_str_data += f'CARD ID:{card["id"]}'
                user_str_data += f'\nFull name: {card["f_name"]} {card["l_name"]}'
                user_str_data += f'\n{card["month"]}/{card["year"]}\nBalance: {card["balance"]}'
            break
    return user_str_data


def print_all_users(some_list: list) -> None:
    for user in some_list:
        print("====================")
        result = get_user_data_by_id(some_list, user["id"])
        print(result)


def find_user_by_id(some_list: list, some_id: str) -> int:
    index = -1
    for i in range(len(some_list)):
        if some_list[i]["id"] == some_id:
            index = i
            break
    return index


def remove_user(some_list: list, some_id: str) -> bool:
    is_success = False
    index = find_user_by_id(some_list, some_id)
    if index != -1:
        del some_list[index]
        is_success = True
    return is_success


def add_user(some_list: list, new_user: dict) -> bool:
    is_success = False
    if find_user_by_id(some_list, new_user["id"]) == -1:
        some_list.append(new_user)
        is_success = True
    return is_success


def change_id(some_list: list, some_id: str, new_id: str) -> bool:
    is_success = False
    user_index = find_user_by_id(some_list, some_id)
    if user_index != -1:
        change_index = find_user_by_id(some_list, new_id)
        if change_index == -1:
            some_list[user_index]["id"] = new_id
            is_success = True
    return is_success


db_users = list()
db_users.append(user_1)
db_users.append(user_2)

while True:
    print("1. Show all users")
    print("2. Add new user")
    print("3. Show user by id")
    print("4. Change user data by id")
    print("5. Remove user by id")
    print("6. Close program")
    choice = input("Your choice: ")
    if choice == "1":
        print_all_users(db_users)
    elif choice == "2":
        new_id = input("ENTER NEW USER ID: ")
        new_l_name = input("ENTER LAST NAME: ")
        new_f_name = input("ENTER FIRST NAME: ")
        new_user_full_name = {"l_name": new_l_name, "f_name": new_f_name}

        new_day = int(input("DAY: "))
        new_month = int(input("MONTH: "))
        new_year = int(input("YEAR: "))
        new_birth_date = {"day": new_day, "month": new_month, "year": new_year}

        new_cards = []

        new_user = {"id": new_id,
                    "full_name": new_user_full_name,
                    "birth_date": new_birth_date,
                    "bank_cards": new_cards}

        if add_user(db_users, new_user):
            print("ADDED")
        else:
            print("ERROR")

    elif choice == "3":
        user_id = input("ENTER USER ID: ")
        result = get_user_data_by_id(db_users, user_id)
        print(result)
    elif choice == "4":
        user_id = input("ENTER USER ID: ")
        index = find_user_by_id(db_users, user_id)
        if index != -1:
            while True:
                result = get_user_data_by_id(db_users, user_id)
                print(result)
                print("1. Change ID")
                print("2. Change last name")
                print("3. Change name")
                print("4. Change birth date")
                print("5. Add new bank card")
                print("6. Change bank card data by id")
                print("7. Remove bank card by id")
                print("8. Return to main menu")
                choice = input("Your choice: ")
                if choice == "1":
                    new_id = input("ENTER NEW ID: ")
                    if change_id(db_users, user_id, new_id):
                        print("ID CHANGED")
                        user_id = new_id
                    else:
                        print("INCORRECT ID")
                elif choice == "4":
                    new_day = input("DAY: ")
                    new_month = input("MONTH: ")
                    new_year = input("YEAR: ")

                    if new_day != "":
                        db_users[index]["birth_date"]["day"] = new_day
                elif choice == "8":
                    break

        else:
            print("NOT FOUND")
    elif choice == "5":
        user_id = input("ENTER USER ID: ")
        if remove_user(db_users, user_id):
            print("DELETED")
        else:
            print("NOT FOUND")
    elif choice == "6":
        print("END")
        break
    else:
        print("Incorrect choice!")

# Задание 10 - реализовать следующее меню:
#              1. Показать всех пользователей
#              2. Добавить нового пользователя
#              3. Показать пользователя по его идентификатору
#              4. Изменить данные пользователя по его идентификатору
#              5. Удалить пользователя по его идентификатору
#              6. Завершить программу
#
#              При выборе пункта 2 сделать так, чтобы невозможно было добавить пользователя
#              с идентификатором, который уже есть у какого-либо пользователя.
#
#              При выборе пунктов 3, 4, 5 сделать так, чтобы программа оповещала,
#              если не нашла пользователя.
#
#              При выборе пункта 4 после ввода верного идентификатора, должна выводиться полная
#              информация о пользователе, а потом должно появляться следующее меню:
#              1. Изменить идентификатор
#              2. Изменить фамилию
#              3. Изменить имя
#              4. Изменить дату рождения
#              5. Добавить новую банковскую карточку
#              6. Изменить данные банковской карточки по идентификатору
#              7. Удалить банковскую карточку по идентификатору
#              8. Вернуться в главное меню
#
#              В этом меню при выборе 1-го пункта сделать так, чтобы невозможно было
#              изменить идентификатор на тот, который уже есть у какого-либо пользователя.
#
#              При выборе 4-го пункта, программа запрашивает день, месяц, год. Если пользователь
#              вводит пустые данные, то соответствующие данные пользователя не меняются.
#
#              При выборе пункта 5 сделать так, чтобы невозможно было добавить карточку
#              с идентификатором, который уже есть у какой-либо карточки этого пользователя.
#
#              При выборе пункта 6 и 7 сделать так, чтобы программа оповещала, если не нашла карточку.
#
#              При выборе пункта 6 программа последовательно спрашивает данные карточки.
#              Если пользователь вводит пустые данные, то соответствующие данные карточки не меняются.
#
#              При выборе пункта 8 программа должна показывать главное меню.
#
#              Программа завершается только в том случае, если выбран пункт 6 из главного меню.

# ==============================================LESSON40==============================================
# Работа со вложенными словарями
# Сортировка и фильтрация списка словарей

# student_1 = {"name": "Tom", "age": 24, "grades": [10, 12, 11, 12, 11, 11]}
# student_2 = {"name": "Kate", "age": 23, "grades": [12, 12, 12, 12, 12, 12]}
# student_3 = {"name": "Jim", "age": 26, "grades": [8, 9, 7, 10, 10, 11]}
# student_4 = {"name": "Arthur", "age": 29, "grades": [10, 9, 8, 9, 11, 12]}
# student_5 = {"name": "Lisa", "age": 27, "grades": [9, 8, 9, 10, 9, 10]}
#
# db_students = list([student_1, student_2, student_3, student_4, student_5])

# Сортировка списка словарей
# sorted_db_users = sorted(db_students, key=lambda student: student["grades"][0], reverse=False)
# db_students = sorted_db_users
# for student in db_students:
#     print(student)

# Фильтрация списка словарей
# filtered_students = list(filter(lambda student: student["age"] > 25, db_students))
# for student in filtered_students:
#     print(student)


# user_1_full_name = {"l_name": "Jackson", "f_name": "Tom"}
# user_1_birth_date = {"day": 10, "month": 2, "year": 1994}
# card_1 = {"id": "1234123412341234", "f_name": "Tom", "l_name": "Jackson",
#           "month": 10, "year": 2026, "balance": 1500}
# card_2 = {"id": "5869586958695869", "f_name": "Kate", "l_name": "Jackson",
#           "month": 2, "year": 2025, "balance": 1050}
# user_1_bank_cards = [card_1, card_2]
# user_1 = {"id": "1234ABC",
#         "full_name": user_1_full_name,
#         "birth_date": user_1_birth_date,
#         "bank_cards": user_1_bank_cards}
#
# user_2_full_name = {"l_name": "Morgan", "f_name": "Arthur"}
# user_2_birth_date = {"day": 22, "month": 4, "year": 1986}
# card_3 = {"id": "4321432143214321", "f_name": "Arthur", "l_name": "Morgan",
#           "month": 12, "year": 2026, "balance": 750}
# user_2_bank_cards = [card_3]
# user_2 = {"id": "MOR1256",
#         "full_name": user_2_full_name,
#         "birth_date": user_2_birth_date,
#         "bank_cards": user_2_bank_cards}
#
# user_3_full_name = {"l_name": "Raynor", "f_name": "Jim"}
# user_3_birth_date = {"day": 3, "month": 12, "year": 1984}
# user_3_bank_cards = []
# user_3 = {"id": "645SARA",
#         "full_name": user_3_full_name,
#         "birth_date": user_3_birth_date,
#         "bank_cards": user_3_bank_cards}
#
# print("==========ORIG==========")
# db_users = list([user_1, user_2, user_3])
# for user in db_users:
#     for key in user:
#         print(f"{key}: {user[key]}")
#     print()
# print("==========================")

# print("==========SORTED==========")
# sorted_db_users = sorted(db_users, key=lambda user: user["full_name"]["f_name"], reverse=False)
# db_users = sorted_db_users
# for user in db_users:
#     for key in user:
#         print(f"{key}: {user[key]}")
#     print()
# print("==========================")
#
# print("=========FILTERED=========")
# def filter_users_by_card_balance(balance):
#     def filter_users(user):
#         for card in user["bank_cards"]:
#             if card["balance"] >= balance:
#                 return True
#         return False
#     return filter_users
#
#
# filter_users = filter_users_by_card_balance(1400)
# filtered_users = list(filter(filter_users, db_users))
# for user in filtered_users:
#     for key in user:
#         print(f"{key}: {user[key]}")
#     print()
# print("==========================")
