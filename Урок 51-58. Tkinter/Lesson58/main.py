# ==============================================LESSON58==============================================
# Виджеты - Combobox, Radiobutton, Spinbox, Checkbutton, Treeview

import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.geometry("720x680")
root.resizable(False, False)

test_frame = tkinter.Frame(root)
test_frame.pack(expand=True, fill="both")


# # COMBOBOX
# day_combobox = ttk.Combobox(test_frame, width=27, font=("Arial", 16), state="readonly")
# day_combobox["values"] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# day_combobox.place(x=20, y=20)
# day_combobox.current(0)
#
#
# def test_combobox():
#     result = day_combobox.get()
#     print(result)
#
#
# combobox_test_btn = tkinter.Button(test_frame, text="Get combobox", font=("Arial", 16), command=test_combobox)
# combobox_test_btn.place(x=500, y=20)


# # RADIOBUTTON
# def test_radiobutton():
#     print(radiobutton_var.get())
#
#
# radiobutton_var = tkinter.IntVar()
# radiobutton_var.set(1)
# radiobutton_1 = tkinter.Radiobutton(test_frame, text="YES", variable=radiobutton_var, value=1,
#                                     command=test_radiobutton, font=("Arial", 12))
# radiobutton_2 = tkinter.Radiobutton(test_frame, text="NO", variable=radiobutton_var, value=2,
#                                     command=test_radiobutton, font=("Arial", 12))
# radiobutton_1.place(x=200, y=500)
# radiobutton_2.place(x=200, y=520)


# # SPINBOX
# age_lbl = tkinter.Label(test_frame, text="Age:", font=("Arial", 16))
# age_lbl.place(x=20, y=100)
# age_spinbox = tkinter.Spinbox(test_frame, from_=0, to="infinity", font=("Arial", 16), state="readonly")
# age_spinbox.place(x=20, y=140)
#
#
# def test_spinbox():
#     result = age_spinbox.get()
#     print(result)
#
#
# spinbox_test_btn = tkinter.Button(test_frame, text="Get spinbox", font=("Arial", 16), command=test_spinbox)
# spinbox_test_btn.place(x=500, y=100)


# # CHECKBUTTON
# def test_checkbutton():
#     print(checkbutton_var.get())
#
#
# checkbutton_var = tkinter.StringVar(value="YES")
# checkbutton = tkinter.Checkbutton(test_frame, text="Accepted Terms and Conditions", variable=checkbutton_var,
#                                   onvalue="YES", offvalue="NO", command=test_checkbutton, font=("Arial", 12))
# checkbutton.place(x=20, y=600)
# # OR
# # checkbutton_var = tkinter.BooleanVar(value=True)
# # checkbutton = tkinter.Checkbutton(test_frame, text="Accepted Terms and Conditions", variable=checkbutton_var,
# #                                   onvalue=True, offvalue=False, command=test_checkbutton, font=("Arial", 12))
# # checkbutton.place(x=20, y=600)


# # SWITCHER
# def switch_color():
#     color = test_button.cget("bg")
#     if color == "blue":
#         color = "red"
#     elif color == "red":
#         color = "blue"
#     test_button.config(bg=color)
#
#
# test_button = tkinter.Button(test_frame, text="1", bg="blue", command=switch_color, height=2, width=5)
# test_button.place(x=400, y=20)


# HIDE ENTRY FILLING
# test_entry_1 = tkinter.Entry(test_frame, show="*", font=("Arial", 16), width=10)
# test_entry_1.place(x=500, y=160)


# # HIDE ENTRY AND TEMPLATE ENTRY
# test_entry_2 = tkinter.Entry(test_frame, font=("Arial", 16), width=10, fg="grey")
# test_entry_2.place(x=500, y=200)
# test_entry_2.insert(0, "Password")
#
#
# def handle_focus_in(event):
#     if test_entry_2["fg"] == "grey":
#         test_entry_2.config(show="*")
#         test_entry_2.delete(0, tkinter.END)
#         test_entry_2.config(fg='black')
#
#
# def handle_focus_out(event):
#     if test_entry_2.get() == "":
#         test_entry_2.config(fg='grey', show="")
#         test_entry_2.insert(0, "Password")
#
#
# def handle_enter(txt):
#     print(test_entry_2.get())
#     root.focus()
#
#
# test_entry_2.bind("<FocusIn>", handle_focus_in)
# test_entry_2.bind("<FocusOut>", handle_focus_out)
# test_entry_2.bind("<Return>", handle_enter)


# # TREEVIEW
# class Customer:
#     id = -1
#     name = str()
#     age = int()
#
#     def __init__(self, name, age, id):
#         self.name = name
#         self.age = age
#         self.id = id
#
#     def __str__(self):
#         return "{} {} {}".format(self.id, self.name, self.age)
#
#
# customer_1 = Customer("Tom", 25, 120)
# customer_2 = Customer("Bob", 27, 109)
# customer_3 = Customer("Jim", 34, 586)
# customer_list = list([customer_1, customer_2, customer_3])
#
# customer_treeview_columns = ("id", "name", "age")
# customer_treeview = ttk.Treeview(test_frame, columns=customer_treeview_columns, show="headings")
# customer_treeview.place(x=20, y=200)
# customer_treeview.heading(customer_treeview_columns[0], text="ID")
# customer_treeview.heading(customer_treeview_columns[1], text="Name")
# customer_treeview.heading(customer_treeview_columns[2], text="Age")
#
# for customer in customer_list:
#     temp_tuple = (customer.id, customer.name, customer.age)
#     customer_treeview.insert("", tkinter.END, iid=customer.id, values=temp_tuple)
#
# customer_treeview.insert(109, tkinter.END, values=(000, f"{customer_2.id}'s child", 0))
#
#
# def item_selected(event):
#     print("SELECTED:")
#     for index in customer_treeview.selection():
#         print(index)
#         item = customer_treeview.item(index)
#         print(item)
#         print(item["values"])
#         print(type(item["values"][0]))
#     print()
#
#
# customer_treeview.bind("<<TreeviewSelect>>", item_selected)
#
#
# def delete_customer():
#     for index in customer_treeview.selection():
#         item = customer_treeview.item(index)
#         customer_id = item["values"][0]
#
#         for i in range(len(customer_list) - 1, -1, -1):
#             if customer_id == customer_list[i].id:
#                 del customer_list[i]
#         customer_treeview.detach(index)
#
#     print("AFTER DELETE")
#     for cust in customer_list:
#         print(cust)
#     print()
#
#
# delete_data_btn = tkinter.Button(test_frame, text="Delete", font=("Arial", 16), command=delete_customer)
# delete_data_btn.place(x=20, y=440)


root.mainloop()

# ====================================================================================================
# Python - PT58
# ====================================================================================================
