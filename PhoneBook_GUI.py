from tkinter import *
from tkinter import ttk

version = "v1.1.0001"

phone_book = dict()


def clear():
    input_tel.delete(0, END)
    input_last_name.delete(0, END)
    input_first_name.delete(0, END)
    input_patronymic.delete(0, END)
    input_address.delete(0, END)


def add():
    value = list()
    value.append(input_last_name.get())
    value.append(input_first_name.get())
    value.append(input_patronymic.get())
    value.append(input_address.get())
    phone_book[input_tel.get()] = value


window = Tk()
window.title("PhoneBook")
window.geometry("400x200")

label_tel = Label(text="Номер телефона")
label_tel.grid(row=0, column=0, padx=10, pady=5, sticky="w")

input_tel = ttk.Entry()
input_tel.grid(row=0, column=1)

label_last_name = Label(text="Фамилия")
label_last_name.grid(row=1, column=0, padx=10, pady=5, sticky="w")

input_last_name = ttk.Entry()
input_last_name.grid(row=1, column=1)

label_first_name = Label(text="Имя")
label_first_name.grid(row=2, column=0, padx=10, pady=5, sticky="w")

input_first_name = ttk.Entry()
input_first_name.grid(row=2, column=1)

label_patronymic = Label(text="Отчество")
label_patronymic.grid(row=3, column=0, padx=10, pady=5, sticky="w")

input_patronymic = ttk.Entry()
input_patronymic.grid(row=3, column=1)

label_address = Label(text="Адрес")
label_address.grid(row=4, column=0, padx=10, pady=5, sticky="w")

input_address = ttk.Entry()
input_address.grid(row=4, column=1)

button_add = ttk.Button(text="Добавить", command=add)
button_add.grid(row=1, column=2, padx=38)

button_clear = ttk.Button(text="Удалить", command=clear)
button_clear.grid(row=3, column=2, padx=38)

window.mainloop()
