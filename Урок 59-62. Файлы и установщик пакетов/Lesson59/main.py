# ==============================================LESSON59==============================================
# Работа с файлами. Readline, Writeline, Pickle. Бинарная запись DB.


# with open("test01.txt", "w") as test_file:
#     test_file.write("HELLO")

# with open("test01.txt", "r") as test_file:
#     read_data = test_file.read()
#     print(read_data)

# with open("test01.txt", "a") as test_file:
#     test_file.write("Additional text")

# with open("test02.txt", "r") as test_file:
#     read_data = test_file.read()
#     print(read_data)

# with open("test02.txt", "r") as test_file:
#     for line in test_file:
#         print("LINE", line, end="")

# with open("test02.txt", "r") as test_file:
#     first = test_file.readline()
#     print(first)
#     other_lines = test_file.readlines()
#     print(other_lines)

# some_data = ["100", "\n200", "\n300"]
# # some_data = [100, 200, 300]
# with open("test03.txt", "w") as test_file:
#     test_file.writelines(some_data)

# ====================================================================================================
# ПЗ 59.1 - 59.3
# ====================================================================================================


# import pickle
#
#
# class Customer:
#     __id = ""
#     __name = ""
#
#     def __init__(self, id: str, name: str):
#         self.__id = id
#         self.__name = name
#
#     def __str__(self):
#         result = f"{self.__id} {self.__name}"
#         return result
#
#
# class CustomerDB:
#     __customer_list = list()
#
#     def __init__(self):
#         self.__customer_list = list()
#
#     def get_customer_list(self):
#         return self.__customer_list
#
#     def add_customer(self, new_customer: Customer):
#         self.__customer_list.append(new_customer)
#
#     def save_db(self, db_file_path: str):
#         with open(db_file_path, "wb") as data_file:
#             pickle.dump(self, data_file)
#
#     @staticmethod
#     def load_db(db_file_path: str) -> 'CustomerDB':
#         with open(db_file_path, "rb") as data_file:
#             loaded_db = pickle.load(data_file)
#             return loaded_db
#
#
# # customer_1 = Customer("ABC1234", "Tom")
# # customer_2 = Customer("XYZ5869", "Bob")
# # customer_3 = Customer("QWE4221", "Arthur")
# #
# # db = CustomerDB()
# # db.add_customer(customer_1)
# # db.add_customer(customer_2)
# # db.add_customer(customer_3)
# #
# # db.save_db("db01.dat")
#
#
# db = CustomerDB.load_db("db01.dat")
#
# for customer in db.get_customer_list():
#     print(customer)
