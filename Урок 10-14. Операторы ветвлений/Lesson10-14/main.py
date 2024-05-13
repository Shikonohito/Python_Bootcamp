# ==============================================LESSON10==============================================
# Логические операторы >, >=, <, <=, ==, !=
# Приведение типов к bool
# if


# obj_bool = True

# print("1 == 1:", 1 == 1)  # 1 == 1: True
# print("1 == 2:", 1 == 2)  # 1 == 2: False

# print("1 != 1:", 1 != 1)  # 1 != 1: False
# print("1 != 2:", 1 != 2)  # 1 != 2: True

# print("1 > 1:", 1 > 1)  # 1 > 1: False
# print("1 > 2:", 1 > 2)  # 1 > 2: False
#
# print("1 < 1:", 1 < 1)  # 1 < 1: False
# print("1 < 2:", 1 < 2)  # 1 < 2: True

# print("1 >= 1:", 1 >= 1)  # 1 >= 1: True
# print("1 >= 2:", 1 >= 2)  # 1 >= 2: False
#
# print("1 <= 1:", 1 <= 1)  # 1 <= 1: True
# print("1 <= 2:", 1 <= 2)  # 1 <= 2: True


# print(bool(""))  # False
# print(bool(0.0))  # False
# print(bool(None))  # False
# print(bool("IT Step Academy"))  # True
# print(bool(1))  # True

# ====================================================================================================
# ПЗ 10.1 - 10.4
# ====================================================================================================


# if 10 % 2 == 0:
#     print("Число чётное")

# num = int(input("NUMBER: "))
# if num > 2:
#     print(num, "больше чем 2")
#
# if num < 2:
#     print(num, "меньше чем 2")


# ====================================================================================================
# ПЗ 10.5 - 10.11
# ====================================================================================================

# ==============================================LESSON11==============================================
# Логические операторы and, or, not
# Приоритеты логических операторов not, and, or
# if... else...


# condition_1 = True
# condition_2 = False
# print(condition_1 and condition_2)  # Результат False, если хотя бы один False
# print(condition_1 or condition_2)  # Результат True, если хотя бы один True
# print(not condition_1, not condition_2)  # Меняет False на True и наоборот


# condition_1 = True
# condition_2 = True
# condition_3 = False
# print(condition_1 and (condition_2 or condition_3))
# print(condition_1 or (condition_2 and condition_3))


# ====================================================================================================
# ПЗ 11.1 - 11.9
# ====================================================================================================


# num_1 = 5
# num_2 = 10
# if num_1 % 2 == 0 and num_2 % 2 == 0:
#     print("YES")


# num_1 = 5
# num_2 = 10
# if num_1 % 2 == 0 and num_2 % 2 == 0:
#     print("YES")
# else:
#     print("NO")


# num_1 = 5
# num_2 = 10
# condition = num_1 % 2 == 0 and num_2 % 2 == 0
# if condition:
#     print("YES")
# else:
#     print("NO")


# num = int(input("Введите число 5: "))
# if num == 5:
#     print("Верно")
# else:
#     print("Это любое другое число")

# ==============================================LESSON12==============================================
# Практика

# ====================================================================================================
# ПЗ 11.10 - 11.16
# ====================================================================================================

# ==============================================LESSON13==============================================
# if... elif... else...


# step = 1
# if step == 1:
#     print("Успешно сработал if")
# elif step == 2:
#     print("Успешно сработал elif")
# else:
#     print("Успешно сработал else")


# def has_lower_alpha(some_str: str):
#     is_success = False
#     for symb in some_str:
#         if symb.islower():
#             is_success = True
#             break
#     return is_success
#
# def has_upper_alpha(some_str):
#     is_success = False
#     for symb in some_str:
#         if symb.isupper():
#             is_success = True
#             break
#     return is_success
#
# def has_digits(some_str):
#     is_success = False
#     for symb in some_str:
#         if symb.isdigit():
#             is_success = True
#             break
#     return is_success
#
# def has_spec_symbols(some_str):
#     is_success = False
#     for symb in some_str:
#         if not symb.isalnum():
#             is_success = True
#             break
#     return is_success


# password = input("Введите пароль: ")
# if len(password) < 8:
#     print("Длина пароля меньше 8 символов")
# if not has_lower_alpha(password):
#     print('Пароль не содержит строчные буквы')
# if not has_upper_alpha(password):
#     print('Пароль не содержит заглавные буквы')
# if not has_digits(password):
#     print("Пароль не содержит цифры")
# if not has_spec_symbols(password):
#     print("Пароль не содержит спецсимволы")


# password = input("Введите пароль: ")
# if len(password) < 8:
#     print("Длина пароля меньше 8 символов")
# elif not has_lower_alpha(password):
#     print('Пароль не содержит строчные буквы')
# elif not has_upper_alpha(password):
#     print('Пароль не содержит заглавные буквы')
# elif not has_digits(password):
#     print("Пароль не содержит цифры")
# elif not has_spec_symbols(password):
#     print("Пароль не содержит спецсимволы")


# ====================================================================================================
# ПЗ 13.1 - 13.6
# ====================================================================================================


# ==============================================LESSON14==============================================
# Вложенные условные конструкции


# if True:
#     if True:
#         print("11")
#     elif True:
#         print("12")
#     else:
#         if True:
#             print("131")
#         else:
#             print("132")
# else:
#     print("2")


# account = int(input("Сколько денег на Вашем счёте: "))
# if account > 0:
#     withdrawal = int(input("Сколько денег Вы хотите снять: "))
#     if withdrawal <= account:
#         account -= withdrawal
#         print("Вот Ваши", withdrawal, "манат(а).")
#         print("На Вашем счёте осталось", account, "манат(а).")
#     else:
#         print("Вы не можете снять больше", account, "манат.")
# else:
#     print("На Вашем счёте нет денег")

# ====================================================================================================
# ПЗ 14.1 - 14.2
# ДЗ 14.2
# ====================================================================================================