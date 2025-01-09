# ============================================LESSON53-54=============================================
# ООП анкета. Добавление Person в Listbox и DB. Listbox - выбор, удаление, инфо в label.

class Person:
    __id = "0000000"
    __name = "Unknown"
    __age = 0

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


class DB:
    __person_list: list[Person] = list()

    def __init__(self):
        self.__person_list: list[Person] = list()

    def set_persons(self, new_list: list[Person]):
        self.__person_list = new_list

    def get_persons(self):
        return tuple(self.__person_list)

    def __get_person_index(self, person_id: str) -> int:
        found_index = -1
        for i in range(len(self.__person_list)):
            if person_id == self.__person_list[i].get_id():
                found_index = i
                break
        return found_index

    def get_person(self, person_id: str) -> Person | None:
        index = self.__get_person_index(person_id)
        if index != -1:
            person = self.__person_list[index]
        else:
            person = None
        return person

    def add_person(self, new_person: Person) -> bool:
        is_success = False
        index = self.__get_person_index(new_person.get_id())
        if index == -1:
            self.__person_list.append(new_person)
            is_success = True
        return is_success

    def remove_person(self, person_id: str) -> bool:
        is_success = False
        index = self.__get_person_index(person_id)
        if index != -1:
            del self.__person_list[index]
            is_success = True
        return is_success

    def change_person(self, person_id: str, changed_person: Person) -> bool:
        is_success = False
        person_to_change = self.get_person(person_id)
        if person_to_change:
            changed_person_id = changed_person.get_id()
            changed_person_index = self.__get_person_index(changed_person_id)
            if person_id == changed_person_id or changed_person_index == -1:
                person_to_change.set_id(changed_person.get_id())
                person_to_change.set_name(changed_person.get_name())
                person_to_change.set_age(changed_person.get_age())
                is_success = True
        return is_success


import tkinter

person_1 = Person("ABC1234", "Tom", 18)
person_2 = Person("XYZ5869", "Bob", 24)
person_3 = Person("CBE1324", "Tom", 28)
person_4 = Person("XYZ1234", "Kate", 24)
person_5 = Person("RTE2345", "Jim", 16)

data_base = DB()
data_base.add_person(person_1)
data_base.add_person(person_2)
data_base.add_person(person_3)
data_base.add_person(person_4)
data_base.add_person(person_5)

root = tkinter.Tk()
root.title("Listbox")
root.geometry("720x480")
root.resizable(False, False)

frame_person = tkinter.Frame(root)
frame_person.pack(expand=True, fill="both")

person_listbox = tkinter.Listbox(frame_person, font=("Arial", 18), height=13)
person_listbox.place(x=20, y=20)


def refresh_person_listbox():
    person_listbox.delete(0, tkinter.END)
    for person in data_base.get_persons():
        person_listbox.insert(tkinter.END, str(person))


refresh_person_listbox()

person_id_lbl = tkinter.Label(frame_person, text="ID:", font=("Arial", 18))
person_id_lbl.place(x=340, y=20)

person_id_entry = tkinter.Entry(frame_person, font=("Arial", 18))
person_id_entry.place(x=340, y=60)

person_name_lbl = tkinter.Label(frame_person, text="Name:", font=("Arial", 18))
person_name_lbl.place(x=340, y=100)

person_name_entry = tkinter.Entry(frame_person, font=("Arial", 18))
person_name_entry.place(x=340, y=140)

person_age_lbl = tkinter.Label(frame_person, text="Age:", font=("Arial", 18))
person_age_lbl.place(x=340, y=180)

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
    new_age = int(person_age_entry.get())

    # Формируем из данных объект
    new_person = Person(new_id, new_name, new_age)

    # Добавляем объект в бэкенд
    if data_base.add_person(new_person):
        # Формируем строковое представление объекта
        # new_person_listbox = str(new_person)

        # Добавляем строковое представление объекта во фронтенд
        # person_listbox.insert(tkinter.END, new_person_listbox)

        # Обновляем фронтенд
        refresh_person_listbox()

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for person in data_base.get_persons():
        print(f"{person.get_id()} {person.get_name()} {person.get_age()}")


person_add_btn = tkinter.Button(frame_person, text="New", font=("Arial", 14), command=add_person)
person_add_btn.place(x=20, y=400)


def delete_person():
    # Считываем индексы выделенных элементов из фронтенда
    selected_person_indexes = person_listbox.curselection()

    if len(selected_person_indexes) > 0:
        # Выделяем в переменную индекс выбранного элемента
        selected_person_index = selected_person_indexes[0]

        # Считываем элемент по индексу
        selected_person_str = person_listbox.get(selected_person_index)

        # Отдельно выделяем идентификатор
        selected_person_id = selected_person_str.split()[0]

        # Пытаемся удалить из бэкенда
        if data_base.remove_person(selected_person_id):
            # Удаляем из фронтенда
            # person_listbox.delete(selected_person_index)

            # Обновляем фронтенд
            refresh_person_listbox()

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for person in data_base.get_persons():
        print(f"{person.get_id()} {person.get_name()} {person.get_age()}")


person_delete_btn = tkinter.Button(frame_person, text="Delete", font=("Arial", 14), command=delete_person)
person_delete_btn.place(x=75, y=400)


def change_person():
    # Считываем индексы выделенных элементов из фронтенда
    selected_person_indexes = person_listbox.curselection()
    if len(selected_person_indexes) > 0:
        # Выделяем в переменную индекс выбранного элемента
        selected_person_index = selected_person_indexes[0]

        # Считываем элемент по индексу
        selected_person_str = person_listbox.get(selected_person_index)

        # Отдельно выделяем идентификатор
        selected_person_id = selected_person_str.split()[0]

        # Считываем данные из полей фронтенда
        new_id = person_id_entry.get()
        new_name = person_name_entry.get()
        new_age = int(person_age_entry.get())

        # Формируем из данных объект
        new_person = Person(new_id, new_name, new_age)

        # Пытаемся изменить объект в бэкенде
        if data_base.change_person(selected_person_id, new_person):
            # Формируем строковое представление объекта
            # new_person_listbox = str(new_person)

            # Изменяем данные во фронтенде
            # person_listbox.delete(selected_person_index)
            # person_listbox.insert(selected_person_index, new_person_listbox)

            # Обновляем фронтенд
            refresh_person_listbox()

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for person in data_base.get_persons():
        print(f"{person.get_id()} {person.get_name()} {person.get_age()}")


person_change_btn = tkinter.Button(frame_person, text="Change", font=("Arial", 14), command=change_person)
person_change_btn.place(x=150, y=400)


def show_person_data():
    # Считываем индексы выделенных элементов из фронтенда
    selected_person_indexes = person_listbox.curselection()
    if len(selected_person_indexes) > 0:
        # Выделяем в переменную индекс выбранного элемента
        selected_person_index = selected_person_indexes[0]

        # Считываем элемент по индексу
        selected_person_str = person_listbox.get(selected_person_index)

        # Отдельно выделяем идентификатор
        selected_person_id = selected_person_str.split()[0]

        # Запрашиваем из бэкенда объект по идентификатору
        selected_person = data_base.get_person(selected_person_id)
        if selected_person:
            person_data = f"ID: {selected_person.get_id()}\nName: {selected_person.get_name()}\nAge: {selected_person.get_age()}"
            person_info.config(text=person_data, justify="left")


person_info_btn = tkinter.Button(frame_person, text="Info", font=("Arial", 14), command=show_person_data)
person_info_btn.place(x=235, y=400)


# def fill_person_info(event):
#     selected_person_indexes = person_listbox.curselection()
#     if len(selected_person_indexes) > 0:
#         selected_person_str = person_listbox.get(selected_person_indexes[0])
#         selected_person_id = selected_person_str.split()[0]
#         selected_person = data_base.get_person(selected_person_id)
#         if selected_person:
#             person_id_entry.delete(0, tkinter.END)
#             person_id_entry.insert(0, selected_person.get_id())
#             person_name_entry.delete(0, tkinter.END)
#             person_name_entry.insert(0, selected_person.get_name())
#             person_age_entry.delete(0, tkinter.END)
#             person_age_entry.insert(0, str(selected_person.get_age()))
#
#
# person_listbox.bind("<<ListboxSelect>>", fill_person_info)

root.mainloop()


# ====================================================================================================
# Python - PT53-54
# ====================================================================================================
