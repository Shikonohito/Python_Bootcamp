class Taxi:
    __id = "0000000"
    __f_name = "Unknown"
    __l_name = "Unknown"
    __rating_list = list()

    def __init__(self, id: str, f_name: str, l_name: str, rating_list: list[int] = None):
        self.__id = id
        self.__f_name = f_name
        self.__l_name = l_name
        if rating_list:
            self.__rating_list = rating_list
        else:
            self.__rating_list = list()

    def __str__(self):
        result = f"{self.__id} {self.__f_name} {self.__l_name}"
        return result

    def set_id(self, new_id: str):
        self.__id = new_id

    def get_id(self):
        return self.__id

    def set_f_name(self, f_name: str):
        self.__f_name = f_name

    def get_f_name(self):
        return self.__f_name

    def set_l_name(self, l_name: str):
        self.__l_name = l_name

    def get_l_name(self):
        return self.__l_name

    def set_rating_list(self, rating_list: list[int]):
        self.__rating_list = rating_list

    def get_rating_list(self):
        return tuple(self.__rating_list)

    def add_rating(self, rating: int) -> bool:
        is_success = False
        if 1 <= rating and rating <= 5:
            self.__rating_list.append(rating)
            is_success = True
        return is_success

    def get_avg(self):
        if len(self.__rating_list) > 0:
            return sum(self.__rating_list) / len(self.__rating_list)
        else:
            return 0


class DB:
    __taxi_list: list[Taxi] = list()

    def __init__(self):
        self.__taxi_list: list[Taxi] = list()

    def set_taxi_drivers(self, new_list: list[Taxi]):
        self.__taxi_list = new_list

    def get_taxi_drivers(self):
        return tuple(self.__taxi_list)

    def __get_taxi_index(self, taxi_id: str) -> int:
        found_index = -1
        for i in range(len(self.__taxi_list)):
            if taxi_id == self.__taxi_list[i].get_id():
                found_index = i
                break
        return found_index

    def get_taxi(self, taxi_id: str) -> Taxi | None:
        index = self.__get_taxi_index(taxi_id)
        if index != -1:
            taxi = self.__taxi_list[index]
        else:
            taxi = None
        return taxi

    def add_taxi(self, new_taxi: Taxi) -> bool:
        is_success = False
        index = self.__get_taxi_index(new_taxi.get_id())
        if index == -1:
            self.__taxi_list.append(new_taxi)
            is_success = True
        return is_success

    def remove_taxi(self, taxi_id: str) -> bool:
        is_success = False
        index = self.__get_taxi_index(taxi_id)
        if index != -1:
            del self.__taxi_list[index]
            is_success = True
        return is_success

    def change_taxi(self, taxi_id: str, changed_taxi: Taxi) -> bool:
        is_success = False
        taxi_to_change = self.get_taxi(taxi_id)
        if taxi_to_change:
            changed_taxi_id = changed_taxi.get_id()
            changed_taxi_index = self.__get_taxi_index(changed_taxi_id)
            if taxi_id == changed_taxi_id or changed_taxi_index == -1:
                taxi_to_change.set_id(changed_taxi.get_id())
                taxi_to_change.set_f_name(changed_taxi.get_f_name())
                taxi_to_change.set_l_name(changed_taxi.get_l_name())
                taxi_to_change.set_rating_list(list(changed_taxi.get_rating_list()))
                is_success = True
        return is_success

    def add_rating(self, taxi_id: str, rating: int) -> bool:
        is_success = False
        taxi = self.get_taxi(taxi_id)
        if taxi:
            is_success = taxi.add_rating(rating)
        return is_success

    def get_avg(self, taxi_id: str):
        taxi = self.get_taxi(taxi_id)
        avg_result = 0
        if taxi:
            avg_result = taxi.get_avg()
        return avg_result


import tkinter

taxi_1 = Taxi("ABC1234", "Teston", "Lebra", [5, 4, 5])
taxi_2 = Taxi("XYZ5869", "Bob", "Grid", [1, 3, 5])
taxi_3 = Taxi("CBE1324", "Kate", "Rho")

data_base = DB()
data_base.add_taxi(taxi_1)
data_base.add_taxi(taxi_2)
data_base.add_taxi(taxi_3)

root = tkinter.Tk()
root.title("Listbox")
root.geometry("720x580")
root.resizable(False, False)

frame_taxi = tkinter.Frame(root)
frame_taxi.pack(expand=True, fill="both")

taxi_listbox = tkinter.Listbox(frame_taxi, font=("Arial", 18), height=13)
taxi_listbox.place(x=20, y=20)


def fill_taxi_listbox():
    taxi_listbox.delete(0, tkinter.END)
    for taxi in data_base.get_taxi_drivers():
        taxi_listbox.insert(tkinter.END, str(taxi))


fill_taxi_listbox()

taxi_id_lbl = tkinter.Label(frame_taxi, text="ID:", font=("Arial", 18))
taxi_id_lbl.place(x=340, y=20)

taxi_id_entry = tkinter.Entry(frame_taxi, font=("Arial", 18))
taxi_id_entry.place(x=340, y=60)

taxi_f_name_lbl = tkinter.Label(frame_taxi, text="First Name:", font=("Arial", 18))
taxi_f_name_lbl.place(x=340, y=100)

taxi_f_name_entry = tkinter.Entry(frame_taxi, font=("Arial", 18))
taxi_f_name_entry.place(x=340, y=140)

taxi_l_name_lbl = tkinter.Label(frame_taxi, text="Last Name:", font=("Arial", 18))
taxi_l_name_lbl.place(x=340, y=180)

taxi_l_name_entry = tkinter.Entry(frame_taxi, font=("Arial", 18))
taxi_l_name_entry.place(x=340, y=220)

taxi_rating_lbl = tkinter.Label(frame_taxi, text="Rating:", font=("Arial", 18))
taxi_rating_lbl.place(x=340, y=280)

taxi_rating_entry = tkinter.Entry(frame_taxi, font=("Arial", 18), width=2)
taxi_rating_entry.place(x=430, y=280)

taxi_info_lbl = tkinter.Label(frame_taxi, text="Taxi info:", font=("Arial", 18))
taxi_info_lbl.place(x=340, y=360)

taxi_info = tkinter.Label(frame_taxi, text="", font=("Arial", 18))
taxi_info.place(x=340, y=400)


def add_taxi():
    # Считываем данные из полей фронтенда
    new_id = taxi_id_entry.get()
    new_f_name = taxi_f_name_entry.get()
    new_l_name = taxi_l_name_entry.get()

    # Формируем из данных объект
    new_taxi = Taxi(new_id, new_f_name, new_l_name)

    # Добавляем объект в бэкенд
    if data_base.add_taxi(new_taxi):
        # Формируем строковое представление объекта
        new_taxi_listbox = str(new_taxi)

        # Добавляем строковое представление объекта во фронтенд
        taxi_listbox.insert(tkinter.END, new_taxi_listbox)

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for taxi in data_base.get_taxi_drivers():
        print(f"{taxi.get_id()} {taxi.get_f_name()} {taxi.get_l_name()}"
              f"{taxi.get_rating_list()} {taxi.get_avg()}")


taxi_add_btn = tkinter.Button(frame_taxi, text="New", font=("Arial", 14), command=add_taxi)
taxi_add_btn.place(x=20, y=400)


def delete_taxi():
    # Считываем индексы выделенных элементов из фронтенда
    taxi_listbox_ind = taxi_listbox.curselection()

    if len(taxi_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_taxi = taxi_listbox.get(taxi_listbox_ind[0])

        # Отдельно выделяем идентификатор
        taxi_id = selected_taxi.split()[0]

        # Пытаемся удалить из бэкенда
        if data_base.remove_taxi(taxi_id):
            # Удаляем из фронтенда
            taxi_listbox.delete(taxi_listbox_ind[0])

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for taxi in data_base.get_taxi_drivers():
        print(f"{taxi.get_id()} {taxi.get_f_name()} {taxi.get_l_name()}"
              f"{taxi.get_rating_list()} {taxi.get_avg()}")


taxi_delete_btn = tkinter.Button(frame_taxi, text="Delete", font=("Arial", 14), command=delete_taxi)
taxi_delete_btn.place(x=75, y=400)


def change_taxi():
    # Считываем индексы выделенных элементов из фронтенда
    taxi_listbox_ind = taxi_listbox.curselection()
    if len(taxi_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_taxi = taxi_listbox.get(taxi_listbox_ind[0])

        # Отдельно выделяем идентификатор
        selected_id = selected_taxi.split()[0]
        selected_taxi = data_base.get_taxi(selected_id)

        # Считываем данные из полей фронтенда
        new_id = taxi_id_entry.get()
        new_f_name = taxi_f_name_entry.get()
        new_l_name = taxi_l_name_entry.get()

        # Формируем из данных объект
        new_taxi = Taxi(new_id, new_f_name, new_l_name, list(selected_taxi.get_rating_list()))

        # Пытаемся изменить объект в бэкенде
        if data_base.change_taxi(selected_id, new_taxi):
            # Формируем строковое представление объекта
            new_taxi_listbox = str(new_taxi)

            # Изменяем данные во фронтенде
            taxi_listbox.delete(taxi_listbox_ind[0])
            taxi_listbox.insert(taxi_listbox_ind[0], new_taxi_listbox)

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for taxi in data_base.get_taxi_drivers():
        print(f"{taxi.get_id()} {taxi.get_f_name()} {taxi.get_l_name()}"
              f"{taxi.get_rating_list()} {taxi.get_avg()}")


taxi_change_btn = tkinter.Button(frame_taxi, text="Change", font=("Arial", 14), command=change_taxi)
taxi_change_btn.place(x=150, y=400)


def show_taxi_data():
    # Считываем индексы выделенных элементов из фронтенда
    taxi_listbox_ind = taxi_listbox.curselection()
    if len(taxi_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_taxi = taxi_listbox.get(taxi_listbox_ind[0])

        # Отдельно выделяем идентификатор
        selected_id = selected_taxi.split()[0]

        # Запрашиваем из бэкенда объект по идентификатору
        taxi = data_base.get_taxi(selected_id)
        if taxi:
            taxi_data = (f"ID: {taxi.get_id()}\nFirst Name: {taxi.get_f_name()}\nSecond Name: {taxi.get_l_name()}"
                         f"\nRatings: {taxi.get_rating_list()}\nAverage rating: {taxi.get_avg()}")
            taxi_info.config(text=taxi_data, justify="left")


taxi_info_btn = tkinter.Button(frame_taxi, text="Info", font=("Arial", 14), command=show_taxi_data)
taxi_info_btn.place(x=235, y=400)


def add_rating_to_taxi():
    # Считываем индексы выделенных элементов из фронтенда
    taxi_listbox_ind = taxi_listbox.curselection()
    if len(taxi_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_taxi = taxi_listbox.get(taxi_listbox_ind[0])

        # Считываем рейтинг
        new_rating = int(taxi_rating_entry.get())

        # Отдельно выделяем идентификатор
        selected_id = selected_taxi.split()[0]

        # Пытаемся добавить оценку через базу данных
        if data_base.add_rating(selected_id, new_rating):
            taxi = data_base.get_taxi(selected_id)
            taxi_data = (f"ID: {taxi.get_id()}\nFirst Name: {taxi.get_f_name()}\nSecond Name: {taxi.get_l_name()}"
                         f"\nRatings: {taxi.get_rating_list()}\nAverage rating: {taxi.get_avg()}")
            taxi_info.config(text=taxi_data, justify="left")

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for taxi in data_base.get_taxi_drivers():
        print(f"{taxi.get_id()} {taxi.get_f_name()} {taxi.get_l_name()}"
              f"{taxi.get_rating_list()} {taxi.get_avg()}")


taxi_add_rating_btn = tkinter.Button(frame_taxi, text="Add rating", font=("Arial", 18), command=add_rating_to_taxi)
taxi_add_rating_btn.place(x=480, y=280)


root.mainloop()
