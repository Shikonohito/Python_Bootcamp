# ==============================================LESSON59==============================================
# Работа с файлами. Readline, Writeline, Pickle. Бинарная запись DB.
import datetime

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
# Задание 1 - пользователь построчно вводит в консоль следующие строки:
#             Имя
#             Фамилия
#             Отчество
#             Требуется записать эти данные файл в одну строчку "Имя Фамилия Отчество".

# Задание 2 - создайте текстовый файл в папке с программой. Построчно заполните её следующим образом:
#             Имя
#             Фамилия
#             Отчество
#             Напишите программу, которая считывает файл и выводит в консоль строку:
#             Имя Фамилия Отчество

# Задание 3 - пользователь вводит в консоль строки данных. Пользователь заканчивает вводить строку
#             только в том случае, если ввёл "END".
#             Например:
#             First
#             Second
#             Third
#             END
#             Программа должна записать в файл каждую строку, кроме END. Гарантируется, что введено
#             будет как минимум одна строка и потом строка END.
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
#     def load_db(self, db_file_path: str):
#         with open(db_file_path, "rb") as data_file:
#             # Считываем временный объект базы данных
#             temp_db: CustomerDB = pickle.load(data_file)
#
#             # Заполняем поля базы данных
#             self.__customer_list = temp_db.get_customer_list()
#
#     # @staticmethod
#     # def static_load_db(db_file_path):
#     #     with open(db_file_path, "rb") as data_file:
#     #         loaded_db: CustomerDB = pickle.load(data_file)
#     #         return loaded_db


# customer_1 = Customer("ABC1234", "Tom")
# customer_2 = Customer("XYZ5869", "Bob")
# customer_3 = Customer("QWE4221", "Arthur")
#
# db = CustomerDB()
# db.add_customer(customer_1)
# db.add_customer(customer_2)
# db.add_customer(customer_3)
#
# db.save_db("db01.dat")


# db = CustomerDB()
# db.load_db("db01.dat")
#
# for customer in db.get_customer_list():
#     print(customer)


# db = CustomerDB.static_load_db("db01.dat")
#
# for customer in db.get_customer_list():
#     print(customer)

# ==============================================LESSON60==============================================
# Использование файлов в Tkinter


# import tkinter
# import pickle
# from tkinter import ttk, messagebox, filedialog
#
# class Person:
#     __id = "0000000"
#     __name = "Unknown"
#     __age = 0
#
#     def __init__(self, id: str, name: str, age: int):
#         self.__id = id
#         self.__name = name
#         self.set_age(age)
#
#     def __str__(self):
#         result = f"{self.__id} {self.__name}"
#         return result
#
#     def set_id(self, new_id: str):
#         self.__id = new_id
#
#     def get_id(self):
#         return self.__id
#
#     def set_name(self, new_name: str):
#         self.__name = new_name
#
#     def get_name(self):
#         return self.__name
#
#     def set_age(self, new_age: int):
#         if new_age < 0:
#             new_age = 0
#         self.__age = new_age
#
#     def get_age(self):
#         return self.__age
#
#
# class Product:
#     __id = "0000000"
#     __name = "Unknown"
#     __price = 0
#
#     def __init__(self, id: str, name: str, price: int):
#         self.__id = id
#         self.__name = name
#         self.set_price(price)
#
#     def __str__(self):
#         result = f"{self.__id} {self.__name}"
#         return result
#
#     def set_id(self, new_id: str):
#         self.__id = new_id
#
#     def get_id(self):
#         return self.__id
#
#     def set_name(self, new_name: str):
#         self.__name = new_name
#
#     def get_name(self):
#         return self.__name
#
#     def set_price(self, price: int):
#         if price < 0:
#             price = 0
#         self.__price = price
#
#     def get_price(self):
#         return self.__price
#
#
# class DB:
#     __person_list = list()
#     __product_list = list()
#
#     def __init__(self):
#         self.__person_list = list()
#         self.__product_list = list()
#
#     def set_persons(self, new_list: list[Person]):
#         self.__person_list = new_list
#
#     def get_persons(self) -> list[Person]:
#         return self.__person_list
#
#     def set_products(self, new_list: list[Product]):
#         self.__product_list = new_list
#
#     def get_products(self) -> list[Product]:
#         return self.__product_list
#
#     def find_person_index_by_id(self, person_id):
#         found_index = -1
#         for i in range(len(self.__person_list)):
#             if person_id == self.__person_list[i].get_id():
#                 found_index = i
#                 break
#         return found_index
#
#     def add_person(self, new_person: Person) -> bool:
#         is_success = False
#         index = self.find_person_index_by_id(new_person.get_id())
#         if index == -1:
#             self.__person_list.append(new_person)
#             is_success = True
#         return is_success
#
#     def remove_person_by_id(self, person_id) -> bool:
#         is_success = False
#         index = self.find_person_index_by_id(person_id)
#         if index != -1:
#             del self.__person_list[index]
#             is_success = True
#         return is_success
#
#     def change_person_by_id(self, person_id, new_person: Person) -> bool:
#         is_success = False
#         index = self.find_person_index_by_id(person_id)
#         if index != -1:
#             new_person_id = new_person.get_id()
#             new_index = self.find_person_index_by_id(new_person_id)
#             if person_id == new_person_id or new_index == -1:
#                 self.__person_list[index] = new_person
#                 is_success = True
#         return is_success
#
#     def get_person_by_id(self, person_id) -> Person:
#         index = self.find_person_index_by_id(person_id)
#         if index != -1:
#             person = self.__person_list[index]
#         else:
#             person = None
#         return person
#
#     def find_product_index_by_id(self, product_id):
#         found_index = -1
#         for i in range(len(self.__product_list)):
#             if product_id == self.__product_list[i].get_id():
#                 found_index = i
#                 break
#         return found_index
#
#     def add_product(self, new_product: Product) -> bool:
#         is_success = False
#         index = self.find_product_index_by_id(new_product.get_id())
#         if index == -1:
#             self.__product_list.append(new_product)
#             is_success = True
#         return is_success
#
#     def remove_product_by_id(self, product_id) -> bool:
#         is_success = False
#         index = self.find_product_index_by_id(product_id)
#         if index != -1:
#             del self.__product_list[index]
#             is_success = True
#         return is_success
#
#     def change_product_by_id(self, product_id, new_product: Product) -> bool:
#         is_success = False
#         index = self.find_product_index_by_id(product_id)
#         if index != -1:
#             new_product_id = new_product.get_id()
#             new_index = self.find_product_index_by_id(new_product_id)
#             if product_id == new_product_id or new_index == -1:
#                 self.__product_list[index] = new_product
#                 is_success = True
#         return is_success
#
#     def get_product_by_id(self, product_id) -> Product:
#         index = self.find_product_index_by_id(product_id)
#         if index != -1:
#             product = self.__product_list[index]
#         else:
#             product = None
#         return product
#
#     def save_db(self, db_file_path):
#         with open(db_file_path, "wb") as data_file:
#             pickle.dump(self, data_file)
#
#     def load_db(self, db_file_path):
#         with open(db_file_path, "rb") as data_file:
#             # Считываем временный объект базы данных
#             temp_db: DB = pickle.load(data_file)
#
#             # Заполняем поля базы данных
#             self.__person_list = temp_db.get_persons()
#             self.__product_list = temp_db.get_products()
#
#     # @staticmethod
#     # def static_load_db(db_file_path) -> "DB":
#     #     with open(db_file_path, "rb") as data_file:
#     #         loaded_db = pickle.load(data_file)
#     #         return loaded_db
#
#
# db = DB()
# # db = DB.static_load_db("database01.dat")
#
# root = tkinter.Tk()
# root.title("Listbox")
# root.geometry("720x480")
# root.resizable(False, False)
#
# # root.iconbitmap(default="img/python.ico")
# # OR
# icon = tkinter.PhotoImage(file="img/python.gif")
# root.iconphoto(False, icon)  # Первый аргумент отвечает за установку иконки на все окна
#
#
# def show_persons():
#     # Скрываем всё, что не нужно
#     frame_product.pack_forget()
#     frame_operations.pack_forget()
#
#     # Показываем всё, что нужно
#     frame_person.pack(fill="both", expand=True)
#     root.geometry("720x480")
#
#
# def show_products():
#     # Скрываем всё, что не нужно
#     frame_person.pack_forget()
#     frame_operations.pack_forget()
#
#     # Показываем всё, что нужно
#     frame_product.pack(fill="both", expand=True)
#     root.geometry("680x350")
#
#
# def show_operations():
#     # Скрываем всё, что не нужно
#     frame_person.pack_forget()
#     frame_product.pack_forget()
#
#     # Показываем всё, что нужно
#     frame_operations.pack(fill="both", expand=True)
#     root.geometry("720x480")
#
#
# def close_program():
#     root.quit()
#
#
# def save_data():
#     # db.save_db("database01.dat")
#
#     filename = filedialog.asksaveasfilename(initialdir=".", title="Select File", filetypes=(("Data files", "*.dat"),
#                                                                                           ("All files", "*.*")))
#     if filename:
#         db.save_db(filename)
#
#
# def fill_person_listbox():
#     person_listbox.delete(0, tkinter.END)
#     for person in db.get_persons():
#         person_listbox.insert(tkinter.END, str(person))
#
#
# def fill_product_listbox():
#     product_listbox.delete(0, tkinter.END)
#     for product in db.get_products():
#         product_listbox.insert(tkinter.END, str(product))
#
#
# def load_data():
#     # db.load_db("database01.dat")
#     # fill_person_listbox()
#     # fill_product_listbox()
#     # person_combobox["values"] = db.get_persons()
#     # product_combobox["values"] = db.get_products()
#
#     filename = filedialog.askopenfilename(initialdir=".", title="Select File", filetypes=(("Data files", "*.dat"),
#                                                                                           ("All files", "*.*")))
#     if filename:
#         db.load_db(filename)
#         fill_person_listbox()
#         fill_product_listbox()
#
#         person_combobox["values"] = db.get_persons()
#         product_combobox["values"] = db.get_products()
#
#
# def exit_program():
#     if messagebox.askyesno("Save Data Base", "Do you want to save data base?"):
#         save_data()
#     if messagebox.askokcancel("Quit", "Do you want to quit?"):
#         root.quit()
#
#
# root.protocol("WM_DELETE_WINDOW", exit_program)
#
# root_menu = tkinter.Menu(root)
# root.config(menu=root_menu)
#
# file_menu = tkinter.Menu(root_menu, tearoff=False)
# file_menu.add_command(label="Save", command=save_data)
# file_menu.add_command(label="Load", command=load_data)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=exit_program)
# root_menu.add_cascade(label="File", menu=file_menu)
#
# show_menu = tkinter.Menu(root_menu, tearoff=False)
# show_menu.add_command(label="Persons", command=show_persons)
# show_menu.add_command(label="Products", command=show_products)
# show_menu.add_command(label="Operations", command=show_operations)
# root_menu.add_cascade(label="Show", menu=show_menu)
#
# # BEGIN FRAME PERSON
# frame_person = tkinter.Frame(root)
# frame_person.pack(expand=True, fill="both")
#
# frame_person_bg_img = tkinter.PhotoImage(file="img/edited_lesson57_frame_person_bg.gif")
# frame_person_bg = tkinter.Label(frame_person, image=frame_person_bg_img)
# frame_person_bg.place(x=0, y=0)
#
# person_listbox = tkinter.Listbox(frame_person, font=("Arial", 18), height=13)
# person_listbox.place(x=20, y=20)
#
# fill_person_listbox()
#
# person_id_lbl = tkinter.Label(frame_person, text="ID:", font=("Arial", 18))
# person_id_lbl.place(x=340, y=20)
# person_id_notify = tkinter.Label(frame_person, text="", font=("Arial", 18))
# person_id_notify.place(x=400, y=20)
#
# person_id_entry = tkinter.Entry(frame_person, font=("Arial", 18))
# person_id_entry.place(x=340, y=60)
#
# person_name_lbl = tkinter.Label(frame_person, text="Name:", font=("Arial", 18))
# person_name_lbl.place(x=340, y=100)
# person_name_notify = tkinter.Label(frame_person, text="", font=("Arial", 18))
# person_name_notify.place(x=440, y=100)
#
# person_name_entry = tkinter.Entry(frame_person, font=("Arial", 18))
# person_name_entry.place(x=340, y=140)
#
# person_age_lbl = tkinter.Label(frame_person, text="Age:", font=("Arial", 18))
# person_age_lbl.place(x=340, y=180)
# person_age_notify = tkinter.Label(frame_person, text="", font=("Arial", 18))
# person_age_notify.place(x=415, y=180)
#
# person_age_entry = tkinter.Entry(frame_person, font=("Arial", 18), width=3)
# person_age_entry.place(x=340, y=220)
#
# person_info_lbl = tkinter.Label(frame_person, text="User info:", font=("Arial", 18))
# person_info_lbl.place(x=340, y=300)
#
# person_info = tkinter.Label(frame_person, text="", font=("Arial", 18))
# person_info.place(x=340, y=340)
#
#
# def add_person():
#     # Считываем данные из полей фронтенда
#     new_id = person_id_entry.get()
#     new_name = person_name_entry.get()
#     new_age = person_age_entry.get()
#
#     is_correct_entries = True
#
#     # Проверяем данные из полей
#     if new_id == "":
#         person_id_notify.config(text="Fill this entry!", fg="red")
#         is_correct_entries = False
#     elif not new_id.isalnum():
#         person_id_notify.config(text="Only letters and numbers!", fg="red")
#         is_correct_entries = False
#     else:  # Приводим данные из фронтенда в порядок
#         person_id_notify.config(text="", fg="black")
#         new_id = new_id.upper()
#
#     if new_name == "":
#         person_name_notify.config(text="Fill this entry!", fg="red")
#         is_correct_entries = False
#     elif not new_name.isalpha():
#         person_name_notify.config(text="Only letters!", fg="red")
#         is_correct_entries = False
#     else:  # Приводим данные из фронтенда в порядок
#         person_name_notify.config(text="", fg="black")
#         new_name = new_name.capitalize()
#
#     if new_age == "":
#         person_age_notify.config(text="Fill this entry!", fg="red")
#         is_correct_entries = False
#     elif not new_age.isdigit():
#         person_age_notify.config(text="Entry must be num!", fg="red")
#         is_correct_entries = False
#     else:  # Приводим данные из фронтенда в порядок
#         person_age_notify.config(text="", fg="black")
#         new_age = int(new_age)
#
#     if is_correct_entries:
#         # Формируем из данных объект
#         new_person = Person(new_id, new_name, new_age)
#
#         # Добавляем объект в бэкенд
#         if db.add_person(new_person):
#             # Формируем строковое представление объекта
#             new_person_listbox = str(new_person)
#
#             # Добавляем строковое представление объекта во фронтенд
#             person_listbox.insert(tkinter.END, new_person_listbox)
#
#             person_combobox["values"] = db.get_persons()
#
#             person_info.config(text="", fg="black")
#         else:
#             person_info.config(text="Duplicate found!", fg="red")
#
#         # Для проверки соответствия наполнения бэкенда и фронтенда
#         print()
#         for person in db.get_persons():
#             print(f"{person.get_id()} {person.get_name()} {person.get_age()}")
#
#
# person_add_btn = tkinter.Button(frame_person, text="New", font=("Arial", 14), command=add_person)
# person_add_btn.place(x=20, y=400)
#
#
# def delete_person():
#     # Считываем индексы выделенных элементов из фронтенда
#     person_listbox_ind = person_listbox.curselection()
#     if len(person_listbox_ind) > 0:
#         # Считываем элемент по индексу
#         selected_person = person_listbox.get(person_listbox_ind[0])
#
#         # Отдельно выделяем идентификатор
#         customer_id = selected_person.split()[0]
#
#         # Пытаемся удалить из бэкенда
#         if db.remove_person_by_id(customer_id):
#             # Удаляем из фронтенда
#             person_listbox.delete(person_listbox_ind[0])
#
#             person_combobox["values"] = db.get_persons()
#
#     # Для проверки соответствия наполнения бэкенда и фронтенда
#     print()
#     for person in db.get_persons():
#         print(f"{person.get_id()} {person.get_name()} {person.get_age()}")
#
#
# person_delete_btn = tkinter.Button(frame_person, text="Delete", font=("Arial", 14), command=delete_person)
# person_delete_btn.place(x=75, y=400)
#
#
# def change_person():
#     # Считываем индексы выделенных элементов из фронтенда
#     person_listbox_ind = person_listbox.curselection()
#     if len(person_listbox_ind) > 0:
#         # Считываем элемент по индексу
#         selected_person = person_listbox.get(person_listbox_ind[0])
#
#         # Отдельно выделяем идентификатор
#         selected_id = selected_person.split()[0]
#
#         # Считываем данные из полей фронтенда
#         new_id = person_id_entry.get()
#         new_name = person_name_entry.get()
#         new_age = person_age_entry.get()
#
#         is_correct_entries = True
#
#         # Проверяем данные из полей
#         if new_id == "":
#             person_id_notify.config(text="Fill this entry!", fg="red")
#             is_correct_entries = False
#         elif not new_id.isalnum():
#             person_id_notify.config(text="Only letters and numbers!", fg="red")
#             is_correct_entries = False
#         else:  # Приводим данные из фронтенда в порядок
#             person_id_notify.config(text="", fg="black")
#             new_id = new_id.upper()
#
#         if new_name == "":
#             person_name_notify.config(text="Fill this entry!", fg="red")
#             is_correct_entries = False
#         elif not new_name.isalpha():
#             person_name_notify.config(text="Only letters!", fg="red")
#             is_correct_entries = False
#         else:  # Приводим данные из фронтенда в порядок
#             person_name_notify.config(text="", fg="black")
#             new_name = new_name.capitalize()
#
#         if new_age == "":
#             person_age_notify.config(text="Fill this entry!", fg="red")
#             is_correct_entries = False
#         elif not new_age.isdigit():
#             person_age_notify.config(text="Entry must be num!", fg="red")
#             is_correct_entries = False
#         else:  # Приводим данные из фронтенда в порядок
#             person_age_notify.config(text="", fg="black")
#             new_age = int(new_age)
#
#         if is_correct_entries:
#             # Формируем из данных объект
#             new_person = Person(new_id, new_name, new_age)
#
#             # Пытаемся изменить объект в бэкенде
#             if db.change_person_by_id(selected_id, new_person):
#                 # Формируем строковое представление объекта
#                 new_person_listbox = str(new_person)
#
#                 # Изменяем данные во фронтенде
#                 person_listbox.delete(person_listbox_ind[0])
#                 person_listbox.insert(person_listbox_ind[0], new_person_listbox)
#
#                 person_combobox["values"] = db.get_persons()
#
#                 person_info.config(text="", fg="black")
#             else:
#                 person_info.config(text="Duplicate found!", fg="red")
#
#         # Для проверки соответствия наполнения бэкенда и фронтенда
#         print()
#         for person in db.get_persons():
#             print(f"{person.get_id()} {person.get_name()} {person.get_age()}")
#
#
# person_change_btn = tkinter.Button(frame_person, text="Change", font=("Arial", 14), command=change_person)
# person_change_btn.place(x=150, y=400)
#
#
# def show_person_data():
#     # Считываем индексы выделенных элементов из фронтенда
#     person_listbox_ind = person_listbox.curselection()
#     if len(person_listbox_ind) > 0:
#         # Считываем элемент по индексу
#         selected_person = person_listbox.get(person_listbox_ind[0])
#
#         # Отдельно выделяем идентификатор
#         selected_id = selected_person.split()[0]
#
#         # Запрашиваем из бэкенда объект по идентификатору
#         person = db.get_person_by_id(selected_id)
#         if person:
#             person_data = f"ID: {person.get_id()}\nName: {person.get_name()}\nAge: {person.get_age()}"
#             person_info.config(text=person_data, justify="left")
#
#
# person_info_btn = tkinter.Button(frame_person, text="Info", font=("Arial", 14), command=show_person_data)
# person_info_btn.place(x=235, y=400)
#
# def fill_person_info(event):
#     person_listbox_ind = person_listbox.curselection()
#     if len(person_listbox_ind) > 0:
#         selected_person = person_listbox.get(person_listbox_ind[0])
#         selected_id = selected_person.split()[0]
#         person = db.get_person_by_id(selected_id)
#         if person:
#             person_id_entry.delete(0, tkinter.END)
#             person_id_entry.insert(0, person.get_id())
#             person_name_entry.delete(0, tkinter.END)
#             person_name_entry.insert(0, person.get_name())
#             person_age_entry.delete(0, tkinter.END)
#             person_age_entry.insert(0, person.get_age())
#
#
# person_listbox.bind("<<ListboxSelect>>", fill_person_info)
#
# # END FRAME PERSON
#
# # BEGIN FRAME PRODUCT
# frame_product = tkinter.Frame(root)
# frame_product.pack_forget()
#
# frame_product_bg_img = tkinter.PhotoImage(file="img/edited_lesson57_frame_product_bg.gif")
# frame_product_bg = tkinter.Label(frame_product, image=frame_product_bg_img)
# frame_product_bg.place(x=0, y=0)
#
# product_listbox = tkinter.Listbox(frame_product, font=("Arial", 18), height=8)
# product_listbox.place(x=20, y=20)
#
# fill_product_listbox()
#
# product_id_lbl = tkinter.Label(frame_product, text="ID:", font=("Arial", 18))
# product_id_lbl.place(x=20, y=260)
#
# product_id_entry = tkinter.Entry(frame_product, font=("Arial", 18), width=10)
# product_id_entry.place(x=20, y=300)
#
# product_name_lbl = tkinter.Label(frame_product, text="Name:", font=("Arial", 18))
# product_name_lbl.place(x=220, y=260)
#
# product_name_entry = tkinter.Entry(frame_product, font=("Arial", 18))
# product_name_entry.place(x=220, y=300)
#
# product_price_lbl = tkinter.Label(frame_product, text="Price:", font=("Arial", 18))
# product_price_lbl.place(x=540, y=260)
#
# product_price_entry = tkinter.Entry(frame_product, font=("Arial", 18), width=8)
# product_price_entry.place(x=540, y=300)
#
# product_info_lbl = tkinter.Label(frame_product, text="Product info:", font=("Arial", 18))
# product_info_lbl.place(x=460, y=20)
#
# product_info = tkinter.Label(frame_product, text="", font=("Arial", 18))
# product_info.place(x=460, y=60)
#
#
# def add_product():
#     # Считываем данные из полей фронтенда
#     new_id = product_id_entry.get()
#     new_name = product_name_entry.get()
#     new_price = int(product_price_entry.get())
#
#     # Формируем из данных объект
#     new_product = Product(new_id, new_name, new_price)
#
#     # Добавляем объект в бэкенд
#     if db.add_product(new_product):
#         # Формируем строковое представление объекта
#         new_product_listbox = str(new_product)
#
#         # Добавляем строковое представление объекта во фронтенд
#         product_listbox.insert(tkinter.END, new_product_listbox)
#
#         product_combobox["values"] = db.get_products()
#
#     # Для проверки соответствия наполнения бэкенда и фронтенда
#     print()
#     for product in db.get_products():
#         print(f"{product.get_id()} {product.get_name()} {product.get_price()}")
#
#
# product_add_btn = tkinter.Button(frame_product, text="New", font=("Arial", 14), command=add_product)
# product_add_btn.place(x=300, y=20)
#
#
# def delete_product():
#     # Считываем индексы выделенных элементов из фронтенда
#     product_listbox_ind = product_listbox.curselection()
#     if len(product_listbox_ind) > 0:
#         # Считываем элемент по индексу
#         selected_product = product_listbox.get(product_listbox_ind[0])
#
#         # Отдельно выделяем идентификатор
#         product_id = selected_product.split()[0]
#
#         # Пытаемся удалить из бэкенда
#         if db.remove_product_by_id(product_id):
#             # Удаляем из фронтенда
#             product_listbox.delete(product_listbox_ind[0])
#
#             product_combobox["values"] = db.get_products()
#
#     # Для проверки соответствия наполнения бэкенда и фронтенда
#     print()
#     for product in db.get_products():
#         print(f"{product.get_id()} {product.get_name()} {product.get_price()}")
#
#
# product_delete_btn = tkinter.Button(frame_product, text="Delete", font=("Arial", 14), command=delete_product)
# product_delete_btn.place(x=300, y=70)
#
#
# def change_product():
#     # Считываем индексы выделенных элементов из фронтенда
#     product_listbox_ind = product_listbox.curselection()
#     if len(product_listbox_ind) > 0:
#         # Считываем элемент по индексу
#         selected_product = product_listbox.get(product_listbox_ind[0])
#
#         # Отдельно выделяем идентификатор
#         selected_id = selected_product.split()[0]
#
#         # Считываем данные из полей фронтенда
#         new_id = product_id_entry.get()
#         new_name = product_name_entry.get()
#         new_price = int(product_price_entry.get())
#
#         # Формируем из данных объект
#         new_product = Product(new_id, new_name, new_price)
#
#         # Пытаемся изменить объект в бэкенде
#         if db.change_product_by_id(selected_id, new_product):
#             # Формируем строковое представление объекта
#             new_product_listbox = str(new_product)
#
#             # Изменяем данные во фронтенде
#             product_listbox.delete(product_listbox_ind[0])
#             product_listbox.insert(product_listbox_ind[0], new_product_listbox)
#
#             product_combobox["values"] = db.get_products()
#
#     # Для проверки соответствия наполнения бэкенда и фронтенда
#     print()
#     for product in db.get_products():
#         print(f"{product.get_id()} {product.get_name()} {product.get_price()}")
#
#
# product_change_btn = tkinter.Button(frame_product, text="Change", font=("Arial", 14), command=change_product)
# product_change_btn.place(x=300, y=120)
#
#
# def show_product_data():
#     # Считываем индексы выделенных элементов из фронтенда
#     product_listbox_ind = product_listbox.curselection()
#     if len(product_listbox_ind) > 0:
#         # Считываем элемент по индексу
#         selected_product = product_listbox.get(product_listbox_ind[0])
#
#         # Отдельно выделяем идентификатор
#         selected_id = selected_product.split()[0]
#
#         # Запрашиваем из бэкенда объект по идентификатору
#         product = db.get_product_by_id(selected_id)
#         if product:
#             product_data = f"ID: {product.get_id()}\nName: {product.get_name()}\nPrice: {product.get_price()}₼"
#             product_info.config(text=product_data, justify="left")
#
#
# product_info_btn = tkinter.Button(frame_product, text="Info", font=("Arial", 14), command=show_product_data)
# product_info_btn.place(x=300, y=170)
# # END FRAME PRODUCT
#
# # BEGIN FRAME OPERATIONS
# frame_operations = tkinter.Frame(root, bg="#34b019")
# frame_operations.pack_forget()
#
# person_lbl = tkinter.Label(frame_operations, text="Person:", font=("Arial", 16), bg="black", fg="#34b019")
# person_lbl.place(x=20, y=20)
# person_combobox = ttk.Combobox(frame_operations, values=db.get_persons(), font=("Arial", 18), state="readonly")
# person_combobox.place(x=20, y=60)
#
# product_lbl = tkinter.Label(frame_operations, text="Product:", font=("Arial", 16), bg="black", fg="#34b019")
# product_lbl.place(x=20, y=120)
# product_combobox = ttk.Combobox(frame_operations, values=db.get_products(), font=("Arial", 18), state="readonly")
# product_combobox.place(x=20, y=160)
#
# operations_info = tkinter.Label(frame_operations, text="", font=("Arial", 16), bg="#34b019")
# operations_info.place(x=20, y=200)
#
#
# def make_operation():
#     person_str = person_combobox.get()
#     product_str = product_combobox.get()
#
#     # person_id = person_str.split()[0]
#     # product_id = product_str.split()[0]
#     # selected_person = db.get_person_by_id(person_id)
#     # selected_product = db.get_product_by_id(product_id)
#
#     operations_info.config(text=f"Person: {person_str}\nProduct: {product_str}", justify="left")
#
#
# make_operation_btn_img = tkinter.PhotoImage(file="img/edited_lesson57_button_make_operation.gif")
# make_operation_btn = tkinter.Button(frame_operations,font=("Arial", 16), command=make_operation,
#                                     image=make_operation_btn_img, bd=2, bg="#000000")
# make_operation_btn.place(x=400, y=20)
# # END FRAME OPERATIONS
#
# root.mainloop()

# ====================================================================================================
# Задание 4. Создать класс Работник. Поля: идентификатор, имя, зарплата, список оценок.
#            Описать свойства, конструктор и строковое представление в виде "Идентификатор Имя Рейтинг".
#            Методы:
#            Добавление оценок - можно добавить только оценку от 0 до 5 включительно.
#            Получение рейтинга - это средняя арифметическая оценка.
#
#            Создать класс "База данных". Поля: список работников.
#            Описать свойство и конструктор.
#            Методы:
#            CRUD работников - добавление, поиск (один возвращает индекс, второй возвращает объект),
#            изменение, удаление работника.
#            Метод получения лучшего сотрудника по рейтингу.
#            Сохранение и загрузка базы данных.
#
#            Создать графическое приложение, в котором можно добавить, изменить, удалить работника,
#            а также увидеть подробную информацию о работнике. Также можно добавить оценку и узнать,
#            какой работник лучший по рейтингу.
#            Реализовать сохранение и загрузку в файл.
# ====================================================================================================

# ==============================================LESSON61==============================================
# Установщик пакетов pip. Использование API.
# https://openweathermap.org/
# Регистрация и получение API-key
# py -m pip --version
# echo %PATH% и найти Python\Scripts
# setx PATH "%PATH%; C:\Python\Scripts"
# pip install requests
# pip uninstall requests
# https://openweathermap.org/current
# https://openweathermap.org/forecast5

# import datetime
# import requests
#
# # current = datetime.datetime.now()
# # print(current)
# # print(current.year, current.month, current.day, current.hour, current.minute)
#
# # print(current)
# # print(current + datetime.timedelta(days=5))
#
#
# API_KEY = "4c62683f9d401f0ad02070f7def1a871"
# BASE_WEATHER_URL = f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}"
# CITY = "Baku"
#
# url = f"{BASE_WEATHER_URL}&q={CITY}&units=metric"
# response = requests.get(url).json()
# print(response)
#
#
# current_datetime = datetime.datetime.now()
# temperature_celsius = response["main"]["temp"]
# temperature_celsius_feels = response["main"]["feels_like"]
# humidity = response["main"]["humidity"]
# wind_speed = response["wind"]["speed"]
# weather_description = response["weather"][0]["description"]
# sunrise_time = datetime.datetime.fromtimestamp(response["sys"]["sunrise"]).time()
# sunset_time = datetime.datetime.fromtimestamp(response["sys"]["sunset"]).time()
#
# print(f"Datetime is: {current_datetime}")
# print(f"Temperature in {CITY} is {temperature_celsius:.2f}°C")
# print(f"Temperature in {CITY} feels like {temperature_celsius_feels:.2f}°C")
# print(f"Humidity in {CITY} is {humidity}%")
# print(f"Wind speed in {CITY} is {wind_speed}m/s")
# print(f"General Weather in {CITY} is {weather_description}")
# print(f"Sun rises in {CITY} at {sunrise_time} local time")
# print(f"Sun sets in {CITY} at {sunset_time} local time")
# print()

# ====================================================================================================
# import datetime
# import requests
#
# API_KEY = "4c62683f9d401f0ad02070f7def1a871"
# BASE_WEATHER_URL = f"https://api.openweathermap.org/data/2.5/forecast?appid={API_KEY}&lang=ru"
# CITY = "Baku"
#
# url = f"{BASE_WEATHER_URL}&q={CITY}&units=metric"
# response = requests.get(url).json()
# # print(url)
# # print(response)
#
#
# print(CITY)
# for elem in response["list"]:
#     print(datetime.datetime.fromtimestamp(elem["dt"]))
#     print(elem["main"]["temp"], "градусов по цельсию")
#     print(elem["wind"]["speed"], "м/с")
#     print(elem["weather"][0]["description"])
#     print()

# ==============================================LESSON62==============================================
# https://www.exchangerate-api.com/docs/overview
# https://jservice.io/

# import datetime
# import requests
#
# API_KEY = "f42a7bbed18114419a78b016"
# BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest"
# CURRENT_CURRENCY = "USD"
# TARGET_CURRENCY = "RUB"
#
# url = f"{BASE_URL}/{CURRENT_CURRENCY}"
# response = requests.get(url).json()
# print(response)
#
# rate = response["conversion_rates"][TARGET_CURRENCY]
# last_upd = datetime.datetime.fromtimestamp(response["time_last_update_unix"])
#
# print(f"Last update: {last_upd}")
# print(f"From {CURRENT_CURRENCY} to {TARGET_CURRENCY} rate: {rate}")

# ====================================================================================================

# import requests
# BASE_URL = "https://jservice.io/api/random"
#
# count = 0
# while True:
#     if count == 5:
#         user_choice = input("You want to quit? (y/n)").lower()
#         count = 0
#         if user_choice == "y":
#             break
#
#     response = requests.get(BASE_URL).json()
#     question = response[0]["question"]
#     answer = response[0]["answer"].lower()
#
#     print(question)
#     print(answer)
#     user_answer = input("Your answer: ").lower()
#     if user_answer == answer:
#         print("Correct!")
#     else:
#         print("Incorrect!")
#
#     count += 1
