class ITStepStudent:
    __login = ""
    __f_name = ""
    __l_name = ""
    __coins = 0
    __crystals = 0
    __rating = 0
    __grades = list()

    def __init__(self, login: str, f_name: str, l_name: str, coins=0, crystals=0, grades=None):
        self.set_login(login)
        self.set_f_name(f_name)
        self.set_l_name(l_name)
        self.set_coins(coins)
        self.set_crystals(crystals)
        self.update_rating()
        if grades:
            self.__grades = grades
            for grade in grades:
                self.__coins += self.grade_to_coins(grade)
        else:
            self.__grades = list()

    def __str__(self):
        return f"Username: {self.__login}\t\tName: {self.__f_name}\t\tSurname: {self.__l_name}"

    def set_login(self, login: str):
        self.__login = login

    def get_login(self):
        return self.__login

    def set_f_name(self, f_name: str):
        self.__f_name = f_name.title()

    def get_f_name(self):
        return self.__f_name

    def set_l_name(self, l_name: str):
        self.__l_name = l_name.title()

    def get_l_name(self):
        return self.__l_name

    def update_rating(self):
        self.__rating = self.__coins + self.__crystals

    def set_coins(self, coins: int):
        if coins > 0:
            self.__coins = coins
            self.update_rating()

    def get_coins(self):
        return self.__coins

    def add_coins(self, coins: int):
        if coins > 0:
            self.__coins += coins
            self.update_rating()

    def remove_coins(self, coins: int):
        if coins > 0:
            self.__coins -= coins
            self.update_rating()

    def set_crystals(self, crystals: int):
        if crystals > 0:
            self.__crystals = crystals
            self.update_rating()

    def get_crystals(self):
        return self.__crystals

    def add_crystals(self, crystals: int):
        if crystals > 0:
            self.__crystals += crystals
            self.update_rating()

    def remove_crystals(self, crystals: int):
        if crystals > 0:
            self.__crystals -= crystals
            self.update_rating()

    def get_rating(self):
        return self.__rating

    def get_grades(self):
        return tuple(self.__grades)

    def grade_to_coins(self, grade: int):
        coins = 0
        if grade <= 8:
            coins = 1
        elif grade == 9:
            coins = 2
        elif grade == 10:
            coins = 3
        elif grade == 11:
            coins = 4
        elif grade == 12:
            coins = 5
        return coins

    def check_grade(self, grade: int):
        return 1 <= grade and grade <= 12

    def add_grade(self, grade: int):
        is_success = False
        if self.check_grade(grade):
            self.__grades.append(grade)
            coins = self.grade_to_coins(grade)
            self.add_coins(coins)
            is_success = True
        return is_success

    def change_grade(self, index: int, grade: int):
        is_success = False
        if self.check_grade(grade) and index < len(self.__grades):
            coins = self.grade_to_coins(self.__grades[index])
            self.remove_coins(coins)
            self.__grades[index] = grade
            coins = self.grade_to_coins(grade)
            self.add_coins(coins)
            is_success = True
        return is_success

    def remove_grade(self, index: int):
        is_success = False
        if index < len(self.__grades):
            coins = self.grade_to_coins(self.__grades[index])
            self.remove_coins(coins)
            del self.__grades[index]
            is_success = True
        return is_success


# ===================================================================

def print_all_students(students: list[ITStepStudent]):
    for student in students:
        print_student(student)
        print("================================")


def print_student(student: ITStepStudent):
    print(student)
    print(f"{student.get_coins()} coins, {student.get_crystals()} crystals. Rating: {student.get_rating()}")
    print(student.get_grades())


def show_main_menu():
    print("1. Показать всех студентов")
    print("2. Выбрать студента по логину")
    print("3. Добавить студента")
    print("4. Удалить студента")
    print("5. Завершить программу")


def show_student_menu():
    print("1. Добавить оценку")
    print("2. Изменить оценку")
    print("3. Удалить оценку")
    print("4. Изменить логин")
    print("5. Изменить имя")
    print("6. Изменить фамилию")
    print("7. Добавить кристалл")
    print("8. Вернуться")


student_list = [ITStepStudent("Teston_xyz", "Teston", "Lebra", grades=[12, 7, 9]),
                ITStepStudent("Abc_5869", "Tom", "Jackson", grades=[9, 8, 8]),
                ITStepStudent("AT_red", "Astrid", "Hofferson", grades=[12, 12, 12])]


def find_student_by_login(student_login: str):
    index = -1
    for i in range(len(student_list)):
        if student_list[i].get_login() == student_login:
            index = i
            break
    return index


def select_student(student_login: str):
    i = find_student_by_login(student_login)
    while i != -1:
        student = student_list[i]
        print_student(student)
        print("=================================")
        show_student_menu()
        choice = input("Выберите действие: ")
        if choice == "1":
            print("=================================")
            input_grade = int(input("Введите оценку от 1 до 12 включительно: "))
            if student.add_grade(input_grade):
                print("Оценка добавлена")
            else:
                print("Оценка должна быть от 1 до 12 включительно.")
            print("=================================")
        elif choice == "2":
            print("=================================")
            index = int(input("Введите номер оценки: ")) - 1
            input_grade = int(input("Введите оценку от 1 до 12 включительно: "))
            if student.change_grade(index, input_grade):
                print("Оценка изменена.")
            else:
                print("Оценка или номер оценки указаны неверно.")
            print("=================================")
        elif choice == "3":
            print("=================================")
            index = int(input("Введите номер оценки: ")) - 1
            if student.remove_grade(index):
                print("Оценка удалена.")
            else:
                print("Номер оценки указан неверно.")
            print("=================================")
        elif choice == "4":
            print("=================================")
            input_login = input("Введите логин: ")
            if find_student_by_login(input_login) == -1:
                student.set_login(input_login)
                print("Логин изменён.")
            else:
                print("Введённый логин уже занят. Введите другой.")
            print("=================================")
        elif choice == "5":
            print("=================================")
            input_f_name = input("Введите имя: ")
            student.set_f_name(input_f_name)
            print("Имя изменено.")
            print("=================================")
        elif choice == "6":
            print("=================================")
            input_l_name = input("Введите фамилию: ")
            student.set_l_name(input_l_name)
            print("Фамилия изменена.")
            print("=================================")
        elif choice == "7":
            print("=================================")
            input_crystal = int(input("Введите количество кристаллов: "))
            student.add_crystals(input_crystal)
            print("Кристаллы добавлены.")
            print("=================================")
        elif choice == "8":
            break


def add_student(student: ITStepStudent):
    is_success = False
    if find_student_by_login(student.get_login()) == -1:
        student_list.append(student)
        is_success = True
    return is_success


def remove_student(student_login):
    is_success = False
    index = find_student_by_login(student_login)
    if index != -1:
        del student_list[index]
        is_success = True
    return is_success


while True:
    show_main_menu()
    choice = input("Выберите действие: ")
    if choice == "1":
        print("=================================")
        print_all_students(student_list)
    elif choice == "2":
        print("=================================")
        input_login = input("Введите логин: ")
        select_student(input_login)
        print("=================================")
    elif choice == "3":
        print("=================================")
        input_login = input("Введите логин: ")
        input_f_name = input("Введите имя: ")
        input_l_name = input("Введите фамилию: ")
        new_student = ITStepStudent(input_login, input_f_name, input_l_name)
        if add_student(new_student):
            print("Студент добавлен")
        else:
            print("Ошибка добавления. Указанный логин уже есть у другого студента.")
        print("=================================")
    elif choice == "4":
        print("=================================")
        input_login = input("Введите логин: ")
        if remove_student(input_login):
            print("Студент успешно удалён.")
        else:
            print("Студента с указанным логином не найден.")
        print("=================================")
    elif choice == "5":
        print("=================================")
        print("Завершение программы.")
        break
