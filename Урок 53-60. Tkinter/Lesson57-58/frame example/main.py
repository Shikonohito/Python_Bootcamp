import tkinter

root = tkinter.Tk()
root.title("Frames")
root.geometry("610x260")
root.resizable(False, False)

first_frame = tkinter.Frame(root)
first_frame.pack(expand=True, fill="both")

second_frame = tkinter.Frame(root)
second_frame.pack_forget()


def switch_to_first_frame():
    # Скрываем всё, что не нужно
    second_frame.pack_forget()

    # Изменяем размеры окна, если хотим
    root.geometry("610x260")

    # Показываем всё, что требуется показать
    first_frame.pack(expand=True, fill="both")


def switch_to_second_frame():
    # Скрываем всё, что не нужно
    first_frame.pack_forget()

    # Изменяем размеры окна, если хотим
    root.geometry("610x560")

    # Показываем всё, что требуется показать
    second_frame.pack(expand=True, fill="both")


# BEGIN FIRST FRAME
switch_to_second_frame_btn = tkinter.Button(first_frame, text="Second frame", font=("Arial", 18), command=switch_to_second_frame)
switch_to_second_frame_btn.place(x=390, y=200)

num_1_lbl = tkinter.Label(first_frame, text="First number:", font=("Arial", 18))
num_2_lbl = tkinter.Label(first_frame, text="Second number:", font=("Arial", 18))
num_1_lbl.place(x=20, y=20)
num_2_lbl.place(x=320, y=20)


num_1_entry = tkinter.Entry(first_frame, font=("Arial", 18))
num_2_entry = tkinter.Entry(first_frame, font=("Arial", 18))
num_1_entry.place(x=20, y=60)
num_2_entry.place(x=320, y=60)

sum_lbl = tkinter.Label(first_frame, text="0", font=("Arial", 18))
sum_lbl.place(x=20, y=200)


def find_sum():
    num_1 = num_1_entry.get()
    num_2 = num_2_entry.get()

    if num_1 != "" and num_2 != "":
        num_1 = float(num_1)
        num_2 = float(num_2)
        result = str(num_1 + num_2)
        sum_lbl.config(text=result)


sum_btn = tkinter.Button(first_frame, text="+", font=("Arial", 18), command=find_sum)
sum_btn.place(x=20, y=120)


def find_dif():
    num_1 = num_1_entry.get()
    num_2 = num_2_entry.get()

    if num_1 != "" and num_2 != "":
        num_1 = float(num_1)
        num_2 = float(num_2)
        result = str(num_1 - num_2)
        sum_lbl.config(text=result)


sum_btn = tkinter.Button(first_frame, text="-", font=("Arial", 18), command=find_dif)
sum_btn.place(x=60, y=120)


def find_prod():
    num_1 = num_1_entry.get()
    num_2 = num_2_entry.get()

    if num_1 != "" and num_2 != "":
        num_1 = float(num_1)
        num_2 = float(num_2)
        result = str(num_1 * num_2)
        sum_lbl.config(text=result)


sum_btn = tkinter.Button(first_frame, text="*", font=("Arial", 18), command=find_prod)
sum_btn.place(x=100, y=120)


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
        sum_lbl.config(text=result)


sum_btn = tkinter.Button(first_frame, text="/", font=("Arial", 18), command=find_div)
sum_btn.place(x=140, y=120)
# END FIRST FRAME

# BEGIN SECOND FRAME
switch_to_first_frame_btn = tkinter.Button(second_frame, text="First frame", font=("Arial", 18), command=switch_to_first_frame)
switch_to_first_frame_btn.place(x=400, y=400)

some_list = ["FIRST ITEM", "SECOND ITEM", "THIRD ITEM"]

some_listbox = tkinter.Listbox(second_frame, font=("Arial", 18), height=13)
some_listbox.place(x=20, y=20)

def fill_listbox():
    some_listbox.delete(0, tkinter.END)
    for item in some_list:
        some_listbox.insert(tkinter.END, str(item))


fill_listbox()
# END SECOND FRAME

root.mainloop()