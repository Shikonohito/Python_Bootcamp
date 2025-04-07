import tkinter
from tkinter import ttk
from tkinter import messagebox

def enter_data():
    accept = accept_var.get()
    if accept == "Accepted":
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        if first_name and last_name:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()
            registration_status = reg_status_var.get()
            result = "{} {} {}. Age is {}. Nationality is {}.\nRegistration status: {}.\n{} completed courses in {} semesters.\n".\
                format(title, first_name, last_name, age, nationality, registration_status, numcourses, numsemesters)
            print(result)

            tkinter.messagebox.showinfo(title="User info", message=result)
        else:
            tkinter.messagebox.showerror(title="Error", message="First name and last name are required.")
    else:
        tkinter.messagebox.showerror(title="Error", message="You have not accepted the terms.")

root = tkinter.Tk()
root.title("Data Entyry Form")

frame = tkinter.Frame(root)
frame.pack()

user_info_frame = tkinter.LabelFrame(frame, text="User Informaion")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)

last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)

last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_label.grid(row=0, column=2)

title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_label.grid(row=2, column=0)

age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=123)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_label.grid(row=2, column=1)

nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia",
                                                             "Europe", "North America", "Oceania", "South America"])
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Registration Status")
registered_label.grid(row=0, column=0)

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not registered")
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="# Completed Courses")
numcourses_label.grid(row=0, column=1)

numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
numsemesters_label.grid(row=0, column=2)

numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=20)

root.mainloop()
