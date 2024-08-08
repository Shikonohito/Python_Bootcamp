num_tasks = int(input("Задач: "))
grade_total = 12
result_grade = 0
for current_task in range(1, num_tasks + 1):
    result_grade += int(input(f"Задание {current_task}. Оценка от 1 до {grade_total}: "))
print(f"Оценка {result_grade / num_tasks}")
