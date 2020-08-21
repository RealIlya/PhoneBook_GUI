from tkinter import *
from tkinter import ttk
import os

version = "v1.3"

phone_book = dict()
tel_list = list()


def clear():
    input_tel.delete(0, END)
    input_last_name.delete(0, END)
    input_first_name.delete(0, END)
    input_patronymic.delete(0, END)
    input_address.delete(0, END)


def add():
    _tel_ = input_tel.get()
    if _tel_ in phone_book:
        label_info.config(text="! Такой номер уже существует !", fg="red")
    else:
        _value_ = list()
        _value_.append(input_last_name.get())
        _value_.append(input_first_name.get())
        _value_.append(input_patronymic.get())
        _value_.append(input_address.get())
        phone_book[_tel_] = _value_

        list_tel.insert(END, _tel_)


def save_in_file():
    with open("PhoneBook.csv", "w") as file:
        for tel in phone_book:
            value = phone_book[tel]
            temp = tel + ";" + value[0] + ";" + value[1] + \
                   ";" + value[2] + ";" + "\n"
            file.write(temp)


def output_data(tel_):
    value_ = phone_book[tel_]
    last_name_ = value_[0]
    first_name_ = value_[1]
    patronymic_ = value_[2]
    address_ = value_[3]

    clear()
    input_tel.insert(0, tel_)
    input_last_name.insert(0, last_name_)
    input_first_name.insert(0, first_name_)
    input_patronymic.insert(0, patronymic_)
    input_address.insert(0, address_)


def select_list_tel(event):
    w = event.widget
    i = int(w.curselection()[0])
    tel = w.get(i)

    output_data(tel)


def search():
    search_text = input_search.get()
    if search_text in phone_book:
        output_data(search_text)
    else:
        for key, item in phone_book.items():
            for val in item:
                if val == search_text:
                    output_data(key)
            else:
                label_info.config(text="Ничего не найдено", fg="red")


window = Tk()
window.title(f"PhoneBook {version}")
window.geometry("550x270")

label_search = Label(text="Поиск")
label_search.grid(row=0, column=0, padx=10, pady=5, sticky="e")

input_search = Entry()
input_search.grid(row=0, column=1, padx=10, pady=5)

label_tel = Label(text="Номер телефона")
label_tel.grid(row=1, column=0, padx=10, pady=5, sticky="w")

input_tel = ttk.Entry()
input_tel.grid(row=1, column=1)

label_last_name = Label(text="Фамилия")
label_last_name.grid(row=2, column=0, padx=10, pady=5, sticky="w")

input_last_name = ttk.Entry()
input_last_name.grid(row=2, column=1)

label_first_name = Label(text="Имя")
label_first_name.grid(row=3, column=0, padx=10, pady=5, sticky="w")

input_first_name = ttk.Entry()
input_first_name.grid(row=3, column=1)

label_patronymic = Label(text="Отчество")
label_patronymic.grid(row=4, column=0, padx=10, pady=5, sticky="w")

input_patronymic = ttk.Entry()
input_patronymic.grid(row=4, column=1)

label_address = Label(text="Адрес")
label_address.grid(row=5, column=0, padx=10, pady=5, sticky="w")

input_address = ttk.Entry()
input_address.grid(row=5, column=1, pady=10)

label_info = Label(text="Программа готова к работе...")
label_info.grid(row=6, column=0, columnspan=26)

button_add = ttk.Button(text="Добавить", command=add)
button_add.grid(row=1, column=2, padx=38)

button_save = ttk.Button(text="Сохранить", command=save_in_file)
button_save.grid(row=2, column=2, padx=38)

button_clear = ttk.Button(text="Удалить", command=clear)
button_clear.grid(row=3, column=2, padx=38)

label_list_tel = Label(text="Список телефонов")
label_list_tel.grid(row=0, column=3)

button_search = ttk.Button(text="Найти", command=search)
button_search.grid(row=0, column=2, padx=10)

list_tel = Listbox()
list_tel.grid(row=1, column=3, rowspan=4)

# <<ListboxSelect>> связывает Listbox и поля ввода
list_tel.bind('<<ListboxSelect>>', select_list_tel)

if os.path.exists("PhoneBook.csv"):
    with open("PhoneBook.csv", "r") as file:
        lines = file.readlines()
        for line in lines:
            elements = line.split(";")  # split игнорирует ;
            # (номер);(имя);(фамилия);(отчество);(адрес)
            tel = elements[0]
            last_name = elements[1]
            first_name = elements[2]
            patronymic = elements[3]
            address = elements[4]

            value = list()
            value.append(last_name)
            value.append(first_name)
            value.append(patronymic)
            value.append(address)
            phone_book[tel] = value

            list_tel.insert(END, tel)

window.mainloop()
