# color = input("Цвет: ").lower()
#
# if color == "красный":
#     print("Стой!")
# elif color == "жёлтый":
#     print("Подожди!")
# elif color == "зелёный":
#     print("Иди!")
# else:
#     print("Неизвестный сигнал.")


# total_price = int(input("Цена корзины: "))
# continuous_days = int(input("Количество дней: "))
#
# discount_coef = 1
# discount_on_total_price_delta = 0.05
# total_price_min_limit = 100
# continuous_days_per_coef = 6
# discount_on_continuous_days_delta = 0.05
# continuous_days_min_limit = 30
# discount_on_continuous_days_limit_delta = 0.05
# discount_coef_min_limit = 0.5
# discount_coef_on_min_limit = 0.5
#
# if total_price >= total_price_min_limit:
#     discount_coef -= discount_on_total_price_delta
#
# discount_coef -= (continuous_days // continuous_days_per_coef) * discount_on_continuous_days_delta
#
# if continuous_days >= continuous_days_min_limit:
#     discount_coef -= discount_on_continuous_days_limit_delta
#
# if discount_coef < discount_coef_min_limit:
#     discount_coef = discount_coef_on_min_limit
#
# total_price_discount = total_price * discount_coef
# print(f"Итоговая стоимость с учётом скидки: {total_price_discount}")


# name = input("Введите имя: ")
# if name:
#     print(f"Привет, {name}")
#
#
# password = input("Введите пароль: ")
# is_admin = False
# if name == "admin" and password == "5869":
#     is_admin = True
#
#
# if is_admin:
#     print("Добро пожаловать, администратор!")
#
#
# acc_online = {}
# if not acc_online:
#     print("Сохранённые данные не найдены.")
#     acc_online["name"] = name
#     age = acc_online.get("age")
#
#     if name:
#         print("Имя присутствует.")
#     else:
#         print("У вас не указан возраст.")
#
#     if age:
#         print("Возраст присутствует.")
#     else:
#         print("У вас не указан возраст.")


# CHOICE_FAST = "1"
# CHOICE_STANDARD = "2"
# CHOICE_PICKUP = "3"
# DELIVERY_TAX_WRONG_SELECTED = -1
#
# delivery = input(f"Выберите способ доставки ({CHOICE_FAST}. Быстрый / "
#                  f"{CHOICE_STANDARD}. Стандартный / "
#                  f"{CHOICE_PICKUP}. Самовывоз): ")
# price = 1000
# tax_rate = 0.15
# delivery_tax = DELIVERY_TAX_WRONG_SELECTED
#
# if delivery == CHOICE_FAST:
#     delivery_tax = 300
# if delivery == CHOICE_STANDARD:
#     delivery_tax = 150
# if delivery == CHOICE_PICKUP:
#     delivery_tax = 0
#
# if delivery_tax == DELIVERY_TAX_WRONG_SELECTED:
#     print("Выбран неверный способ доставки.")
# else:
#     total = price + delivery_tax
#     total_with_tax = price + (price * tax_rate)
#     print(f"Итоговая оплата: {total_with_tax}")


# words = ["дом", "комок", "палка", "топот", "река"]
# to_find_symbol = "о"
#
# i = 0
# while i < len(words):
#     j = 0
#     while j < len(words[i]):
#         if words[i][j] == to_find_symbol:
#             print(words[i])
#             break
#         j += 1
#     i += 1


# some_list = [10, "дом", 55, "библиотека", 25, "информационное обеспечение", 86, "кот"]
# for i in range(1, len(some_list), 2):
#     if len(some_list[i]) > 5:
#         print(some_list[i])


# some_text = input("Введите текст: ")
#
# result = ""
# i = len(some_text) - 1
# while i >= 0:
#     result += some_text[i]
#     i -= 1
#
# print(result)


# some_str = input("Введите строку: ")
# start_index = int(input("Стартовый индекс: "))
# to_find_symbol = input("Введите символ поиска: ")
#
# found_index = -1
# for i in range(start_index, len(some_str)):
#     if some_str[i] == to_find_symbol:
#         found_index = i
#         break
#
# print(found_index)


# some_list = input("Введите числа через пробел: ").split()
#
# for i in range(len(some_list)):
#     some_list[i] = int(some_list[i])
#     if some_list[i] % 2 != 0:
#         some_list[i] = 0
#
# for i in range(len(some_list) - 1):
#     print(some_list[i], end=" ")
# print(some_list[len(some_list) - 1])



# def get_vector_dir(pressed_key: str):
#     result_vector_dir = (0, 0)
#     if pressed_key == "W":
#         result_vector_dir = (1, 0)
#     elif pressed_key == "S":
#         result_vector_dir = (-1, 0)
#     elif pressed_key == "A":
#         result_vector_dir = (0, 1)
#     elif pressed_key == "D":
#         result_vector_dir = (0, -1)
#     return result_vector_dir


# def remove_slice(some_list: list, start=0, end=-1):
#     list_size = len(some_list)
#     if end == -1:
#         end = list_size - 1
#
#     if end >= list_size:
#         end = list_size - 1
#     if start < 0:
#         start = 0
#
#     for i in range(end, start - 1, -1):
#         del some_list[i]


# student_list = [
#     {"id": "S-5869", "name": "Teston", "avg_grade": 11.6},
#     {"id": "S-0955", "name": "Kate", "avg_grade": 9.3},
#     {"id": "S-1143", "name": "Bob", "avg_grade": 10.4}
# ]
#
# new_id = input("Введите идентификатор студента: ")
# new_name = input("Введите имя студента: ")
# new_avg_grade = float(input("Введите среднюю оценку студента: "))
#
# new_student = {"id": new_id, "name": new_name, "avg_grade": new_avg_grade}
#
# INDEX_NOT_FOUND = -1
# index = INDEX_NOT_FOUND
# for i in range(len(student_list)):
#     if student_list[i]["id"] == new_student["id"]:
#         index = i
#         break
#
# if index == INDEX_NOT_FOUND:
#     student_list.append(new_student)


# CHOICE_SHOW_ALL_DATA = "1"
# CHOICE_ADD_ELEMENT = "2"
# CHOICE_CHANGE_ELEMENT = "3"
# CHOICE_DELETE_ELEMENT = "4"
# CHOICE_END_PROGRAM = "5"
# some_dict = {}
#
# while True:
#     print(f"{CHOICE_SHOW_ALL_DATA}. Показать все данные словаря")
#     print(f"{CHOICE_ADD_ELEMENT}. Добавить элемент в словарь")
#     print(f"{CHOICE_CHANGE_ELEMENT}. Изменить значение по ключу в словаре")
#     print(f"{CHOICE_DELETE_ELEMENT}. Удалить значение по ключу из словаря")
#     print(f"{CHOICE_END_PROGRAM}. Завершить программу")
#     choice = input("Выберите действие: ")
#
#     if choice == CHOICE_SHOW_ALL_DATA:
#         for key in some_dict:
#             print(f"{key} - {some_dict[key]}")
#     elif choice == CHOICE_ADD_ELEMENT:
#         new_key = input("Введите новый ключ: ")
#         if new_key not in some_dict:
#             new_value = input("Введите новое значение: ")
#             some_dict[new_key] = new_value
#         else:
#             print("Ключ уже существует.")
#     elif choice == CHOICE_CHANGE_ELEMENT:
#         input_key = input("Введите ключ: ")
#         if input_key in some_dict:
#             new_value = input("Введите новое значение: ")
#             some_dict[input_key] = new_value
#         else:
#             print("Ключ не существует.")
#     elif choice == CHOICE_DELETE_ELEMENT:
#         input_key = input("Введите ключ: ")
#         if input_key in some_dict:
#             del some_dict[input_key]
#         else:
#             print("Ключ не существует.")
#     elif choice == CHOICE_END_PROGRAM:
#         break
#     else:
#         print("Выбранное действие отсутствует.")
#
# print("Завершение программы.")


# def filter_students(some_list: list[dict], symbol: str):
#     result_list = list()
#     for student in some_list:
#         if student["name"][0] == symbol:
#             result_list.append(student)
#     return result_list


# class BankAccount:
#     __id = str()
#     __balance = int()
#     __is_blocked = bool()
#
#     def __init__(self, id: str):
#         self.__id = id
#         self.__balance = 0
#         self.__is_blocked = False
#
#     def __str__(self):
#         result = f"{self.__id} {self.__balance} "
#         if self.__is_blocked:
#             result += "Заблокирован"
#         else:
#             result += "Активный"
#         return result
#
#     def set_id(self, id: str):
#         self.__id = id
#
#     def get_id(self):
#         return self.__id
#
#     def get_status(self):
#         return self.__is_blocked
#
#     def get_balance(self):
#         return self.__balance
#
#     def top_up_balance(self, balance: int) -> bool:
#         is_success = False
#         if not self.__is_blocked and balance >= 0:
#             self.__balance += balance
#             is_success = True
#         return is_success
#
#     def withdraw_balance(self, balance: int) -> bool:
#         is_success = False
#         if not self.__is_blocked and balance >= 0:
#             self.__balance -= balance
#             is_success = True
#         return is_success
#
#     def block(self):
#         self.__is_blocked = True
#
#     def unblock(self):
#         self.__is_blocked = False
#
#
# some_acc = BankAccount("A-5869")
# print(some_acc)
# some_acc.set_id("TEST_ID")
# print(some_acc.get_id())
# print(some_acc.get_status())
# print(some_acc.get_balance())
#
# if some_acc.top_up_balance(1000):
#     print("SUCCESS")
# else:
#     print("FAIL")
# print(some_acc.get_balance())
#
# if some_acc.top_up_balance(-1000):
#     print("SUCCESS")
# else:
#     print("FAIL")
# print(some_acc.get_balance())
#
# if some_acc.withdraw_balance(250):
#     print("SUCCESS")
# else:
#     print("FAIL")
# print(some_acc.get_balance())
#
# if some_acc.withdraw_balance(-250):
#     print("SUCCESS")
# else:
#     print("FAIL")
# print(some_acc.get_balance())
#
# some_acc.block()
# print(some_acc)
# if some_acc.top_up_balance(1000):
#     print("SUCCESS")
# else:
#     print("FAIL")
# print(some_acc.get_balance())
#
# if some_acc.withdraw_balance(250):
#     print("SUCCESS")
# else:
#     print("FAIL")
# print(some_acc.get_balance())
#
# some_acc.unblock()
# print(some_acc)
# if some_acc.top_up_balance(1000):
#     print("SUCCESS")
# else:
#     print("FAIL")
# print(some_acc.get_balance())
#
# if some_acc.withdraw_balance(250):
#     print("SUCCESS")
# else:
#     print("FAIL")
# print(some_acc.get_balance())
