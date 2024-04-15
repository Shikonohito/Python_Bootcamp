# ==============================================LESSON51==============================================
# Позиционирование. Label, Entry, Button.

# import tkinter
#
# root = tkinter.Tk()
# root.geometry("600x250+800+400")
# root.resizable(False, False)
#
# root.title("Приложение на Tkinter")


# PACK
# side - top, bottom, left, right - от какого края заполнять.
# Например от top будет заполняться сверху вниз, но может расширяться влево и вправо.
# expand - True, False - резервирует виджету оставшееся свободное место.
# fill - x, y, Both, None - заполняет виджетом всё его резервированное место по указанным направлениям.
# label_1 = tkinter.Label(root, text="label_1", background="red", font=("Arial", 20))
# label_1.pack(side="left", fill="both")
#
# label_2 = tkinter.Label(root, text="label_2", background="blue", font=("Arial", 20))
# label_2.pack(side="top", fill="both", expand=True)
#
# label_3 = tkinter.Label(root, text="label_3", background="green", font=("Arial", 20))
# label_3.pack(side="top", fill="both")


# FRAME & GRID
# user_data_frame = tkinter.LabelFrame(root, text="User Information")
# user_data_frame.pack(expand=True, fill="both")
# user_data_frame.grid_configure(padx=10, pady=5)
#
# for widget in user_data_frame.winfo_children():
#     widget.grid_configure(padx=10, pady=5)
#
# label_1 = tkinter.Label(user_data_frame, text="label_1", background="red", font=("Arial", 20))
# label_1.grid(row=0, column=0, sticky="w")
#
# label_2 = tkinter.Label(user_data_frame, text="label_2", background="blue", font=("Arial", 20))
# label_2.grid(row=0, column=1, sticky="n")
#
# label_3 = tkinter.Label(user_data_frame, text="label_3", background="green", font=("Arial", 20))
# label_3.grid(row=0, column=2, sticky="e")
#
# entry_1 = tkinter.Entry(user_data_frame, font=("Arial", 12))
# entry_1.grid(row=1, column=0)
#
# entry_2 = tkinter.Entry(user_data_frame, font=("Arial", 12))
# entry_2.grid(row=1, column=1)
#
# entry_3 = tkinter.Entry(user_data_frame, font=("Arial", 12))
# entry_3.grid(row=1, column=2)


# PLACE
# label_1 = tkinter.Label(root, text="label_1", background="red", font=("Arial", 20))
# label_1.place(y=0, x=0, height=100, width=100)
#
# label_3 = tkinter.Label(root, text="label_3", background="green", font=("Arial", 20))
# label_3.place(y=0, x=200, height=100, width=100)
#
# label_2 = tkinter.Label(root, text="label_2", background="blue", font=("Arial", 20))
# label_2.place(y=50, x=100)
#
# root.mainloop()


# import tkinter
#
# root = tkinter.Tk()
# root.geometry("600x250")
# root.resizable(False, False)
# root.title("Lesson51")
#
# user_data_frame = tkinter.Frame(root)
# user_data_frame.pack(expand=True, fill="both")
#
# user_name_label = tkinter.Label(user_data_frame, text="Name:", font=("Arial", 18))
# user_age_label = tkinter.Label(user_data_frame, text="Age:", font=("Arial", 18))
# user_name_label.place(y=20, x=20)
# user_age_label.place(y=20, x=300)
#
# user_name_entry = tkinter.Entry(user_data_frame, font=("Arial", 18))
# user_age_entry = tkinter.Entry(user_data_frame, font=("Arial", 18))
# user_name_entry.place(y=60, x=20)
# user_age_entry.place(y=60, x=300)
#
#
# def console_print():
#     name = user_name_entry.get()
#     age = int(user_age_entry.get())
#     print(name, age)
#
#     result = f"{name}\n{age}"
#     user_result_label.config(text=result, justify="left")
#
#
# user_confirm_btn = tkinter.Button(text="Confirm", command=console_print, font=("Arial", 18))
# user_confirm_btn.place(y=180, x=400)
#
# user_result_label = tkinter.Label(text="TEXT", font=("Arial", 18))
# user_result_label.place(y=180, x=20)
#
# root.mainloop()

# ====================================================================================================
# Задание 1.
# import tkinter
#
# root = tkinter.Tk()
# root.title("Num sum")
# root.geometry("610x260")
# root.resizable(False, False)
#
# frame = tkinter.Frame(root)
# frame.pack(expand=True, fill="both")
#
# num_1_lbl = tkinter.Label(frame, text="First number:", font=("Arial", 18))
# num_2_lbl = tkinter.Label(frame, text="Second number:", font=("Arial", 18))
# num_1_lbl.place(x=20, y=20)
# num_2_lbl.place(x=320, y=20)
#
#
# # def entry_is_float(data_input: str):
# #     count_dot = data_input.count(".")
# #
# #     if data_input == "":
# #         return True
# #     elif count_dot <= 1:
# #         symb_nums = ".0123456789"
# #         is_num = False
# #         for symb in data_input:
# #             is_num = False
# #             for num in symb_nums:
# #                 if symb == num:
# #                     is_num = True
# #                     break
# #             if not is_num:
# #                 break
# #         return is_num
# #     else:
# #         return False
# #
# #
# # def entry_is_int(data_input: str):
# #     count_dot = data_input.count(".")
# #     print(count_dot)
# #     if data_input:
# #         print(data_input)
# #         return True
# #
# #     elif data_input == "":
# #         print(data_input)
# #         return True
# #
# #     else:
# #         print(data_input)
# #         return False
# #
# #
# # reg = frame.register(entry_is_float)
# # num_1_entry = tkinter.Entry(frame, font=("Arial", 18), validate="key", validatecommand=(reg, "%P"))
# # num_2_entry = tkinter.Entry(frame, font=("Arial", 18), validate="key", validatecommand=(reg, "%P"))
# # num_1_entry.place(x=20, y=60)
# # num_2_entry.place(x=320, y=60)
#
#
# num_1_entry = tkinter.Entry(frame, font=("Arial", 18))
# num_2_entry = tkinter.Entry(frame, font=("Arial", 18))
# num_1_entry.place(x=20, y=60)
# num_2_entry.place(x=320, y=60)
#
# sum_lbl = tkinter.Label(frame, text="0", font=("Arial", 18))
# sum_lbl.place(x=20, y=200)
#
#
# def find_sum():
#     num_1 = num_1_entry.get()
#     num_2 = num_2_entry.get()
#
#     if num_1 != "" and num_2 != "":
#         num_1 = float(num_1)
#         num_2 = float(num_2)
#         result = str(num_1 + num_2)
#         sum_lbl.config(text=result)
#
#
# sum_btn = tkinter.Button(frame, text="+", font=("Arial", 18), command=find_sum)
# sum_btn.place(x=20, y=120)
#
#
# def find_dif():
#     num_1 = num_1_entry.get()
#     num_2 = num_2_entry.get()
#
#     if num_1 != "" and num_2 != "":
#         num_1 = float(num_1)
#         num_2 = float(num_2)
#         result = str(num_1 - num_2)
#         sum_lbl.config(text=result)
#
#
# sum_btn = tkinter.Button(frame, text="-", font=("Arial", 18), command=find_dif)
# sum_btn.place(x=60, y=120)
#
#
# def find_prod():
#     num_1 = num_1_entry.get()
#     num_2 = num_2_entry.get()
#
#     if num_1 != "" and num_2 != "":
#         num_1 = float(num_1)
#         num_2 = float(num_2)
#         result = str(num_1 * num_2)
#         sum_lbl.config(text=result)
#
#
# sum_btn = tkinter.Button(frame, text="*", font=("Arial", 18), command=find_prod)
# sum_btn.place(x=100, y=120)
#
#
# def find_div():
#     num_1 = num_1_entry.get()
#     num_2 = num_2_entry.get()
#
#     if num_1 != "" and num_2 != "":
#         num_1 = float(num_1)
#         num_2 = float(num_2)
#         if num_2 != 0:
#             result = str(num_1 / num_2)
#         else:
#             result = "Divided by Zero"
#         sum_lbl.config(text=result)
#
#
# sum_btn = tkinter.Button(frame, text="/", font=("Arial", 18), command=find_div)
# sum_btn.place(x=140, y=120)
#
#
# # def hide_frame():
# #     frame.pack_forget()
# #
# #
# # hide_frame_btn = tkinter.Button(root, text="Hide frame", font=("Arial", 18), command=hide_frame)
# # hide_frame_btn.place(x=390, y=200)
# #
# #
# # def show_frame():
# #     frame.pack(expand=True, fill="both")
# #
# #
# # show_frame_btn = tkinter.Button(root, text="Show frame", font=("Arial", 18), command=show_frame)
# # show_frame_btn.place(x=200, y=200)
#
# root.mainloop()

# ====================================================================================================

# ==============================================LESSON52==============================================
# Listbox. Добавление, Удаление, Изменение, Поиск.

# customer_1 = {"id": "ABC1234", "name": "Tom"}
# customer_2 = {"id": "DEF5869", "name": "Bob"}
# customer_3 = {"id": "QWE1556", "name": "Kate"}
# customer_list = [customer_1, customer_2, customer_3]
#
#
# def backend_find_customer_by_id(customer_id):
#     found_index = -1
#     for i in range(len(customer_list)):
#         if customer_id == customer_list[i]["id"]:
#             found_index = i
#             break
#     return found_index
#
#
# def backend_add_customer(new_customer):
#     is_success = False
#     index = backend_find_customer_by_id(new_customer["id"])
#     if index == -1:
#         customer_list.append(new_customer)
#         is_success = True
#     return is_success
#
#
# def backend_change_customer_by_id(customer_id, new_customer):
#     is_success = False
#     index = backend_find_customer_by_id(customer_id)
#     if index != -1:
#         new_person_id = new_customer["id"]
#         new_index = backend_find_customer_by_id(new_person_id)
#         if customer_id == new_person_id or new_index == -1:
#             customer_list[index] = new_customer
#             is_success = True
#     return is_success
#
#
# def backend_remove_customer_by_id(customer_id):
#     is_success = False
#     index = backend_find_customer_by_id(customer_id)
#     if index != -1:
#         del customer_list[index]
#         is_success = True
#     return is_success
#
#
# def backend_get_customer_by_id(customer_id):
#     index = backend_find_customer_by_id(customer_id)
#     if index != -1:
#         customer = customer_list[index]
#     else:
#         customer = None
#     return customer
#
#
# import tkinter
#
# root = tkinter.Tk()
# root.title("Listbox")
# root.geometry("720x480")
# root.resizable(False, False)
#
# customer_frame = tkinter.Frame(root)
# customer_frame.pack(expand=True, fill="both")
#
# customer_listbox = tkinter.Listbox(customer_frame, font=("Arial", 18), height=13)
# customer_listbox.place(x=20, y=20)
#
#
# def fill_customer_listbox():
#     customer_listbox.delete(0, tkinter.END)
#     for item in customer_list:
#         listbox_item = f'{item["id"]} {item["name"]}'
#         customer_listbox.insert(tkinter.END, listbox_item)
#
#
# fill_customer_listbox()
#
# customer_id_lbl = tkinter.Label(customer_frame, text="ID:", font=("Arial", 18))
# customer_id_lbl.place(x=340, y=20)
#
# customer_id_entry = tkinter.Entry(customer_frame, font=("Arial", 18))
# customer_id_entry.place(x=340, y=60)
#
# customer_name_lbl = tkinter.Label(customer_frame, text="Name:", font=("Arial", 18))
# customer_name_lbl.place(x=340, y=100)
#
# customer_name_entry = tkinter.Entry(customer_frame, font=("Arial", 18))
# customer_name_entry.place(x=340, y=140)
#
# customer_info_lbl = tkinter.Label(customer_frame, text="Customer info:", font=("Arial", 18))
# customer_info_lbl.place(x=340, y=300)
#
# customer_info = tkinter.Label(customer_frame, text="", font=("Arial", 18))
# customer_info.place(x=340, y=340)
#
#
# def add_customer():
#     # Считываем данные из полей фронтенда
#     new_id = customer_id_entry.get()
#     new_name = customer_name_entry.get()
#
#     # Формируем из данных объект
#     new_customer = {"id": new_id, "name": new_name}
#
#     # Пытаемся добавить объект в бэкенд
#     if backend_add_customer(new_customer):
#         # Формируем строковое представление объекта
#         new_customer_listbox = f'{new_customer["id"]} {new_customer["name"]}'
#
#         # Добавляем строковое представление объекта во фронтенд
#         customer_listbox.insert(tkinter.END, new_customer_listbox)
#
#     # Для проверки соответствия наполнения бэкенда и фронтенда
#     print()
#     for item in customer_list:
#         print(item)
#
#
# customer_add_btn = tkinter.Button(customer_frame, text="New", font=("Arial", 14), command=add_customer)
# customer_add_btn.place(x=20, y=400)
#
#
# def delete_customer():
#     # Считываем индексы выделенных элементов из фронтенда
#     customer_listbox_ind = customer_listbox.curselection()
#     print(customer_listbox_ind)
#     if len(customer_listbox_ind) > 0:
#         # Считываем элемент по индексу
#         selected_customer = customer_listbox.get(customer_listbox_ind[0])
#         print(selected_customer)
#
#         # Отдельно выделяем идентификатор
#         customer_id = selected_customer.split()[0]
#         print(customer_id)
#
#         # Пытаемся удалить из бэкенда
#         if backend_remove_customer_by_id(customer_id):
#             # Удаляем из фронтенда
#             customer_listbox.delete(customer_listbox_ind[0])
#
#     # Для проверки соответствия наполнения бэкенда и фронтенда
#     print()
#     for item in customer_list:
#         print(item)
#
#
# customer_delete_btn = tkinter.Button(customer_frame, text="Delete", font=("Arial", 14), command=delete_customer)
# customer_delete_btn.place(x=75, y=400)
#
#
# def change_customer():
#     # Считываем индексы выделенных элементов из фронтенда
#     customer_listbox_ind = customer_listbox.curselection()
#     if len(customer_listbox_ind) > 0:
#         # Считываем элемент по индексу
#         selected_customer = customer_listbox.get(customer_listbox_ind[0])
#
#         # Отдельно выделяем идентификатор
#         selected_id = selected_customer.split()[0]
#
#         # Считываем данные из полей фронтенда
#         new_id = customer_id_entry.get()
#         new_name = customer_name_entry.get()
#
#         # Формируем из данных объект
#         new_customer = {"id": new_id, "name": new_name}
#
#         # Пытаемся изменить объект в бэкенде
#         if backend_change_customer_by_id(selected_id, new_customer):
#             # Формируем строковое представление объекта
#             new_customer_listbox = f'{new_customer["id"]} {new_customer["name"]}'
#
#             # Изменяем данные во фронтенде
#             customer_listbox.delete(customer_listbox_ind[0])
#             customer_listbox.insert(customer_listbox_ind[0], new_customer_listbox)
#
#     # Для проверки соответствия наполнения бэкенда и фронтенда
#     print()
#     for item in customer_list:
#         print(item)
#
#
# customer_change_btn = tkinter.Button(customer_frame, text="Change", font=("Arial", 14), command=change_customer)
# customer_change_btn.place(x=150, y=400)
#
#
# def show_customer_data():
#     # Считываем индексы выделенных элементов из фронтенда
#     customer_listbox_ind = customer_listbox.curselection()
#     if len(customer_listbox_ind) > 0:
#         # Считываем элемент по индексу
#         selected_customer = customer_listbox.get(customer_listbox_ind[0])
#
#         # Отдельно выделяем идентификатор
#         selected_id = selected_customer.split()[0]
#
#         # Запрашиваем из бэкенда объект по идентификатору
#         customer = backend_get_customer_by_id(selected_id)
#         if customer:
#             customer_data = f'{customer["id"]} {customer["name"]} {customer["age"]}'
#             customer_info.config(text=customer_data)
#
#
# customer_info_btn = tkinter.Button(customer_frame, text="Info", font=("Arial", 14), command=show_customer_data)
# customer_info_btn.place(x=235, y=400)
#
# root.mainloop()

# ====================================================================================================
# Задание 2 - добавить ещё два поля: Фамилия, возраст. Дополнить функции добавления, изменения.
# ====================================================================================================


# ============================================LESSON53-54=============================================
# ООП анкета. Добавление Person в Listbox и DB. Listbox - выбор, удаление, инфо в label.


# ====================================================================================================
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
# class DB:
#     __person_list = list()
#
#     def __init__(self):
#         self.__person_list = list()
#
#     def set_persons(self, new_list: list[Person]):
#         self.__person_list = new_list
#
#     def get_persons(self) -> list[Person]:
#         return self.__person_list
#
#     def find_by_id(self, person_id):
#         found_index = -1
#         for i in range(len(self.__person_list)):
#             if person_id == self.__person_list[i].get_id():
#                 found_index = i
#                 break
#         return found_index
#
#     def add_person(self, new_person: Person):
#         is_success = False
#         index = self.find_by_id(new_person.get_id())
#         if index == -1:
#             self.__person_list.append(new_person)
#             is_success = True
#         return is_success
#
#     def remove_person_by_id(self, person_id):
#         is_success = False
#         index = self.find_by_id(person_id)
#         if index != -1:
#             del self.__person_list[index]
#             is_success = True
#         return is_success
#
#     def change_person_by_id(self, person_id, new_person: Person):
#         is_success = False
#         index = self.find_by_id(person_id)
#         if index != -1:
#             new_person_id = new_person.get_id()
#             new_index = self.find_by_id(new_person_id)
#             if person_id == new_person_id or new_index == -1:
#                 self.__person_list[index] = new_person
#                 is_success = True
#         return is_success
#
#     def get_person_by_id(self, person_id):
#         index = self.find_by_id(person_id)
#         if index != -1:
#             person = self.__person_list[index]
#         else:
#             person = None
#         return person
#
#
# # db_person = DB()
# #
# # person_1 = Person("ABC1234", "Tom", 18)
# # db_person.add_person(person_1)
# #
# # person_2 = Person("XYZ5869", "Bob", 24)
# # db_person.add_person(person_2)
# #
# # person_3 = Person("CBE1324", "Tom", 28)
# # db_person.add_person(person_3)
# #
# # person_4 = Person("ABC1234", "Kate", 24)
# # db_person.add_person(person_4)  # Не добавит
# #
# # person_5 = Person("RTE2345", "Jim", 16)
# # db_person.add_person(person_5)
# #
# # for person in db_person.get_persons():
# #     print(person)
# # print("=========")
# #
# # person_6 = Person("ABC1234", "Arthur", 30)
# # db_person.change_person_by_id("ABC1234", person_6)
# #
# # for person in db_person.get_persons():
# #     print(person)
# # print("=========")
# #
# # db_person.remove_person_by_id("ABC1234")
# #
# # for person in db_person.get_persons():
# #     print(person)
#
#
# import tkinter
#
# person_1 = Person("ABC1234", "Tom", 18)
# person_2 = Person("XYZ5869", "Bob", 24)
# person_3 = Person("CBE1324", "Tom", 28)
# person_4 = Person("XYZ1234", "Kate", 24)
# person_5 = Person("RTE2345", "Jim", 16)
#
# db_person = DB()
# db_person.add_person(person_1)
# db_person.add_person(person_2)
# db_person.add_person(person_3)
# db_person.add_person(person_4)
# db_person.add_person(person_5)
#
# root = tkinter.Tk()
# root.title("Listbox")
# root.geometry("720x480")
# root.resizable(False, False)
#
# frame_person = tkinter.Frame(root)
# frame_person.pack(expand=True, fill="both")
#
# person_listbox = tkinter.Listbox(frame_person, font=("Arial", 18), height=13)
# person_listbox.place(x=20, y=20)
#
#
# def fill_person_listbox():
#     person_listbox.delete(0, tkinter.END)
#     for person in db_person.get_persons():
#         person_listbox.insert(tkinter.END, str(person))
#
#
# fill_person_listbox()
#
# person_id_lbl = tkinter.Label(frame_person, text="ID:", font=("Arial", 18))
# person_id_lbl.place(x=340, y=20)
#
# person_id_entry = tkinter.Entry(frame_person, font=("Arial", 18))
# person_id_entry.place(x=340, y=60)
#
# person_name_lbl = tkinter.Label(frame_person, text="Name:", font=("Arial", 18))
# person_name_lbl.place(x=340, y=100)
#
# person_name_entry = tkinter.Entry(frame_person, font=("Arial", 18))
# person_name_entry.place(x=340, y=140)
#
# person_age_lbl = tkinter.Label(frame_person, text="Age:", font=("Arial", 18))
# person_age_lbl.place(x=340, y=180)
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
#     new_age = int(person_age_entry.get())
#
#     # Формируем из данных объект
#     new_person = Person(new_id, new_name, new_age)
#
#     # Добавляем объект в бэкенд
#     if db_person.add_person(new_person):
#         # Формируем строковое представление объекта
#         new_person_listbox = str(new_person)
#
#         # Добавляем строковое представление объекта во фронтенд
#         person_listbox.insert(tkinter.END, new_person_listbox)
#
#     # Для проверки соответствия наполнения бэкенда и фронтенда
#     print()
#     for person in db_person.get_persons():
#         print(f"{person.get_id()} {person.get_name()} {person.get_age()}")
#
#
# person_add_btn = tkinter.Button(frame_person, text="New", font=("Arial", 14), command=add_person)
# person_add_btn.place(x=20, y=400)
#
#
# def delete_person():
#     # Считываем индексы выделенных элементов из фронтенда
#     person_listbox_ind = person_listbox.curselection()
#
#     if len(person_listbox_ind) > 0:
#         # Считываем элемент по индексу
#         selected_person = person_listbox.get(person_listbox_ind[0])
#
#         # Отдельно выделяем идентификатор
#         customer_id = selected_person.split()[0]
#
#         # Пытаемся удалить из бэкенда
#         if db_person.remove_person_by_id(customer_id):
#             # Удаляем из фронтенда
#             person_listbox.delete(person_listbox_ind[0])
#
#     # Для проверки соответствия наполнения бэкенда и фронтенда
#     print()
#     for person in db_person.get_persons():
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
#         new_age = int(person_age_entry.get())
#
#         # Формируем из данных объект
#         new_person = Person(new_id, new_name, new_age)
#
#         # Пытаемся изменить объект в бэкенде
#         if db_person.change_person_by_id(selected_id, new_person):
#             # Формируем строковое представление объекта
#             new_person_listbox = str(new_person)
#
#             # Изменяем данные во фронтенде
#             person_listbox.delete(person_listbox_ind[0])
#             person_listbox.insert(person_listbox_ind[0], new_person_listbox)
#
#     # Для проверки соответствия наполнения бэкенда и фронтенда
#     print()
#     for person in db_person.get_persons():
#         print(f"{person.get_id()} {person.get_name()} {person.get_age()}")
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
#         person = db_person.get_person_by_id(selected_id)
#         if person:
#             person_data = f"ID: {person.get_id()}\nName: {person.get_name()}\nAge: {person.get_age()}"
#             person_info.config(text=person_data, justify="left")
#
#
# person_info_btn = tkinter.Button(frame_person, text="Info", font=("Arial", 14), command=show_person_data)
# person_info_btn.place(x=235, y=400)
#
#
# def fill_person_info(event):
#     person_listbox_ind = person_listbox.curselection()
#     if len(person_listbox_ind) > 0:
#         selected_person = person_listbox.get(person_listbox_ind[0])
#         selected_id = selected_person.split()[0]
#         person = db_person.get_person_by_id(selected_id)
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
# root.mainloop()

# ====================================================================================================


# ====================================================================================================
# Задание E3 - создать класс "Банковская карта".
#              Поля - Идентификатор, Имя, Фамилия, Баланс.
#              Описать - конструктор, строковое представление (только id), свойства, пополнение, снятие с баланса.
#              Создать класс "База данных".
#              Поля - список карточек.
#              Описать - конструктор, свойства, поиск, добавление, изменение, удаление банковской карты.
#              Создать визуальное приложение, в котором можно добавлять, изменять, удалять банковскую карту,
#              а также по нажатию кнопки снимать определённое количество денег с её баланса или пополнять её.

# Задание 3 - создать класс "Банковская карта".
#             Поля - Идентификатор, Имя, Фамилия, Баланс.
#             Описать - конструктор, строковое представление, свойства, пополнение, снятие с баланса.
#             Дополнить класс "Person" полем "Список банковских карт".
#             Переделать - конструктор (принимает необязательный список).
#             Описать - свойства, поиск, добавление, изменение, удаление банковской карты, пополнение
#             и снятие с баланса.
#             Дополнить класс "DB" методами:
#             добавление, изменение, удаление банковской карты выбранному клиенту, пополнение и снятие
#             с баланса выбранной карточки.
#             На фронтенде сделать так, чтобы можно было со всем этим работать.
# ====================================================================================================


# ==============================================LESSON55-56==============================================
# Использование виджета Frame и Menu.


# ====================================================================================================
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
#     __bank_cards = list()
#
#     def get_bank_cards(self):
#         return self.__bank_cards
#
#     def set_bank_cards(self, new_bank_cards: list[dict]):
#         self.__bank_cards = new_bank_cards
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
#
# # db_person = DB()
# #
# # person_1 = Person("ABC1234", "Tom", 18)
# # db_person.add_person(person_1)
# #
# # person_2 = Person("XYZ5869", "Bob", 24)
# # db_person.add_person(person_2)
# #
# # person_3 = Person("CBE1324", "Tom", 28)
# # db_person.add_person(person_3)
# #
# # person_4 = Person("ABC1234", "Kate", 24)
# # db_person.add_person(person_4)  # Не добавит
# #
# # person_5 = Person("RTE2345", "Jim", 16)
# # db_person.add_person(person_5)
# #
# # for person in db_person.get_persons():
# #     print(person)
# # print("=========")
# #
# # person_6 = Person("ABC1234", "Arthur", 30)
# # db_person.change_person_by_id("ABC1234", person_6)
# #
# # for person in db_person.get_persons():
# #     print(person)
# # print("=========")
# #
# # db_person.remove_person_by_id("ABC1234")
# #
# # for person in db_person.get_persons():
# #     print(person)
#
#
# import tkinter
# from tkinter import ttk
#
# person_1 = Person("ABC1234", "Tom", 18)
# person_2 = Person("XYZ5869", "Bob", 24)
# person_3 = Person("CBE1324", "Tom", 28)
# person_4 = Person("XYZ1234", "Kate", 24)
# person_5 = Person("RTE2345", "Jim", 16)
#
# product_1 = Product("50004", "Apple", 5)
# product_2 = Product("50005", "Bread", 2)
# product_3 = Product("50006", "Tomato", 6)
#
# db = DB()
# db.add_person(person_1)
# db.add_person(person_2)
# db.add_person(person_3)
# db.add_person(person_4)
# db.add_person(person_5)
#
# db.add_product(product_1)
# db.add_product(product_2)
# db.add_product(product_3)
#
# root = tkinter.Tk()
# root.title("Listbox")
# root.geometry("720x480")
# root.resizable(False, False)
#
#
# def show_persons():
#     # Скрываем всё, что не нужно
#     frame_product.pack_forget()
#     frame_operations.pack_forget()
#
#     # Показываем всё, что требуется показать
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
# def close_program():
#     root.quit()
#
#
# root_menu = tkinter.Menu(root)
# root.config(menu=root_menu)
# show_menu = tkinter.Menu(root_menu, tearoff=False)
# show_menu.add_command(label="Persons", command=show_persons)
# show_menu.add_command(label="Products", command=show_products)
# show_menu.add_command(label="Operations", command=show_operations)
# show_menu.add_separator()
# show_menu.add_command(label="Exit", command=close_program)
# root_menu.add_cascade(label="Show", menu=show_menu)
#
#
# # BEGIN FRAME PERSON
# frame_person = tkinter.Frame(root)
# frame_person.pack(expand=True, fill="both")
#
# person_listbox = tkinter.Listbox(frame_person, font=("Arial", 18), height=13)
# person_listbox.place(x=20, y=20)
#
#
# def fill_person_listbox():
#     person_listbox.delete(0, tkinter.END)
#     for person in db.get_persons():
#         person_listbox.insert(tkinter.END, str(person))
#
#
# fill_person_listbox()
#
# person_id_lbl = tkinter.Label(frame_person, text="ID:", font=("Arial", 18))
# person_id_lbl.place(x=340, y=20)
#
# person_id_entry = tkinter.Entry(frame_person, font=("Arial", 18))
# person_id_entry.place(x=340, y=60)
#
# person_name_lbl = tkinter.Label(frame_person, text="Name:", font=("Arial", 18))
# person_name_lbl.place(x=340, y=100)
#
# person_name_entry = tkinter.Entry(frame_person, font=("Arial", 18))
# person_name_entry.place(x=340, y=140)
#
# person_age_lbl = tkinter.Label(frame_person, text="Age:", font=("Arial", 18))
# person_age_lbl.place(x=340, y=180)
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
#     new_age = int(person_age_entry.get())
#
#     # Формируем из данных объект
#     new_person = Person(new_id, new_name, new_age)
#
#     # Добавляем объект в бэкенд
#     if db.add_person(new_person):
#         # Формируем строковое представление объекта
#         new_person_listbox = str(new_person)
#
#         # Добавляем строковое представление объекта во фронтенд
#         person_listbox.insert(tkinter.END, new_person_listbox)
#
#         person_combobox["values"] = db.get_persons()
#
#     # Для проверки соответствия наполнения бэкенда и фронтенда
#     print()
#     for person in db.get_persons():
#         print(f"{person.get_id()} {person.get_name()} {person.get_age()}")
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
#         new_age = int(person_age_entry.get())
#
#         # Формируем из данных объект
#         new_person = Person(new_id, new_name, new_age)
#
#         # Пытаемся изменить объект в бэкенде
#         if db.change_person_by_id(selected_id, new_person):
#             # Формируем строковое представление объекта
#             new_person_listbox = str(new_person)
#
#             # Изменяем данные во фронтенде
#             person_listbox.delete(person_listbox_ind[0])
#             person_listbox.insert(person_listbox_ind[0], new_person_listbox)
#
#             person_combobox["values"] = db.get_persons()
#
#     # Для проверки соответствия наполнения бэкенда и фронтенда
#     print()
#     for person in db.get_persons():
#         print(f"{person.get_id()} {person.get_name()} {person.get_age()}")
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
# # def fill_person_info(event):
# #     person_listbox_ind = person_listbox.curselection()
# #     if len(person_listbox_ind) > 0:
# #         selected_person = person_listbox.get(person_listbox_ind[0])
# #         selected_id = selected_person.split()[0]
# #         person = db_person.get_person_by_id(selected_id)
# #         if person:
# #             person_id_entry.delete(0, tkinter.END)
# #             person_id_entry.insert(0, person.get_id())
# #             person_name_entry.delete(0, tkinter.END)
# #             person_name_entry.insert(0, person.get_name())
# #             person_age_entry.delete(0, tkinter.END)
# #             person_age_entry.insert(0, person.get_age())
# #
# #
# # person_listbox.bind("<<ListboxSelect>>", fill_person_info)
#
# # END FRAME PERSON
#
# # BEGIN FRAME PRODUCT
# frame_product = tkinter.Frame(root)
# frame_product.pack_forget()
#
# product_listbox = tkinter.Listbox(frame_product, font=("Arial", 18), height=8)
# product_listbox.place(x=20, y=20)
#
#
# def fill_product_listbox():
#     product_listbox.delete(0, tkinter.END)
#     for product in db.get_products():
#         product_listbox.insert(tkinter.END, str(product))
#
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
# frame_operations = tkinter.Frame(root)
# frame_operations.pack_forget()
#
# person_lbl = tkinter.Label(frame_operations, text="Person:", font=("Arial", 16))
# person_lbl.place(x=20, y=20)
# person_combobox = ttk.Combobox(frame_operations, values=db.get_persons(), font=("Arial", 18), state="readonly")
# person_combobox.place(x=20, y=60)
#
# # person_list = db.get_persons()
# # person_list[0].set_bank_cards([{"id": "1234", "balance": 100}, {"id": "5869", "balance": 200}])
# # person_list[1].set_bank_cards([{"id": "4221", "balance": 99999}, {"id": "0001", "balance": 1}])
#
# person_cards_combobox = ttk.Combobox(frame_operations, values=[], font=("Arial", 18), state="readonly")
# person_cards_combobox.place(x=20, y=300)
#
#
# # def fill_person_cards_combobox(event):
# #     person_str = person_combobox.get()
# #     id_person_str = person_str.split()[0]
# #
# #     obj_person = db.get_person_by_id(id_person_str)
# #
# #     some_list = list()
# #     for card in obj_person.get_bank_cards():
# #         if card["balance"] > 200:
# #             some_list.append(card)
# #
# #     person_cards_combobox["values"] = some_list
# #     person_cards_combobox.set("")
# #
# #
# # person_combobox.bind("<<ComboboxSelected>>", fill_person_cards_combobox)
#
# product_lbl = tkinter.Label(frame_operations, text="Product:", font=("Arial", 16))
# product_lbl.place(x=20, y=120)
# product_combobox = ttk.Combobox(frame_operations, values=db.get_products(), font=("Arial", 18), state="readonly")
# product_combobox.place(x=20, y=160)
#
# operations_info = tkinter.Label(frame_operations, text="", font=("Arial", 16))
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
# make_operation_btn = tkinter.Button(frame_operations, text="Make operation", font=("Arial", 16), command=make_operation)
# make_operation_btn.place(x=400, y=20)
# # END FRAME OPERATIONS
#
# root.mainloop()

# ====================================================================================================
# Задание на меню и фреймы.
# Создать визуальное приложение, которое использует Frame, Menu, Label, Entry, Button, Listbox.
# Сделать 2 фрейма. Переходы между фреймами оформить через меню. В самом меню 3-я кнопка - выход.
# На первом фрейме вписываем имя и возраст, нажимаем кнопку, и эти данные появляются где-то на этом фрейме.
# На втором фрейме вписываем идентификатор, название товара, нажимаем кнопку и товар добавляется в листбокс.
# Реализовать с использованием списка.

# ====================================================================================================


# ==============================================LESSON57==============================================
# Добавление картинки. Виджеты.
# https://imageresizer.com/


# ====================================================================================================
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
#
# import tkinter
# from tkinter import ttk
#
# person_1 = Person("ABC1234", "Tom", 18)
# person_2 = Person("XYZ5869", "Bob", 24)
# person_3 = Person("CBE1324", "Tom", 28)
# person_4 = Person("XYZ1234", "Kate", 24)
# person_5 = Person("RTE2345", "Jim", 16)
#
# product_1 = Product("50004", "Apple", 5)
# product_2 = Product("50005", "Bread", 2)
# product_3 = Product("50006", "Tomato", 6)
#
# db = DB()
# db.add_person(person_1)
# db.add_person(person_2)
# db.add_person(person_3)
# db.add_person(person_4)
# db.add_person(person_5)
#
# db.add_product(product_1)
# db.add_product(product_2)
# db.add_product(product_3)
#
# root = tkinter.Tk()
# root.title("Listbox")
# root.geometry("720x480")
# root.resizable(False, False)
#
# root.iconbitmap(default="img/python.ico")
# # OR
# # icon = tkinter.PhotoImage(file="img/python.gif")
# # root.iconphoto(False, icon)  # Первый аргумент отвечает за установку иконки на все окна
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
# def close_program():
#     root.quit()
#
#
# root_menu = tkinter.Menu(root)
# root.config(menu=root_menu)
# show_menu = tkinter.Menu(root_menu, tearoff=False)
# show_menu.add_command(label="Persons", command=show_persons)
# show_menu.add_command(label="Products", command=show_products)
# show_menu.add_command(label="Operations", command=show_operations)
# show_menu.add_separator()
# show_menu.add_command(label="Exit", command=close_program)
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
#
# def fill_person_listbox():
#     person_listbox.delete(0, tkinter.END)
#     for person in db.get_persons():
#         person_listbox.insert(tkinter.END, str(person))
#
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
#
# def fill_product_listbox():
#     product_listbox.delete(0, tkinter.END)
#     for product in db.get_products():
#         product_listbox.insert(tkinter.END, str(product))
#
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

# ==============================================LESSON58==============================================
# Виджеты. Создание графического приложения.

# import tkinter
# from tkinter import ttk
#
# root = tkinter.Tk()
# root.geometry("720x680")
# root.resizable(False, False)
#
# test_frame = tkinter.Frame(root)
# test_frame.pack(expand=True, fill="both")
#
#
# # # SWITCHER
# # def switch_color():
# #     color = test_button.cget("bg")
# #     if color == "blue":
# #         color = "red"
# #     elif color == "red":
# #         color = "blue"
# #     test_button.config(bg=color)
# #
# #
# # test_button = tkinter.Button(test_frame, text="1", bg="blue", command=switch_color, height=2, width=5)
# # test_button.place(x=400, y=20)
#
#
# # # HIDE ENTRY FILLING
# # test_entry_1 = tkinter.Entry(test_frame, show="*", font=("Arial", 16), width=10)
# # test_entry_1.place(x=500, y=160)
#
#
# # # HIDE ENTRY AND TEMPLATE ENTRY
# # test_entry_2 = tkinter.Entry(test_frame, font=("Arial", 16), width=10, fg="grey")
# # test_entry_2.place(x=500, y=200)
# # test_entry_2.insert(0, "Password")
# #
# #
# # def handle_focus_in(event):
# #     if test_entry_2["fg"] == "grey":
# #         test_entry_2.config(show="*")
# #         test_entry_2.delete(0, tkinter.END)
# #         test_entry_2.config(fg='black')
# #
# #
# # def handle_focus_out(event):
# #     if test_entry_2.get() == "":
# #         test_entry_2.config(fg='grey', show="")
# #         test_entry_2.insert(0, "Password")
# #
# #
# # def handle_enter(txt):
# #     print(test_entry_2.get())
# #     root.focus()
# #
# #
# # test_entry_2.bind("<FocusIn>", handle_focus_in)
# # test_entry_2.bind("<FocusOut>", handle_focus_out)
# # test_entry_2.bind("<Return>", handle_enter)
#
#
# # # COMBOBOX
# # day_combobox = ttk.Combobox(test_frame, width=27, font=("Arial", 16), state="readonly")
# # day_combobox["values"] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# # day_combobox.place(x=20, y=20)
# # day_combobox.current(0)
# #
# #
# # def test_combobox():
# #     result = day_combobox.get()
# #     print(result)
# #
# #
# # combobox_test_btn = tkinter.Button(test_frame, text="Get combobox", font=("Arial", 16), command=test_combobox)
# # combobox_test_btn.place(x=500, y=20)
#
#
# # # SPINBOX
# # age_lbl = tkinter.Label(test_frame, text="Age:", font=("Arial", 16))
# # age_lbl.place(x=20, y=100)
# # age_spinbox = tkinter.Spinbox(test_frame, from_=0, to="infinity", font=("Arial", 16), state="readonly")
# # age_spinbox.place(x=20, y=140)
# #
# #
# # def test_spinbox():
# #     result = age_spinbox.get()
# #     print(result)
# #
# #
# # spinbox_test_btn = tkinter.Button(test_frame, text="Get spinbox", font=("Arial", 16), command=test_spinbox)
# # spinbox_test_btn.place(x=500, y=100)
#
# # # TREEVIEW
# # class Customer:
# #     id = -1
# #     name = str()
# #     age = int()
# #
# #     def __init__(self, name, age, id):
# #         self.name = name
# #         self.age = age
# #         self.id = id
# #
# #     def __str__(self):
# #         return "{} {} {}".format(self.id, self.name, self.age)
# #
# #
# # customer_1 = Customer("Tom", 25, 120)
# # customer_2 = Customer("Bob", 27, 109)
# # customer_3 = Customer("Jim", 34, 586)
# # customer_list = list([customer_1, customer_2, customer_3])
# #
# # customer_treeview_columns = ("id", "name", "age")
# # customer_treeview = ttk.Treeview(test_frame, columns=customer_treeview_columns, show="headings")
# # customer_treeview.place(x=20, y=200)
# # customer_treeview.heading(customer_treeview_columns[0], text="ID")
# # customer_treeview.heading(customer_treeview_columns[1], text="Name")
# # customer_treeview.heading(customer_treeview_columns[2], text="Age")
# #
# # for customer in customer_list:
# #     temp_tuple = (customer.id, customer.name, customer.age)
# #     customer_treeview.insert("", tkinter.END, iid=customer.id, values=temp_tuple)
# #
# # customer_treeview.insert(109, tkinter.END, values=(000, f"{customer_2.id}'s child", 0))
# #
# #
# # def item_selected(event):
# #     print("SELECTED:")
# #     for index in customer_treeview.selection():
# #         print(index)
# #         item = customer_treeview.item(index)
# #         print(item)
# #         print(item["values"])
# #         print(type(item["values"][0]))
# #     print()
# #
# #
# # customer_treeview.bind("<<TreeviewSelect>>", item_selected)
# #
# #
# # def delete_customer():
# #     for index in customer_treeview.selection():
# #         item = customer_treeview.item(index)
# #         customer_id = item["values"][0]
# #
# #         for i in range(len(customer_list) - 1, -1, -1):
# #             if customer_id == customer_list[i].id:
# #                 del customer_list[i]
# #         customer_treeview.detach(index)
# #
# #     print("AFTER DELETE")
# #     for cust in customer_list:
# #         print(cust)
# #     print()
# #
# #
# # delete_data_btn = tkinter.Button(test_frame, text="Delete", font=("Arial", 16), command=delete_customer)
# # delete_data_btn.place(x=20, y=440)
#
#
# # # CHECKBUTTON
# # def test_checkbutton():
# #     print(checkbutton_var.get())
# #
# #
# # checkbutton_var = tkinter.StringVar(value="YES")
# # checkbutton = tkinter.Checkbutton(test_frame, text="Accepted Terms and Conditions", variable=checkbutton_var,
# #                                   onvalue="YES", offvalue="NO", command=test_checkbutton, font=("Arial", 12))
# # checkbutton.place(x=20, y=600)
# # # OR
# # # checkbutton_var = tkinter.BooleanVar(value=True)
# # # checkbutton = tkinter.Checkbutton(test_frame, text="Accepted Terms and Conditions", variable=checkbutton_var,
# # #                                   onvalue=True, offvalue=False, command=test_checkbutton, font=("Arial", 12))
# # # checkbutton.place(x=20, y=600)
#
#
# # # RADIOBUTTON
# # def test_radiobutton():
# #     print(radiobutton_var.get())
# #
# #
# # radiobutton_var = tkinter.IntVar()
# # radiobutton_1 = tkinter.Radiobutton(test_frame, text="YES", variable=radiobutton_var, value=1,
# #                                     command=test_radiobutton, font=("Arial", 12))
# # radiobutton_2 = tkinter.Radiobutton(test_frame, text="NO", variable=radiobutton_var, value=2,
# #                                     command=test_radiobutton, font=("Arial", 12))
# # radiobutton_1.place(x=200, y=500)
# # radiobutton_2.place(x=200, y=520)
#
#
# root.mainloop()

# ====================================================================================================
# Задание 4 - создать приложение, которое при запуске встречает нас окном входа, где нужно вписать Логин
#             и Пароль.
#             Если они совпадают с Логином и Паролем из базы данных, то приложение переключается на фрейм
#             с базой данных клиентов.
#             Добавить в приложение картинки в качестве заднего фона.
#             Создать классы "Клиент" и "База данных". Реализовать в приложении поиск, добавление, удаление, изменение
#             клиента. У клиента должно быть как минимум 3 поля.
