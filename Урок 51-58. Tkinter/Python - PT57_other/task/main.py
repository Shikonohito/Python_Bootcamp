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


import tkinter
from tkinter import ttk

student_1 = Student("ABC1234", "Tom", [12, 10, 12])
student_2 = Student("XYZ5869", "Bob", [12, 12, 12])
student_3 = Student("CBE1324", "Tom", [11, 10, 12])
student_4 = Student("XYZ1234", "Kate", [10, 10, 11])
student_5 = Student("RTE2345", "Jim", [9, 11, 11])

student_list = [student_1, student_2, student_3, student_4, student_5]

root = tkinter.Tk()
root.title("Frames and Menu")
root.geometry("720x480")
root.resizable(False, False)

frame_student = tkinter.Frame(root)
frame_student.pack(expand=True, fill="both")

frame_grades = tkinter.Frame(root)
frame_grades.pack_forget()


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
    for student in student_list:
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

    if is_all_checked:
        # Формируем из данных объект
        new_student = Student(new_id, new_name)

        # Добавляем объект в бэкенд
        student_list.append(new_student)

        # Формируем строковое представление объекта
        new_student_listbox = str(new_student)

        # Добавляем строковое представление объекта во фронтенд
        fs_student_listbox.insert(tkinter.END, new_student_listbox)

        # Обновляем комбобокс
        fg_student_combobox["values"] = student_list


fs_student_add_btn = tkinter.Button(frame_student, text="New", font=("Arial", 14), command=fs_add_student)
fs_student_add_btn.place(x=20, y=400)


def fs_delete_student():
    # Считываем индексы выделенных элементов из фронтенда
    student_listbox_ind = fs_student_listbox.curselection()
    if len(student_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_student_index = student_listbox_ind[0]

        # Пытаемся удалить из бэкенда
        student_list.pop(selected_student_index)

        # Удаляем из фронтенда
        fs_student_listbox.delete(student_listbox_ind[0])

        # Обновляем комбобокс
        fg_student_combobox["values"] = student_list


fs_student_delete_btn = tkinter.Button(frame_student, text="Delete", font=("Arial", 14), command=fs_delete_student)
fs_student_delete_btn.place(x=75, y=400)


def show_student_data():
    # Считываем индексы выделенных элементов из фронтенда
    student_listbox_ind = fs_student_listbox.curselection()
    if len(student_listbox_ind) > 0:
        # Считываем элемент по индексу
        selected_student_index = student_listbox_ind[0]

        # Запрашиваем из бэкенда объект
        student = student_list[selected_student_index]

        # Формируем строковое представление для отображение в лейбле
        student_data = f"ID: {student.get_id()}\nName: {student.get_name()}"
        fs_student_info.config(text=student_data, justify="left", fg="black")


fs_student_info_btn = tkinter.Button(frame_student, text="Info", font=("Arial", 14), command=show_student_data)
fs_student_info_btn.place(x=235, y=400)
# END FRAME STUDENT

# BEGIN FRAME GRADES
fg_student_lbl = tkinter.Label(frame_grades, text="Student:", font=("Arial", 16))
fg_student_lbl.place(x=20, y=20)
fg_student_combobox = ttk.Combobox(frame_grades, values=student_list, font=("Arial", 18), state="readonly")
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


def show_grades():
    student_str = fg_student_combobox.get()
    fg_selected_student_info.config(text=f"{student_str}", justify="left")

    student_index = fg_student_combobox.current()
    student = student_list[student_index]

    fill_grades_listbox(student)


fg_show_grades_btn = tkinter.Button(frame_grades, text="Show grades", font=("Arial", 16), command=show_grades)
fg_show_grades_btn.place(x=400, y=430)


def fg_add_grade():
    grade = fg_student_grade_entry.get()

    student_index = fg_student_combobox.current()
    student = student_list[student_index]

    student.add_grade(int(grade))
    show_grades()


fg_add_grades_btn = tkinter.Button(frame_grades, text="Add grade", font=("Arial", 16), command=fg_add_grade)
fg_add_grades_btn.place(x=20, y=140)

# END FRAME OPERATIONS

root.mainloop()
