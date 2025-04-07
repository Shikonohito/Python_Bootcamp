# ==============================================LESSON59==============================================
# Добавление картинки. Виджеты.
# https://imageresizer.com/

class Person:
    __id = str()
    __name = str()
    __age = int()

    def __init__(self, id: str, name: str, age: int):
        self.__id = id
        self.__name = name
        self.set_age(age)

    def __str__(self):
        result = f"{self.__id} {self.__name}"
        return result

    def set_id(self, new_id: str):
        self.__id = new_id

    def get_id(self):
        return self.__id

    def set_name(self, new_name: str):
        self.__name = new_name

    def get_name(self):
        return self.__name

    def set_age(self, new_age: int):
        if new_age < 0:
            new_age = 0
        self.__age = new_age

    def get_age(self):
        return self.__age


class Product:
    __id = str()
    __name = str()
    __price = int()

    def __init__(self, id: str, name: str, price: int):
        self.__id = id
        self.__name = name
        self.set_price(price)

    def __str__(self):
        result = f"{self.__id} {self.__name}"
        return result

    def set_id(self, new_id: str):
        self.__id = new_id

    def get_id(self):
        return self.__id

    def set_name(self, new_name: str):
        self.__name = new_name

    def get_name(self):
        return self.__name

    def set_price(self, price: int):
        if price < 0:
            price = 0
        self.__price = price

    def get_price(self):
        return self.__price


import tkinter
from tkinter import ttk

person_1 = Person("ABC1234", "Tom", 18)
person_2 = Person("XYZ5869", "Bob", 24)
person_3 = Person("CBE1324", "Tom", 28)
person_4 = Person("XYZ1234", "Kate", 24)
person_5 = Person("RTE2345", "Jim", 16)

product_1 = Product("50004", "Apple", 5)
product_2 = Product("50005", "Bread", 2)
product_3 = Product("50006", "Tomato", 6)

person_list = [person_1, person_2, person_3, person_4, person_5]
product_list = [product_1, product_2, product_3]


root = tkinter.Tk()
root.title("PhotoImage")
root.geometry("720x480")
root.resizable(False, False)

root.iconbitmap(default="img/python.ico")
# OR
# icon = tkinter.PhotoImage(file="img/python.gif")
# root.iconphoto(False, icon)  # Первый аргумент отвечает за установку иконки на все окна

frame_person = tkinter.Frame(root)
frame_person.pack(expand=True, fill="both")

frame_person_bg_img = tkinter.PhotoImage(file="img/frame_person_bg.gif")
frame_person_bg = tkinter.Label(frame_person, image=frame_person_bg_img)
frame_person_bg.place(x=0, y=0)


frame_product = tkinter.Frame(root)
frame_product.pack_forget()

frame_product_bg_img = tkinter.PhotoImage(file="img/frame_product_bg.gif")
frame_product_bg = tkinter.Label(frame_product, image=frame_product_bg_img)
frame_product_bg.place(x=0, y=0)


frame_operations = tkinter.Frame(root, bg="#34b019")
frame_operations.pack_forget()


def show_persons():
    # Скрываем всё, что не нужно
    frame_product.pack_forget()
    frame_operations.pack_forget()

    # Показываем всё, что нужно
    frame_person.pack(fill="both", expand=True)
    root.geometry("720x480")


def show_products():
    # Скрываем всё, что не нужно
    frame_person.pack_forget()
    frame_operations.pack_forget()

    # Показываем всё, что нужно
    frame_product.pack(fill="both", expand=True)
    root.geometry("680x350")


def show_operations():
    # Скрываем всё, что не нужно
    frame_person.pack_forget()
    frame_product.pack_forget()

    # Показываем всё, что нужно
    frame_operations.pack(fill="both", expand=True)
    root.geometry("720x480")

def close_program():
    root.quit()


root_menu = tkinter.Menu(root)
root.config(menu=root_menu)
show_menu = tkinter.Menu(root_menu, tearoff=False)
show_menu.add_command(label="Persons", command=show_persons)
show_menu.add_command(label="Products", command=show_products)
show_menu.add_command(label="Operations", command=show_operations)
show_menu.add_separator()
show_menu.add_command(label="Exit", command=close_program)
root_menu.add_cascade(label="Show", menu=show_menu)

# BEGIN FRAME PERSON
person_listbox = tkinter.Listbox(frame_person, font=("Arial", 18), height=13)
person_listbox.place(x=20, y=20)


def fill_person_listbox():
    person_listbox.delete(0, tkinter.END)
    for person in person_list:
        person_listbox.insert(tkinter.END, str(person))


fill_person_listbox()

person_id_lbl = tkinter.Label(frame_person, text="ID:", font=("Arial", 18))
person_id_lbl.place(x=340, y=20)
person_id_notify = tkinter.Label(frame_person, text="", font=("Arial", 18))
person_id_notify.place(x=400, y=20)

person_id_entry = tkinter.Entry(frame_person, font=("Arial", 18))
person_id_entry.place(x=340, y=60)

person_name_lbl = tkinter.Label(frame_person, text="Name:", font=("Arial", 18))
person_name_lbl.place(x=340, y=100)
person_name_notify = tkinter.Label(frame_person, text="", font=("Arial", 18))
person_name_notify.place(x=440, y=100)

person_name_entry = tkinter.Entry(frame_person, font=("Arial", 18))
person_name_entry.place(x=340, y=140)

person_age_lbl = tkinter.Label(frame_person, text="Age:", font=("Arial", 18))
person_age_lbl.place(x=340, y=180)
person_age_notify = tkinter.Label(frame_person, text="", font=("Arial", 18))
person_age_notify.place(x=415, y=180)

person_age_entry = tkinter.Entry(frame_person, font=("Arial", 18), width=3)
person_age_entry.place(x=340, y=220)

person_info_lbl = tkinter.Label(frame_person, text="User info:", font=("Arial", 18))
person_info_lbl.place(x=340, y=300)

person_info = tkinter.Label(frame_person, text="", font=("Arial", 18))
person_info.place(x=340, y=340)


def add_person():
    # Считываем данные из полей фронтенда
    new_id = person_id_entry.get()
    new_name = person_name_entry.get()
    new_age = person_age_entry.get()

    is_correct_entries = True

    # Проверяем данные из полей
    if new_id == "":
        person_id_notify.config(text="Fill this entry!", fg="red")
        is_correct_entries = False
    elif not new_id.isalnum():
        person_id_notify.config(text="Only letters and numbers!", fg="red")
        is_correct_entries = False
    else:  # Приводим данные из фронтенда в порядок
        person_id_notify.config(text="", fg="black")
        new_id = new_id.upper()

    if new_name == "":
        person_name_notify.config(text="Fill this entry!", fg="red")
        is_correct_entries = False
    elif not new_name.isalpha():
        person_name_notify.config(text="Only letters!", fg="red")
        is_correct_entries = False
    else:  # Приводим данные из фронтенда в порядок
        person_name_notify.config(text="", fg="black")
        new_name = new_name.capitalize()

    if new_age == "":
        person_age_notify.config(text="Fill this entry!", fg="red")
        is_correct_entries = False
    elif not new_age.isdigit():
        person_age_notify.config(text="Entry must be num!", fg="red")
        is_correct_entries = False
    else:  # Приводим данные из фронтенда в порядок
        person_age_notify.config(text="", fg="black")
        new_age = int(new_age)

    if is_correct_entries:
        # Формируем из данных объект
        new_person = Person(new_id, new_name, new_age)

        # Добавляем объект в бэкенд
        person_list.append(new_person)

        # Формируем строковое представление объекта
        new_person_listbox = str(new_person)

        # Добавляем строковое представление объекта в листбокс
        person_listbox.insert(tkinter.END, new_person_listbox)

        # Обновляем комбобокс
        person_combobox["values"] = person_list


person_add_btn = tkinter.Button(frame_person, text="New", font=("Arial", 14), command=add_person,
                                fg="#FFFFFF", bg="#000000")
person_add_btn.place(x=20, y=400)


def delete_person():
    # Считываем индексы выделенных элементов из фронтенда
    person_listbox_ind = person_listbox.curselection()
    if len(person_listbox_ind) > 0:
        # Считываем индекс
        selected_person_index = person_listbox_ind[0]

        # Удаляем из бэкенда
        person_list.pop(selected_person_index)

        # Удаляем из листбокса
        person_listbox.delete(selected_person_index)

        # Обновляем комбобокс
        person_combobox["values"] = person_list
        person_combobox.set("")


person_delete_btn = tkinter.Button(frame_person, text="Delete", font=("Arial", 14), command=delete_person,
                                   fg="#FFFFFF", bg="#000000")
person_delete_btn.place(x=75, y=400)


def show_person_data():
    # Считываем индексы выделенных элементов из фронтенда
    person_listbox_ind = person_listbox.curselection()
    if len(person_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_person_index = person_listbox_ind[0]

        # Запрашиваем из бэкенда объект
        person = person_list[selected_person_index]

        # Формируем строковое представление и выводим в лейбл
        person_data = f"ID: {person.get_id()}\nName: {person.get_name()}\nAge: {person.get_age()}"
        person_info.config(text=person_data, justify="left")


person_info_btn = tkinter.Button(frame_person, text="Info", font=("Arial", 14), command=show_person_data,
                                 fg="#FFFFFF", bg="#000000")
person_info_btn.place(x=235, y=400)
# END FRAME PERSON

# BEGIN FRAME PRODUCT
product_listbox = tkinter.Listbox(frame_product, font=("Arial", 18), height=8)
product_listbox.place(x=20, y=20)


def fill_product_listbox():
    product_listbox.delete(0, tkinter.END)
    for product in product_list:
        product_listbox.insert(tkinter.END, str(product))


fill_product_listbox()

product_id_lbl = tkinter.Label(frame_product, text="ID:", font=("Arial", 18))
product_id_lbl.place(x=20, y=260)

product_id_entry = tkinter.Entry(frame_product, font=("Arial", 18), width=10)
product_id_entry.place(x=20, y=300)

product_name_lbl = tkinter.Label(frame_product, text="Name:", font=("Arial", 18))
product_name_lbl.place(x=220, y=260)

product_name_entry = tkinter.Entry(frame_product, font=("Arial", 18))
product_name_entry.place(x=220, y=300)

product_price_lbl = tkinter.Label(frame_product, text="Price:", font=("Arial", 18))
product_price_lbl.place(x=540, y=260)

product_price_entry = tkinter.Entry(frame_product, font=("Arial", 18), width=8)
product_price_entry.place(x=540, y=300)

product_info_lbl = tkinter.Label(frame_product, text="Product info:", font=("Arial", 18))
product_info_lbl.place(x=460, y=20)

product_info = tkinter.Label(frame_product, text="", font=("Arial", 18))
product_info.place(x=460, y=60)


def add_product():
    # Считываем данные из полей фронтенда
    new_id = product_id_entry.get()
    new_name = product_name_entry.get()
    new_price = int(product_price_entry.get())

    # Формируем из данных объект
    new_product = Product(new_id, new_name, new_price)

    # Добавляем объект в бэкенд
    product_list.append(new_product)

    # Формируем строковое представление объекта
    new_product_listbox = str(new_product)

    # Добавляем строковое представление объекта в листбокс
    product_listbox.insert(tkinter.END, new_product_listbox)

    # Обновляем комбобокс
    product_combobox["values"] = product_list


product_add_btn = tkinter.Button(frame_product, text="New", font=("Arial", 14), command=add_product)
product_add_btn.place(x=300, y=20)


def delete_product():
    # Считываем индексы выделенных элементов из фронтенда
    product_listbox_ind = product_listbox.curselection()
    if len(product_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_product_index = product_listbox_ind

        # Удаляем из бэкенда
        product_list.pop(selected_product_index)

        # Удаляем из фронтенда
        product_listbox.delete(selected_product_index)

        # Обновляем комбобокс
        product_combobox["values"] = product_list
        product_combobox.set("")


product_delete_btn = tkinter.Button(frame_product, text="Delete", font=("Arial", 14), command=delete_product)
product_delete_btn.place(x=300, y=70)


def show_product_data():
    # Считываем индексы выделенных элементов из фронтенда
    product_listbox_ind = product_listbox.curselection()
    if len(product_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_product_index = product_listbox_ind[0]

        # Запрашиваем из бэкенда объект
        product = product_list[selected_product_index]

        # Формируем строковое представление и выводим в лейбл
        product_data = f"ID: {product.get_id()}\nName: {product.get_name()}\nPrice: {product.get_price()}₼"
        product_info.config(text=product_data, justify="left")


product_info_btn = tkinter.Button(frame_product, text="Info", font=("Arial", 14), command=show_product_data)
product_info_btn.place(x=300, y=170)
# END FRAME PRODUCT

# BEGIN FRAME OPERATIONS
person_lbl = tkinter.Label(frame_operations, text="Person:", font=("Arial", 16), bg="black", fg="#34b019")
person_lbl.place(x=20, y=20)
person_combobox = ttk.Combobox(frame_operations, values=person_list, font=("Arial", 18), state="readonly")
person_combobox.place(x=20, y=60)

product_lbl = tkinter.Label(frame_operations, text="Product:", font=("Arial", 16), bg="black", fg="#34b019")
product_lbl.place(x=20, y=120)
product_combobox = ttk.Combobox(frame_operations, values=product_list, font=("Arial", 18), state="readonly")
product_combobox.place(x=20, y=160)

operations_info = tkinter.Label(frame_operations, text="", font=("Arial", 16), bg="#34b019")
operations_info.place(x=20, y=200)


def make_operation():
    person_str = person_combobox.get()
    product_str = product_combobox.get()

    # person_id = person_str.split()[0]
    # product_id = product_str.split()[0]
    # selected_person = data_base.get_person(person_id)
    # selected_product = data_base.get_product(product_id)

    operations_info.config(text=f"Person: {person_str}\nProduct: {product_str}", justify="left")


make_operation_btn_img = tkinter.PhotoImage(file="img/button_make_operation.gif")
make_operation_btn = tkinter.Button(frame_operations,font=("Arial", 16), command=make_operation,
                                    image=make_operation_btn_img, bd=2, bg="#000000")
make_operation_btn.place(x=400, y=20)
# END FRAME OPERATIONS

root.mainloop()
