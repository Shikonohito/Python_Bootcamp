# ==============================================LESSON41==============================================
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


# ==============================================LESSON42==============================================
# Урок 42. Создание и работа со своим классом

# ====================================================================================================
# ПЗ 42.1 - 42.4
# ====================================================================================================

# ==============================================LESSON43==============================================
# Принципы ООП - Инкапсуляция
# Спецификаторы доступа public, private, protected
# Свойства - геттеры и сеттеры
# Деструктор __del__()


# class Positive_Num:
#     num = 0
#
#     def __init__(self, num: int):
#         self.num = num
#
#     def __str__(self):
#         return str(self.num)
#
#
# some_positive_num = Positive_Num(100)
# print(some_positive_num)
#
# some_positive_num = Positive_Num("Some text")
# print(some_positive_num)
#
# some_positive_num.num = "NOT NUM"
# print(some_positive_num)


# class Positive_Num:
#     __num = 0
#
#     def __init__(self, num: int):
#         self.set_num(num)
#
#     def __str__(self):
#         return str(self.__num)
#
#     def __validate_num(self, num: int):
#         if not isinstance(num, int) or num <= 0:
#             raise ValueError("Value must be a positive integer")
#
#     def set_num(self, num: int):
#         self.__validate_num(num)
#         self.__num = num


# some_positive_num = Positive_Num(100)
# print(some_positive_num)
#
# some_positive_num = Positive_Num("Some text")
# print(some_positive_num)
#
# print(some_positive_num.__num)
# some_positive_num.__num = "Some text"
# print(some_positive_num, some_positive_num.__num, sep="\t\t")


# some_positive_num = Positive_Num(100)
# some_positive_num.set_num(50)
# print(some_positive_num)
# some_positive_num.set_num("Some text")
# print(some_positive_num)


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


# ==============================================LESSON45==============================================
# Принципы ООП - Полиморфизм
# Статические методы, методы класса и экземпляра класса
# Полиморфизм на примерах
# Утиная типизация


# class Animal:
#     def make_sound(self):
#         return "???"
#
#
# class Cat(Animal):
#     def make_sound(self):
#         return "Meow"
#
#
# class Dog(Animal):
#     def make_sound(self):
#         return "Bark"
#
#
# dog = Dog()
# cat = Cat()
# animals = [dog, cat]
#
# for animal in animals:
#     print(animal.make_sound())


# class Student:
#     __name = "Unknown"
#     __scholarship = 0
#
#     def __init__(self, name, scholarship):
#         self.__name = name
#         self.__scholarship = scholarship
#
#     def get_schoolarship(self):
#         return f"Scholarship: {self.__scholarship}"
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
#     def get_salary(self):
#         return f"Salary: {self.__salary}"
#
#
# student_1 = Student("Tom", 400)
# employee_1 = Employee("Teston", 2500)
#
# for human in (student_1, employee_1):
#     print(human.?)


# ====================================================================================================

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
#         # print(__name)  # Не видит ни методы, ни поля
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
# print(student_1)
# student_1.set_group("Java")
# Student.switch_default_group()
# print(student_1)
# Student.switch_default_group()
# print(student_1)

# ====================================================================================================
# ПЗ 45.1 - 45.2
# ====================================================================================================


# ==============================================LESSON46==============================================
# magic-методы
# Перегрузка операторов
# __eq__(), __ne__(), __lt__(), __le__(), __gt__(), __ge__(), __getitem__(), __setitem__(), __contains__


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
#     def __getitem__(self, item):  # если __contains__ отсутствует, in использует его
#         if item < len(self.__grades):
#             result = self.__grades[item]
#         else:
#             result = -1
#         return result
#
#     def __eq__(self, other):
#         return self.__name == other.__name and self.__age == other.__age
#
#     def __contains__(self, item):  # in использует его
#         is_found = False
#         for grade in self.__grades:
#             if grade == item:
#                 is_found = True
#                 break
#         return is_found
#
#     def __add__(self, other):
#         self.__grades.append(other)
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
# print(12 in student_2)
#
# student_1 + 20
# print(student_1)

# ====================================================================================================
# ПЗ 46.1 - 46.2
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
# class Teacher:
#     __name = ""
#
#     def __init__(self, name=""):
#         self.__name = name
#
#     def __str__(self):
#         return f"{self.__name}"
#
#
# class Group:
#     __title = "Unknown"
#     __amount_students = 0
#     __students = list()
#     __teacher = Teacher()
#
#     def __init__(self, teacher_name: str, title):
#         self.__teacher = Teacher(teacher_name)  # Композиция
#         self.__title = title
#
#     def add_student(self, student: Student):  # Агрегация
#         self.__amount_students += 1
#         self.__students.append(student)
#
#     def get_title(self):
#         return self.__title
#
#     def __str__(self):
#         result = f"Teacher: {self.__teacher}\nGroup: {self.__title}\t\tNumber of students: {self.__amount_students}"
#         for student in self.__students:
#             result += "\n{}".format(student)
#         return result
#
#
# student_1 = Student("Tom", 25)
# group = Group("Teston", "Python")
# group.add_student(student_1)
# print(group)


# ====================================================================================================
# ДЗ 48.1 - 48.2
# ====================================================================================================


# ==============================================LESSON48==============================================
# Использование своих классов.

# ====================================================================================================
# ДЗ 48.1 - 48.2
# ====================================================================================================
