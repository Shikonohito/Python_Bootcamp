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
