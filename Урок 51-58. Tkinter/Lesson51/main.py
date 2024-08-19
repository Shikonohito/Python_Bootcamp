# ==============================================LESSON51==============================================
# Позиционирование. Label, Entry, Button.

# import tkinter
#
# root = tkinter.Tk()
# root.geometry("600x250+800+400")
# root.resizable(False, False)
#
# root.title("Приложение на Tkinter")
#
#
# # PACK
# # side - top, bottom, left, right - от какого края заполнять.
# # Например от top будет заполняться сверху вниз, но может расширяться влево и вправо.
# # expand - True, False - резервирует виджету оставшееся свободное место.
# # fill - x, y, Both, None - заполняет виджетом всё его резервированное место по указанным направлениям.
# label_1 = tkinter.Label(root, text="label_1", background="red", font=("Arial", 20))
# label_1.pack(side="left", fill="both")
#
# label_2 = tkinter.Label(root, text="label_2", background="blue", font=("Arial", 20))
# label_2.pack(side="top", fill="both", expand=True)
#
# label_3 = tkinter.Label(root, text="label_3", background="green", font=("Arial", 20))
# label_3.pack(side="top", fill="both")
#
#
# # FRAME & GRID
# user_data_frame = tkinter.LabelFrame(root, text="User Information")
# user_data_frame.pack(expand=True, fill="both")
# user_data_frame.grid_configure(padx=10, pady=5)
#
# for widget in user_data_frame.winfo_children():
#     widget.grid_configure(padx=10, pady=5)
#
# label_1 = tkinter.Label(user_data_frame, text="label_1", background="red", font=("Arial", 20))
# label_1.grid(row=0, column=0, sticky="w")
#
# label_2 = tkinter.Label(user_data_frame, text="label_2", background="blue", font=("Arial", 20))
# label_2.grid(row=0, column=1, sticky="n")
#
# label_3 = tkinter.Label(user_data_frame, text="label_3", background="green", font=("Arial", 20))
# label_3.grid(row=0, column=2, sticky="e")
#
# entry_1 = tkinter.Entry(user_data_frame, font=("Arial", 12))
# entry_1.grid(row=1, column=0)
#
# entry_2 = tkinter.Entry(user_data_frame, font=("Arial", 12))
# entry_2.grid(row=1, column=1)
#
# entry_3 = tkinter.Entry(user_data_frame, font=("Arial", 12))
# entry_3.grid(row=1, column=2)
#
#
# # PLACE
# label_1 = tkinter.Label(root, text="label_1", background="red", font=("Arial", 20))
# label_1.place(y=0, x=0, height=100, width=100)
#
# label_3 = tkinter.Label(root, text="label_3", background="green", font=("Arial", 20))
# label_3.place(y=0, x=200, height=100, width=100)
#
# label_2 = tkinter.Label(root, text="label_2", background="blue", font=("Arial", 20))
# label_2.place(y=50, x=100)
#
# root.mainloop()


# ====================================================================================================


# import tkinter
#
# root = tkinter.Tk()
# root.geometry("600x250")
# root.resizable(False, False)
# root.title("Lesson51")
#
# user_data_frame = tkinter.Frame(root)
# user_data_frame.pack(expand=True, fill="both")
#
# user_name_label = tkinter.Label(user_data_frame, text="Name:", font=("Arial", 18))
# user_age_label = tkinter.Label(user_data_frame, text="Age:", font=("Arial", 18))
# user_name_label.place(y=20, x=20)
# user_age_label.place(y=20, x=300)
#
# user_name_entry = tkinter.Entry(user_data_frame, font=("Arial", 18))
# user_age_entry = tkinter.Entry(user_data_frame, font=("Arial", 18))
# user_name_entry.place(y=60, x=20)
# user_age_entry.place(y=60, x=300)
#
#
# def console_print():
#     name = user_name_entry.get()
#     age = int(user_age_entry.get())
#     print(name, age)
#
#     result = f"{name}\n{age}"
#     user_result_label.config(text=result, justify="left")
#
#
# user_confirm_btn = tkinter.Button(text="Confirm", command=console_print, font=("Arial", 18))
# user_confirm_btn.place(y=180, x=400)
#
# user_result_label = tkinter.Label(text="TEXT", font=("Arial", 18))
# user_result_label.place(y=180, x=20)
#
# root.mainloop()

# ====================================================================================================
# ПЗ 51.1
# ====================================================================================================
