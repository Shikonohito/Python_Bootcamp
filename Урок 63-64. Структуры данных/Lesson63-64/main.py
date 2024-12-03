# ==============================================LESSON63==============================================
# Стек. Очередь.

# class Stack:
#     __collection = list()
#     __size = 0
#     __peek = None
#
#     def __init__(self, new_data=None):
#         if new_data is None:
#             self.__collection = list()
#             self.__size = 0
#             self.__peek = None
#         else:
#             self.__collection = new_data
#             self.__size = len(new_data)
#             self.__peek = self.__collection[self.__size - 1]
#
#     def __str__(self):
#         result = ""
#         if self.__size >= 1:
#             result += "{}".format(self.__collection[self.__size - 1])
#         if self.__size >= 2:
#             for i in range(self.__size - 2, -1, -1):
#                 result += "\n{}".format(self.__collection[i])
#         return result
#
#     def push(self, item):
#         self.__collection.append(item)
#         self.__size += 1
#         self.__peek = item
#
#     def pop(self):
#         to_pop = None
#         if self.__size >= 1:
#             to_pop = self.__collection[self.__size - 1]
#             del self.__collection[self.__size - 1]
#             self.__size -= 1
#             if self.__size == 0:
#                 self.__peek = None
#             else:
#                 self.__peek = self.__collection[self.__size - 1]
#         return to_pop
#
#     def peek(self):
#         return self.__peek
#
#     def contains(self, item):
#         is_found = False
#         for i in range(self.__size):
#             if item == self.__collection[i]:
#                 is_found = True
#         return is_found
#
#
# my_stack = Stack([100, 200, 300])
# print("STACK:")
# print(my_stack)
# print("PEEK:", my_stack.peek())
# print()
#
# my_stack.push(400)
# print("STACK:")
# print(my_stack)
# print("PEEK:", my_stack.peek())
# print()
#
# pop_result = my_stack.pop()
# print("STACK:")
# print(my_stack)
# print("PEEK:", my_stack.peek())
# print("POP ITEM:", pop_result)
# print()
#
# if my_stack.contains(200):
#     print("YES")


# class Queue:
#     __collection = list()
#     __size = 0
#     __peek = None
#
#     def __init__(self, new_data=None):
#         if new_data is None:
#             self.__collection = list()
#             self.__size = 0
#             self.__peek = None
#         else:
#             self.__collection = new_data
#             self.__size = len(new_data)
#             self.__peek = self.__collection[self.__size - 1]
#
#     def __str__(self):
#         result = ""
#         if self.__size >= 1:
#             result += "{}".format(self.__collection[self.__size - 1])
#         if self.__size >= 2:
#             for i in range(self.__size - 2, -1, -1):
#                 result += "\n{}".format(self.__collection[i])
#         return result
#
#     def enqueue(self, item):
#         self.__collection.insert(0, item)
#         self.__size += 1
#
#         if self.__peek is None:
#             self.__peek = item
#
#     def dequeue(self):
#         to_dequeue = None
#         if self.__size >= 1:
#             to_dequeue = self.__collection[self.__size - 1]
#             del self.__collection[self.__size - 1]
#             self.__size -= 1
#             if self.__size == 0:
#                 self.__peek = None
#             else:
#                 self.__peek = self.__collection[self.__size - 1]
#         return to_dequeue
#
#     def peek(self):
#         return self.__peek
#
#     def contains(self, item):
#         is_found = False
#         for i in range(self.__size):
#             if item == self.__collection[i]:
#                 is_found = True
#         return is_found
#
#
# my_queue = Queue([300, 200, 100])
# print("QUEUE:")
# print(my_queue)
# print("PEEK:", my_queue.peek())
# print()
#
# my_queue.enqueue(400)
# print("QUEUE:")
# print(my_queue)
# print("PEEK:", my_queue.peek())
# print()
#
# dequeue_result = my_queue.dequeue()
# print("QUEUE:")
# print(my_queue)
# print("PEEK:", my_queue.peek())
# print("DEQUEUE ITEM:", dequeue_result)
# print()
#
# if my_queue.contains(200):
#     print("YES")

# ====================================================================================================
# pip install structlinks
# from structlinks.DataStructures.Stack import Stack
#
# my_stack = Stack([100, 200, 300])
# print("STACK:")
# print(my_stack)
#
# my_stack.push(400)
# print("STACK:")
# print(my_stack)
# print()
#
# pop_result = my_stack.pop()
# print("STACK:")
# print(my_stack)
# print("POP ITEM:", pop_result)
# print()


# from structlinks.DataStructures import Queue
#
# my_queue = Queue([300, 200, 100])
# print("QUEUE:")
# print(my_queue)
# print()
#
# my_queue.enqueue(400)
# print("QUEUE:")
# print(my_queue)
# print()
#
# dequeue_result = my_queue.dequeue()
# print("QUEUE:")
# print(my_queue)
# print("DEQUEUE ITEM:", dequeue_result)
# print()

# ==============================================LESSON64==============================================
# Односвязный и двусвязный список.


# class Node:
#     value = None
#     next_node = None
#
#     def __init__(self, value=None, next_node=None):
#         self.value = value
#         self.next_node = next_node
#
#     def __str__(self):
#         return str(self.value)
#
#     def copy(self):
#         return Node(self.value, self.next_node)
#
#
# class LinkedList:
#     __head = None
#     __size = 0
#
#     def __init__(self):
#         self.__head = None
#         self.__size = 0
#
#     def __str__(self):
#         result = ""
#         current_node = self.__head
#         if self.__size >= 1:
#             result += "{}->".format(current_node)
#         if self.__size >= 2:
#             while current_node.next_node:
#                 current_node = current_node.next_node
#                 result += "{}->".format(current_node)
#         result += "None"
#         return result
#
#     def get_head(self):
#         return self.__head
#
#     def insert(self, index, item):
#         new_node = Node(item)
#         if index <= 0:
#             new_node.next_node = self.__head
#             self.__head = new_node
#             self.__size += 1
#         else:
#             if self.__head is None:
#                 self.__head = new_node
#             else:
#                 pre_node = None
#                 current_node = self.__head
#                 i = 0
#                 while current_node and i < index:
#                     pre_node = current_node
#                     current_node = current_node.next_node
#                     i += 1
#                 if current_node:
#                     new_node.next_node = current_node
#                 pre_node.next_node = new_node
#                 self.__size += 1
#
#     def remove(self, index):
#         if self.__head:
#             if index <= 0:
#                 self.__head = self.__head.next_node
#             else:
#                 pre_node = None
#                 current_node = self.__head
#                 i = 0
#                 while current_node.next_node and i < index:
#                     pre_node = current_node
#                     current_node = current_node.next_node
#                     i += 1
#                 pre_node.next_node = current_node.next_node
#             self.__size -= 1
#
#     def find(self, item):
#         index = -1
#         if self.__head:
#             current_node = self.__head
#             i = 0
#             while i < self.__size and current_node:
#                 if current_node.value == item:
#                     index = i
#                     break
#                 current_node = current_node.next_node
#                 i += 1
#         return index
#
#
# my_linked_list = LinkedList()
# print(my_linked_list)
# print()
#
# my_linked_list.insert(5, 100)
# # print(my_linked_list)
# # print()
#
# my_linked_list.insert(6, 200)
# # print(my_linked_list)
# # print()
#
# my_linked_list.insert(20, 300)
# # print(my_linked_list)
# # print()
#
# my_linked_list.insert(0, 400)
# # print(my_linked_list)
# # print()
#
# my_linked_list.insert(1, 600)
# # print(my_linked_list)
# # print()
#
# my_linked_list.insert(5, 700)
# print(my_linked_list)
# print()
#
# my_linked_list.remove(0)
# print(my_linked_list)
# print()
#
# my_linked_list.remove(20)
# print(my_linked_list)
# print()
#
# my_linked_list.remove(1)
# print(my_linked_list)
# print()
#
# print(my_linked_list.find(300))

# ====================================================================================================
# pip install structlinks
# LinkedList
# from structlinks.DataStructures import LinkedList
#
# my_linked_list = LinkedList([1, 10, 3, 5])
# print(my_linked_list)
#
# length = len(my_linked_list)
# print(length)
#
# my_linked_list.append(2)
# print(my_linked_list)
#
# my_linked_list.insert(0, 200)
# print(my_linked_list)
#
# item = my_linked_list[1]
# print(item)
#
# my_linked_list[2] = 100
# print(my_linked_list)
#
# part = my_linked_list[2:]
# print(part)
#
# popped = my_linked_list.pop(0)
# print(my_linked_list)
# print("POPPED ITEM:", popped)
#
# my_linked_list.remove(1)
# print(my_linked_list)
#
# print(2 in my_linked_list)
# print(1 in my_linked_list)


# DoublyLinkedList
# from structlinks.DataStructures import DoublyLinkedList
#
# my_double_linked_list = DoublyLinkedList([1, 10, 3, 5])
# print(my_double_linked_list)
#
# length = len(my_double_linked_list)
# print(length)
#
# my_double_linked_list.append(2)
# print(my_double_linked_list)
#
# my_double_linked_list.insert(0, 200)
# print(my_double_linked_list)
#
# item = my_double_linked_list[1]
# print(item)
#
# my_double_linked_list[2] = 100
# print(my_double_linked_list)
#
# part = my_double_linked_list[2:]
# print(part)
#
# popped = my_double_linked_list.pop(0)
# print(my_double_linked_list)
# print("POPPED ITEM:", popped)
#
# my_double_linked_list.remove(1)
# print(my_double_linked_list)
#
# print(2 in my_double_linked_list)
# print(1 in my_double_linked_list)
