# Используя описанный ниже код бэкенда, создайте графическое приложение,
# в котором есть возможность добавить, показать, изменить, удалить сотрудника.
# Используйте виджеты Label, Entry, Button, Listbox.

class Employee:
    __id = str()
    __name = str()
    __age = str()

    def __init__(self, id: str, name: str, age: int):
        self.__id = id
        self.__name = name
        self.set_age(age)

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
        if age >= 0:
            self.__age = age
        else:
            self.__age = 0

    def get_age(self):
        return self.__age


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
                employee.set_name(changed_employee.get_name())
                employee.set_age(changed_employee.get_age())
                is_success = True
        return is_success


# ТЕСТОВЫЕ ДАННЫЕ
employee_1 = Employee("E-001", "Teston", 25)
employee_2 = Employee("E-055", "Tom", 28)
employee_3 = Employee("E-029", "Kate", 27)
employee_4 = Employee("E-014", "Bob", 29)
employee_5 = Employee("E-059", "Jack", 35)

data_base = DB()
data_base.add_employee(employee_1)
data_base.add_employee(employee_2)
data_base.add_employee(employee_3)
data_base.add_employee(employee_4)
data_base.add_employee(employee_5)
