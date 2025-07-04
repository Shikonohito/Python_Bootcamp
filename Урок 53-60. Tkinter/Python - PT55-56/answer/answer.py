import tkinter
# Используя описанный ниже код бэкенда, создайте графическое приложение,
# в котором есть возможность добавить, показать, изменить, удалить сотрудника.
# Используйте виджеты Label, Entry, Button, Listbox.

class Employee:
    __id = str()
    __role = str()
    __salary = int()

    def __init__(self, id: str, role: str, salary: int):
        self.__id = id
        self.__role = role
        self.set_salary(salary)

    def __str__(self):
        return f"{self.__id} {self.__role}"

    def set_id(self, id: str):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_role(self, role: str):
        self.__role = role

    def get_role(self):
        return self.__role

    def set_salary(self, salary: int):
        if salary >= 0:
            self.__salary = salary
        else:
            self.__salary = 0

    def get_salary(self):
        return self.__salary


class DB:
    __employee_list: list[Employee] = list()

    def __init__(self, employee_list: list[Employee] = None):
        if employee_list:
            self.__employee_list = employee_list
        else:
            self.__employee_list: list[Employee] = list()

    def get_employees(self):
        return tuple(self.__employee_list)

    def __get_employee_index(self, employee_id: str) -> int:
        found_index = -1
        for i in range(len(self.__employee_list)):
            if employee_id == self.__employee_list[i].get_id():
                found_index = i
                break
        return found_index

    def get_employee(self, employee_id: str) -> Employee | None:
        found_index = self.__get_employee_index(employee_id)
        found_employee = None
        if found_index != -1:
            found_employee = self.__employee_list[found_index]
        return found_employee

    def add_employee(self, new_employee: Employee) -> bool:
        is_success = False
        found_index = self.__get_employee_index(new_employee.get_id())
        if found_index == -1:
            self.__employee_list.append(new_employee)
            is_success = True
        return is_success

    def remove_employee(self, employee_id: str) -> bool:
        is_success = False
        found_index = self.__get_employee_index(employee_id)
        if found_index != -1:
            del self.__employee_list[found_index]
            is_success = True
        return is_success

    def change_employee(self, employee_id: str, changed_employee: Employee) -> bool:
        is_success = False
        employee = self.get_employee(employee_id)
        if employee:
            changed_employee_id = changed_employee.get_id()
            changed_employee_index = self.__get_employee_index(changed_employee_id)
            if employee_id == changed_employee_id or changed_employee_index == -1:
                employee.set_id(changed_employee_id)
                employee.set_role(changed_employee.get_role())
                employee.set_salary(changed_employee.get_salary())
                is_success = True
        return is_success


# ТЕСТОВЫЕ ДАННЫЕ
employee_1 = Employee("E-001", "Software Developer", 1400)
employee_2 = Employee("E-055", "Mobile Developer", 1200)
employee_3 = Employee("E-029", "Software Engineer", 2500)
employee_4 = Employee("E-014", "QA Tester", 800)
employee_5 = Employee("E-059", "Software Developer", 1400)

data_base = DB()
data_base.add_employee(employee_1)
data_base.add_employee(employee_2)
data_base.add_employee(employee_3)
data_base.add_employee(employee_4)
data_base.add_employee(employee_5)

root = tkinter.Tk()
root.title("Python - PT53-54")
root.geometry("720x480")
root.resizable(False, False)

frame_employee = tkinter.Frame(root)
frame_employee.pack(expand=True, fill="both")

employee_listbox = tkinter.Listbox(frame_employee, font=("Arial", 18), height=13, width=23)
employee_listbox.place(x=20, y=20)


def refresh_employee_listbox():
    employee_listbox.delete(0, tkinter.END)
    for employee in data_base.get_employees():
        employee_listbox.insert(tkinter.END, str(employee))


refresh_employee_listbox()

employee_id_lbl = tkinter.Label(frame_employee, text="ID:", font=("Arial", 18))
employee_id_lbl.place(x=340, y=20)

employee_id_entry = tkinter.Entry(frame_employee, font=("Arial", 18))
employee_id_entry.place(x=340, y=60)

employee_role_lbl = tkinter.Label(frame_employee, text="Role:", font=("Arial", 18))
employee_role_lbl.place(x=340, y=100)

employee_role_entry = tkinter.Entry(frame_employee, font=("Arial", 18))
employee_role_entry.place(x=340, y=140)

employee_salary_lbl = tkinter.Label(frame_employee, text="Salary:", font=("Arial", 18))
employee_salary_lbl.place(x=340, y=180)

employee_salary_entry = tkinter.Entry(frame_employee, font=("Arial", 18), width=3)
employee_salary_entry.place(x=340, y=220)

employee_info_lbl = tkinter.Label(frame_employee, text="Employee info:", font=("Arial", 18))
employee_info_lbl.place(x=340, y=300)

employee_info = tkinter.Label(frame_employee, text="", font=("Arial", 18))
employee_info.place(x=340, y=340)


def add_employee():
    # Считываем данные из полей фронтенда
    new_id = employee_id_entry.get()
    new_role = employee_role_entry.get()
    new_salary = int(employee_salary_entry.get())

    # Формируем из данных объект
    new_employee = Employee(new_id, new_role, new_salary)

    # Добавляем объект в бэкенд
    if data_base.add_employee(new_employee):
        # Формируем строковое представление объекта
        new_employee_listbox = str(new_employee)

        # Добавляем строковое представление объекта во фронтенд
        employee_listbox.insert(tkinter.END, new_employee_listbox)

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for employee in data_base.get_employees():
        print(f"{employee.get_id()} {employee.get_role()} {employee.get_salary()}")


employee_add_btn = tkinter.Button(frame_employee, text="New", font=("Arial", 14), command=add_employee)
employee_add_btn.place(x=20, y=400)


def delete_employee():
    # Считываем индексы выделенных элементов из фронтенда
    selected_employee_indexes = employee_listbox.curselection()

    if selected_employee_indexes:
        # Выделяем в переменную индекс выбранного элемента
        selected_employee_index = selected_employee_indexes[0]

        # Считываем элемент по индексу
        selected_employee_str = employee_listbox.get(selected_employee_index)

        # Отдельно выделяем идентификатор
        selected_employee_id = selected_employee_str.split()[0]

        # Пытаемся удалить из бэкенда
        if data_base.remove_employee(selected_employee_id):
            # Удаляем из фронтенда
            employee_listbox.delete(selected_employee_index)

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for employee in data_base.get_employees():
        print(f"{employee.get_id()} {employee.get_role()} {employee.get_salary()}")


employee_delete_btn = tkinter.Button(frame_employee, text="Delete", font=("Arial", 14), command=delete_employee)
employee_delete_btn.place(x=75, y=400)


def change_employee():
    # Считываем индексы выделенных элементов из фронтенда
    selected_employee_indexes = employee_listbox.curselection()
    if selected_employee_indexes:
        # Выделяем в переменную индекс выбранного элемента
        selected_employee_index = selected_employee_indexes[0]

        # Считываем элемент по индексу
        selected_employee_str = employee_listbox.get(selected_employee_index)

        # Отдельно выделяем идентификатор
        selected_employee_id = selected_employee_str.split()[0]

        # Считываем данные из полей фронтенда
        new_id = employee_id_entry.get()
        new_role = employee_role_entry.get()
        new_salary = int(employee_salary_entry.get())

        # Формируем из данных объект
        new_employee = Employee(new_id, new_role, new_salary)

        # Пытаемся изменить объект в бэкенде
        if data_base.change_employee(selected_employee_id, new_employee):
            # Формируем строковое представление объекта
            new_employee_listbox = str(new_employee)

            # Изменяем данные во фронтенде
            employee_listbox.delete(selected_employee_index)
            employee_listbox.insert(selected_employee_index, new_employee_listbox)

    # Для проверки соответствия наполнения бэкенда и фронтенда
    print()
    for employee in data_base.get_employees():
        print(f"{employee.get_id()} {employee.get_role()} {employee.get_salary()}")


employee_change_btn = tkinter.Button(frame_employee, text="Change", font=("Arial", 14), command=change_employee)
employee_change_btn.place(x=150, y=400)


def show_employee_data():
    # Считываем индексы выделенных элементов из фронтенда
    selected_employee_indexes = employee_listbox.curselection()
    if selected_employee_indexes:
        # Выделяем в переменную индекс выбранного элемента
        selected_employee_index = selected_employee_indexes[0]

        # Считываем элемент по индексу
        selected_employee_str = employee_listbox.get(selected_employee_index)

        # Отдельно выделяем идентификатор
        selected_employee_id = selected_employee_str.split()[0]

        # Запрашиваем из бэкенда объект по идентификатору
        selected_employee = data_base.get_employee(selected_employee_id)
        if selected_employee:
            employee_data = f"ID: {selected_employee.get_id()}\nRole: {selected_employee.get_role()}\nSalary: {selected_employee.get_salary()}"
            employee_info.config(text=employee_data, justify="left")

        # Для проверки соответствия наполнения бэкенда и фронтенда
        print()
        for employee in data_base.get_employees():
            print(f"{employee.get_id()} {employee.get_role()} {employee.get_salary()}")


employee_info_btn = tkinter.Button(frame_employee, text="Info", font=("Arial", 14), command=show_employee_data)
employee_info_btn.place(x=235, y=400)


root.mainloop()
