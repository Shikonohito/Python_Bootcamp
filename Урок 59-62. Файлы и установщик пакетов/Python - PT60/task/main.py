# Используя код, указанный ниже, реализуйте в бэкенде и во фронтенде сохранение и загрузку в файл.

import tkinter
from tkinter import ttk

class Student:
    __id = str()
    __name = str()

    def __init__(self, id: str, name: str):
        self.__id = id
        self.__name = name

    def __str__(self):
        return f"{self.__id} {self.__name}"


class Teacher:
    __id = str()
    __name = str()

    def __init__(self, id: str, name: str):
        self.__id = id
        self.__name = name

    def __str__(self):
        return f"{self.__id} {self.__name}"


class Group:
    __name = str()

    def __init__(self, name: str):
        self.__name = name

    def __str__(self):
        return f"{self.__name}"


class DB:
    __students: list[Student] = list()
    __teachers: list[Teacher] = list()
    __groups: list[Group] = list()

    def __init__(self, students: list[Student] = None, teachers: list[Teacher] = None, groups: list[Group] = None):
        if students:
            self.__students = students
        else:
            self.__students: list[Student] = list()

        if teachers:
            self.__teachers = teachers
        else:
            self.__teachers: list[Teacher] = list()

        if groups:
            self.__groups = groups
        else:
            self.__groups: list[Group] = list()

    def get_students(self):
        return tuple(self.__students)

    def get_teachers(self):
        return tuple(self.__teachers)

    def get_groups(self):
        return tuple(self.__groups)

    # РЕАЛИЗУЙТЕ ЭТОТ МЕТОД
    def save_db(self, db_file_path: str):
        pass

    # РЕАЛИЗУЙТЕ ЭТОТ МЕТОД
    @staticmethod
    def load_db(db_file_path: str) -> 'DB':
        pass


student_1 = Student("S-001", "Teston")
student_2 = Student("S-025", "Bob")
student_3 = Student("S-012", "Kate")
student_list = [student_1, student_2, student_3]

teacher_1 = Teacher("T-67", "Arthur")
teacher_2 = Teacher("T-78", "Alice")
teacher_list = [teacher_1, teacher_2]

group_1 = Group("266-Python")
group_2 = Group("286-Python")
group_list = [group_1, group_2]

data_base = DB(student_list, teacher_list, group_list)

# data_base = DB()

root = tkinter.Tk()

root.title("Save and load")
root.geometry("910x480")
root.resizable(False, False)

root_menu = tkinter.Menu(root)
root.config(menu=root_menu)

# РЕАЛИЗУЙТЕ ЭТУ ФУНКЦИЮ
def save_data():
    pass

# РЕАЛИЗУЙТЕ ЭТУ ФУНКЦИЮ
def load_data():
    pass


file_menu = tkinter.Menu(root_menu, tearoff=False)
file_menu.add_command(label="Save", command=save_data)
file_menu.add_command(label="Load", command=load_data)

root_menu.add_cascade(label="File", menu=file_menu)

main_frame = tkinter.Frame(root)
main_frame.pack(expand=True, fill="both")

mf_student_listbox = tkinter.Listbox(main_frame, font=("Arial", 18), height=13)
mf_student_listbox.place(x=20, y=20)

mf_student_combobox = ttk.Combobox(main_frame, values=data_base.get_students(), font=("Arial", 18),
                                   state="readonly", width=19)
mf_student_combobox.place(x=20, y=400)


def mf_fill_student_listbox():
    mf_student_listbox.delete(0, tkinter.END)
    for student in data_base.get_students():
        mf_student_listbox.insert(tkinter.END, str(student))


mf_fill_student_listbox()


mf_teacher_listbox = tkinter.Listbox(main_frame, font=("Arial", 18), height=13)
mf_teacher_listbox.place(x=320, y=20)

mf_teacher_combobox = ttk.Combobox(main_frame, values=data_base.get_teachers(), font=("Arial", 18),
                                   state="readonly", width=19)
mf_teacher_combobox.place(x=320, y=400)


def mf_fill_teacher_listbox():
    mf_teacher_listbox.delete(0, tkinter.END)
    for teacher in data_base.get_teachers():
        mf_teacher_listbox.insert(tkinter.END, str(teacher))


mf_fill_teacher_listbox()


mf_group_listbox = tkinter.Listbox(main_frame, font=("Arial", 18), height=13)
mf_group_listbox.place(x=620, y=20)

mf_group_combobox = ttk.Combobox(main_frame, values=data_base.get_groups(), font=("Arial", 18),
                                   state="readonly", width=19)
mf_group_combobox.place(x=620, y=400)


def mf_fill_group_listbox():
    mf_group_listbox.delete(0, tkinter.END)
    for group in data_base.get_groups():
        mf_group_listbox.insert(tkinter.END, str(group))


mf_fill_group_listbox()

root.mainloop()
