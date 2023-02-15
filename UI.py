import customtkinter as CTk
import tkinter as Tk
import sqlite3

# настройка темы интерфейса
CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("blue")

# переменные
password = ()
login = ()

data_read = {}


# функция ввывода
def prin():
    global password
    global login
    text_password.configure(state='normal')
    text_login.configure(state='normal')
    password = (entry_password.get())
    login = (entry_login.get())
    if password != '' and login != '' and password != "пустота" and login != "пустота":
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            data_login = [(login, password)]
            cursor.executemany("INSERT INTO data(login,password) VALUES(?,?)", data_login)
        cursor.execute("SELECT * FROM data")
        print(cursor.fetchall())
    else:
        entry_password.delete(0, Tk.END)
        entry_login.delete(0, Tk.END)
        entry_password.insert(Tk.END, "пустота")
        entry_login.insert(Tk.END, "пустота")

    text_password.configure(state='disable')
    text_login.configure(state='disable')


# функция добавления данных в бд
def serch():
    global login
    global password
    password = (entry_password.get())
    login = (entry_login.get())
    text_password.configure(state='normal')
    text_login.configure(state='normal')
    text_login.delete(0.0, Tk.END)
    text_password.delete(0.0, Tk.END)
    password_get = (entry_password.get())
    login_get = (entry_login.get())

    if password == login == '':
        entry_password.insert(Tk.END, "пустота")
        entry_login.insert(Tk.END, "пустота")

    elif login != '' or password != '':
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()

            loginC = cursor.execute("SELECT login FROM data WHERE password = '{}';".format(password_get))
            loginC = (cursor.fetchall())
            login_len = (len(loginC))
            print("login" + str(loginC))
            if loginC == [] and password_get != '' and password_get != 'поиск по логину':
                text_login.insert(Tk.END, 'ничего не найдено')
            for i in range(login_len):
                text_login.insert(Tk.END, f'{loginC[i]}\n')

            passwordC = cursor.execute("SELECT password FROM data WHERE login = '{}';".format(login_get))
            passwordC = (cursor.fetchall())
            password_len = (len(passwordC))
            print("password" + str(passwordC))
            if passwordC == [] and login_get != '' and login_get != 'поиск по паролю':
                text_password.insert(Tk.END, 'ничего не найдено')
            for j in range(password_len):
                text_password.insert(Tk.END, f'{passwordC[j]}\n')

    if password == '' or password == "поиск по логину":
        print(password)
        entry_password.delete(0, Tk.END)
        entry_password.insert(Tk.END, "поиск по логину")
    elif login == '' or login == "поиск по паролю":
        print(login)
        entry_login.delete(0, Tk.END)
        entry_login.insert(Tk.END, "поиск по паролю")

    text_password.configure(state='disable')
    text_login.configure(state='disable')


# настройка интерфейса
window = CTk.CTk()
window.title('a_p')
window.geometry('600x460')
window.resizable(False, False)

CTk.CTkLabel(window, text_color="black", text="Администратор Паролей", corner_radius=60, fg_color="white") \
    .place(x=210, y=15)

crt = CTk.CTkFrame(window, width=550, height=400)
crt.place(x=25, y=50)

btn_serch = CTk.CTkButton(window, text="Найти", command=serch)  # создание кнопки найти
btn_serch.place(x=60, y=30)

btn_print = CTk.CTkButton(window, text="Занести", command=prin)  # создание кнопки занести
btn_print.place(x=400, y=30)

text_login = CTk.CTkTextbox(window, height=130, width=225, text_color="brown")
text_login.configure(state='disable')
text_login.place(x=335, y=120)
text_t_login = CTk.CTkLabel(window, text="Логин", text_color="brown", width=225).place(x=335, y=92)
text_t_login_2 = CTk.CTkLabel(window, text="Логин", text_color="brown", width=225).place(x=40, y=92)
entry_login = CTk.CTkEntry(window, width=225, height=130, text_color="brown")
entry_login.place(x=40, y=120)

text_password = CTk.CTkTextbox(window, height=130, width=225, text_color="green")
text_password.configure(state='disable')
text_password.place(x=335, y=292)
text_t_password = CTk.CTkLabel(window, text="Пароль", text_color="green", width=225).place(x=335, y=264)
text_t_password_2 = CTk.CTkLabel(window, text="Пароль", text_color="green", width=225).place(x=40, y=264)
entry_password = CTk.CTkEntry(window, width=225, height=130, text_color="green")
entry_password.place(x=40, y=292)

window.mainloop()  # конец
