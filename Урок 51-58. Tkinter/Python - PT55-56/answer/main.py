# Используя код, указанный ниже, реализуйте меню и переходы на
# фреймы клиентов, продуктов и операций клиента над продуктами.

class Product:
    __id = str()
    __name = str()
    __price = float()
    __amount = int()

    def __init__(self, id: str, name: str, price: float, amount: int):
        self.__id = id
        self.__name = name
        self.set_price(price)
        self.set_amount(amount)

    def __str__(self):
        result = f"{self.__id} {self.__name} {self.__amount}"
        return result

    def set_id(self, new_id: str):
        self.__id = new_id

    def get_id(self):
        return self.__id

    def set_name(self, new_name: str):
        self.__name = new_name

    def get_name(self):
        return self.__name

    def set_price(self, price: float):
        if price < 0:
            price = 0
        self.__price = price

    def get_price(self):
        return self.__price

    def set_amount(self, amount: int):
        if amount < 0:
            amount = 0
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def increase_amount(self, amount: int):
        self.__amount += amount

    def decrease_amount(self, amount: int):
        self.__amount -= amount


class Customer:
    __id = str()
    __name = str()
    __age = 0
    __product_list: list[Product] = list()

    def __init__(self, id: str, name: str, age: int, product_list: list[Product] = None):
        self.__id = id
        self.__name = name
        self.set_age(age)

        if product_list:
            self.__product_list = product_list
        else:
            self.__product_list: list[Product] = list()

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

    def set_products(self, product_list: list[Product]):
        self.__product_list = product_list

    def get_products(self):
        return tuple(self.__product_list)

    def __get_product_index(self, product_id: str) -> int:
        found_index = -1
        for i in range(len(self.__product_list)):
            if product_id == self.__product_list[i].get_id():
                found_index = i
                break
        return found_index

    def get_product(self, product_id: str) -> Product | None:
        index = self.__get_product_index(product_id)
        if index != -1:
            product = self.__product_list[index]
        else:
            product = None
        return product

    def add_product(self, new_product: Product) -> int:
        index = self.__get_product_index(new_product.get_id())
        if index == -1:
            self.__product_list.append(new_product)
            result = 1
        else:
            self.__product_list[index].increase_amount(new_product.get_amount())
            result = 2
        return result

    def remove_product(self, product_id: str) -> bool:
        is_success = False
        index = self.__get_product_index(product_id)
        if index != -1:
            del self.__product_list[index]
            is_success = True
        return is_success

    def change_product(self, product_id: str, changed_product: Product) -> bool:
        is_success = False
        product = self.get_product(product_id)
        if product:
            changed_product_id = changed_product.get_id()
            changed_product_index = self.__get_product_index(changed_product_id)
            if product_id == changed_product_id or changed_product_index == -1:
                product.set_id(changed_product.get_id())
                product.set_name(changed_product.get_name())
                product.set_price(changed_product.get_price())
                product.set_amount(changed_product.get_amount())
                is_success = True
        return is_success

    def clear_product_list(self):
        self.__product_list = list()


class DB:
    __customer_list: list[Customer] = list()
    __product_list: list[Product] = list()

    def __init__(self, customer_list: list[Customer] = None, product_list: list[Product] = None):
        if customer_list:
            self.__customer_list = customer_list
        else:
            self.__customer_list: list[Customer] = list()

        if product_list:
            self.__product_list = product_list
        else:
            self.__product_list: list[Product] = list()

    def set_customers(self, new_list: list[Customer]):
        self.__customer_list = new_list

    def get_customers(self):
        return tuple(self.__customer_list)

    def set_products(self, new_list: list[Product]):
        self.__product_list = new_list

    def get_products(self):
        return tuple(self.__product_list)

    def __get_customer_index(self, customer_id: str) -> int:
        found_index = -1
        for i in range(len(self.__customer_list)):
            if customer_id == self.__customer_list[i].get_id():
                found_index = i
                break
        return found_index

    def get_customer(self, customer_id) -> Customer | None:
        index = self.__get_customer_index(customer_id)
        customer = None
        if index != -1:
            customer = self.__customer_list[index]
        return customer

    def add_customer(self, new_customer: Customer) -> bool:
        is_success = False
        index = self.__get_customer_index(new_customer.get_id())
        if index == -1:
            self.__customer_list.append(new_customer)
            is_success = True
        return is_success

    def remove_customer(self, customer_id: str) -> bool:
        is_success = False
        index = self.__get_customer_index(customer_id)
        if index != -1:
            del self.__customer_list[index]
            is_success = True
        return is_success

    def change_customer(self, customer_id: str, changed_customer: Customer) -> bool:
        is_success = False
        customer = self.get_customer(customer_id)
        if customer:
            changed_customer_id = changed_customer.get_id()
            changed_customer_index = self.__get_customer_index(changed_customer_id)
            if customer_id == changed_customer_id or changed_customer_index == -1:
                customer.set_id(changed_customer.get_id())
                customer.set_name(changed_customer.get_name())
                customer.set_age(changed_customer.get_age())
                is_success = True
        return is_success

    def __get_product_index(self, product_id: str) -> int:
        found_index = -1
        for i in range(len(self.__product_list)):
            if product_id == self.__product_list[i].get_id():
                found_index = i
                break
        return found_index

    def get_product(self, product_id: str) -> Product | None:
        index = self.__get_product_index(product_id)
        if index != -1:
            product = self.__product_list[index]
        else:
            product = None
        return product

    def add_product(self, new_product: Product) -> bool:
        is_success = False
        index = self.__get_product_index(new_product.get_id())
        if index == -1:
            self.__product_list.append(new_product)
            is_success = True
        return is_success

    def remove_product(self, product_id: str) -> bool:
        is_success = False
        index = self.__get_product_index(product_id)
        if index != -1:
            del self.__product_list[index]
            is_success = True
        return is_success

    def change_product(self, product_id: str, changed_product: Product) -> bool:
        is_success = False
        product = self.get_product(product_id)
        if product:
            changed_product_id = changed_product.get_id()
            changed_product_index = self.__get_product_index(changed_product_id)
            if product_id == changed_product_id or changed_product_index == -1:
                product.set_id(changed_product.get_id())
                product.set_name(changed_product.get_name())
                product.set_price(changed_product.get_price())
                product.set_amount(changed_product.get_amount())
                is_success = True
        return is_success

    def can_decrease_products(self, product_list: tuple[Product, ...]) -> bool:
        is_success = True
        for product in product_list:
            db_product = self.get_product(product.get_id())
            if not db_product or product.get_amount() > db_product.get_amount():
                is_success = False
                break
        return is_success

    def decrease_products(self, product_list: tuple[Product, ...]):
        for product in product_list:
            db_product = self.get_product(product.get_id())
            db_product.decrease_amount(product.get_amount())

    def make_transaction(self, customer_id: str):
        is_success = False
        customer = self.get_customer(customer_id)
        if customer:
            customer_products = customer.get_products()
            if self.can_decrease_products(customer_products):
                self.decrease_products(customer_products)
                customer.clear_product_list()
                is_success = True
        return is_success


import tkinter
from tkinter import ttk

customer_1 = Customer("ABC1234", "Tom", 18)
customer_2 = Customer("XYZ5869", "Bob", 24)
customer_3 = Customer("CBE1324", "Tom", 28)
customer_4 = Customer("XYZ1234", "Kate", 24)
customer_5 = Customer("RTE2345", "Jim", 16)

product_1 = Product("50004", "Apple", 5, 100)
product_2 = Product("50005", "Bread", 2, 150)
product_3 = Product("50006", "Tomato", 6, 450)

data_base = DB()
data_base.add_customer(customer_1)
data_base.add_customer(customer_2)
data_base.add_customer(customer_3)
data_base.add_customer(customer_4)
data_base.add_customer(customer_5)

data_base.add_product(product_1)
data_base.add_product(product_2)
data_base.add_product(product_3)

root = tkinter.Tk()
root.title("Listbox")
root.geometry("720x480")
root.resizable(False, False)

frame_customers = tkinter.Frame(root)
frame_customers.pack(expand=True, fill="both")

frame_products = tkinter.Frame(root)
frame_products.pack_forget()

frame_operations = tkinter.Frame(root)
frame_operations.pack_forget()

def show_customers():
    # Скрываем всё, что не нужно
    frame_products.pack_forget()
    frame_operations.pack_forget()

    # Показываем всё, что нужно
    frame_customers.pack(fill="both", expand=True)
    root.geometry("720x480")


def show_products():
    # Скрываем всё, что не нужно
    frame_customers.pack_forget()
    frame_operations.pack_forget()

    # Показываем всё, что нужно
    frame_products.pack(fill="both", expand=True)
    root.geometry("880x350")


def show_operations():
    # Скрываем всё, что не нужно
    frame_customers.pack_forget()
    frame_products.pack_forget()

    # Показываем всё, что нужно
    frame_operations.pack(fill="both", expand=True)
    root.geometry("720x480")

def close_program():
    root.quit()


root_menu = tkinter.Menu(root)
root.config(menu=root_menu)
show_menu = tkinter.Menu(root_menu, tearoff=False)
show_menu.add_command(label="Customers", command=show_customers)
show_menu.add_command(label="Products", command=show_products)
show_menu.add_command(label="Operations", command=show_operations)
show_menu.add_separator()
show_menu.add_command(label="Exit", command=close_program)
root_menu.add_cascade(label="Show", menu=show_menu)

# BEGIN FRAME CUSTOMERS
fc_customer_listbox = tkinter.Listbox(frame_customers, font=("Arial", 18), height=13)
fc_customer_listbox.place(x=20, y=20)


def fill_customer_listbox():
    fc_customer_listbox.delete(0, tkinter.END)
    for customer in data_base.get_customers():
        fc_customer_listbox.insert(tkinter.END, str(customer))


fill_customer_listbox()

fc_customer_id_lbl = tkinter.Label(frame_customers, text="ID:", font=("Arial", 18))
fc_customer_id_lbl.place(x=340, y=20)

fc_customer_id_entry = tkinter.Entry(frame_customers, font=("Arial", 18))
fc_customer_id_entry.place(x=340, y=60)

fc_customer_name_lbl = tkinter.Label(frame_customers, text="Name:", font=("Arial", 18))
fc_customer_name_lbl.place(x=340, y=100)

fc_customer_name_entry = tkinter.Entry(frame_customers, font=("Arial", 18))
fc_customer_name_entry.place(x=340, y=140)

fc_customer_age_lbl = tkinter.Label(frame_customers, text="Age:", font=("Arial", 18))
fc_customer_age_lbl.place(x=340, y=180)

fc_customer_age_entry = tkinter.Entry(frame_customers, font=("Arial", 18), width=3)
fc_customer_age_entry.place(x=340, y=220)

fc_customer_info_lbl = tkinter.Label(frame_customers, text="User info:", font=("Arial", 18))
fc_customer_info_lbl.place(x=340, y=300)

fc_customer_info = tkinter.Label(frame_customers, text="", font=("Arial", 18))
fc_customer_info.place(x=340, y=340)


def fc_add_customer():
    # Считываем данные из полей фронтенда
    new_id = fc_customer_id_entry.get()
    new_name = fc_customer_name_entry.get()
    new_age = fc_customer_age_entry.get()

    # Проверяем/Корректируем данные из полей фронтенда
    new_id = new_id.upper()
    new_name = new_name.capitalize()
    new_age = int(new_age)

    # Формируем из данных объект
    new_customer = Customer(new_id, new_name, new_age)

    # Добавляем объект в бэкенд
    if data_base.add_customer(new_customer):
        # Формируем строковое представление объекта
        new_customer_listbox = str(new_customer)

        # Добавляем строковое представление объекта во фронтенд
        fc_customer_listbox.insert(tkinter.END, new_customer_listbox)
        fo_customer_combobox["values"] = data_base.get_customers()

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for customer in data_base.get_customers():
        print(f"{customer.get_id()} {customer.get_name()} {customer.get_age()}")


fc_customer_add_btn = tkinter.Button(frame_customers, text="New", font=("Arial", 14), command=fc_add_customer)
fc_customer_add_btn.place(x=20, y=400)


def fc_delete_customer():
    # Считываем индексы выделенных элементов из фронтенда
    customer_listbox_ind = fc_customer_listbox.curselection()
    if len(customer_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_customer = fc_customer_listbox.get(customer_listbox_ind[0])

        # Отдельно выделяем идентификатор
        customer_id = selected_customer.split()[0]

        # Пытаемся удалить из бэкенда
        if data_base.remove_customer(customer_id):
            # Удаляем из фронтенда
            fc_customer_listbox.delete(customer_listbox_ind[0])

            fo_customer_combobox["values"] = data_base.get_customers()
            fo_customer_combobox.set("")

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for customer in data_base.get_customers():
        print(f"{customer.get_id()} {customer.get_name()} {customer.get_age()}")


fc_customer_delete_btn = tkinter.Button(frame_customers, text="Delete", font=("Arial", 14), command=fc_delete_customer)
fc_customer_delete_btn.place(x=75, y=400)


def fc_change_customer():
    # Считываем индексы выделенных элементов из фронтенда
    customer_listbox_ind = fc_customer_listbox.curselection()
    if len(customer_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_customer = fc_customer_listbox.get(customer_listbox_ind[0])

        # Отдельно выделяем идентификатор
        selected_id = selected_customer.split()[0]

        # Считываем данные из полей фронтенда
        new_id = fc_customer_id_entry.get()
        new_name = fc_customer_name_entry.get()
        new_age = fc_customer_age_entry.get()

        # Проверяем/Корректируем данные из полей фронтенда
        new_id = new_id.upper()
        new_name = new_name.capitalize()
        new_age = int(new_age)

        # Формируем из данных объект
        new_customer = Customer(new_id, new_name, new_age)

        # Пытаемся изменить объект в бэкенде
        if data_base.change_customer(selected_id, new_customer):
            # Формируем строковое представление объекта
            new_customer_listbox = str(new_customer)

            # Изменяем данные во фронтенде
            fc_customer_listbox.delete(customer_listbox_ind[0])
            fc_customer_listbox.insert(customer_listbox_ind[0], new_customer_listbox)

            fo_customer_combobox["values"] = data_base.get_customers()
            fo_customer_combobox.set("")

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for customer in data_base.get_customers():
        print(f"{customer.get_id()} {customer.get_name()} {customer.get_age()}")


customer_change_btn = tkinter.Button(frame_customers, text="Change", font=("Arial", 14), command=fc_change_customer)
customer_change_btn.place(x=150, y=400)


def fc_show_customer_data():
    # Считываем индексы выделенных элементов из фронтенда
    customer_listbox_ind = fc_customer_listbox.curselection()
    if len(customer_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_customer = fc_customer_listbox.get(customer_listbox_ind[0])

        # Отдельно выделяем идентификатор
        selected_id = selected_customer.split()[0]

        # Запрашиваем из бэкенда объект по идентификатору
        customer = data_base.get_customer(selected_id)
        if customer:
            customer_data = f"ID: {customer.get_id()}\nName: {customer.get_name()}\nAge: {customer.get_age()}"
            fc_customer_info.config(text=customer_data, justify="left")


fc_customer_info_btn = tkinter.Button(frame_customers, text="Info", font=("Arial", 14), command=fc_show_customer_data)
fc_customer_info_btn.place(x=235, y=400)

# def fc_fill_customer_info(event):
#     customer_listbox_ind = fc_customer_listbox.curselection()
#     if len(customer_listbox_ind) > 0:
#         selected_customer = fc_customer_listbox.get(customer_listbox_ind[0])
#         selected_id = selected_customer.split()[0]
#         customer = data_base.get_customer(selected_id)
#         if customer:
#             fc_customer_id_entry.delete(0, tkinter.END)
#             fc_customer_id_entry.insert(0, customer.get_id())
#             fc_customer_name_entry.delete(0, tkinter.END)
#             fc_customer_name_entry.insert(0, customer.get_name())
#             fc_customer_age_entry.delete(0, tkinter.END)
#             fc_customer_age_entry.insert(0, customer.get_age())
#
#
# fc_customer_listbox.bind("<<ListboxSelect>>", fill_customer_info)

# END FRAME CUSTOMERS

# BEGIN FRAME PRODUCTS
fp_product_listbox = tkinter.Listbox(frame_products, font=("Arial", 18), height=8)
fp_product_listbox.place(x=20, y=20)


def fill_product_listbox():
    fp_product_listbox.delete(0, tkinter.END)
    for product in data_base.get_products():
        fp_product_listbox.insert(tkinter.END, str(product))


fill_product_listbox()

fp_product_id_lbl = tkinter.Label(frame_products, text="ID:", font=("Arial", 18))
fp_product_id_lbl.place(x=20, y=260)

fp_product_id_entry = tkinter.Entry(frame_products, font=("Arial", 18), width=10)
fp_product_id_entry.place(x=20, y=300)

fp_product_name_lbl = tkinter.Label(frame_products, text="Name:", font=("Arial", 18))
fp_product_name_lbl.place(x=220, y=260)

fp_product_name_entry = tkinter.Entry(frame_products, font=("Arial", 18))
fp_product_name_entry.place(x=220, y=300)

fp_product_price_lbl = tkinter.Label(frame_products, text="Price:", font=("Arial", 18))
fp_product_price_lbl.place(x=540, y=260)

fp_product_price_entry = tkinter.Entry(frame_products, font=("Arial", 18), width=8)
fp_product_price_entry.place(x=540, y=300)

fp_product_amount_lbl = tkinter.Label(frame_products, text="Amount:", font=("Arial", 18))
fp_product_amount_lbl.place(x=700, y=260)

fp_product_amount_entry = tkinter.Entry(frame_products, font=("Arial", 18), width=8)
fp_product_amount_entry.place(x=700, y=300)

fp_product_info_lbl = tkinter.Label(frame_products, text="Product info:", font=("Arial", 18))
fp_product_info_lbl.place(x=460, y=20)

fp_product_info = tkinter.Label(frame_products, text="", font=("Arial", 18))
fp_product_info.place(x=460, y=60)


def fp_add_product():
    # Считываем данные из полей фронтенда
    new_id = fp_product_id_entry.get()
    new_name = fp_product_name_entry.get()
    new_price = float(fp_product_price_entry.get())
    new_amount = int(fp_product_amount_entry.get())

    # Формируем из данных объект
    new_product = Product(new_id, new_name, new_price, new_amount)

    # Добавляем объект в бэкенд
    if data_base.add_product(new_product):
        # Формируем строковое представление объекта
        new_product_listbox = str(new_product)

        # Добавляем строковое представление объекта во фронтенд
        fp_product_listbox.insert(tkinter.END, new_product_listbox)

        fo_product_combobox["values"] = data_base.get_products()

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for product in data_base.get_products():
        print(f"{product.get_id()} {product.get_name()} {product.get_price()}")


fp_product_add_btn = tkinter.Button(frame_products, text="New", font=("Arial", 14), command=fp_add_product)
fp_product_add_btn.place(x=300, y=20)


def fp_delete_product():
    # Считываем индексы выделенных элементов из фронтенда
    product_listbox_ind = fp_product_listbox.curselection()
    if len(product_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_product = fp_product_listbox.get(product_listbox_ind[0])

        # Отдельно выделяем идентификатор
        product_id = selected_product.split()[0]

        # Пытаемся удалить из бэкенда
        if data_base.remove_product(product_id):
            # Удаляем из фронтенда
            fp_product_listbox.delete(product_listbox_ind[0])

            fo_product_combobox["values"] = data_base.get_products()
            fo_product_combobox.set("")

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for product in data_base.get_products():
        print(f"{product.get_id()} {product.get_name()} {product.get_price()}")


fp_product_delete_btn = tkinter.Button(frame_products, text="Delete", font=("Arial", 14), command=fp_delete_product)
fp_product_delete_btn.place(x=300, y=70)


def fp_change_product():
    # Считываем индексы выделенных элементов из фронтенда
    product_listbox_ind = fp_product_listbox.curselection()
    if len(product_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_product = fp_product_listbox.get(product_listbox_ind[0])

        # Отдельно выделяем идентификатор
        selected_id = selected_product.split()[0]

        # Считываем данные из полей фронтенда
        new_id = fp_product_id_entry.get()
        new_name = fp_product_name_entry.get()
        new_price = float(fp_product_price_entry.get())
        new_amount = int(fp_product_amount_entry.get())

        # Формируем из данных объект
        new_product = Product(new_id, new_name, new_price, new_amount)

        # Пытаемся изменить объект в бэкенде
        if data_base.change_product(selected_id, new_product):
            # Формируем строковое представление объекта
            new_product_listbox = str(new_product)

            # Изменяем данные во фронтенде
            fp_product_listbox.delete(product_listbox_ind[0])
            fp_product_listbox.insert(product_listbox_ind[0], new_product_listbox)

            fo_product_combobox["values"] = data_base.get_products()
            fo_product_combobox.set("")

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for product in data_base.get_products():
        print(f"{product.get_id()} {product.get_name()} {product.get_price()}")


fp_product_change_btn = tkinter.Button(frame_products, text="Change", font=("Arial", 14), command=fp_change_product)
fp_product_change_btn.place(x=300, y=120)


def fp_show_product_data():
    # Считываем индексы выделенных элементов из фронтенда
    product_listbox_ind = fp_product_listbox.curselection()
    if len(product_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_product = fp_product_listbox.get(product_listbox_ind[0])

        # Отдельно выделяем идентификатор
        selected_id = selected_product.split()[0]

        # Запрашиваем из бэкенда объект по идентификатору
        product = data_base.get_product(selected_id)
        if product:
            product_data = (f"ID: {product.get_id()}\nName: {product.get_name()}\n"
                            f"Price: {product.get_price()}₼\nAmount: {product.get_amount()}")
            fp_product_info.config(text=product_data, justify="left")


fp_product_info_btn = tkinter.Button(frame_products, text="Info", font=("Arial", 14), command=fp_show_product_data)
fp_product_info_btn.place(x=300, y=170)
# END FRAME PRODUCT

# BEGIN FRAME OPERATIONS
fo_customer_lbl = tkinter.Label(frame_operations, text="Customer:", font=("Arial", 16))
fo_customer_lbl.place(x=20, y=20)
fo_customer_combobox = ttk.Combobox(frame_operations, values=data_base.get_customers(), font=("Arial", 18), state="readonly")
fo_customer_combobox.place(x=20, y=60)

fo_product_lbl = tkinter.Label(frame_operations, text="Product:", font=("Arial", 16))
fo_product_lbl.place(x=20, y=220)
fo_product_combobox = ttk.Combobox(frame_operations, values=data_base.get_products(), font=("Arial", 18), state="readonly")
fo_product_combobox.place(x=20, y=260)

fo_product_amount_lbl = tkinter.Label(frame_operations, text="Amount:", font=("Arial", 18))
fo_product_amount_lbl.place(x=20, y=300)
fo_product_amount_entry = tkinter.Entry(frame_operations, font=("Arial", 18), width=8)
fo_product_amount_entry.place(x=20, y=340)

fo_operations_info = tkinter.Label(frame_operations, text="", font=("Arial", 16))
fo_operations_info.place(x=20, y=380)

fo_product_listbox = tkinter.Listbox(frame_operations, font=("Arial", 18), height=12)
fo_product_listbox.place(x=400, y=60)

fo_customer_selected_lbl = tkinter.Label(frame_operations, text="", font=("Arial", 16))
fo_customer_selected_lbl.place(x=400, y=20)

fo_customer_lbl = tkinter.Label(frame_operations, text="Customer:", font=("Arial", 16))
fo_customer_lbl.place(x=20, y=20)


def fill_customer_product_listbox(customer_products: tuple[Product, ...]):
    fo_product_listbox.delete(0, tkinter.END)
    for product in customer_products:
        fo_product_listbox.insert(tkinter.END, str(product))


def fo_show_customer_products():
    customer_str = fo_customer_combobox.get()
    customer_id = customer_str.split()[0]

    selected_customer = data_base.get_customer(customer_id)
    if selected_customer:
        fill_customer_product_listbox(selected_customer.get_products())
        fo_customer_selected_lbl.config(text=str(selected_customer))


fo_customer_select_btn = tkinter.Button(frame_operations, text="Show customer products", font=("Arial", 16),
                                    command=fo_show_customer_products)
fo_customer_select_btn.place(x=20, y=140)


# def show_customer_products(event):
#     customer_str = fo_customer_combobox.get()
#     customer_id = customer_str.split()[0]
#
#     selected_customer = data_base.get_customer(customer_id)
#     if selected_customer:
#         fill_customer_product_listbox(selected_customer)
#         fo_customer_selected_lbl.config(text=str(selected_customer))
#
#
# fo_customer_combobox.bind("<<ComboboxSelected>>", show_customer_products)


def fo_add_product_to_customer():
    customer_str = fo_customer_combobox.get()
    product_str = fo_product_combobox.get()
    product_amount = fo_product_amount_entry.get()

    customer_id = customer_str.split()[0]
    product_id = product_str.split()[0]
    selected_customer = data_base.get_customer(customer_id)
    selected_product = data_base.get_product(product_id)

    if selected_customer and selected_product:
        product_to_add = Product(selected_product.get_id(),
                                 selected_product.get_name(),
                                 selected_product.get_price(),
                                 int(product_amount))
        result = selected_customer.add_product(product_to_add)
        if result == 1 or result == 2:
            fo_operations_info.config(text="Product added", justify="left")
            fill_customer_product_listbox(selected_customer.get_products())
            fo_customer_selected_lbl.config(text=str(selected_customer))
        else:
            fo_operations_info.config(text="Error", justify="left")


fo_add_product_btn = tkinter.Button(frame_operations, text="Add product", font=("Arial", 16),
                                    command=fo_add_product_to_customer)
fo_add_product_btn.place(x=20, y=420)


def fo_make_transaction():
    customer_str = fo_customer_combobox.get()

    customer_id = customer_str.split()[0]
    customer = data_base.get_customer(customer_id)

    if data_base.make_transaction(customer_id):
        fill_product_listbox()
        fill_customer_product_listbox(customer.get_products())
        fo_product_combobox["values"] = data_base.get_products()
        fo_product_combobox.set("")
        fo_operations_info.config(text="Transaction success!", justify="left")
    else:
        fo_operations_info.config(text="Error!", justify="left")


fo_make_transaction_btn = tkinter.Button(frame_operations, text="Make transaction", font=("Arial", 16),
                                    command=fo_make_transaction)
fo_make_transaction_btn.place(x=400, y=420)
# END FRAME OPERATIONS

root.mainloop()