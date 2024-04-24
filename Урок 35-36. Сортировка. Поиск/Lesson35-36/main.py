# ==============================================LESSON35==============================================
# https://airtucha.github.io/SortVis/
# Сортировка выбором
# Быстрая сортировка


# def sort_choice(num_list):
#     list_len = len(num_list)
#     for i in range(0, list_len):
#         min_index = i
#         for j in range(i, list_len):
#             if num_list[j] < num_list[min_index]:
#                 min_index = j
#         temp = num_list[i]
#         num_list[i] = num_list[min_index]
#         num_list[min_index] = temp
#
#
# my_list = [23, 71, 25, 95, 100, 12, 67]
# sort_choice(my_list)
# print(*my_list)


# def sort_quick(num_list, start, end):
#     if end - start > 1:
#         p = partition(num_list, start, end)  # Сортировка и получение индекса разбиения
#         sort_quick(num_list, start, p)
#         sort_quick(num_list, p + 1, end)
#
# def partition(num_list, start, end):
#     pivot = num_list[start]
#     i = start + 1
#     j = end - 1
#
#     while True:
#         while i <= j and num_list[i] <= pivot:  # Ищем индекс числа, который больше опорного
#             i += 1
#         while i <= j and num_list[j] >= pivot:  # Ищем индекс числа, который меньше опорного
#             j -= 1
#
#         if i <= j:
#             temp = num_list[i]
#             num_list[i] = num_list[j]
#             num_list[j] = temp
#         else:  # Если индексы пересеклись, значит по индексу j должен находиться опорное число
#             temp = num_list[start]
#             num_list[start] = num_list[j]
#             num_list[j] = temp
#             return j  # Возвращаем индекс опорного числа, который теперь находится на своём месте
#
#
# my_list = [25, 100, 36, 20, 12, 18, 60, 80, 15, 16]
# sort_quick(my_list, 0, len(my_list))
# print(*my_list)


# ==============================================LESSON36==============================================
# Линейный поиск
# Бинарный поиск
# 16 названий чисел ~ 65536 максимальное число


# def find_linear(num_list, to_find):
#     len_list = len(num_list)
#     index_find = -1
#     for i in range(len_list):
#         if num_list[i] == to_find:
#             index_find = i
#             break
#     return index_find
#
#
# my_list = [25, 100, 36, 20, 12, 18, 60, 80, 15, 16]
# # my_list = [12, 15, 16, 18, 20, 25, 36, 60, 80, 100]
# ind_find = find_linear(my_list, 16)
# if ind_find == -1:
#     print("Not Found")
# else:
#     print(ind_find)


# def find_bin(num_list, to_find):
#     left = 0
#     right = len(num_list)
#     index_find = -1
#     while left <= right:
#         mid = (left + right) // 2
#         if num_list[mid] == to_find:
#             index_find = mid
#             break
#
#         if to_find > num_list[mid]:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return index_find
#
#
# my_list = [12, 15, 16, 18, 20, 25, 36, 60, 80, 100]
# ind_find = find_bin(my_list, 16)
# if ind_find == -1:
#     print("Not Found")
# else:
#     print(ind_find)
