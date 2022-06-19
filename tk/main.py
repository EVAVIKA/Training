from tkinter import *
from tkinter import messagebox

def cont(name, mail, password):
    if check_password(password):
        messagebox.showinfo('information', name + '\n' + mail + '\n' + password)
    else:
        messagebox.showerror('error', 'Неправильный пароль, переделай')

def check_password(password):
    if len(password) < 8 or password == password.lower():
        return False 
    return True 

window = Tk()
window.title('Регистрация')
window.geometry('800x600')
window.grid_columnconfigure(0, weight = 1)
window.grid_columnconfigure(1, weight = 1)
window.grid_columnconfigure(2, weight = 1)

label_name = Label(window, text = 'Имя') 
label_name.grid(column = 1, row = 0, sticky = W)
entry_name = Entry(window, width = 150)
entry_name.grid(column = 1, row = 1)

label_mail = Label(window, text = 'Почта') 
label_mail.grid(column = 1, row = 2, sticky = W)
entry_mail = Entry(window, width = 150)
entry_mail.grid(column = 1, row = 3)

label_password = Label(window, text = 'Пароль') 
label_password.grid(column = 1, row = 4, sticky = W)
entry_password = Entry(window, show = '•', width = 150)
entry_password.grid(column = 1, row = 5)

Label(window).grid(column = 1, row = 6)

button = Button(window, text = 'Далее', command = lambda: cont(entry_name.get(), entry_mail.get(), entry_password.get()) )
button.grid(column = 1, row = 7, sticky = E)

window.mainloop()
