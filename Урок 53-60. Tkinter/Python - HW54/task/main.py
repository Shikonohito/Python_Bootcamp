human_1 = {"id": "ABC1234", "f_name": "Teston", "l_name": "Lebra", "birth_day": 22, "birth_month": 4, "birth_year": 1997}
human_2 = {"id": "DEF5869", "f_name": "Bob", "l_name": "Jackson", "birth_day": 10, "birth_month": 2, "birth_year": 1995}
human_3 = {"id": "QWE1556", "f_name": "Kate", "l_name": "Grid", "birth_day": 27, "birth_month": 12, "birth_year": 1999}
human_list = [human_1, human_2, human_3]


def backend_find_human_index(human_id):
    found_index = -1
    for i in range(len(human_list)):
        if human_id == human_list[i]["id"]:
            found_index = i
            break
    return found_index


def backend_get_human(human_id):
    index = backend_find_human_index(human_id)
    if index != -1:
        human = human_list[index]
    else:
        human = None
    return human


def backend_add_human(new_human):
    is_success = False
    index = backend_find_human_index(new_human["id"])
    if index == -1:
        human_list.append(new_human)
        is_success = True
    return is_success


def backend_change_human(human_to_change_id, changed_human):
    is_success = False
    human_to_change = backend_get_human(human_to_change_id)
    if human_to_change:
        human_to_change_id = human_to_change["id"]
        changed_human_id = changed_human["id"]
        changed_human_index = backend_find_human_index(changed_human_id)
        if human_to_change_id == changed_human_id or changed_human_index == -1:
            human_to_change["id"] = changed_human["id"]
            human_to_change["f_name"] = changed_human["f_name"]
            human_to_change["l_name"] = changed_human["l_name"]
            human_to_change["birth_day"] = changed_human["birth_day"]
            human_to_change["birth_month"] = changed_human["birth_month"]
            human_to_change["birth_year"] = changed_human["birth_year"]
            is_success = True
    return is_success


def backend_remove_human(human_id):
    is_success = False
    index = backend_find_human_index(human_id)
    if index != -1:
        del human_list[index]
        is_success = True
    return is_success


import tkinter

root = tkinter.Tk()
root.title("Listbox")
root.geometry("720x480")
root.resizable(False, False)

human_frame = tkinter.Frame(root)
human_frame.pack(expand=True, fill="both")

human_listbox = tkinter.Listbox(human_frame, font=("Arial", 18), height=13)
human_listbox.place(x=20, y=20)


def refresh_human_listbox():
    human_listbox.delete(0, tkinter.END)
    for item in human_list:
        listbox_item = f'{item["id"]} {item["f_name"]} {item["l_name"]}'
        human_listbox.insert(tkinter.END, listbox_item)


refresh_human_listbox()

human_id_lbl = tkinter.Label(human_frame, text="ID:", font=("Arial", 18))
human_id_lbl.place(x=340, y=20)

human_id_entry = tkinter.Entry(human_frame, font=("Arial", 18))
human_id_entry.place(x=340, y=60)

human_f_name_lbl = tkinter.Label(human_frame, text="First Name:", font=("Arial", 18))
human_f_name_lbl.place(x=340, y=100)

human_f_name_entry = tkinter.Entry(human_frame, font=("Arial", 18))
human_f_name_entry.place(x=340, y=140)

human_l_name_lbl = tkinter.Label(human_frame, text="Last Name:", font=("Arial", 18))
human_l_name_lbl.place(x=340, y=180)

human_l_name_entry = tkinter.Entry(human_frame, font=("Arial", 18))
human_l_name_entry.place(x=340, y=220)

human_birth_date_lbl = tkinter.Label(human_frame, text="Birth date (DD/MM/YYYY):", font=("Arial", 18))
human_birth_date_lbl.place(x=340, y=260)

human_birth_day_entry = tkinter.Entry(human_frame, font=("Arial", 18), width=2)
human_birth_day_entry.place(x=340, y=300)

human_day_slash_month_lbl = tkinter.Label(human_frame, text="/", font=("Arial", 26))
human_day_slash_month_lbl.place(x=375, y=295)

human_birth_month_entry = tkinter.Entry(human_frame, font=("Arial", 18), width=2)
human_birth_month_entry.place(x=400, y=300)

human_month_slash_year_lbl = tkinter.Label(human_frame, text="/", font=("Arial", 26))
human_month_slash_year_lbl.place(x=435, y=295)

human_birth_year_entry = tkinter.Entry(human_frame, font=("Arial", 18), width=4)
human_birth_year_entry.place(x=460, y=300)

human_info_lbl = tkinter.Label(human_frame, text="human info:", font=("Arial", 18))
human_info_lbl.place(x=340, y=360)

human_info = tkinter.Label(human_frame, text="", font=("Arial", 18))
human_info.place(x=340, y=400)


def add_human():
    # Считываем данные из полей фронтенда
    new_id = human_id_entry.get()
    new_f_name = human_f_name_entry.get()
    new_l_name = human_l_name_entry.get()
    new_birth_day = int(human_birth_day_entry.get())
    new_birth_month = int(human_birth_month_entry.get())
    new_birth_year = int(human_birth_year_entry.get())

    # Формируем из данных объект
    new_human = {"id": new_id, "f_name": new_f_name, "l_name": new_l_name,
                 "birth_day": new_birth_day, "birth_month": new_birth_month, "birth_year": new_birth_year}

    # Пытаемся добавить объект в бэкенд
    if backend_add_human(new_human):
        # Формируем строковое представление объекта
        new_human_listbox = f'{new_human["id"]} {new_human["f_name"]} {new_human["l_name"]}'

        # Добавляем строковое представление объекта во фронтенд
        human_listbox.insert(tkinter.END, new_human_listbox)

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for item in human_list:
        print(item)


human_add_btn = tkinter.Button(human_frame, text="New", font=("Arial", 14), command=add_human)
human_add_btn.place(x=20, y=400)


def delete_human():
    # Считываем индексы выделенных элементов из фронтенда
    human_listbox_indexes = human_listbox.curselection()
    print(human_listbox_indexes)
    if human_listbox_indexes > 0:
        # Считываем элемент по индексу
        selected_human_str = human_listbox.get(human_listbox_indexes[0])
        print(selected_human_str)

        # Отдельно выделяем идентификатор
        human_id = selected_human_str.split()[0]
        print(human_id)

        # Пытаемся удалить из бэкенда
        if backend_remove_human(human_id):
            # Удаляем из фронтенда
            human_listbox.delete(human_listbox_indexes[0])

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for item in human_list:
        print(item)


human_delete_btn = tkinter.Button(human_frame, text="Delete", font=("Arial", 14), command=delete_human)
human_delete_btn.place(x=75, y=400)


def change_human():
    # Считываем индексы выделенных элементов из фронтенда
    human_listbox_indexes = human_listbox.curselection()
    if human_listbox_indexes:
        # Считываем элемент по индексу
        selected_human_str = human_listbox.get(human_listbox_indexes[0])

        # Отдельно выделяем идентификатор
        selected_id = selected_human_str.split()[0]

        # Считываем данные из полей фронтенда
        new_id = human_id_entry.get()
        new_f_name = human_f_name_entry.get()
        new_l_name = human_l_name_entry.get()
        new_birth_day = int(human_birth_day_entry.get())
        new_birth_month = int(human_birth_month_entry.get())
        new_birth_year = int(human_birth_year_entry.get())

        # Формируем из данных объект
        new_human = {"id": new_id, "f_name": new_f_name, "l_name": new_l_name,
                     "birth_day": new_birth_day, "birth_month": new_birth_month, "birth_year": new_birth_year}

        # Пытаемся изменить объект в бэкенде
        if backend_change_human(selected_id, new_human):
            # Формируем строковое представление объекта
            new_human_listbox = f'{new_human["id"]} {new_human["f_name"]}'

            # Изменяем данные во фронтенде
            human_listbox.delete(human_listbox_indexes[0])
            human_listbox.insert(human_listbox_indexes[0], new_human_listbox)

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for item in human_list:
        print(item)


human_change_btn = tkinter.Button(human_frame, text="Change", font=("Arial", 14), command=change_human)
human_change_btn.place(x=150, y=400)


def show_human_data():
    # Считываем индексы выделенных элементов из фронтенда
    human_listbox_indexes = human_listbox.curselection()
    if human_listbox_indexes:
        # Считываем элемент по индексу
        selected_human_str = human_listbox.get(human_listbox_indexes[0])

        # Отдельно выделяем идентификатор
        selected_id = selected_human_str.split()[0]

        # Запрашиваем из бэкенда объект по идентификатору
        human = backend_get_human(selected_id)
        if human:
            human_data = (f'{human["id"]} {human["f_name"]} {human["l_name"]} '
                          f'{human["birth_day"]} {human["birth_month"]} {human["birth_year"]}')
            human_info.config(text=human_data)


human_info_btn = tkinter.Button(human_frame, text="Info", font=("Arial", 14), command=show_human_data)
human_info_btn.place(x=235, y=400)

root.mainloop()
