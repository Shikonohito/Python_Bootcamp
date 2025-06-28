import tkinter

root = tkinter.Tk()
root.title("Num sum")
root.geometry("610x260")
root.resizable(False, False)

frame = tkinter.Frame(root)
frame.pack(expand=True, fill="both")

num_1_lbl = tkinter.Label(frame, text="First number:", font=("Arial", 18))
num_1_lbl.place(x=20, y=20)

num_2_lbl = tkinter.Label(frame, text="Second number:", font=("Arial", 18))
num_2_lbl.place(x=320, y=20)


# def entry_is_float(data_input: str):
#     count_dot = data_input.count(".")
#
#     if data_input == "":
#         return True
#     elif count_dot <= 1:
#         symb_nums = ".0123456789"
#         is_num = False
#         for symb in data_input:
#             is_num = False
#             for num in symb_nums:
#                 if symb == num:
#                     is_num = True
#                     break
#             if not is_num:
#                 break
#         return is_num
#     else:
#         return False
#
#
# def entry_is_int(data_input: str):
#     count_dot = data_input.count(".")
#     print(count_dot)
#     if data_input:
#         print(data_input)
#         return True
#
#     elif data_input == "":
#         print(data_input)
#         return True
#
#     else:
#         print(data_input)
#         return False
#
#
# reg = frame.register(entry_is_float)
# num_1_entry = tkinter.Entry(frame, font=("Arial", 18), validate="key", validatecommand=(reg, "%P"))
# num_2_entry = tkinter.Entry(frame, font=("Arial", 18), validate="key", validatecommand=(reg, "%P"))
# num_1_entry.place(x=20, y=60)
# num_2_entry.place(x=320, y=60)


num_1_entry = tkinter.Entry(frame, font=("Arial", 18))
num_1_entry.place(x=20, y=60)

num_2_entry = tkinter.Entry(frame, font=("Arial", 18))
num_2_entry.place(x=320, y=60)

result_lbl = tkinter.Label(frame, text="0", font=("Arial", 18))
result_lbl.place(x=20, y=200)


def find_sum():
    num_1 = num_1_entry.get()
    num_2 = num_2_entry.get()

    if num_1 != "" and num_2 != "":
        num_1 = float(num_1)
        num_2 = float(num_2)
        result = str(num_1 + num_2)
        result_lbl.config(text=result)


sum_btn = tkinter.Button(frame, text="+", font=("Arial", 18), command=find_sum)
sum_btn.place(x=20, y=120)


def find_dif():
    num_1 = num_1_entry.get()
    num_2 = num_2_entry.get()

    if num_1 != "" and num_2 != "":
        num_1 = float(num_1)
        num_2 = float(num_2)
        result = str(num_1 - num_2)
        result_lbl.config(text=result)


dif_btn = tkinter.Button(frame, text="-", font=("Arial", 18), command=find_dif)
dif_btn.place(x=60, y=120)


def find_prod():
    num_1 = num_1_entry.get()
    num_2 = num_2_entry.get()

    if num_1 != "" and num_2 != "":
        num_1 = float(num_1)
        num_2 = float(num_2)
        result = str(num_1 * num_2)
        result_lbl.config(text=result)


prod_btn = tkinter.Button(frame, text="*", font=("Arial", 18), command=find_prod)
prod_btn.place(x=100, y=120)


def find_div():
    num_1 = num_1_entry.get()
    num_2 = num_2_entry.get()

    if num_1 != "" and num_2 != "":
        num_1 = float(num_1)
        num_2 = float(num_2)
        if num_2 != 0:
            result = str(num_1 / num_2)
        else:
            result = "Divided by Zero"
        result_lbl.config(text=result)


div_btn = tkinter.Button(frame, text="/", font=("Arial", 18), command=find_div)
div_btn.place(x=140, y=120)


# def hide_frame():
#     frame.pack_forget()
#
#
# hide_frame_btn = tkinter.Button(root, text="Hide frame", font=("Arial", 18), command=hide_frame)
# hide_frame_btn.place(x=390, y=200)
#
#
# def show_frame():
#     frame.pack(expand=True, fill="both")
#
#
# show_frame_btn = tkinter.Button(root, text="Show frame", font=("Arial", 18), command=show_frame)
# show_frame_btn.place(x=200, y=200)

root.mainloop()