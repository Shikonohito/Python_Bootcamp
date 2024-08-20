import pickle
import tkinter
from tkinter import ttk, messagebox, filedialog

class Student:
    __id = str()
    __name = str()
    __age = int()
    __gender = "M"

    def __init__(self, id: str, name: str, age: int, gender: str):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__gender = gender

    def __str__(self):
        return f"{self.__id} {self.__name}"

    def set_id(self, id: str):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age: int):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_gender(self, gender: str):
        self.__gender = gender

    def get_gender(self):
        return self.__gender


class Group:
    __name = str()
    __teachers_name = str()
    __student_list: list[Student] = list()

    def __init__(self, name: str, teachers_name: str, student_list: list[Student] = None):
        self.__name = name
        self.__teachers_name = teachers_name

        if student_list:
            self.__student_list = student_list
        else:
            self.__student_list: list[Student] = list()

    def __str__(self):
        return f"{self.__name}"

    def __get_student_index(self, student_id: str) -> int:
        found_index = -1
        for i in range(len(self.__student_list)):
            if student_id == self.__student_list[i].get_id():
                found_index = i
                break
        return found_index

    def get_student(self, student_id) -> Student | None:
        found_student = None
        found_index = self.__get_student_index(student_id)
        if found_index != -1:
            found_student = self.__student_list[found_index]
        return found_student

    def add_student(self, student: Student) -> bool:
        is_success = False
        found_index = self.__get_student_index(student.get_id())
        if found_index == -1:
            self.__student_list.append(student)
            is_success = True
        return is_success

    def remove_student(self, student_id: str) -> bool:
        is_success = False
        found_index = self.__get_student_index(student_id)
        if found_index != -1:
            del self.__student_list[found_index]
            is_success = True
        return is_success

    def get_students(self):
        return tuple(self.__student_list)

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_teachers_name(self, name: str):
        self.__teachers_name = name

    def get_teachers_name(self):
        return self.__teachers_name


class DB:
    __students: list[Student] = list()
    __groups: list[Group] = list()

    def __init__(self, students: list[Student] = None, groups: list[Group] = None):
        if students:
            self.__students = students
        else:
            self.__students = list()

        if groups:
            self.__groups = groups
        else:
            self.__groups = list()

    def get_students(self):
        return tuple(self.__students)

    def get_groups(self):
        return tuple(self.__groups)

    def __get_student_index(self, student_id: str) -> int:
        found_index = -1
        for i in range(len(self.__students)):
            if student_id == self.__students[i].get_id():
                found_index = i
                break
        return found_index

    def get_student(self, student_id) -> Student | None:
        found_student = None
        found_index = self.__get_student_index(student_id)
        if found_index != -1:
            found_student = self.__students[found_index]
        return found_student

    def add_student(self, student: Student) -> bool:
        is_success = False
        found_index = self.__get_student_index(student.get_id())
        if found_index == -1:
            self.__students.append(student)
            is_success = True
        return is_success

    def remove_student(self, student_id: str) -> bool:
        is_success = False
        found_index = self.__get_student_index(student_id)
        if found_index != -1:
            del self.__students[found_index]
            for group in self.__groups:
                group.remove_student(student_id)
            is_success = True
        return is_success

    def change_student(self, student_id: str, changed_student: Student) -> bool:
        is_success = False
        student = self.get_student(student_id)
        if student:
            changed_student_id = changed_student.get_id()
            changed_student_index = self.__get_student_index(changed_student_id)
            if changed_student_id == student_id or changed_student_index == -1:
                student.set_id(changed_student.get_id())
                student.set_name(changed_student.get_name())
                student.set_age(changed_student.get_age())
                student.set_gender(changed_student.get_gender())
                is_success = True
        return is_success

    def __get_group_index(self, group_name: str) -> int:
        found_index = -1
        for i in range(len(self.__groups)):
            if group_name == self.__groups[i].get_name():
                found_index = i
                break
        return found_index

    def get_group(self, group_name) -> Group | None:
        found_group = None
        found_index = self.__get_group_index(group_name)
        if found_index != -1:
            found_group = self.__groups[found_index]
        return found_group

    def add_group(self, group: Group) -> bool:
        is_success = False
        found_index = self.__get_group_index(group.get_name())
        if found_index == -1:
            self.__groups.append(group)
            is_success = True
        return is_success

    def remove_group(self, group_name: str) -> bool:
        is_success = False
        found_index = self.__get_group_index(group_name)
        if found_index != -1:
            del self.__groups[found_index]
            is_success = True
        return is_success

    def change_group(self, group_name: str, changed_group: Group) -> bool:
        is_success = False
        group = self.get_group(group_name)
        if group:
            changed_group_name = changed_group.get_name()
            changed_group_index = self.__get_group_index(changed_group_name)
            if changed_group_name == group_name or changed_group_index == -1:
                group.set_name(changed_group_name)
                group.set_teachers_name(changed_group.get_teachers_name())
                is_success = True
        return is_success

    def save_db(self, db_file_path: str):
        with open(db_file_path, "wb") as data_file:
            pickle.dump(self, data_file)

    @staticmethod
    def load_db(db_file_path: str) -> 'DB':
        with open(db_file_path, "rb") as data_file:
            loaded_db = pickle.load(data_file)
            return loaded_db

    def set_copy(self, other: 'DB'):
        self.__students = list(other.get_students())
        self.__groups = list(other.get_groups())



# student_1 = Student("ABC1234", "Tom", 18, "M")
# student_2 = Student("XYZ5869", "Bob", 25, "M")
# student_3 = Student("CBE1324", "Jack", 28, "M")
# student_4 = Student("XYZ1234", "Kate", 24, "F")
# student_5 = Student("RTE2345", "Jim", 16, "M")
#
# group_1 = Group("256-Python", "Teston", [student_1, student_2])
# group_2 = Group("257-Python", "Teston", [student_3])
# group_3 = Group("246-Python", "Arthur")
#
# data_base = DB()
# data_base.add_student(student_1)
# data_base.add_student(student_2)
# data_base.add_student(student_3)
# data_base.add_student(student_4)
# data_base.add_student(student_5)
#
# data_base.add_group(group_1)
# data_base.add_group(group_2)
# data_base.add_group(group_3)


data_base = DB()

root = tkinter.Tk()
root.title("Combobox and radiobutton")
root.geometry("720x480")
root.resizable(False, False)

frame_student = tkinter.Frame(root)
frame_student.pack(expand=True, fill="both")

frame_group = tkinter.Frame(root)
frame_group.pack_forget()


frame_group_details = tkinter.Frame(root)
frame_group_details.pack_forget()


def show_frame_student():
    # Скрываем всё, что не нужно
    frame_group.pack_forget()
    frame_group_details.pack_forget()

    # Показываем всё, что нужно
    frame_student.pack(fill="both", expand=True)
    root.geometry("720x480")


def show_frame_group():
    # Скрываем всё, что не нужно
    frame_student.pack_forget()
    frame_group_details.pack_forget()

    # Показываем всё, что нужно
    frame_group.pack(fill="both", expand=True)
    root.geometry("680x350")


def show_frame_group_details():
    # Скрываем всё, что не нужно
    frame_student.pack_forget()
    frame_group.pack_forget()

    # Показываем всё, что нужно
    frame_group_details.pack(fill="both", expand=True)
    root.geometry("720x480")


def close_program():
    root.quit()


def save_data():
    data_base.save_db("database01.dat")


def load_data():
    global data_base
    data_base = DB.load_db("database01.dat")

    # Обновляем виджеты для правильного отображения данных
    fs_fill_student_listbox()
    fg_fill_group_listbox()
    fgd_student_combobox["values"] = data_base.get_students()
    fgd_group_combobox["values"] = data_base.get_groups()


# def save_data():
#     filename = filedialog.asksaveasfilename(initialdir=".",
#                                             title="Select File",
#                                             filetypes=(("Data files", "*.dat"),
#                                                        ("All files", "*.*")))
#     if filename:
#         data_base.save_db(filename + ".dat")


# def load_data():
#     filename = filedialog.askopenfilename(initialdir=".",
#                                           title="Select File",
#                                           filetypes=(("Data files", "*.dat"),
#                                                      ("All files", "*.*")))
#     if filename:
#         global data_base
#         data_base = DB.load_db(filename)
#
#         # Обновляем виджеты для правильного отображения данных
#         fs_fill_student_listbox()
#         fg_fill_group_listbox()
#         fgd_student_combobox["values"] = data_base.get_students()
#         fgd_group_combobox["values"] = data_base.get_groups()


# def exit_program():
#     if messagebox.askyesno("Save Data Base", "Do you want to save data base?"):
#         save_data()
#     if messagebox.askokcancel("Quit", "Do you want to quit?"):
#         root.quit()
#
#
# root.protocol("WM_DELETE_WINDOW", exit_program)

root_menu = tkinter.Menu(root)
root.config(menu=root_menu)

file_menu = tkinter.Menu(root_menu, tearoff=False)
file_menu.add_command(label="Save", command=save_data)
file_menu.add_command(label="Load", command=load_data)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=close_program)

root_menu.add_cascade(label="File", menu=file_menu)

show_menu = tkinter.Menu(root_menu, tearoff=False)
show_menu.add_command(label="Students", command=show_frame_student)
show_menu.add_command(label="Groups", command=show_frame_group)
show_menu.add_command(label="Group details", command=show_frame_group_details)

root_menu.add_cascade(label="Show", menu=show_menu)

# BEGIN FRAME STUDENT
fs_student_listbox = tkinter.Listbox(frame_student, font=("Arial", 18), height=13)
fs_student_listbox.place(x=20, y=20)


def fs_fill_student_listbox():
    fs_student_listbox.delete(0, tkinter.END)
    for student in data_base.get_students():
        fs_student_listbox.insert(tkinter.END, str(student))


fs_fill_student_listbox()

fs_student_id_lbl = tkinter.Label(frame_student, text="ID:", font=("Arial", 18))
fs_student_id_lbl.place(x=340, y=20)

fs_student_id_entry = tkinter.Entry(frame_student, font=("Arial", 18))
fs_student_id_entry.place(x=340, y=60)

fs_student_name_lbl = tkinter.Label(frame_student, text="Name:", font=("Arial", 18))
fs_student_name_lbl.place(x=340, y=100)

fs_student_name_entry = tkinter.Entry(frame_student, font=("Arial", 18))
fs_student_name_entry.place(x=340, y=140)

fs_student_age_lbl = tkinter.Label(frame_student, text="Age:", font=("Arial", 18))
fs_student_age_lbl.place(x=340, y=180)

fs_student_age_entry = tkinter.Entry(frame_student, font=("Arial", 18), width=3)
fs_student_age_entry.place(x=340, y=220)

fs_student_gender_lbl = tkinter.Label(frame_student, text="Gender:", font=("Arial", 18))
fs_student_gender_lbl.place(x=420, y=180)

fs_student_gender_var = tkinter.StringVar()
fs_student_gender_var.set("M")
fs_student_gender_rbtn_1 = tkinter.Radiobutton(frame_student, text="Male", variable=fs_student_gender_var,
                                               value="M", font=("Arial", 18))
fs_student_gender_rbtn_2 = tkinter.Radiobutton(frame_student, text="Female", variable=fs_student_gender_var,
                                               value="F", font=("Arial", 18))
fs_student_gender_rbtn_1.place(x=420, y=220)
fs_student_gender_rbtn_2.place(x=540, y=220)

fs_student_info_lbl = tkinter.Label(frame_student, text="Student info:", font=("Arial", 18))
fs_student_info_lbl.place(x=340, y=300)

fs_student_info = tkinter.Label(frame_student, text="", font=("Arial", 18))
fs_student_info.place(x=340, y=340)


def fs_add_student():
    # Считываем данные из полей фронтенда
    new_id = fs_student_id_entry.get()
    new_name = fs_student_name_entry.get()
    new_age = int(fs_student_age_entry.get())
    new_gender = fs_student_gender_var.get()

    # Формируем из данных объект
    new_student = Student(new_id, new_name, new_age, new_gender)

    # Добавляем объект в бэкенд
    if data_base.add_student(new_student):
        # Формируем строковое представление объекта
        new_student_listbox = str(new_student)

        # Добавляем строковое представление объекта во фронтенд
        fs_student_listbox.insert(tkinter.END, new_student_listbox)

        fgd_student_combobox["values"] = data_base.get_students()


    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for student in data_base.get_students():
        print(f"{student.get_id()} {student.get_name()} {student.get_age()} {student.get_gender()}")


fs_student_add_btn = tkinter.Button(frame_student, text="New", font=("Arial", 14), command=fs_add_student)
fs_student_add_btn.place(x=20, y=400)


def fs_delete_student():
    # Считываем индексы выделенных элементов из фронтенда
    student_listbox_ind = fs_student_listbox.curselection()
    if len(student_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_student = fs_student_listbox.get(student_listbox_ind[0])

        # Отдельно выделяем идентификатор
        customer_id = selected_student.split()[0]

        # Пытаемся удалить из бэкенда
        if data_base.remove_student(customer_id):
            # Удаляем из фронтенда
            fs_student_listbox.delete(student_listbox_ind[0])
            fgd_fill_student_listbox(tuple())
            fgd_group_selected.config(text="")
            fgd_student_combobox["values"] = data_base.get_students()
            fgd_student_combobox.set("")

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for student in data_base.get_students():
        print(f"{student.get_id()} {student.get_name()} {student.get_age()} {student.get_gender()}")


fs_student_delete_btn = tkinter.Button(frame_student, text="Delete", font=("Arial", 14), command=fs_delete_student)
fs_student_delete_btn.place(x=75, y=400)


def fs_change_student():
    # Считываем индексы выделенных элементов из фронтенда
    student_listbox_ind = fs_student_listbox.curselection()
    if len(student_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_student = fs_student_listbox.get(student_listbox_ind[0])

        # Отдельно выделяем идентификатор
        selected_id = selected_student.split()[0]

        # Считываем данные из полей фронтенда
        new_id = fs_student_id_entry.get()
        new_name = fs_student_name_entry.get()
        new_age = int(fs_student_age_entry.get())
        new_gender = fs_student_gender_var.get()

        # Формируем из данных объект
        new_student = Student(new_id, new_name, new_age, new_gender)

        # Пытаемся изменить объект в бэкенде
        if data_base.change_student(selected_id, new_student):
            # Формируем строковое представление объекта
            new_student_listbox = str(new_student)

            # Изменяем данные во фронтенде
            fs_student_listbox.delete(student_listbox_ind[0])
            fs_student_listbox.insert(student_listbox_ind[0], new_student_listbox)

            fgd_student_combobox["values"] = data_base.get_students()
            fgd_student_combobox.set("")


    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for student in data_base.get_students():
        print(f"{student.get_id()} {student.get_name()} {student.get_age()} {student.get_gender()}")


fs_student_change_btn = tkinter.Button(frame_student, text="Change", font=("Arial", 14), command=fs_change_student)
fs_student_change_btn.place(x=150, y=400)


def fs_show_student_data():
    # Считываем индексы выделенных элементов из фронтенда
    student_listbox_ind = fs_student_listbox.curselection()
    if len(student_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_student = fs_student_listbox.get(student_listbox_ind[0])

        # Отдельно выделяем идентификатор
        selected_id = selected_student.split()[0]

        # Запрашиваем из бэкенда объект по идентификатору
        student = data_base.get_student(selected_id)
        if student:
            student_data = (f"ID: {student.get_id()}\nName: {student.get_name()}\nAge: {student.get_age()}"
                            f"\nGender: {student.get_gender()}")
            fs_student_info.config(text=student_data, justify="left")


fs_student_info_btn = tkinter.Button(frame_student, text="Info", font=("Arial", 14), command=fs_show_student_data)
fs_student_info_btn.place(x=235, y=400)
# END FRAME STUDENT

# BEGIN FRAME GROUP
fg_group_listbox = tkinter.Listbox(frame_group, font=("Arial", 18), height=8)
fg_group_listbox.place(x=20, y=20)


def fg_fill_group_listbox():
    fg_group_listbox.delete(0, tkinter.END)
    for group in data_base.get_groups():
        fg_group_listbox.insert(tkinter.END, str(group))


fg_fill_group_listbox()

fg_group_name_lbl = tkinter.Label(frame_group, text="Name:", font=("Arial", 18))
fg_group_name_lbl.place(x=20, y=260)

fg_group_name_entry = tkinter.Entry(frame_group, font=("Arial", 18))
fg_group_name_entry.place(x=20, y=300)

fg_group_teachers_name_lbl = tkinter.Label(frame_group, text="Teacher's name:", font=("Arial", 18))
fg_group_teachers_name_lbl.place(x=300, y=260)

fg_group_teachers_name_entry = tkinter.Entry(frame_group, font=("Arial", 18))
fg_group_teachers_name_entry.place(x=300, y=300)

fg_group_info_lbl = tkinter.Label(frame_group, text="Group info:", font=("Arial", 18))
fg_group_info_lbl.place(x=400, y=20)

fg_group_info = tkinter.Label(frame_group, text="", font=("Arial", 18))
fg_group_info.place(x=400, y=60)


def fg_add_group():
    # Считываем данные из полей фронтенда
    new_name = fg_group_name_entry.get()
    new_teachers_name = fg_group_teachers_name_entry.get()

    # Формируем из данных объект
    new_group = Group(new_name, new_teachers_name)

    # Добавляем объект в бэкенд
    if data_base.add_group(new_group):
        # Формируем строковое представление объекта
        new_group_listbox = str(new_group)

        # Добавляем строковое представление объекта во фронтенд
        fg_group_listbox.insert(tkinter.END, new_group_listbox)

        fgd_group_combobox["values"] = data_base.get_groups()

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for group in data_base.get_groups():
        print(f"{group.get_name()} {group.get_teachers_name()}")


fg_product_add_btn = tkinter.Button(frame_group, text="New", font=("Arial", 14), command=fg_add_group)
fg_product_add_btn.place(x=300, y=20)


def fg_delete_group():
    # Считываем индексы выделенных элементов из фронтенда
    group_listbox_ind = fg_group_listbox.curselection()
    if len(group_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_group = fg_group_listbox.get(group_listbox_ind[0])

        # Отдельно выделяем идентификатор
        group_name = selected_group.split()[0]

        # Пытаемся удалить из бэкенда
        if data_base.remove_group(group_name):
            # Удаляем из фронтенда
            fg_group_listbox.delete(group_listbox_ind[0])

            fgd_group_combobox["values"] = data_base.get_groups()
            fgd_group_combobox.set("")

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for group in data_base.get_groups():
        print(f"{group.get_name()} {group.get_teachers_name()}")


fg_group_delete_btn = tkinter.Button(frame_group, text="Delete", font=("Arial", 14), command=fg_delete_group)
fg_group_delete_btn.place(x=300, y=70)


def fg_change_group():
    # Считываем индексы выделенных элементов из фронтенда
    group_listbox_ind = fg_group_listbox.curselection()
    if len(group_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_group = fg_group_listbox.get(group_listbox_ind[0])

        # Отдельно выделяем идентификатор
        selected_name = selected_group.split()[0]

        # Считываем данные из полей фронтенда
        new_name = fg_group_name_entry.get()
        new_teachers_name = fg_group_teachers_name_entry.get()

        # Формируем из данных объект
        new_group = Group(new_name, new_teachers_name)

        # Пытаемся изменить объект в бэкенде
        if data_base.change_group(selected_name, new_group):
            # Формируем строковое представление объекта
            new_group_listbox = str(new_group)

            # Изменяем данные во фронтенде
            fg_group_listbox.delete(group_listbox_ind[0])
            fg_group_listbox.insert(group_listbox_ind[0], new_group_listbox)

            fgd_group_combobox["values"] = data_base.get_groups()
            fgd_group_combobox.set("")

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for group in data_base.get_groups():
        print(f"{group.get_name()} {group.get_teachers_name()}")


fg_group_change_btn = tkinter.Button(frame_group, text="Change", font=("Arial", 14), command=fg_change_group)
fg_group_change_btn.place(x=300, y=120)

def fg_show_group_data():
    # Считываем индексы выделенных элементов из фронтенда
    group_listbox_ind = fg_group_listbox.curselection()
    if len(group_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_group = fg_group_listbox.get(group_listbox_ind[0])

        # Отдельно выделяем идентификатор
        selected_name = selected_group.split()[0]

        # Запрашиваем из бэкенда объект по идентификатору
        group = data_base.get_group(selected_name)
        if group:
            group_data = f"Name: {group.get_name()}\nTeacher's name: {group.get_teachers_name()}"
            fg_group_info.config(text=group_data, justify="left")


fg_group_info_btn = tkinter.Button(frame_group, text="Info", font=("Arial", 14), command=fg_show_group_data)
fg_group_info_btn.place(x=300, y=170)
# END FRAME GROUP

# BEGIN FRAME OPERATIONS
fgd_group_lbl = tkinter.Label(frame_group_details, text="Group:", font=("Arial", 16))
fgd_group_lbl.place(x=20, y=20)
fgd_group_combobox = ttk.Combobox(frame_group_details, values=data_base.get_groups(), font=("Arial", 18), state="readonly")
fgd_group_combobox.place(x=20, y=60)

fgd_student_lbl = tkinter.Label(frame_group_details, text="Student:", font=("Arial", 16))
fgd_student_lbl.place(x=20, y=120)
fgd_student_combobox = ttk.Combobox(frame_group_details, values=data_base.get_students(), font=("Arial", 18), state="readonly")
fgd_student_combobox.place(x=20, y=160)

fgd_group_selected_lbl = tkinter.Label(frame_group_details, text="Selected:", font=("Arial", 16))
fgd_group_selected_lbl.place(x=400, y=20)
fgd_group_selected = tkinter.Label(frame_group_details, text="", font=("Arial", 16))
fgd_group_selected.place(x=500, y=20)

fgd_student_listbox = tkinter.Listbox(frame_group_details, font=("Arial", 18))
fgd_student_listbox.place(x=400, y=60)


def fgd_fill_student_listbox(students: tuple[Student, ...]):
    fgd_student_listbox.delete(0, tkinter.END)
    for student in students:
        fgd_student_listbox.insert(tkinter.END, str(student))


fgd_operations_info = tkinter.Label(frame_group_details, text="", font=("Arial", 16))
fgd_operations_info.place(x=20, y=200)


def fgd_select_group():
    group_str = fgd_group_combobox.get()
    selected_group_name = group_str.split()[0]
    selected_group = data_base.get_group(selected_group_name)
    if selected_group:
        fgd_fill_student_listbox(selected_group.get_students())
        fgd_group_selected.config(text=str(selected_group))


fgd_select_group_btn = tkinter.Button(frame_group_details, text="Select", font=("Arial", 16), command=fgd_select_group)
fgd_select_group_btn.place(x=200, y=10)


def fgd_add_student_to_group():
    group_str = fgd_group_combobox.get()
    selected_group_name = group_str.split()[0]
    selected_group = data_base.get_group(selected_group_name)

    student_str = fgd_student_combobox.get()
    selected_student_id = student_str.split()[0]
    selected_student = data_base.get_student(selected_student_id)
    if selected_group and selected_student:
        if selected_group.add_student(selected_student):
            fgd_fill_student_listbox(selected_group.get_students())
            fgd_group_selected.config(text=str(selected_group))
            fgd_operations_info.config(text="")
        else:
            fgd_operations_info.config(text="Student already in group!")

        # Для проверки соответствия наполнения бэкенда и фронтенда
        print()
        for student in selected_group.get_students():
            print(f"{student.get_id()} {student.get_name()} {student.get_age()} {student.get_gender()}")


fgd_add_student_to_group_btn = tkinter.Button(frame_group_details, text="Add", font=("Arial", 16),
                                              command=fgd_add_student_to_group)
fgd_add_student_to_group_btn.place(x=200, y=110)


def fgd_remove_student_from_group():
    selected_group_name = fgd_group_selected.cget("text")
    selected_group = data_base.get_group(selected_group_name)
    if selected_group:
        student_listbox_ind = fgd_student_listbox.curselection()
        if len(student_listbox_ind) > 0:
            # Считываем элемент по индексу
            selected_student = fgd_student_listbox.get(student_listbox_ind[0])

            # Отдельно выделяем идентификатор
            student_id = selected_student.split()[0]

            # Пытаемся удалить из бэкенда
            if selected_group.remove_student(student_id):
                # Удаляем из фронтенда
                fgd_student_listbox.delete(student_listbox_ind[0])

                fgd_student_combobox["values"] = data_base.get_groups()
                fgd_student_combobox.set("")

        # Для проверки соответствия наполнения бэкенда и фронтенда
        print()
        for student in selected_group.get_students():
            print(f"{student.get_id()} {student.get_name()} {student.get_age()} {student.get_gender()}")


fgd_remove_student_from_group_btn = tkinter.Button(frame_group_details, text="Remove", font=("Arial", 16),
                                              command=fgd_remove_student_from_group)
fgd_remove_student_from_group_btn.place(x=400, y=350)
# END FRAME OPERATIONS

root.mainloop()
