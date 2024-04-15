# ================================LESSON41================================
# https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
# BaseException - базовое исключение, от него наследуется всё
# Exception - "стандартные исключения" и пользовательские исключения
# TypeError - операция применена к объекту несоответствующего типа.
# ValueError - функция получает аргумент правильного типа, но некорректного значения.
# ZeroDivisionError - деление на ноль
# IndexError - индекс не входит в диапазон элементов.
# KeyError - несуществующий ключ (в словаре, множестве или другом объекте).
# try...except
# try...except...else...finally
# raise



# boxes = int(input("Введите количество коробок: "))
# print("12" + 52)
# print(25 / 0)

# my_list = [10, 20, 30]
# print(my_list[50])

# my_dict = {"key_1": 50, "key_2": 80}
# print(my_dict["key_50"])


# try:
#     num_sum = int(input("Введите сумму: "))
#     count = int(input("Введите количество: "))
# except:
#     print("Возникла ошибка! Вы ввели не число.")
#
# print("После конструкции try...except")


# try:
#     num_sum = int(input("Введите сумму: "))
#     count = int(input("Введите количество: "))
#     num_avg = num_sum / count
#     print("Среднее арифметическое: " + num_avg)
# except:
#     print("Возникла ошибка! Вы ввели не число.")


# try:
#     num_sum = int(input("Введите сумму: "))
#     count = int(input("Введите количество: "))
#     num_avg = num_sum / count
#     print("Среднее арифметическое: " + num_avg)
# except ValueError:
#     print("Возникла ошибка! Вы ввели не число.")
# except ZeroDivisionError:
#     print("Нельзя поделить на ноль!")
# except TypeError:
#     print("В программе не получилось вывести данные!")


# try:
#     num_sum = int(input("Введите сумму: "))
#     count = int(input("Введите количество: "))
#     num_avg = num_sum / count
#     print("Среднее арифметическое: " + num_avg)
# except (ValueError, ZeroDivisionError, TypeError):
#     print("Возникла ошибка! Что-то пошло не так.")


# try:
#     num_sum = int(input("Введите сумму: "))
#     count = int(input("Введите количество: "))
#     num_avg = num_sum / count
#     print("Среднее арифметическое: " + num_avg)
# except ValueError:
#     print("Возникла ошибка! Вы ввели не число.")
# except ZeroDivisionError:
#     print("Нельзя поделить на ноль!")
# except:
#     print("Возникла ошибка! Что-то пошло не так.")


# try:
#     num_sum = int(input("Введите сумму: "))
#     count = int(input("Введите количество: "))
#     num_avg = num_sum / count
# except ValueError:
#     print("Возникла ошибка! Вы ввели не число.")
# except ZeroDivisionError:
#     print("Нельзя поделить на ноль!")
# else:
#     print(num_avg)
#     print("Блок try отработал без исключений")
# finally:
#     print("Работает")
#     print("блок")
#     print("finally")


# try:
#     f = open("demofile.txt", "w")
#     try:
#         f.write("Lorum Ipsum")
#     except:
#         print("Something went wrong when writing to the file")
#     finally:
#         f.close()
# except:
#     print("Something went wrong when opening the file")


# name = input("Введите имя: ")
# year = int(input("Введите год рождения: "))
#
# print(f"Имя: {name}\nВозраст: {2023 - year}")


# try:
#     name = input("Введите имя: ")
#     if not name.isalpha():
#         raise Exception
#
#     year = int(input("Введите год рождения: "))
#     if year < 1900 or year > 2023:
#         raise Exception
#
#     print(f"Имя: {name}\nВозраст: {2023 - year}")
# except Exception:
#     print("Что-то пошло не так.")


# try:
#     name = input("Введите имя: ")
#     year = int(input("Введите год рождения: "))
#     if year < 1900:
#         raise Exception(f"ИСКЛЮЧЕНИЕ! Год меньше 1900: {year}")
#     print(f"Имя: {name}\nВозраст: {2023 - year}")
# except ValueError as exc:
#     print(exc)
# except Exception as exc:
#     print(exc)


# default_year = 1900
# name = "Unknown"
# try:
#     name = input("Введите имя: ")
#     year = int(input("Введите год рождения: "))
#     if year < 1900:
#         raise Exception(year)
# except ValueError as exc:
#     print(exc.args)
#     year = default_year
#     print(f"Вы указали неверный год, поэтому будет выставлен год по умолчанию: {default_year}")
# except Exception as exc:
#     input_year, = exc.args
#     year = default_year
#     print(f"Вы указали {input_year} год, поэтому будет выставлен год по умолчанию: {default_year}")
# print(f"Имя: {name}\nВозраст: {2023 - year}")

# ====================================================================================================
# Задание 1 - пользователь вводит одно число на первой строке и второе число на второй строке.
#             Программа должна поделить первое число на второе и вывести результат.
#             Обработайте исключение, которое возникает при делении на 0, и выведите ошибку.

# Задание 2 - пользователь вводит строку. Программа должна преобразовать её в число и вывести.
#             Обработайте исключение, которое возникает, если ввести текст, и выведите ошибку.

# Задание 3 - программа запрашивает у пользователя имя и возраст. Создайте и обработайте возможные
#             исключения для имени и возраста.

# Задание 4 - пользователь вводит счёт из 16 цифр и сумму денег, которую хочет снять со счёта.
#             Программа должна вывести, сколько денег было снято и сколько осталось на счету.
#             Обработайте исключения, которые могут возникнуть.
#             Также обработайте исключение, если пользователь введёт отрицательную сумму или
#             номер счёта меньше или больше 16 цифр.
# ====================================================================================================
