# Дополните код, указанный ниже, так, чтобы для студента можно было выбрать пол
# с помощью радиокнопки на первом фрейме.
# Также реализуйте выбор группы и выбор студента через комбобоксы на третьем фрейме,
# с возможностью добавить студента в группу и показать студентов выбранной группы.


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

    def get_students(self):
        return self.__student_list

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_teachers_name(self, name: str):
        self.__teachers_name = name

    def get_teachers_name(self):
        return self.__teachers_name


import tkinter
from tkinter import ttk

student_1 = Student("ABC1234", "Tom", 18, "M")
student_2 = Student("XYZ5869", "Bob", 25, "M")
student_3 = Student("CBE1324", "Jack", 28, "M")
student_4 = Student("XYZ1234", "Kate", 24, "F")
student_5 = Student("RTE2345", "Jim", 16, "M")

group_1 = Group("256-Python", "Teston", [student_1, student_2])
group_2 = Group("257-Python", "Teston", [student_3])
group_3 = Group("246-Python", "Arthur")

student_list = [student_1, student_2, student_3, student_4, student_5]
group_list = [group_1, group_2, group_3]

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


root_menu = tkinter.Menu(root)
root.config(menu=root_menu)
show_menu = tkinter.Menu(root_menu, tearoff=False)
show_menu.add_command(label="Students", command=show_frame_student)
show_menu.add_command(label="Groups", command=show_frame_group)
show_menu.add_command(label="Group details", command=show_frame_group_details)
show_menu.add_separator()
show_menu.add_command(label="Exit", command=close_program)
root_menu.add_cascade(label="Show", menu=show_menu)

# BEGIN FRAME STUDENT
fs_student_listbox = tkinter.Listbox(frame_student, font=("Arial", 18), height=13)
fs_student_listbox.place(x=20, y=20)


def fs_fill_student_listbox():
    fs_student_listbox.delete(0, tkinter.END)
    for student in student_list:
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
    student_list.append(new_student)

    # Формируем строковое представление объекта
    new_student_listbox = str(new_student)

    # Добавляем строковое представление объекта во фронтенд
    fs_student_listbox.insert(tkinter.END, new_student_listbox)

    # Обновляем комбобокс
    fgd_student_combobox["values"] = student_list


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

        # Обновляем коллекции фронтенда
        fgd_fill_student_listbox(tuple())
        fgd_group_selected.config(text="")
        fgd_student_combobox["values"] = student_list
        fgd_student_combobox.set("")


fs_student_delete_btn = tkinter.Button(frame_student, text="Delete", font=("Arial", 14), command=fs_delete_student)
fs_student_delete_btn.place(x=75, y=400)


def fs_show_student_data():
    # Считываем индексы выделенных элементов из фронтенда
    student_listbox_ind = fs_student_listbox.curselection()
    if len(student_listbox_ind) > 0:
        # Считываем индекс
        selected_student_index = student_listbox_ind[0]

        # Запрашиваем из бэкенда объект
        student = student_list[selected_student_index]

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
    for group in group_list:
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
    group_list.append(new_group)

    # Формируем строковое представление объекта
    new_group_listbox = str(new_group)

    # Добавляем строковое представление объекта во фронтенд
    fg_group_listbox.insert(tkinter.END, new_group_listbox)

    # Обновляем комбобокс
    fgd_group_combobox["values"] = group_list


fg_product_add_btn = tkinter.Button(frame_group, text="New", font=("Arial", 14), command=fg_add_group)
fg_product_add_btn.place(x=300, y=20)


def fg_delete_group():
    # Считываем индексы выделенных элементов из фронтенда
    group_listbox_ind = fg_group_listbox.curselection()
    if len(group_listbox_ind) > 0:
        # Считываем индекс
        selected_group_index = group_listbox_ind[0]

        # Пытаемся удалить из бэкенда
        group_list.pop(selected_group_index)

        # Удаляем из фронтенда
        fg_group_listbox.delete(group_listbox_ind[0])

        # Обновляем комбобокс
        fgd_group_combobox["values"] = group_list
        fgd_group_combobox.set("")


fg_group_delete_btn = tkinter.Button(frame_group, text="Delete", font=("Arial", 14), command=fg_delete_group)
fg_group_delete_btn.place(x=300, y=70)


def fg_show_group_data():
    # Считываем индексы выделенных элементов из фронтенда
    group_listbox_ind = fg_group_listbox.curselection()
    if len(group_listbox_ind) > 0:
        # Считываем индекс
        selected_group_index = group_listbox_ind[0]

        # Запрашиваем из бэкенда объект
        group = group_list[selected_group_index]

        group_data = f"Name: {group.get_name()}\nTeacher's name: {group.get_teachers_name()}"
        fg_group_info.config(text=group_data, justify="left")


fg_group_info_btn = tkinter.Button(frame_group, text="Info", font=("Arial", 14), command=fg_show_group_data)
fg_group_info_btn.place(x=300, y=170)
# END FRAME GROUP

# BEGIN FRAME OPERATIONS
fgd_group_lbl = tkinter.Label(frame_group_details, text="Group:", font=("Arial", 16))
fgd_group_lbl.place(x=20, y=20)
fgd_group_combobox = ttk.Combobox(frame_group_details, values=group_list, font=("Arial", 18), state="readonly")
fgd_group_combobox.place(x=20, y=60)

fgd_student_lbl = tkinter.Label(frame_group_details, text="Student:", font=("Arial", 16))
fgd_student_lbl.place(x=20, y=120)
fgd_student_combobox = ttk.Combobox(frame_group_details, values=student_list, font=("Arial", 18), state="readonly")
fgd_student_combobox.place(x=20, y=160)

fgd_group_selected_lbl = tkinter.Label(frame_group_details, text="Selected:", font=("Arial", 16))
fgd_group_selected_lbl.place(x=400, y=20)
fgd_group_selected = tkinter.Label(frame_group_details, text="", font=("Arial", 16))
fgd_group_selected.place(x=500, y=20)

fgd_student_listbox = tkinter.Listbox(frame_group_details, font=("Arial", 18))
fgd_student_listbox.place(x=400, y=60)


def fgd_fill_student_listbox(students: list[Student]):
    fgd_student_listbox.delete(0, tkinter.END)
    for student in students:
        fgd_student_listbox.insert(tkinter.END, str(student))


fgd_operations_info = tkinter.Label(frame_group_details, text="TEST", font=("Arial", 16))
fgd_operations_info.place(x=20, y=200)

selected_group = None


def fgd_select_group():
    global selected_group
    group_index = fgd_group_combobox.current()
    selected_group = group_list[group_index]

    fgd_fill_student_listbox(selected_group.get_students())
    fgd_group_selected.config(text=str(selected_group))


fgd_select_group_btn = tkinter.Button(frame_group_details, text="Select", font=("Arial", 16), command=fgd_select_group)
fgd_select_group_btn.place(x=200, y=10)


def fgd_add_student_to_group():
    student_index = fgd_student_combobox.current()
    selected_student = student_list[student_index]

    if selected_group:
        group_students = selected_group.get_students()
        group_students.append(selected_student)

        fgd_fill_student_listbox(group_students)
        fgd_group_selected.config(text=str(selected_group))
        fgd_operations_info.config(text="")


fgd_add_student_to_group_btn = tkinter.Button(frame_group_details, text="Add", font=("Arial", 16),
                                              command=fgd_add_student_to_group)
fgd_add_student_to_group_btn.place(x=200, y=110)


def fgd_remove_student_from_group():
    global selected_group
    if selected_group:
        student_listbox_ind = fgd_student_listbox.curselection()
        selected_student_index = student_listbox_ind[0]

        group_students = selected_group.get_students()
        group_students.pop(selected_student_index)

        # Удаляем из фронтенда
        fgd_student_listbox.delete(selected_student_index)


fgd_remove_student_from_group_btn = tkinter.Button(frame_group_details, text="Remove", font=("Arial", 16),
                                              command=fgd_remove_student_from_group)
fgd_remove_student_from_group_btn.place(x=400, y=350)
# END FRAME OPERATIONS

root.mainloop()
