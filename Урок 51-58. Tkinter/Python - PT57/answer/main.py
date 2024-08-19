# Используя код, указанный ниже, оформите задний фон фреймов,
# реализуйте проверки полей и оповещения о результатах работы кнопок.

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
            self.__grades: list[int] = list()

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

    def __get_student_index(self, student_id: str):
        found_index = -1
        for i in range(len(self.__student_list)):
            if student_id == self.__student_list[i].get_id():
                found_index = i
                break
        return found_index

    def get_student(self, student_id: str) -> None | Student:
        index = self.__get_student_index(student_id)
        if index != -1:
            student = self.__student_list[index]
        else:
            student = None
        return student

    def add_student(self, student: Student):
        is_success = False
        index = self.__get_student_index(student.get_id())
        if index == -1:
            self.__student_list.append(student)
            is_success = True
        return is_success

    def remove_student_by_id(self, student_id: str):
        is_success = False
        index = self.__get_student_index(student_id)
        if index != -1:
            del self.__student_list[index]
            is_success = True
        return is_success

    def change_student(self, student_id: str, changed_student: Student):
        is_success = False
        student = self.get_student(student_id)
        if student:
            changed_student_id = changed_student.get_id()
            changed_student_index = self.__get_student_index(changed_student_id)
            if student_id == changed_student_id or changed_student_index == -1:
                student.set_id(changed_student.get_id())
                student.set_name(changed_student.get_name())
                is_success = True
        return is_success


import tkinter
from tkinter import ttk

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

root.iconbitmap(default="img/python.ico")
# OR
# icon = tkinter.PhotoImage(file="img/python.gif")
# root.iconphoto(False, icon)  # Первый аргумент отвечает за установку иконки на все окна

frame_student = tkinter.Frame(root)
frame_student.pack(expand=True, fill="both")

frame_student_bg_img = tkinter.PhotoImage(file="img/students_resized.gif")
frame_student_bg = tkinter.Label(frame_student, image=frame_student_bg_img)
frame_student_bg.place(x=0, y=0)

frame_grades = tkinter.Frame(root)
frame_grades.pack_forget()

frame_grades_bg_img = tkinter.PhotoImage(file="img/grades_resized.gif")
frame_grades_bg = tkinter.Label(frame_grades, image=frame_grades_bg_img)
frame_grades_bg.place(x=0, y=0)


def show_students():
    # Скрываем всё, что не нужно
    frame_grades.pack_forget()

    # Изменяем размеры окна, если хотим
    root.geometry("720x480")

    # Показываем всё, что требуется показать
    frame_student.pack(fill="both", expand=True)


def show_grades():
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
show_menu.add_command(label="Students", command=show_students)
show_menu.add_command(label="Grades", command=show_grades)
show_menu.add_separator()
show_menu.add_command(label="Exit", command=close_program)
root_menu.add_cascade(label="Show", menu=show_menu)


# BEGIN FRAME STUDENT
fs_student_listbox = tkinter.Listbox(frame_student, font=("Arial", 18), height=13)
fs_student_listbox.place(x=20, y=20)


def fill_student_listbox():
    fs_student_listbox.delete(0, tkinter.END)
    for student in data_base.get_students():
        fs_student_listbox.insert(tkinter.END, str(student))


fill_student_listbox()

fs_student_id_lbl = tkinter.Label(frame_student, text="ID:", font=("Arial", 18))
fs_student_id_lbl.place(x=340, y=20)

fs_student_id_notify = tkinter.Label(frame_student, text="", font=("Arial", 18), fg="red")
fs_student_id_notify.place(x=400, y=20)

fs_student_id_entry = tkinter.Entry(frame_student, font=("Arial", 18))
fs_student_id_entry.place(x=340, y=60)

fs_student_name_lbl = tkinter.Label(frame_student, text="Name:", font=("Arial", 18))
fs_student_name_lbl.place(x=340, y=100)

fs_student_name_notify = tkinter.Label(frame_student, text="", font=("Arial", 18), fg="red")
fs_student_name_notify.place(x=440, y=100)

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

    is_all_checked = True

    if new_id == "":
        fs_student_id_notify.config(text="Enter id!")
        is_all_checked = False
    else:
        fs_student_id_notify.config(text="")

    if new_name == "":
        fs_student_name_notify.config(text="Enter name!")
        is_all_checked = False
    else:
        fs_student_name_notify.config(text="")

    if is_all_checked:
        # Формируем из данных объект
        new_student = Student(new_id, new_name)

        # Добавляем объект в бэкенд
        if data_base.add_student(new_student):
            # Формируем строковое представление объекта
            new_student_listbox = str(new_student)

            # Добавляем строковое представление объекта во фронтенд
            fs_student_listbox.insert(tkinter.END, new_student_listbox)

            fg_student_combobox["values"] = data_base.get_students()

            fs_student_info.config(text="Student added.", fg="green")

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for student in data_base.get_students():
        print(student)


fs_student_add_btn = tkinter.Button(frame_student, text="New", font=("Arial", 14), command=fs_add_student)
fs_student_add_btn.place(x=20, y=400)


def fs_delete_student():
    # Считываем индексы выделенных элементов из фронтенда
    student_listbox_ind = fs_student_listbox.curselection()
    if len(student_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_student = fs_student_listbox.get(student_listbox_ind[0])

        # Отдельно выделяем идентификатор
        student_id = selected_student.split()[0]

        # Пытаемся удалить из бэкенда
        if data_base.remove_student_by_id(student_id):
            # Удаляем из фронтенда
            fs_student_listbox.delete(student_listbox_ind[0])

            fg_student_combobox["values"] = data_base.get_students()

            fs_student_info.config(text="Student deleted.", fg="green")
    else:
        fs_student_info.config(text="Select student to delete!", fg="red")

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for student in data_base.get_students():
        print(student)


fs_student_delete_btn = tkinter.Button(frame_student, text="Delete", font=("Arial", 14), command=fs_delete_student)
fs_student_delete_btn.place(x=75, y=400)


def change_student():
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

        is_all_checked = True

        if new_id == "":
            fs_student_id_notify.config(text="Enter id!")
            is_all_checked = False
        else:
            fs_student_id_notify.config(text="")

        if new_name == "":
            fs_student_name_notify.config(text="Enter name!")
            is_all_checked = False
        else:
            fs_student_name_notify.config(text="")

        if is_all_checked:
            # Формируем из данных объект
            new_student = Student(new_id, new_name)

            # Пытаемся изменить объект в бэкенде
            if data_base.change_student(selected_id, new_student):
                # Формируем строковое представление объекта
                new_student_listbox = str(new_student)

                # Изменяем данные во фронтенде
                fs_student_listbox.delete(student_listbox_ind[0])
                fs_student_listbox.insert(student_listbox_ind[0], new_student_listbox)

                # Обновляем фронтенд для корректного отображения
                fg_student_combobox["values"] = data_base.get_students()
                fg_student_combobox.set("")
                fg_selected_student_info.config(text="", justify="left")
                fg_grades_listbox.delete(0, tkinter.END)

                fs_student_info.config(text="Student data changed.", fg="green")

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for student in data_base.get_students():
        print(student)


fs_student_change_btn = tkinter.Button(frame_student, text="Change", font=("Arial", 14), command=change_student)
fs_student_change_btn.place(x=150, y=400)


def show_student_data():
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
            student_data = f"ID: {student.get_id()}\nName: {student.get_name()}"
            fs_student_info.config(text=student_data, justify="left", fg="black")


fs_student_info_btn = tkinter.Button(frame_student, text="Info", font=("Arial", 14), command=show_student_data)
fs_student_info_btn.place(x=235, y=400)

# def fill_student_info(event):
#     student_listbox_ind = fs_student_listbox.curselection()
#     if len(student_listbox_ind) > 0:
#         selected_student = fs_student_listbox.get(student_listbox_ind[0])
#         selected_id = selected_student.split()[0]
#         student = data_base.get_student(selected_id)
#         if student:
#             fs_student_id_entry.delete(0, tkinter.END)
#             fs_student_id_entry.insert(0, student.get_id())
#             fs_student_name_entry.delete(0, tkinter.END)
#             fs_student_name_entry.insert(0, student.get_name())
#
#
# fs_student_listbox.bind("<<ListboxSelect>>", fill_student_info)

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

fg_student_grade_notify = tkinter.Label(frame_grades, text="", font=("Arial", 16), fg="red")
fg_student_grade_notify.place(x=150, y=100)


def fill_grades_listbox(student: Student):
    fg_grades_listbox.delete(0, tkinter.END)
    for grade in student.get_grades():
        fg_grades_listbox.insert(tkinter.END, str(grade))


# def show_grades_event(event):
#     student_str = fg_student_combobox.get()
#     fg_selected_student_info.config(text=f"{student_str}", justify="left")
#
#     student_str_id = student_str.split()[0]
#     student = data_base.get_student(student_str_id)
#
#     if student:
#         fill_grades_listbox(student)
#
#
# fg_student_combobox.bind("<<ComboboxSelected>>", show_grades_event)


def show_grades():
    student_str = fg_student_combobox.get()
    fg_selected_student_info.config(text=f"{student_str}", justify="left")

    student_str_id = student_str.split()[0]
    student = data_base.get_student(student_str_id)

    if student:
        fill_grades_listbox(student)


fg_show_grades_btn = tkinter.Button(frame_grades, text="Show grades", font=("Arial", 16), command=show_grades)
fg_show_grades_btn.place(x=400, y=430)


def fg_add_grade():
    grade = fg_student_grade_entry.get()
    is_all_correct = True
    if not grade.isnumeric():
        fg_student_grade_notify.config(text="Grade must be num!", fg="red")
        is_all_correct = False
    else:
        grade = int(grade)
        if grade < 0 or grade > 12:
            fg_student_grade_notify.config(text="Grade must be [1, 12]!", fg="red")
            is_all_correct = False

    student_str = fg_student_combobox.get()
    if not student_str:
        fg_student_grade_notify.config(text="Select student!", fg="red")
        is_all_correct = False

    if is_all_correct:
        student_str_id = student_str.split()[0]
        student = data_base.get_student(student_str_id)

        if student:
            student.add_grade(grade)
            show_grades()
            fg_student_grade_notify.config(text="Grade added.", fg="green")


fg_add_grades_btn = tkinter.Button(frame_grades, text="Add grade", font=("Arial", 16), command=fg_add_grade)
fg_add_grades_btn.place(x=20, y=140)

# END FRAME OPERATIONS

root.mainloop()
