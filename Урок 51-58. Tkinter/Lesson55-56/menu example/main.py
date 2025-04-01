# ==============================================LESSON55-56==============================================
# Использование виджета Frame и Menu.
import tkinter
from tkinter import ttk

class Student:
    __id = ""
    __name = ""
    __grades: list[int] = list()

    def __init__(self, id: str, name: str, grades: list[int] = None):
        self.__id = id
        self.__name = name.title()
        if grades:
            self.__grades = grades
        else:
            self.__grades = list()

    def __str__(self):
        result = f"{self.__id} {self.__name}"
        return result

    def set_id(self, id: str):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_grades(self, grades: list[int]):
        self.__grades = grades

    def get_grades(self):
        return tuple(self.__grades)

    def add_grade(self, grade: int) -> bool:
        is_success = False
        if 1 <= grade and grade <= 12:
            self.__grades.append(grade)
            is_success = True
        return is_success


class DB:
    __student_list: list[Student] = list()

    def __init__(self):
        self.__student_list: list[Student] = list()

    def set_students(self, student_list: list[Student]):
        self.__student_list = student_list

    def get_students(self):
        return tuple(self.__student_list)

    def get_student_index(self, student_id: str):
        found_index = -1
        for i in range(len(self.__student_list)):
            if student_id == self.__student_list[i].get_id():
                found_index = i
                break
        return found_index

    def get_student(self, student_id: str) -> None | Student:
        index = self.get_student_index(student_id)
        if index != -1:
            student = self.__student_list[index]
        else:
            student = None
        return student

    def add_student(self, student: Student):
        is_success = False
        index = self.get_student_index(student.get_id())
        if index == -1:
            self.__student_list.append(student)
            is_success = True
        return is_success

    def remove_student_by_id(self, student_id: str):
        is_success = False
        index = self.get_student_index(student_id)
        if index != -1:
            del self.__student_list[index]
            is_success = True
        return is_success

    def change_student(self, student_id: str, changed_student: Student):
        is_success = False
        student = self.get_student(student_id)
        if student:
            changed_student_id = changed_student.get_id()
            changed_student_index = self.get_student_index(changed_student_id)
            if student_id == changed_student_id or changed_student_index == -1:
                student.set_id(changed_student.get_id())
                student.set_name(changed_student.get_name())
                is_success = True
        return is_success


student_1 = Student("ABC1234", "Tom", [12, 10, 12])
student_2 = Student("XYZ5869", "Bob", [12, 12, 12])
student_3 = Student("CBE1324", "Tom", [11, 10, 12])
student_4 = Student("XYZ1234", "Kate", [10, 10, 11])
student_5 = Student("RTE2345", "Jim", [9, 11, 11])

data_base = DB()
data_base.add_student(student_1)
data_base.add_student(student_2)
data_base.add_student(student_3)
data_base.add_student(student_4)
data_base.add_student(student_5)

root = tkinter.Tk()
root.title("Frames and Menu")
root.geometry("720x480")
root.resizable(False, False)

frame_student = tkinter.Frame(root)
frame_student.pack(expand=True, fill="both")

frame_grades = tkinter.Frame(root)
frame_grades.pack_forget()


def show_frame_students():
    # Скрываем всё, что не нужно
    frame_grades.pack_forget()

    # Изменяем размеры окна, если хотим
    root.geometry("720x480")

    # Показываем всё, что требуется показать
    frame_student.pack(fill="both", expand=True)


def show_frame_grades():
    # Скрываем всё, что не нужно
    frame_student.pack_forget()

    # Изменяем размеры окна, если хотим
    root.geometry("720x480")

    # Показываем всё, что нужно
    frame_grades.pack(fill="both", expand=True)


def close_program():
    root.quit()


root_menu = tkinter.Menu(root)
root.config(menu=root_menu)
show_menu = tkinter.Menu(root_menu, tearoff=False)
show_menu.add_command(label="Students", command=show_frame_students)
show_menu.add_command(label="Grades", command=show_frame_grades)
show_menu.add_separator()
show_menu.add_command(label="Exit", command=close_program)
root_menu.add_cascade(label="Show", menu=show_menu)


# BEGIN FRAME STUDENT
fs_student_listbox = tkinter.Listbox(frame_student, font=("Arial", 18), height=13)
fs_student_listbox.place(x=20, y=20)


def refresh_fs_student_listbox():
    fs_student_listbox.delete(0, tkinter.END)
    for student in data_base.get_students():
        fs_student_listbox.insert(tkinter.END, str(student))


refresh_fs_student_listbox()

fs_student_id_lbl = tkinter.Label(frame_student, text="ID:", font=("Arial", 18))
fs_student_id_lbl.place(x=340, y=20)

fs_student_id_entry = tkinter.Entry(frame_student, font=("Arial", 18))
fs_student_id_entry.place(x=340, y=60)

fs_student_name_lbl = tkinter.Label(frame_student, text="Name:", font=("Arial", 18))
fs_student_name_lbl.place(x=340, y=100)

fs_student_name_entry = tkinter.Entry(frame_student, font=("Arial", 18))
fs_student_name_entry.place(x=340, y=140)

fs_student_info_lbl = tkinter.Label(frame_student, text="User info:", font=("Arial", 18))
fs_student_info_lbl.place(x=340, y=300)

fs_student_info = tkinter.Label(frame_student, text="", font=("Arial", 18))
fs_student_info.place(x=340, y=340)


def fs_add_student():
    # Считываем данные из полей фронтенда
    new_id = fs_student_id_entry.get()
    new_name = fs_student_name_entry.get()

    # Формируем из данных объект
    new_student = Student(new_id, new_name)

    # Добавляем объект в бэкенд
    if data_base.add_student(new_student):
        # На фрейме студента обновляем листбокс
        refresh_fs_student_listbox()

        # На фрейме оценок обновляем комбобокс
        fg_student_combobox["values"] = data_base.get_students()

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for student in data_base.get_students():
        print(student)


fs_student_add_btn = tkinter.Button(frame_student, text="New", font=("Arial", 14), command=fs_add_student)
fs_student_add_btn.place(x=20, y=400)


def fs_delete_student():
    # Считываем индексы выделенных элементов из фронтенда
    selected_student_indexes = fs_student_listbox.curselection()
    if len(selected_student_indexes) > 0:
        # Выделяем в переменную индекс выбранного элемента
        selected_student_index = selected_student_indexes[0]

        # Считываем элемент по индексу
        selected_student_str = fs_student_listbox.get(selected_student_index)

        # Отдельно выделяем идентификатор
        selected_student_id = selected_student_str.split()[0]

        # Пытаемся удалить из бэкенда
        if data_base.remove_student_by_id(selected_student_id):
            # На фрейме студента обновляем листбокс
            refresh_fs_student_listbox()

            # На фрейме оценок обновляем комбобокс
            fg_student_combobox["values"] = data_base.get_students()

            # На фрейме оценок выставляем в комбобокс пустую строку
            fg_student_combobox.set("")

            # На фрейме оценок обновляем текст выбранного студента
            fg_selected_student_info.config(text="", justify="left")

            # На фрейме оценок обновляем листбокс оценок студента
            fg_grades_listbox.delete(0, tkinter.END)

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for student in data_base.get_students():
        print(student)


fs_student_delete_btn = tkinter.Button(frame_student, text="Delete", font=("Arial", 14), command=fs_delete_student)
fs_student_delete_btn.place(x=75, y=400)


def fs_change_student():
    # Считываем индексы выделенных элементов из фронтенда
    selected_student_indexes = fs_student_listbox.curselection()
    if len(selected_student_indexes) > 0:
        # Выделяем в переменную индекс выбранного элемента
        selected_student_index = selected_student_indexes[0]

        # Считываем элемент по индексу
        selected_student_str = fs_student_listbox.get(selected_student_index)

        # Отдельно выделяем идентификатор
        selected_student_id = selected_student_str.split()[0]

        # Считываем данные из полей фронтенда
        new_id = fs_student_id_entry.get()
        new_name = fs_student_name_entry.get()

        # Формируем из данных объект
        new_student = Student(new_id, new_name)

        # Пытаемся изменить объект в бэкенде
        if data_base.change_student(selected_student_id, new_student):
            # На фрейме студента обновляем листбокс
            refresh_fs_student_listbox()

            # На фрейме оценок обновляем комбобокс
            fg_student_combobox["values"] = data_base.get_students()

            # На фрейме оценок выставляем в комбобокс пустую строку
            fg_student_combobox.set("")

            # На фрейме оценок обновляем текст выбранного студента
            fg_selected_student_info.config(text="", justify="left")

            # На фрейме оценок обновляем листбокс оценок студента
            fg_grades_listbox.delete(0, tkinter.END)

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for student in data_base.get_students():
        print(student)


fs_student_change_btn = tkinter.Button(frame_student, text="Change", font=("Arial", 14), command=fs_change_student)
fs_student_change_btn.place(x=150, y=400)


def fs_show_student_data():
    # Считываем индексы выделенных элементов из фронтенда
    selected_student_indexes = fs_student_listbox.curselection()
    if len(selected_student_indexes) > 0:
        # Выделяем в переменную индекс выбранного элемента
        selected_student_index = selected_student_indexes[0]

        # Считываем элемент по индексу
        selected_student_str = fs_student_listbox.get(selected_student_index)

        # Отдельно выделяем идентификатор
        selected_student_id = selected_student_str.split()[0]

        # Запрашиваем из бэкенда объект по идентификатору
        selected_student = data_base.get_student(selected_student_id)
        if selected_student:
            student_data = f"ID: {selected_student.get_id()}\nName: {selected_student.get_name()}"
            fs_student_info.config(text=student_data, justify="left")


fs_student_info_btn = tkinter.Button(frame_student, text="Info", font=("Arial", 14), command=fs_show_student_data)
fs_student_info_btn.place(x=235, y=400)

# def fs_fill_student_info(event):
#     selected_student_indexes = fs_student_listbox.curselection()
#     if len(selected_student_indexes) > 0:
#         selected_student_str = fs_student_listbox.get(selected_student_indexes[0])
#         selected_student_id = selected_student_str.split()[0]
#         selected_student = data_base.get_student(selected_student_id)
#         if selected_student:
#             fs_student_id_entry.delete(0, tkinter.END)
#             fs_student_id_entry.insert(0, selected_student.get_id())
#             fs_student_name_entry.delete(0, tkinter.END)
#             fs_student_name_entry.insert(0, selected_student.get_name())
#
#
# fs_student_listbox.bind("<<ListboxSelect>>", fs_fill_student_info)

# END FRAME STUDENT

# BEGIN FRAME GRADES
fg_student_lbl = tkinter.Label(frame_grades, text="Student:", font=("Arial", 16))
fg_student_lbl.place(x=20, y=20)
fg_student_combobox = ttk.Combobox(frame_grades, values=data_base.get_students(), font=("Arial", 18), state="readonly")
fg_student_combobox.place(x=20, y=60)

fg_selected_student_info_lbl = tkinter.Label(frame_grades, text="Student:", font=("Arial", 16))
fg_selected_student_info_lbl.place(x=400, y=20)
fg_selected_student_info = tkinter.Label(frame_grades, text="", font=("Arial", 16))
fg_selected_student_info.place(x=480, y=20)

fg_grades_listbox = tkinter.Listbox(frame_grades, font=("Arial", 18), height=13)
fg_grades_listbox.place(x=400, y=60)

fg_student_grade_lbl = tkinter.Label(frame_grades, text="Grade:", font=("Arial", 16))
fg_student_grade_lbl.place(x=20, y=100)
fg_student_grade_entry = tkinter.Entry(frame_grades, width=3, font=("Arial", 16))
fg_student_grade_entry.place(x=100, y=100)


def refresh_fg_grades_listbox(student: Student):
    fg_grades_listbox.delete(0, tkinter.END)
    for grade in student.get_grades():
        fg_grades_listbox.insert(tkinter.END, str(grade))


# def fg_show_grades_event(event):
#     selected_student_str = fg_student_combobox.get()
#     fg_selected_student_info.config(text=f"{selected_student_str}", justify="left")
#
#     selected_student_id = selected_student_str.split()[0]
#     selected_student = data_base.get_student(selected_student_id)
#
#     if selected_student:
#         refresh_fg_grades_listbox(selected_student)
#
#
# fg_student_combobox.bind("<<ComboboxSelected>>", fg_show_grades_event)


def fg_show_grades():
    selected_student_str = fg_student_combobox.get()
    fg_selected_student_info.config(text=f"{selected_student_str}", justify="left")

    selected_student_id = selected_student_str.split()[0]
    selected_student = data_base.get_student(selected_student_id)

    if selected_student:
        refresh_fg_grades_listbox(selected_student)


fg_show_grades_btn = tkinter.Button(frame_grades, text="Show grades", font=("Arial", 16), command=fg_show_grades)
fg_show_grades_btn.place(x=400, y=430)


def fg_add_grade():
    grade = int(fg_student_grade_entry.get())
    selected_student_str = fg_student_combobox.get()
    selected_student_id = selected_student_str.split()[0]
    selected_student = data_base.get_student(selected_student_id)

    if selected_student:
        selected_student.add_grade(grade)
        show_grades()


fg_add_grades_btn = tkinter.Button(frame_grades, text="Add grade", font=("Arial", 16), command=fg_add_grade)
fg_add_grades_btn.place(x=20, y=140)

# END FRAME OPERATIONS

root.mainloop()

# ====================================================================================================
# Python - PT55-56
# ====================================================================================================
