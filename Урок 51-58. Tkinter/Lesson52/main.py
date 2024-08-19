# ==============================================LESSON52==============================================
# Listbox. Добавление, Удаление, Изменение, Поиск.

customer_1 = {"id": "ABC1234", "name": "Tom"}
customer_2 = {"id": "DEF5869", "name": "Bob"}
customer_3 = {"id": "QWE1556", "name": "Kate"}
customer_list = [customer_1, customer_2, customer_3]


def backend_find_customer_index(customer_id):
    found_index = -1
    for i in range(len(customer_list)):
        if customer_id == customer_list[i]["id"]:
            found_index = i
            break
    return found_index


def backend_get_customer(customer_id):
    index = backend_find_customer_index(customer_id)
    if index != -1:
        customer = customer_list[index]
    else:
        customer = None
    return customer


def backend_add_customer(new_customer):
    is_success = False
    index = backend_find_customer_index(new_customer["id"])
    if index == -1:
        customer_list.append(new_customer)
        is_success = True
    return is_success


def backend_change_customer(customer_to_change_id, changed_customer):
    is_success = False
    customer_to_change = backend_get_customer(customer_to_change_id)
    if customer_to_change:
        customer_to_change_id = customer_to_change["id"]
        changed_customer_id = changed_customer["id"]
        changed_customer_index = backend_find_customer_index(changed_customer_id)
        if customer_to_change_id == changed_customer_id or changed_customer_index == -1:
            customer_to_change["id"] = changed_customer["id"]
            customer_to_change["name"] = changed_customer["name"]
            is_success = True
    return is_success


def backend_remove_customer(customer_id):
    is_success = False
    index = backend_find_customer_index(customer_id)
    if index != -1:
        del customer_list[index]
        is_success = True
    return is_success


import tkinter

root = tkinter.Tk()
root.title("Listbox")
root.geometry("720x480")
root.resizable(False, False)

customer_frame = tkinter.Frame(root)
customer_frame.pack(expand=True, fill="both")

customer_listbox = tkinter.Listbox(customer_frame, font=("Arial", 18), height=13)
customer_listbox.place(x=20, y=20)


def fill_customer_listbox():
    customer_listbox.delete(0, tkinter.END)
    for item in customer_list:
        listbox_item = f'{item["id"]} {item["name"]}'
        customer_listbox.insert(tkinter.END, listbox_item)


fill_customer_listbox()

customer_id_lbl = tkinter.Label(customer_frame, text="ID:", font=("Arial", 18))
customer_id_lbl.place(x=340, y=20)

customer_id_entry = tkinter.Entry(customer_frame, font=("Arial", 18))
customer_id_entry.place(x=340, y=60)

customer_name_lbl = tkinter.Label(customer_frame, text="Name:", font=("Arial", 18))
customer_name_lbl.place(x=340, y=100)

customer_name_entry = tkinter.Entry(customer_frame, font=("Arial", 18))
customer_name_entry.place(x=340, y=140)

customer_info_lbl = tkinter.Label(customer_frame, text="Customer info:", font=("Arial", 18))
customer_info_lbl.place(x=340, y=360)

customer_info = tkinter.Label(customer_frame, text="", font=("Arial", 18))
customer_info.place(x=340, y=400)


def add_customer():
    # Считываем данные из полей фронтенда
    new_id = customer_id_entry.get()
    new_name = customer_name_entry.get()

    # Формируем из данных объект
    new_customer = {"id": new_id, "name": new_name}

    # Пытаемся добавить объект в бэкенд
    if backend_add_customer(new_customer):
        # Формируем строковое представление объекта
        new_customer_listbox = f'{new_customer["id"]} {new_customer["name"]}'

        # Добавляем строковое представление объекта во фронтенд
        customer_listbox.insert(tkinter.END, new_customer_listbox)

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for item in customer_list:
        print(item)


customer_add_btn = tkinter.Button(customer_frame, text="New", font=("Arial", 14), command=add_customer)
customer_add_btn.place(x=20, y=400)


def delete_customer():
    # Считываем индексы выделенных элементов из фронтенда
    customer_listbox_ind = customer_listbox.curselection()
    print(customer_listbox_ind)
    if len(customer_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_customer = customer_listbox.get(customer_listbox_ind[0])
        print(selected_customer)

        # Отдельно выделяем идентификатор
        customer_id = selected_customer.split()[0]
        print(customer_id)

        # Пытаемся удалить из бэкенда
        if backend_remove_customer(customer_id):
            # Удаляем из фронтенда
            customer_listbox.delete(customer_listbox_ind[0])

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for item in customer_list:
        print(item)


customer_delete_btn = tkinter.Button(customer_frame, text="Delete", font=("Arial", 14), command=delete_customer)
customer_delete_btn.place(x=75, y=400)


def change_customer():
    # Считываем индексы выделенных элементов из фронтенда
    customer_listbox_ind = customer_listbox.curselection()
    if len(customer_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_customer = customer_listbox.get(customer_listbox_ind[0])

        # Отдельно выделяем идентификатор
        selected_id = selected_customer.split()[0]

        # Считываем данные из полей фронтенда
        new_id = customer_id_entry.get()
        new_name = customer_name_entry.get()

        # Формируем из данных объект
        new_customer = {"id": new_id, "name": new_name}

        # Пытаемся изменить объект в бэкенде
        if backend_change_customer(selected_id, new_customer):
            # Формируем строковое представление объекта
            new_customer_listbox = f'{new_customer["id"]} {new_customer["name"]}'

            # Изменяем данные во фронтенде
            customer_listbox.delete(customer_listbox_ind[0])
            customer_listbox.insert(customer_listbox_ind[0], new_customer_listbox)

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for item in customer_list:
        print(item)


customer_change_btn = tkinter.Button(customer_frame, text="Change", font=("Arial", 14), command=change_customer)
customer_change_btn.place(x=150, y=400)


def show_customer_data():
    # Считываем индексы выделенных элементов из фронтенда
    customer_listbox_ind = customer_listbox.curselection()
    if len(customer_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_customer = customer_listbox.get(customer_listbox_ind[0])

        # Отдельно выделяем идентификатор
        selected_id = selected_customer.split()[0]

        # Запрашиваем из бэкенда объект по идентификатору
        customer = backend_get_customer(selected_id)
        if customer:
            customer_data = f'{customer["id"]} {customer["name"]}'
            customer_info.config(text=customer_data)


customer_info_btn = tkinter.Button(customer_frame, text="Info", font=("Arial", 14), command=show_customer_data)
customer_info_btn.place(x=235, y=400)

root.mainloop()

# ====================================================================================================
# ПЗ 52.1
# ====================================================================================================
