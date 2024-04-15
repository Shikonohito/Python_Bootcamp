# ==============================================LESSON64==============================================
# Создать класс Customer. Поля:
# age - принимает тип данных int от 0 до 123 включительно.
#       Если передавать ниже нуля, то выставляется 0.
#       Если передавать не int, то выставляется 0.
#       Если передавать больше 123, то выставляется 123.
#
# name - принимает тип данных str только из символов алфавита.
#        Если передавать имя только большими буквами, имя должно переводиться с первой заглавной буквой.
#        Если передавать имя только с маленькими буквами, имя должно переводиться с первой заглавной буквой.
#        Если передавать строку только с цифрами, в имя должна выставляться строка "Unknown".
#        Если передавать строку с буквами и цифрами, в имя должна выставляться строка "Unknown".
#        Если передавать не str, в имя должна выставляться строка "Unknown".
#
# married - принимает тип данных bool.
#           Если передавать True, выставляется True.
#           Если передавать False, выставляется False.
#           Если передавать не bool, выставляется False.


# class Customer:
#     __name = ""
#     __age = 0
#     __married = False
#
#     def __init__(self, name: str, age: int, married: bool):
#         self.__name = name
#         self.__age = age
#         self.__married = married
#
#     def __str__(self):
#         result = f"Name: {self.__name}\nAge: {self.__age}"
#         if self.__married:
#             result += "\nMarried: Yes"
#         else:
#             result += "\nMarried: No"
#         return result
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         if isinstance(age, int):
#             if age > 123:
#                 self.__age = 123
#             elif age < 0:
#                 self.__age = 0
#             else:
#                 self.__age = age
#         else:
#             self.__age = 0
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         if isinstance(name, str):
#             if name.isalpha():
#                 self.__name = name.capitalize()
#             else:
#                 self.__name = "Unknown"
#         else:
#             self.__name = "Unknown"
#
#     def get_married(self):
#         return self.__married
#
#     def set_married(self, married):
#         self.__married = married
#
#
# import unittest
#
#
# class CustomerInitTest(unittest.TestCase):
#     def test_initialization(self):
#         customer = Customer("Tom", 25, True)
#         expected = "Tom"
#         actual = customer.get_name()
#         self.assertEqual(expected, actual)
#
#         expected = 25
#         actual = customer.get_age()
#         self.assertEqual(expected, actual)
#
#         expected = True
#         actual = customer.get_married()
#         self.assertEqual(expected, actual)
#
#
# class CustomerAgeTest(unittest.TestCase):
#     def setUp(self):
#         self.customer = Customer("Tom", 25, True)
#
#     def test_0_set_30(self):
#         self.customer.set_age(30)
#         expected = 30
#         actual = self.customer.get_age()
#         self.assertEqual(expected, actual)
#
#     def test_1_set_greater_than_123(self):
#         self.customer.set_age(500)
#         expected = 123
#         actual = self.customer.get_age()
#         self.assertEqual(expected, actual)
#
#     def test_2_set_equal_to_123(self):
#         self.customer.set_age(123)
#         expected = 123
#         actual = self.customer.get_age()
#         self.assertEqual(expected, actual)
#
#     def test_3_set_less_than_0(self):
#         self.customer.set_age(-120)
#         expected = 0
#         actual = self.customer.get_age()
#         self.assertEqual(expected, actual)
#
#     def test_4_set_equal_to_0(self):
#         self.customer.set_age(0)
#         expected = 0
#         actual = self.customer.get_age()
#         self.assertEqual(expected, actual)
#
#     def test_5_set_str(self):
#         self.customer.set_age("Some str")
#         expected = 0
#         actual = self.customer.get_age()
#         self.assertEqual(expected, actual)
#
#
# class CustomerNameTest(unittest.TestCase):
#     def setUp(self):
#         self.customer = Customer("Tom", 25, True)
#
#     def test_0_set_alpha_str(self):
#         self.customer.set_name("Tom")
#         expected = "Tom"
#         actual = self.customer.get_name()
#         self.assertEqual(expected, actual)
#
#     def test_1_set_upper_alpha_str(self):
#         self.customer.set_name("TOM")
#         expected = "Tom"
#         actual = self.customer.get_name()
#         self.assertEqual(expected, actual)
#
#     def test_2_set_lower_alpha_str(self):
#         self.customer.set_name("tom")
#         expected = "Tom"
#         actual = self.customer.get_name()
#         self.assertEqual(expected, actual)
#
#     def test_3_set_digit_str(self):
#         self.customer.set_name("123")
#         expected = "Unknown"
#         actual = self.customer.get_name()
#         self.assertEqual(expected, actual)
#
#     def test_4_set_alphadigit_str(self):
#         self.customer.set_name("Tom123")
#         expected = "Unknown"
#         actual = self.customer.get_name()
#         self.assertEqual(expected, actual)
#
#     def test_5_set_int(self):
#         self.customer.set_name(25)
#         expected = "Unknown"
#         actual = self.customer.get_name()
#         self.assertEqual(expected, actual)
#
#
# class CustomerMarriedTest(unittest.TestCase):
#     def setUp(self):
#         self.customer = Customer("Tom", 25, True)
#
#     def test_0_set_true(self):
#         self.customer.set_married(True)
#         expected = True
#         actual = self.customer.get_married()
#         self.assertEqual(expected, actual)
#
#     def test_1_set_false(self):
#         self.customer.set_married(False)
#         expected = False
#         actual = self.customer.get_married()
#         self.assertEqual(expected, actual)
#
#     def test_2_set_str(self):
#         self.customer.set_married("Some str")
#         expected = False
#         actual = self.customer.get_married()
#         self.assertEqual(expected, actual)
#
#
# if __name__ == "__main__":
#     unittest.main()

# ====================================================================================================

# class Student:
#     def __init__(self, name: str, age: int, group: str, grades: list):
#         self.__name = name
#         self.__age = age
#         self.__group = group
#         self.__grades = grades
#         self.__avg_grade = sum(self.__grades) / len(self.__grades)
#
#     def get_name(self) -> str:
#         return self.__name
#     def set_name(self, name: str) -> None:
#         self.__name = name
#
#     def get_age(self) -> int:
#         return self.__age
#     def set_age(self, age: int) -> None:
#         self.__age = age
#
#     def get_group(self) -> str:
#         return self.__group
#     def set_group(self, group: str) -> None:
#         self.__group = group
#
#     def get_grades(self) -> list:
#         return self.__grades
#     def set_grades(self, grades: list) -> None:
#         self.__grades = grades
#
#     def get_avg(self) -> float:
#         return self.__avg_grade
#
#     def add_grade(self, grade: int) -> None:
#         self.__grades.append(grade)


# name - 6 tests
# age - 5 tests
# group - 4 tests
# grades - 6 tests
# avg_grade - 2 tests

# name:
# 1. Передаю "конкретное значение определённого типа", ожидаю "конкретное значение определённого типа".

# age:
# 1.