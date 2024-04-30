# ==============================================LESSON42==============================================
# ООП - Классы и объекты
# Принципы ООП - Абстракция
# Создание класса
# Создание объекта класса
# Поля (атрибуты), методы
# Метод __str__()
# Конструктор __init__()


# class Student:
#     name = "Unknown"
#     age = 0
#     group = "Unknown"
#
#     def __str__(self):
#         result = f"Name: {self.name}, Age: {self.age}"
#         return result
#
#     def __init__(self, new_name: str, new_age: int, new_group: str):
#         self.name = new_name
#         self.age = new_age
#         self.group = new_group
#
#
# # student_1 = Student()
# # student_2 = Student()
#
# student_list = list()
# # student_list.append(student_1)
# # student_list.append(student_2)
#
# for student in student_list:
#     print(student)
#
# print(student_list)
#
# student_3 = Student("Tom", 23, "Python")
# student_4 = Student("Kate", 25, "Python")
# student_5 = Student("Bob", 23, "C#")
# student_list.append(student_3)
# student_list.append(student_4)
# student_list.append(student_5)
#
# for student in student_list:
#     print(student)


# ====================================================================================================
# ПЗ 42.1 - 42.2
# ====================================================================================================


# ==============================================LESSON43==============================================
# Принципы ООП - Инкапсуляция
# Спецификаторы доступа public, private, protected
# Свойства - геттеры и сеттеры
# Деструктор __del__()


# class Student:
#     f_name = "Unknown"  # Public field
#     age = 18  # Public field
#
#     def __init__(self, f_name: str, age: int):
#         self.f_name = f_name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.f_name} {self.age}"
#
#
# student_1 = Student("Teston", -55)
# print(student_1.age)
#
# student_2 = Student("Teston", 25)
# student_2.age = -55
# print(student_2.age)


# class Student:
#     __f_name = "Unknown"  # Private field
#     __age = 18  # Private field
#
#     def __init__(self, f_name: str, age: int):
#         self.__f_name = f_name
#         self.set_age(age)
#
#     def __str__(self):
#         return f"{self.__f_name} {self.__age}"
#
#     def set_age(self, age: int):
#         if age < 0:
#             self.__age = 18
#         else:
#             self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#     def set_name(self, name: str):
#         self.__f_name = name
#
#     def get_name(self):
#         return self.__f_name
#
#
# student_1 = Student("Teston", -55)
# print(student_1.get_age())
# student_1.set_age(25)
# print(student_1.get_age())
# print(student_1)

# print(student_1.__f_name)
# print(student_1._Student__f_name)  # Обходной путь
# student_1.__f_name = "Tom"
# print(student_1.__f_name)
# print(student_1)

# ====================================================================================================
# Инкапсуляция со стороны

# from BankCard import BankCard
#
# card_1 = BankCard("5869586958695869", "Teston", "Lebra", 10, 2028, 5000)
# print(card_1)
# card_1.set_card_id("1234123412341234")
# card_1.set_f_name("Tom")
# card_1.set_l_name("Jackson")
# card_1.set_month(11)
# card_1.set_year(2023)
# card_1.set_balance(3000)
# print(card_1)
#
# print()
# if card_1.top_up(500):
#     print("Баланс успешно пополнен")
# print(card_1)
#
# print()
# if card_1.withdraw(500):
#     print("Деньги успешно сняты с баланса")
# print(card_1)
#
# print()
# if card_1.is_expired():
#     print("Карта просрочена")

# ====================================================================================================
# Деструктор __del__()

# class Student:
#     __f_name = "Unknown"  # Private field
#     __age = 18  # Private field
#
#     def __init__(self, f_name: str, age: int):
#         self.__f_name = f_name
#         self.set_age(age)
#
#     def __str__(self):
#         return f"{self.__f_name} {self.__age}"
#
#     def set_age(self, age: int):
#         if age < 0:
#             self.__age = 18
#         else:
#             self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#     def set_name(self, name: str):
#         self.__f_name = name
#
#     def get_name(self):
#         return self.__f_name
#
#     def __del__(self):
#         print("DESTRUCTOR IS WORKING")
#
#
# student_1 = Student("Teston", 23)
#
#
# student_2 = Student("Teston", 23)
# student_3 = student_2
# print("===================")
# del student_2
# print("===================")
# del student_3
# print("===================")


# ====================================================================================================
# ПЗ 43.1 - 43.2
# ====================================================================================================


# ==============================================LESSON44==============================================
# Принципы ООП - Наследование
# Наследование на примерах
# Переопределение конструктора и вызов конструктора родителя super()
# Переопределение метода и вызов базового метода при помощи super()


# class Human:
#     _name = "Unknown"
#     _age = 0
#
#     def __init__(self, name="Unknown", age=0):
#         self._name = name
#         self._age = age
#
#     def __str__(self):
#         result = f"{self._name} {self._age}"
#         return result
#
#
# class Employee(Human):  # Наследование
#     __work = "Unknown"
#     __salary = 0
#
#     # Переопределение конструктора родителя
#     def __init__(self, name="Unknown", age=0, work="Unknown", salary=0):
#         super().__init__(name, age)  # Вызов конструктора родителя
#         self.__work = work
#         self.__salary = salary
#
#     # Переопределение метода родителя
#     def __str__(self):
#         result = f"{self._name} {self._age} {self.__work} {self.__salary}"
#         return result
#
#
# human_1 = Human("Tom", 25)
# print(human_1)
#
# employee_1 = Employee("Bob", 25, "Programmer", 1250)
# print(employee_1)
#
# print(employee_1._name)

# ====================================================================================================

# class Product:
#     _id = str()
#     _type = str()
#     _price = float()
#
#     def __init__(self, id: str, type: str, price: float):
#         self.set_id(id)
#         self.set_type(type)
#         self.set_price(price)
#
#     def __str__(self):
#         return f"{self._id} {self._type} {self._price}"
#
#     def set_id(self, id: str):
#         self._id = id
#
#     def get_id(self):
#         return self._id
#
#     def set_type(self, type: str):
#         self._type = type.lower()
#
#     def get_type(self):
#         return self._type
#
#     def set_price(self, price: float):
#         self._price = price
#
#     def get_price(self):
#         return self._price
#
#
# class Phone(Product):
#     __brand = ""
#     __model = ""
#
#     def __init__(self, id: str, type: str, price: float, brand: str, model: str):
#         super().__init__(id, type, price)
#         self.set_brand(brand)
#         self.set_model(model)
#
#     def __str__(self):
#         return f"{self._id} {self._type} {self.__brand} {self.__model} {self._price}"
#
#     def set_brand(self, brand: str):
#         self.__brand = brand
#
#     def get_brand(self):
#         return self.__brand
#
#     def set_model(self, model: str):
#         self.__model = model
#
#     def get_model(self):
#         return self.__model
#
#
# class Laptop(Product):
#     __cpu = ""
#     __gpu = ""
#
#     def __init__(self, id: str, type: str, price: float, cpu: str, gpu: str):
#         super().__init__(id, type, price)
#         self.set_cpu(cpu)
#         self.set_gpu(gpu)
#
#     def __str__(self):
#         return f"{self._id} {self._type} {self.__cpu} {self.__gpu} {self._price}"
#
#     def set_cpu(self, cpu: str):
#         self.__cpu = cpu
#
#     def get_cpu(self):
#         return self.__cpu
#
#     def set_gpu(self, gpu: str):
#         self.__gpu = gpu
#
#     def get_gpu(self):
#         return self.__gpu
#
#
# def product_total_sum(product_list: list[Product]):
#     total_sum = 0
#     for product in product_list:
#         total_sum += product.get_price()
#     return total_sum
#
#
# phone_1 = Phone("ABC123", "Phone", 5000, "Samsung", "A99")
# phone_2 = Phone("ABC124", "Phone", 9999, "iPhone", "99 Plus")
# laptop_1 = Laptop("ABC125", "Laptop", 4000, "i9-13980HX", "RTX 4080")
# laptop_2 = Laptop("ABC126", "Laptop", 4500, "AMD Ryzen 5 7645HX", "RTX 4050")
#
# products = [phone_1, phone_2, laptop_1, laptop_2]
#
# total_price = product_total_sum(products)
# print(total_price)

# ====================================================================================================
# ПЗ 44.1 - 44.2
# ====================================================================================================
# Задание 1 - создать класс "Студент". Этот класс должен хранить поля "Идентификатор", "Имя", "Фамилия",
#             "Отчество", "Группа", "Список оценок", "Средняя оценка".
#             Определить для класса строковое представление __str__ и конструктор __init__.
#             Определить для класса метод добавления оценки. Оценка может быть от 1 до 12 включительно.

# Задание 2 - создать класс "Сотрудник". Этот класс должен хранить поля "Идентификатор", "Имя", "Фамилия",
#             "Список оценок", "Средний рейтинг".
#             Определить для класса строковое представление __str__ и конструктор __init__.
#             Определить для класса метод добавления оценки. Оценка может быть от 1 до 5 включительно.

# Задание 3 - создать классы "Продукт" и "Покупатель".
#             Класс "Продукт" должен хранить поля "Идентификатор", "Название", "Цена".
#             Класс "Покупатель" должен хранить поля "Идентификатор", "Имя", "Фамилия", "Список продуктов".
#             Для обоих классов определить строковое представление __str__ и конструктор __init__.
#             Для класса "Покупатель" определить метод добавления продукта в список продуктов.

# Задание 4 - на основе Задания 3 сделать следующее:
#             Класс "Покупатель" должен хранить дополнительно поле "Баланс".
#             Для класса "Покупатель" определить метод покупки продуктов из списка продуктов.
#             При вызове этого метода, из баланса покупателя должна сниматься итоговая сумма продуктов
#             из списка продуктов, а список продуктов должен опустошаться.

# Задание 5 - создать класс "Студент". Этот класс должен хранить поля "Идентификатор", "Имя", "Фамилия",
#             "Группа", "Список оценок", "Средняя оценка". Все поля должны быть приватными.
#             Определить для класса методы __str__ и __init__, а также сеттеры и геттеры.
#             Определить для класса метод добавления оценки. Оценка может быть от 1 до 12 включительно.

# Задание 6 - на основе Задания 5 выполнить следующее:
#             Реализовать следующее меню
#             1. Вывести в консоль список студентов
#             2. Добавить нового студента
#             3. Добавить оценку студенту
#             4. Показать информацию по идентификатору студента
#             5. Изменить данные студента по идентификатору
#             6. Удалить студента по идентификатору
#             7. Завершить программу

# Задание 7 - создать классы "Продукт" и "Покупатель".
#             Класс "Продукт" должен хранить поля "Идентификатор", "Название", "Цена".
#             Класс "Покупатель" должен хранить поля "Идентификатор", "Имя", "Фамилия", "Список продуктов".
#             Для обоих классов определить строковое представление __str__ и конструктор __init__, а также
#             сеттеры и геттеры.
#             Для класса "Покупатель" __str__ должен возвращать только строку формата "Идентификатор Имя Фамилия".
#             Для класса "Покупатель" определить метод добавления продукта в список продуктов.

# Задание 8 - на основе Задания 7 сделать следующее:
#             Класс "Покупатель" должен хранить дополнительно поле "Баланс". Сделать для него сеттер и геттер.
#             Для класса "Покупатель" определить метод покупки продуктов из списка продуктов.
#             При вызове этого метода, из баланса покупателя должна сниматься итоговая сумма продуктов
#             из списка продуктов, а список продуктов должен опустошаться.

# Задание 9 - создать класс "Человек". Этот класс должен хранить поля "Имя", "Фамилия", "Возраст".
#             Все поля должны быть protected. Определить для класса конструктор __init__, методы __str__,
#             сеттеры и геттеры.
#             Cоздать класс "Студент", который наследуется от класса "Человек". Этот класс должен
#             хранить поля "Группа", "Список оценок", "Средняя оценка". Все поля должны быть приватными.
#             Определить для класса конструктор __init__, методы __str__, сеттеры и геттеры, а также
#             добавление оценки.

# Задание 10 - создать класс "Устройство". Этот класс должен хранить "Название", "Описание".
#              Определить для класса конструктор и строковое представление.
#              Определить метод "Приготовить" - просто выводит в консоль "Готовка".
#              Создать ещё 3 класса - "Кофемашина", "Блендер", "Мясорубка". Сделать так, чтобы они
#              наследовались от "Устройство".
#              Переопределить для них конструктор и строковое представление.
#              Переопределить для них метод "Приготовить" по своему усмотрению.

# Задание 11 - создать класс "Пользователь". Этот класс должен хранить "Логин", "Пароль", "Имя".
#              Определить конструктор и строковое представление, а также сеттеры и геттеры.
#              Создать классы "Сотрудник" и "Клиент", которые наследуются от класса "Пользователь".
#              "Сотрудник" и "Клиент" должны хранить "Роль".
#              Определить конструктор и строковое представление, а также сеттеры и геттеры.
#              Используя эти классы, реализуйте меню:
#              1. Войти
#              2. Зарегистрироваться
#              3. Завершить программу
#
#              При выборе пункта 1, программа запрашивает "Логин" и "Пароль". Если они верны, то в
#              зависимости от роли пользователя выводится меню. Для "Сотрудника" это:
#              1. Показать всех пользователей
#              2. Зарегистрировать сотрудника
#              3. Выйти из аккаунта
#              4. Завершить программу
#
#              При выборе пункта 1, программа выводит список всех зарегистрированных пользователей.
#              При выборе пункта 2, программа запрашивает "Имя", "Логин", "Пароль", создаёт объект
#              класса "Сотрудник" и помещает его в список пользователей.
#              При выборе пункта 3, программа возвращается в предыдущее меню.
#              При выборе пункта 4, программа завершается.
#
#              Для "Клиента" это меню:
#              1. Показать всех пользователей
#              2. Выйти из аккаунта
#              3. Завершить программу
#
#              При выборе пункта 1, программа выводит список всех зарегистрированных пользователей.
#              При выборе пункта 2, программа возвращается в предыдущее меню.
#              При выборе пункта 3, программа завершается.
#
#              В главном меню при выборе пункта 2, программа запрашивает "Имя", "Логин", "Пароль" и
#              создаёт объект класса "Клиент" и помещает его в список пользователей.
#              В главном меню при выборе пункта 3, программа завершается.
# ====================================================================================================


# ==============================================LESSON45==============================================
# Принципы ООП - Полиморфизм
# Статические методы, методы класса и экземпляра класса
# Полиморфизм на примерах
# Утиная типизация


# class Student:
#     __name = "Unknown"
#     __age = 0
#     __group = "C#"
#
#     def __init__(self, name: str, age: int):
#         self.__name = name
#         self.__age = age
#
#     def __str__(self):
#         result = f"{self.__name} {self.__age} {self.__group}"
#         return result
#
#     def set_group(self, group: str):  # Метод экземпляра класса
#         self.__group = group
#
#     @staticmethod
#     def generate_student():  # Статический метод
#         return Student("TestName", 47)
#
#     @classmethod
#     def switch_default_group(cls):  # Метод класса
#         if cls.__group == "Python":
#             cls.__group = "C#"
#         else:
#             cls.__group = "Python"


# Object method working example
# student_1 = Student("Tom", 25)
# print(student_1)
#
# student_1.set_group("Java")
# print(student_1)


# Static method working example
# print(Student.generate_student())


# Class method working example
# student_1 = Student("Tom", 25)
# student_2 = Student("Bob", 19)
# print(student_1)
# print(student_2)
#
# print()
# Student.switch_default_group()
# print(student_1)
# print(student_2)
#
# print()
# Student.switch_default_group()
# print(student_1)
# print(student_2)


# student_1 = Student("Tom", 25)
# student_1.set_group("Java")
# Student.switch_default_group()
# print(student_1)


# Полиморфизм
# class Cat:
#     def say(self):
#         print("Meow!")
#
#
# class Dog:
#     def say(self):
#         print("Woof!")
#
#
# class Human:
#     def say(self):
#         print("Hello!")
#
#
# some_cat = Cat()
# some_dog = Dog()
# some_human = Human()
#
# for animal in (some_cat, some_dog, some_human):
#     animal.say()  # Утиная типизация


# class Student:
#     __name = "Unknown"
#     __scholarship = 0
#
#     def __init__(self, name, scholarship):
#         self.__name = name
#         self.__scholarship = scholarship
#
#     def get_income(self):
#         return "Scholarship: {}".format(self.__scholarship)
#
#
# class Employee:
#     __name = "Unknown"
#     __salary = 0
#
#     def __init__(self, name, salary):
#         self.__name = name
#         self.__salary = salary * 0.95
#
#     def get_income(self):
#         return "Salary: {}".format(self.__salary)
#
#
# student_1 = Student("Tom", 400)
# employee_1 = Employee("Bob", 2500)
#
# for human in (student_1, employee_1):
#     print(human.get_income())
#
# print(student_1.get_income())
# print(employee_1.get_income())

# ====================================================================================================
# ДЗ48 Задание 1.
# Создайте класс "Банковская карта". Укажите в ней поля "Идентификатор", "Имя", "Фамилия", "Месяц",
# "Год", "Баланс".
# Определите для класса строковое представление. Оно должно возвращать строку формата
# "Идентификатор Имя Баланс".
# Определите для класса конструктор. Он должен принимать каждое поле.
# Определите для класса свойства.
# В конструкторе и свойстве для "Баланс" сделать так, что если для баланса выставляется число
# меньше нуля, то программа выставляет 0.
#
# Определите для класса метод пополнения баланса.
# Метод принимает целое число. Если число отрицательное, то метод возвращает False.
# В противном случае метод добавляет к балансу число и возвращает True.
#
# Определите для класса метод снятия с баланса.
# Метод принимает целое число. Если число отрицательное или число больше баланса, то метод
# возвращает False.
# В противном случае метод снимает с баланса число и возвращает True.

# ====================================================================================================

# ==============================================LESSON46==============================================
# magic-методы
# Перегрузка операторов
# __eq__(), __ne__(), __lt__(), __le__(), __gt__(), __ge__(), __getitem__(), __setitem__()


# class Student:
#     __name = "Unknown"
#     __age = 0
#     __grades = list()
#     __average_grade = 0
#
#     def __init__(self, name, age, grades):
#         self.__name = name
#         self.__age = age
#         self.__grades = grades
#         if len(self.__grades) > 0:
#             self.__average_grade = sum(self.__grades) / len(self.__grades)
#
#     def __str__(self):
#         result = f"{self.__name} {self.__age} {self.__grades} {self.__average_grade}"
#         return result
#
#     def __gt__(self, other):
#         return self.__average_grade > other.__average_grade
#
#     def student_gt(self, other):
#         return self.__average_grade > other.__average_grade
#
#     def __lt__(self, other):
#         return self.__average_grade < other.__average_grade
#
#     def __getitem__(self, item):
#         if item < len(self.__grades):
#             result = self.__grades[item]
#         else:
#             result = -1
#         return result
#
#     # def __eq__(self, other):
#     #     return self.__name == other.__name and self.__age == other.__age
#
#
# student_1 = Student("Tom", 25, [11, 12, 10, 12])
# student_2 = Student("Tom", 25, [10, 9, 10, 12])
#
# print(student_1)
# print(student_2)
# print(student_1.student_gt(student_2))
# print(student_1 > student_2)
# print(student_1 < student_2)
# print(student_1[0])
# print(student_1 == student_2)

# ====================================================================================================

# ДЗ48 Задание 2. (на основе задания 1)
# Создайте класс "Клиент". Укажите в нём поля "Идентификатор", "Имя", "Фамилия", "Список банковских карт".
# Определите для класса строковое представление. Оно должно возвращать строку формата
# "Идентификатор Имя Фамилия".
# Определите для класса конструктор. Он должен принимать все поля.
# Определите для класса свойства.
#
# Определите для класса поиск банковской карты.
# Метод принимает идентификатор банковской карты, возвращает индекс списка, если идентификатор найден
# в списке, и -1, если не найден.
#
# Определите для класса получение банковской карты по идентификатору.
# Метод принимает идентификатор банковской карты. Метод вызывает поиск идентификатора.
# Если идентификатор есть в списке, то возвращает объект по найденному индексу.
# В противном случае возвращает None.
#
# Определите для класса добавление банковской карты.
# Метод принимает объект класса "Банковская карта". Метод вызывает метод поиска банковской карты.
# Если идентификатор этой банковской карты уже есть в списке, то возвращается False.
# В противном случае банковская карта добавляется в список банковских карт и возвращается True.
#
# Определите для класса изменение банковской карты.
# Метод принимает идентификатор банковской карты для поиска и объект класса "Банковская карта".
# Метод вызывает метод поиска банковской карты.
# Если идентификатор для поиска есть в списке и идентификатор для поиска совпадает с идентификатором
# из принятого объекта или идентификатор для поиска есть в списке, но идентификатора
# из принятого объекта нет в списке, то происходит замена.
# Объект по идентификатору для поиска заменяется на принятый объект и возвращается True.
#
# Определите для класса удаление банковской карты.
# Метод принимает идентификатор банковской карты. Метод вызывает метод поиска банковской карты.
# Если идентификатор этой банковской карты есть в списке, то банковская карта удаляется из списка
# и возвращается True. В противном случае возвращается False.
#
# Определите для класса метод пополнения баланса банковской карты.
# Метод принимает идентификатор банковской карты и число. Метод вызывает поиск по идентификатору.
# Если идентификатор этой банковской карты есть в списке, то у этой банковской карты вызывается
# метод пополнения и перехватывается то, что этот метод вернёт (True или False).
# Далее оно возвращается. В противном случае возвращается False.
#
# Определите для класса метод снятия баланса банковской карты.
# Метод принимает идентификатор банковской карты и число. Метод вызывает поиск по идентификатору.
# Если идентификатор этой банковской карты есть в списке, то у этой банковской карты вызывается
# метод снятия и перехватывается то, что этот метод вернёт (True или False). Далее оно возвращается.
# В противном случае возвращается False.
# ====================================================================================================


# ==============================================LESSON47==============================================
# Агрегация
# Композиция


# class Student:
#     __name = "Unknown"
#     __age = 0
#
#     def __init__(self, name: str, age: int):
#         self.__name = name
#         self.__age = age
#
#     def __str__(self):
#         result = f"{self.__name} {self.__age}"
#         return result
#
#
# class Group:
#     __title = "Unknown"
#     __amount_students = 0
#     __students = list()
#
#     def __init__(self, title="Unknown"):
#         self.__title = title
#
#     def add_student(self, student: Student):  # Агрегация
#         self.__amount_students += 1
#         self.__students.append(student)
#
#     def create_student(self, name: str, age: int):
#         new_student = Student(name, age)  # Композиция
#         self.add_student(new_student)
#
#     def get_title(self):
#         return self.__title
#
#     def __str__(self):
#         result = f"{self.__title} {self.__amount_students}"
#         for student in self.__students:
#             result += "\n{}".format(student)
#         return result


# student_1 = Student("Tom", 25)
# group = Group("Python")
# group.add_student(student_1)
# print(group)

# print()
# group.create_student("Kate", 25)
# print(group)

# ====================================================================================================

# class BankCard:
#     __id = ""
#     __f_name = ""
#     __l_name = ""
#     __month = 0
#     __year = 0
#     __balance = 0
#
#     # Это конструктор. Принимает идентификатор, имя, ...
#     def __init__(self, id: str, f_name: str, l_name: str, month: int, year: int, balance: int):
#         self.__id = id
#         self.__f_name = f_name
#         self.__l_name = l_name
#         self.__month = month
#         self.__year = year
#         self.__balance = balance
#
#     def __str__(self):
#         result = f"{self.__id} {self.__f_name} {self.__balance}"
#         return result
#
#     def set_f_name(self, f_name: str):
#         self.__f_name = f_name
#
#     def get_f_name(self):
#         return self.__f_name
#
#     def set_l_name(self, l_name: str):
#         self.__l_name = l_name
#
#     def get_l_name(self):
#         return self.__l_name
#
#     def set_id(self, id: str):
#         self.__id = id
#
#     def get_id(self):
#         return self.__id
#
#     def set_month(self, month: int):
#         if month >= 1 and month <= 12:
#             self.__month = month
#         else:
#             self.__month = 1
#
#     def get_month(self):
#         return self.__month
#
#     def set_year(self, year):
#         if year >= 1900 and year <= 2028:
#             self.__year = year
#         else:
#             self.__year = 2028
#
#     def get_year(self):
#         return self.__year
#
#     def set_balance(self, balance: int):
#         if balance >= 0:
#             self.__balance = balance
#         else:
#             self.__balance = 0
#
#     def get_balance(self):
#         return self.__balance
#
#     def withdraw(self, money: int) -> bool:
#         is_success = False
#         if money >= 0 and money <= self.__balance:
#             self.__balance -= money
#             is_success = True
#         return is_success
#
#     def deposit(self, money: int) -> bool:
#         is_success = False
#         if money > 0:
#             self.__balance += money
#             is_success = True
#         return is_success
#
#
# class Customer:
#     __id = ""
#     __f_name = ""
#     __l_name = ""
#     __bank_cards = list()
#
#     def __init__(self, id: str, f_name: str, l_name: str, bank_cards: list[BankCard]):
#         self.__id = id
#         self.__f_name = f_name
#         self.__l_name = l_name
#         self.__bank_cards = bank_cards
#
#     def __str__(self):
#         result = f"{self.__id} {self.__f_name} {self.__l_name}"
#         return result
#
#     def set_id(self, id: str):
#         self.__id = id
#
#     def get_id(self):
#         return self.__id
#
#     def set_f_name(self, f_name: str):
#         self.__f_name = f_name
#
#     def get_f_name(self):
#         return self.__f_name
#
#     def set_l_name(self, l_name: str):
#         self.__l_name = l_name
#
#     def get_l_name(self):
#         return self.__l_name
#
#     def set_bank_cards(self, bank_cards: list[BankCard]):
#         self.__bank_cards = bank_cards
#
#     def get_bank_cards(self):
#         return self.__bank_cards
#
#     def find_card_index_by_id(self, card_id: str):
#         index = -1
#         for i in range(len(self.__bank_cards)):
#             if self.__bank_cards[i].get_id() == card_id:
#                 index = i
#                 break
#         return index
#
#     def find_card_by_id(self, card_id: str) -> BankCard:
#         index = self.find_card_index_by_id(card_id)
#         if index == -1:
#             bank_card = None
#         else:
#             bank_card = self.__bank_cards[index]
#         return bank_card
#
#     def add_bank_card(self, new_card: BankCard) -> bool:
#         is_success = False
#         index = self.find_card_index_by_id(new_card.get_id())
#         if index == -1:
#             self.__bank_cards.append(new_card)
#             is_success = True
#         return is_success
#
#     def change_bank_card_by_id(self, current_card_id: str, new_card: BankCard) -> bool:
#         is_success = False
#         index_current = self.find_card_index_by_id(current_card_id)
#         if index_current:
#             index_new_card = self.find_card_index_by_id(new_card.get_id())
#             if index_new_card == -1 or index_new_card == index_current:
#                 self.__bank_cards[index_current] = new_card
#                 is_success = True
#         return is_success
#
#     def remove_bank_card_by_id(self, card_id: str) -> bool:
#         is_success = False
#         index = self.find_card_index_by_id(card_id)
#         if index != -1:
#             del self.__bank_cards[index]
#             is_success = True
#         return is_success
#
#     def deposit_card_by_id(self, card_id: str, money: int) -> bool:
#         is_success = False
#         index = self.find_card_index_by_id(card_id)
#         if index != -1:
#             is_success = self.__bank_cards[index].deposit(money)
#         return is_success
#
#     def withdraw_card_by_id(self, card_id: str, money: int) -> bool:
#         is_success = False
#         index = self.find_card_index_by_id(card_id)
#         if index != -1:
#             is_success = self.__bank_cards[index].withdraw(money)
#         return is_success
#
# card_1 = BankCard("1234123412341234", "Tom", "Jackson", 5, 2028, 1250)
# card_2 = BankCard("5869586958695869", "Tom", "Jackson", 5, 2028, 750)
#
# customer_1 = Customer("ABC1234", "Tom", "Jackson", [card_1, card_2])

# print(customer_1.find_card_index_by_id("5869586958695869"))
# print(customer_1.find_card_by_id("5869586958695869"))

# card_3 = BankCard("4221422142214221", "Arthur", "Morgan", 10, 2028, 500)
# if customer_1.add_bank_card(card_3):
#     print("ADDED")
#     for card in customer_1.get_bank_cards():
#         print(card)
# else:
#     print("FOUND DUPLICATE")
#
# card_4 = BankCard("4221422142214221", "Arthur", "Morgan", 10, 2028, 500)
# if customer_1.add_bank_card(card_4):
#     print("ADDED")
#     for card in customer_1.get_bank_cards():
#         print(card)
# else:
#     print("FOUND DUPLICATE")


# for card in customer_1.get_bank_cards():
#     print(card)
# print()
#
# card_5 = BankCard("5869586958695869", "Arthur", "Morgan", 3, 2026, 250)
# # card_6 = BankCard("4221422142214221", "Arthur", "Morgan", 10, 2028, 500)
# if customer_1.change_bank_card_by_id("5869586958695869", card_5):
#     print("CHANGED")
#     for card in customer_1.get_bank_cards():
#         print(card)
# else:
#     print("FOUND DUPLICATE")


# if customer_1.remove_bank_card_by_id("q33253253"):
#     print("DELETED")
#     for card in customer_1.get_bank_cards():
#         print(card)
# else:
#     print("NOT FOUND")
#     for card in customer_1.get_bank_cards():
#         print(card)


# if customer_1.deposit_card_by_id("5869586958695869", 150):
#     print("SUCCESS")
# else:
#     print("ERROR")
#
# for card in customer_1.get_bank_cards():
#     print(card)


# ДЗ48 Задание 3. (на основе заданий 1 и 2)
# Создайте класс "База данных". Укажите в нём поле "Список клиентов".
# Определите для класса конструктор. Он должен принимать список клиентов.
# Определите для класса свойства.
#
# Определите для класса поиск клиента.
# Метод принимает идентификатор клиента, возвращает индекс списка, если идентификатор найден
# в списке, и -1, если не найден.
#
# Определите для класса получение клиента по идентификатору.
# Метод принимает идентификатор клиента. Метод вызывает поиск клиента.
# Если идентификатор есть в списке, то возвращает объект по найденному индексу.
# В противном случае возвращает None.
#
# Определите для класса добавление клиента.
# Метод принимает объект класса "Клиент". Метод вызывает метод поиска клиента.
# Если идентификатор этого клиента уже есть в списке, то возвращается False.
# В противном случае клиент добавляется в список клиентов и возвращается True.
#
# Определите для класса изменение клиента.
# Метод принимает идентификатор клиента для поиска и объект класса "Клиент".
# Метод вызывает метод поиска клиента.
# Если идентификатор для поиска есть в списке и идентификатор для поиска совпадает
# с идентификатором из принятого объекта или идентификатор для поиска есть в списке,
# но идентификатора из принятого объекта нет в списке, то происходит замена.
# Объект по идентификатору для поиска заменяется на принятый объект и возвращается True.
#
# Определите для класса удаление клиента.
# Метод принимает идентификатор клиента. Метод вызывает метод поиска клиента.
# Если идентификатор этого клиента есть в списке, то клиент удаляется из списка и возвращается True.
# В противном случае возвращается False.
# ====================================================================================================


# ==============================================LESSON48==============================================
# Использование своих классов.

# ====================================================================================================
# ДЗ48 Задание 4. (на основе заданий 1, 2 и 3)
# Реализовать следующее меню:
# 1. Показать всех клиентов
# 2. Добавить нового клиента
# 3. Показать клиента по его идентификатору
# 4. Изменить данные клиента по его идентификатору
# 5. Удалить клиента по его идентификатору
# 6. Завершить программу
#
# При выборе пункта 1 программа вызывает свойство списка из объекта класса "База данных",
# проходится по каждому клиенту и выводит их в консоль.
#
# При выборе пункта 2 должны запрашиваться данные из консоли, формироваться объект
# класса "Клиент" и вызываться метод добавления клиента у объекта класса "База данных".
# В зависимости от результата работы этого метода, в консоли выводится оповещение.
#
# При выборе пункта 3 должен запрашиваться идентификатор из консоли, вызываться метод
# получения строкового представления по идентификатору у объекта класса "База данных"
# и выводиться результат работы метода.
#
# При выборе пункта 4 должен запрашиваться идентификатор клиента из консоли для поиска
# и вызываться метод получения клиента по идентификатору у объекта класса "База данных".
# Если результат работы не None, то программа выводит строковое представление найденного клиента.
# Потом выводится следующее меню:
# 1. Изменить идентификатор, имя и фамилию клиента по его идентификатору
# 2. Добавить новую банковскую карточку клиенту
# 3. Изменить данные банковской карточки у клиента
# 4. Удалить банковскую карточку у клиента
# 5. Пополнить баланс банковской карты
# 6. Снять с баланса банковской карты
# 7. Вернуться в главное меню
#
# При выборе пункта 1 должны запрашиваться из консоли новый идентификатор клиента, имя и фамилия.
# Список карт забирается у найденного клиента.
# Далее формируется новый объект класса "Клиент" из этих данных и вызывается метод
# изменения клиента у объекта класса "Базы данных".
# В зависимости от результата работы этого метода, в консоли выводится оповещение.
#
# При выборе пункта 2 должны запрашиваться данные из консоли, формироваться объект
# класса "Банковская карта" и вызываться метод добавления карты у клиента.
# В зависимости от результата работы этого метода, в консоли выводится оповещение.
#
# При выборе пункта 3 должен запрашиваться идентификатор банковской карты из консоли и вызываться
# метод получения банковской карты по идентификатору у клиента.
# Если результат работы не None, то программа выводит строковое представление найденной
# банковской карты.
# Потом программа запрашивает из консоли новый идентификатор, имя, фамилия, месяц, год,
# баланс, формирует из этих данных новый объект класса "Банковская карта" и вызывает метод
# изменения банковской карты у клиента.
# В зависимости от результата работы этого метода, в консоли выводится оповещение.
#
# При выборе пункта 4 должен запрашиваться идентификатор банковской карты из консоли и
# вызываться метод удаления банковской карты у клиента.
# В зависимости от результата работы этого метода, в консоли выводится оповещение.
#
# При выборе пункта 5 должен запрашиваться идентификатор банковской карты и число из консоли,
# после этого вызываться метод пополнения баланса банковской карты у клиента.
# В зависимости от результата работы этого метода, в консоли выводится оповещение.
#
# При выборе пункта 6 должен запрашиваться идентификатор банковской карты и число из консоли,
# после этого вызываться метод снятия с баланса банковской карты у клиента.
# В зависимости от результата работы этого метода, в консоли выводится оповещение.
#
# При выборе пункта 7 программа возвращается в главное меню.
#
# В главном меню при выборе пункта 5 должен запрашиваться идентификатор клиента из консоли и
# вызываться метод удаления клиента у объекта класса "База данных".
# В зависимости от результата работы этого метода, в консоли выводится оповещение.
#
# В главном меню при выборе пункта 6 программа завершается.
# ====================================================================================================
