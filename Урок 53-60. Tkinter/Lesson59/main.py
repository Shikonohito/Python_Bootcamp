# ==============================================LESSON59==============================================
# Добавление картинки. Виджеты.
# https://imageresizer.com/

import tkinter
from tkinter import ttk

class Student:
    __id = ""
    __name = ""

    def __init__(self, id: str, name: str):
        self.__id = id
        self.__name = name.title()

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


class Group:
    __id = str()
    __teacher_name = str()
    __students: list[Student] = list()

    def __init__(self, id: str, teacher_name: str):
        self.__id = id
        self.__teacher_name = teacher_name
        self.__students: list[Student] = list()

    def __str__(self):
        return f"{self.__id} {self.__teacher_name}"

    def set_id(self, id: str):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_teacher_name(self, teacher_name: str):
        self.__teacher_name = teacher_name

    def get_teacher_name(self):
        return self.__teacher_name

    def set_students(self, students: list[Student]):
        self.__students = students

    def get_students(self):
        return tuple(self.__students)

    def get_student_index(self, student_id: str):
        found_index = -1
        for i in range(len(self.__students)):
            if student_id == self.__students[i].get_id():
                found_index = i
                break
        return found_index

    def get_student(self, student_id: str) -> None | Student:
        index = self.get_student_index(student_id)
        if index != -1:
            student = self.__students[index]
        else:
            student = None
        return student

    def add_student(self, student: Student):
        is_success = False
        index = self.get_student_index(student.get_id())
        if index == -1:
            self.__students.append(student)
            is_success = True
        return is_success

    def remove_student_by_id(self, student_id: str):
        is_success = False
        index = self.get_student_index(student_id)
        if index != -1:
            del self.__students[index]
            is_success = True
        return is_success


class DB:
    __students: list[Student] = list()
    __groups: list[Group] = list()

    def __init__(self, students: None | list[Student] = None, groups: None | list[Group] = None):
        if students:
            self.__students: list[Student] = students
        else:
            self.__students: list[Student] = list()

        if groups:
            self.__groups: list[Group] = groups
        else:
            self.__groups: list[Group] = list()

    def set_students(self, students: list[Student]):
        self.__students = students

    def get_students(self):
        return tuple(self.__students)

    def get_student_index(self, student_id: str):
        found_index = -1
        for i in range(len(self.__students)):
            if student_id == self.__students[i].get_id():
                found_index = i
                break
        return found_index

    def get_student(self, student_id: str) -> None | Student:
        index = self.get_student_index(student_id)
        if index != -1:
            student = self.__students[index]
        else:
            student = None
        return student

    def add_student(self, student: Student):
        is_success = False
        index = self.get_student_index(student.get_id())
        if index == -1:
            self.__students.append(student)
            is_success = True
        return is_success

    def remove_student_by_id(self, student_id: str):
        is_success = False
        index = self.get_student_index(student_id)
        if index != -1:
            del self.__students[index]
            for group in self.__groups:
                group.remove_student_by_id(student_id)
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

    def set_groups(self, groups: list[Group]):
        self.__groups = groups

    def get_groups(self):
        return tuple(self.__groups)

    def get_group_index(self, group_id: str):
        found_index = -1
        for i in range(len(self.__groups)):
            if group_id == self.__groups[i].get_id():
                found_index = i
                break
        return found_index

    def get_group(self, group_id: str) -> None | Group:
        index = self.get_group_index(group_id)
        if index != -1:
            group = self.__groups[index]
        else:
            group = None
        return group

    def add_group(self, group: Group):
        is_success = False
        index = self.get_group_index(group.get_id())
        if index == -1:
            self.__groups.append(group)
            is_success = True
        return is_success

    def remove_group_by_id(self, group_id: str):
        is_success = False
        index = self.get_group_index(group_id)
        if index != -1:
            del self.__groups[index]
            is_success = True
        return is_success

    def change_group(self, group_id: str, changed_group: Group):
        is_success = False
        group = self.get_group(group_id)
        if group:
            changed_group_id = changed_group.get_id()
            changed_group_index = self.get_student_index(changed_group_id)
            if group_id == changed_group_id or changed_group_index == -1:
                group.set_id(changed_group.get_id())
                group.set_teacher_name(changed_group.get_teacher_name())
                is_success = True
        return is_success


student_1 = Student("ABC1234", "Tom")
student_2 = Student("XYZ5869", "Bob")
student_3 = Student("CBE1324", "Tom")
student_4 = Student("XYZ1234", "Kate")
student_5 = Student("RTE2345", "Jim")

group_1 = Group("G-5869", "Teston Lebra")
group_2 = Group("G-0078", "Astrid Grid")

data_base = DB()
data_base.add_student(student_1)
data_base.add_student(student_2)
data_base.add_student(student_3)
data_base.add_student(student_4)
data_base.add_student(student_5)

data_base.add_group(group_1)
data_base.add_group(group_2)

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

frame_student_img = tkinter.PhotoImage(file="img/frame_student_bg.gif")
frame_student_bg = tkinter.Label(frame_student, image=frame_student_img)
frame_student_bg.place(x=0, y=0)

frame_groups = tkinter.Frame(root)
frame_groups.pack_forget()

frame_groups_bg_img = tkinter.PhotoImage(file="img/frame_group_bg.gif")
frame_groups_bg = tkinter.Label(frame_groups, image=frame_groups_bg_img)
frame_groups_bg.place(x=0, y=0)

frame_assign_to_group = tkinter.Frame(root, bg="#34b019")
frame_assign_to_group.pack_forget()


def show_frame_students():
    # Скрываем всё, что не нужно
    frame_groups.pack_forget()
    frame_assign_to_group.pack_forget()

    # Изменяем размеры окна, если хотим
    root.geometry("720x480")

    # Показываем всё, что требуется показать
    frame_student.pack(fill="both", expand=True)


def show_frame_groups():
    # Скрываем всё, что не нужно
    frame_student.pack_forget()
    frame_assign_to_group.pack_forget()

    # Изменяем размеры окна, если хотим
    root.geometry("720x480")

    # Показываем всё, что требуется показать
    frame_groups.pack(fill="both", expand=True)


def show_frame_assign_to_group():
    # Скрываем всё, что не нужно
    frame_groups.pack_forget()
    frame_student.pack_forget()

    # Изменяем размеры окна, если хотим
    root.geometry("720x480")

    # Показываем всё, что требуется показать
    frame_assign_to_group.pack(fill="both", expand=True)


def close_program():
    root.quit()


root_menu = tkinter.Menu(root)
root.config(menu=root_menu)
show_menu = tkinter.Menu(root_menu, tearoff=False)
show_menu.add_command(label="Students", command=show_frame_students)
show_menu.add_command(label="Groups", command=show_frame_groups)
show_menu.add_command(label="Assign to Group", command=show_frame_assign_to_group)
show_menu.add_separator()
show_menu.add_command(label="Exit", command=close_program)
root_menu.add_cascade(label="Show", menu=show_menu)


# BEGIN FRAME STUDENT
fs_student_listbox = tkinter.Listbox(frame_student, font=("Arial", 18), height=13, fg="#ecc36c", bg="#427293")
fs_student_listbox.place(x=20, y=20)


def refresh_fs_student_listbox():
    fs_student_listbox.delete(0, tkinter.END)
    for student in data_base.get_students():
        fs_student_listbox.insert(tkinter.END, str(student))


refresh_fs_student_listbox()

fs_student_id_lbl = tkinter.Label(frame_student, text="ID:", font=("Arial", 18), fg="#ecc36c", bg="#427293")
fs_student_id_lbl.place(x=340, y=20)

fs_student_id_ntfy = tkinter.Label(frame_student, text="", font=("Arial", 18), fg="red", bg="#427293")
fs_student_id_ntfy.place(x=380, y=20)

fs_student_id_entry = tkinter.Entry(frame_student, font=("Arial", 18), fg="#ecc36c", bg="#427293")
fs_student_id_entry.place(x=340, y=60)

fs_student_name_lbl = tkinter.Label(frame_student, text="Name:", font=("Arial", 18), fg="#ecc36c", bg="#427293")
fs_student_name_lbl.place(x=340, y=100)

fs_student_name_ntfy = tkinter.Label(frame_student, text="", font=("Arial", 18), fg="red", bg="#427293")
fs_student_name_ntfy.place(x=420, y=100)

fs_student_name_entry = tkinter.Entry(frame_student, font=("Arial", 18), fg="#ecc36c", bg="#427293")
fs_student_name_entry.place(x=340, y=140)

fs_student_info_lbl = tkinter.Label(frame_student, text="User info:", font=("Arial", 18), fg="#ecc36c", bg="#427293")
fs_student_info_lbl.place(x=340, y=300)

fs_student_info = tkinter.Label(frame_student, text="", font=("Arial", 18), fg="#ecc36c", bg="#427293")
fs_student_info.place(x=340, y=340)

def fs_is_all_fields_correct():
    is_all_correct = True
    if not fs_student_id_entry.get():
        is_all_correct = False
        fs_student_id_ntfy.config(text="Fill this entry", justify="left")
    else:
        fs_student_id_ntfy.config(text="", justify="left")

    if not fs_student_name_entry.get():
        is_all_correct = False
        fs_student_name_ntfy.config(text="Fill this entry", justify="left")
    else:
        fs_student_name_ntfy.config(text="", justify="left")

    return is_all_correct


def fs_add_student():
    new_id = fs_student_id_entry.get()
    new_name = fs_student_name_entry.get()

    if fs_is_all_fields_correct():
        new_student = Student(new_id, new_name)

        if data_base.add_student(new_student):
            refresh_fs_student_listbox()
            fatg_student_combobox["values"] = data_base.get_students()
        else:
            fs_student_id_ntfy.config(text="Id already in list", justify="left")

        print()
        for student in data_base.get_students():
            print(student)


fs_student_add_btn = tkinter.Button(frame_student, text="New", font=("Arial", 14), command=fs_add_student,
                                    fg="#ecc36c", bg="#427293")
fs_student_add_btn.place(x=20, y=400)


def fs_delete_student():
    selected_student_indexes = fs_student_listbox.curselection()
    if len(selected_student_indexes) > 0:
        fs_student_info.config(text="", justify="left", fg="black")
        selected_student_index = selected_student_indexes[0]
        selected_student_str = fs_student_listbox.get(selected_student_index)
        selected_student_id = selected_student_str.split()[0]

        if data_base.remove_student_by_id(selected_student_id):
            fs_student_id_ntfy.config(text="", justify="left")
            refresh_fs_student_listbox()
            fatg_student_combobox["values"] = data_base.get_students()
            fatg_student_combobox.set("")
            fatg_student_listbox.delete(0, tkinter.END)
            fatg_selected_group_info.config(text="", justify="left")
    else:
        fs_student_info.config(text="Select student", justify="left", fg="red")

    print()
    for student in data_base.get_students():
        print(student)


fs_student_delete_btn = tkinter.Button(frame_student, text="Delete", font=("Arial", 14), command=fs_delete_student,
                                       fg="#ecc36c", bg="#427293")
fs_student_delete_btn.place(x=75, y=400)


def fs_change_student():
    selected_student_indexes = fs_student_listbox.curselection()
    if len(selected_student_indexes) > 0:
        fs_student_info.config(text="", justify="left", fg="black")
        selected_student_index = selected_student_indexes[0]
        selected_student_str = fs_student_listbox.get(selected_student_index)
        selected_student_id = selected_student_str.split()[0]

        new_id = fs_student_id_entry.get()
        new_name = fs_student_name_entry.get()

        if fs_is_all_fields_correct():

            new_student = Student(new_id, new_name)

            if data_base.change_student(selected_student_id, new_student):
                fs_student_id_ntfy.config(text="", justify="left")
                refresh_fs_student_listbox()
                fatg_student_combobox["values"] = data_base.get_students()
                fatg_student_combobox.set("")
                fatg_student_listbox.delete(0, tkinter.END)
                fatg_selected_group_info.config(text="", justify="left")
            else:
                fs_student_id_ntfy.config(text="Id already in list", justify="left")
    else:
        fs_student_info.config(text="Select student", justify="left", fg="red")

    print()
    for student in data_base.get_students():
        print(student)


fs_student_change_btn = tkinter.Button(frame_student, text="Change", font=("Arial", 14), command=fs_change_student,
                                       fg="#ecc36c", bg="#427293")
fs_student_change_btn.place(x=150, y=400)


def fs_show_student_data():
    selected_student_indexes = fs_student_listbox.curselection()
    if len(selected_student_indexes) > 0:
        selected_student_index = selected_student_indexes[0]
        selected_student_str = fs_student_listbox.get(selected_student_index)
        selected_student_id = selected_student_str.split()[0]

        selected_student = data_base.get_student(selected_student_id)
        if selected_student:
            student_data = f"ID: {selected_student.get_id()}\nName: {selected_student.get_name()}"
            fs_student_info.config(text=student_data, justify="left")


fs_student_info_btn = tkinter.Button(frame_student, text="Info", font=("Arial", 14), command=fs_show_student_data,
                                     fg="#ecc36c", bg="#427293")
fs_student_info_btn.place(x=235, y=400)
# END FRAME STUDENT

# BEGIN FRAME GROUP
fg_group_listbox = tkinter.Listbox(frame_groups, font=("Arial", 18), height=13)
fg_group_listbox.place(x=20, y=20)


def refresh_fg_group_listbox():
    fg_group_listbox.delete(0, tkinter.END)
    for group in data_base.get_groups():
        fg_group_listbox.insert(tkinter.END, str(group))


refresh_fg_group_listbox()

fg_group_id_lbl = tkinter.Label(frame_groups, text="ID:", font=("Arial", 18))
fg_group_id_lbl.place(x=340, y=20)

fg_group_id_entry = tkinter.Entry(frame_groups, font=("Arial", 18))
fg_group_id_entry.place(x=340, y=60)

fg_group_name_lbl = tkinter.Label(frame_groups, text="Name:", font=("Arial", 18))
fg_group_name_lbl.place(x=340, y=100)

fg_group_name_entry = tkinter.Entry(frame_groups, font=("Arial", 18))
fg_group_name_entry.place(x=340, y=140)

fg_group_info_lbl = tkinter.Label(frame_groups, text="Group info:", font=("Arial", 18))
fg_group_info_lbl.place(x=340, y=300)

fg_group_info = tkinter.Label(frame_groups, text="", font=("Arial", 18))
fg_group_info.place(x=340, y=340)


def fg_add_group():
    new_id = fg_group_id_entry.get()
    new_name = fg_group_name_entry.get()

    new_group = Group(new_id, new_name)

    if data_base.add_group(new_group):
        refresh_fg_group_listbox()
        fatg_group_combobox["values"] = data_base.get_groups()

    print()
    for group in data_base.get_groups():
        print(group)


fg_group_add_btn = tkinter.Button(frame_groups, text="New", font=("Arial", 14), command=fg_add_group)
fg_group_add_btn.place(x=20, y=400)


def fg_delete_group():
    selected_group_indexes = fg_group_listbox.curselection()
    if len(selected_group_indexes) > 0:
        selected_group_index = selected_group_indexes[0]
        selected_group_str = fg_group_listbox.get(selected_group_index)
        selected_group_id = selected_group_str.split()[0]

        if data_base.remove_group_by_id(selected_group_id):
            refresh_fg_group_listbox()
            fatg_group_combobox["values"] = data_base.get_groups()
            fatg_group_combobox.set("")
            fatg_student_listbox.delete(0, tkinter.END)
            fatg_selected_group_info.config(text="", justify="left")

    print()
    for group in data_base.get_groups():
        print(group)


fg_group_delete_btn = tkinter.Button(frame_groups, text="Delete", font=("Arial", 14), command=fg_delete_group)
fg_group_delete_btn.place(x=75, y=400)


def fg_change_group():
    selected_group_indexes = fg_group_listbox.curselection()
    if len(selected_group_indexes) > 0:
        selected_group_index = selected_group_indexes[0]
        selected_group_str = fg_group_listbox.get(selected_group_index)
        selected_group_id = selected_group_str.split()[0]

        new_id = fg_group_id_entry.get()
        new_teacher_name = fg_group_name_entry.get()

        new_group = Group(new_id, new_teacher_name)

        if data_base.change_group(selected_group_id, new_group):
            refresh_fg_group_listbox()
            fatg_group_combobox["values"] = data_base.get_groups()
            fatg_group_combobox.set("")
            fatg_student_listbox.delete(0, tkinter.END)
            fatg_selected_group_info.config(text="", justify="left")

    print()
    for group in data_base.get_groups():
        print(group)


fg_group_change_btn = tkinter.Button(frame_groups, text="Change", font=("Arial", 14), command=fg_change_group)
fg_group_change_btn.place(x=150, y=400)


def fg_show_group_data():
    selected_group_indexes = fg_group_listbox.curselection()
    if len(selected_group_indexes) > 0:
        selected_group_index = selected_group_indexes[0]
        selected_group_str = fg_group_listbox.get(selected_group_index)
        selected_group_id = selected_group_str.split()[0]

        selected_group = data_base.get_group(selected_group_id)
        if selected_group:
            group_data = f"ID: {selected_group.get_id()}\nTeacher: {selected_group.get_teacher_name()}"
            fg_group_info.config(text=group_data, justify="left")


fg_group_info_btn = tkinter.Button(frame_groups, text="Info", font=("Arial", 14), command=fg_show_group_data)
fg_group_info_btn.place(x=235, y=400)
# END FRAME GROUP

# BEGIN FRAME ASSIGN TO GROUP
fatg_group_lbl = tkinter.Label(frame_assign_to_group, text="Group:", font=("Arial", 16))
fatg_group_lbl.place(x=20, y=20)
fatg_group_combobox = ttk.Combobox(frame_assign_to_group, values=data_base.get_groups(), font=("Arial", 18), state="readonly")
fatg_group_combobox.place(x=20, y=60)

fatg_student_lbl = tkinter.Label(frame_assign_to_group, text="Student:", font=("Arial", 16))
fatg_student_lbl.place(x=20, y=120)
fatg_student_combobox = ttk.Combobox(frame_assign_to_group, values=data_base.get_students(), font=("Arial", 18), state="readonly")
fatg_student_combobox.place(x=20, y=160)

fatg_selected_group_info_lbl = tkinter.Label(frame_assign_to_group, text="Group:", font=("Arial", 16))
fatg_selected_group_info_lbl.place(x=400, y=20)
fatg_selected_group_info = tkinter.Label(frame_assign_to_group, text="", font=("Arial", 16))
fatg_selected_group_info.place(x=480, y=20)

fatg_student_listbox = tkinter.Listbox(frame_assign_to_group, font=("Arial", 18), height=13)
fatg_student_listbox.place(x=400, y=60)


def refresh_fatg_student_listbox(group: Group):
    fatg_student_listbox.delete(0, tkinter.END)
    for student in group.get_students():
        fatg_student_listbox.insert(tkinter.END, str(student))


def fatg_show_students_listbox():
    selected_group_str = fatg_group_combobox.get()
    fatg_selected_group_info.config(text=f"{selected_group_str}", justify="left")

    selected_group_list = selected_group_str.split()
    if len(selected_group_list) > 0:
        selected_group_id = selected_group_list[0]
    else:
        selected_group_id = ""
    selected_group = data_base.get_group(selected_group_id)

    if selected_group:
        refresh_fatg_student_listbox(selected_group)


fatg_show_students_btn = tkinter.Button(frame_assign_to_group, text="Show students", font=("Arial", 16), command=fatg_show_students_listbox)
fatg_show_students_btn.place(x=400, y=430)


def fatg_add_student():
    selected_group_str = fatg_group_combobox.get()
    fatg_selected_group_info.config(text=f"{selected_group_str}", justify="left")

    selected_group_id = selected_group_str.split()[0]
    selected_group = data_base.get_group(selected_group_id)

    selected_student_str = fatg_student_combobox.get()
    selected_student_id = selected_student_str.split()[0]
    selected_student = data_base.get_student(selected_student_id)

    if selected_group and selected_student:
        selected_group.add_student(selected_student)
        refresh_fatg_student_listbox(selected_group)

    print()
    for group in data_base.get_groups():
        print("=" * 25, group, "=" * 25)
        for student in group.get_students():
            print(student)

fatg_add_student_btn_img = tkinter.PhotoImage(file="img/add_student_bg.gif")
fatg_add_student_btn = tkinter.Button(frame_assign_to_group, text="Add student", font=("Arial", 16), command=fatg_add_student,
                                      image=fatg_add_student_btn_img, bd=2, bg="#000000")
fatg_add_student_btn.place(x=20, y=240)


def fatg_remove_student():
    selected_student_indexes = fatg_student_listbox.curselection()
    if len(selected_student_indexes) > 0:
        selected_student_index = selected_student_indexes[0]
        selected_student_str = fatg_student_listbox.get(selected_student_index)
        selected_student_id = selected_student_str.split()[0]

        selected_group_str = fatg_selected_group_info.cget("text")
        selected_group_id = selected_group_str.split()[0]
        selected_group = data_base.get_group(selected_group_id)

        if selected_group.remove_student_by_id(selected_student_id):
            refresh_fatg_student_listbox(selected_group)

    print()
    for group in data_base.get_groups():
        print("=" * 25, group, "=" * 25)
        for student in group.get_students():
            print(student)


fatg_remove_student_btn = tkinter.Button(frame_assign_to_group, text="Remove", font=("Arial", 16), command=fatg_remove_student)
fatg_remove_student_btn.place(x=570, y=430)
# END FRAME OPERATIONS

root.mainloop()
