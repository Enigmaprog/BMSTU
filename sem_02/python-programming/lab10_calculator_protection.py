from tkinter import *
from tkinter import messagebox

import parser

root = Tk()
root.title("Перевод системы счисления")
root.geometry('330x80')
text_pragromma = "Программа: Перевод, который переводит из десятичной системы \
                 в шестиречную ситему счислений\n"
text_avtor = "Автор: Батбилэг Номуундалай Программист из BND "
def pragromma():
    messagebox.showinfo("О программе", text_pragromma)
def avtor():
    messagebox.showinfo("О разработчике", text_avtor)
def ustgal():
    a.delete(0, END)
def perevod():
    try:
        x = int(a.get())
        if x > 0 and int:
            n= " "
            while x > 0:
                y = str(x%6)
                x = int(x / 6)
                n = y + n
            messagebox.showinfo("Ответ", n)
        else:
            messagebox.showinfo("Ошибка","Извините вы вели отрицательное число")
    except:
        messagebox.showinfo("Ошибка","Извините вводите числа")



#поле
a = StringVar()
a = Entry(textvariable=a, width=50)
a.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

#кнопки
bvrustgal = Button(text="C", command = ustgal, width=20)
bvrustgal.grid(row=2 ,column=1 ,padx=5 ,pady=5)
hurwuult = Button(text="10-->6", command = perevod, width=20)
hurwuult.grid(row=2 ,column=2, padx=5 ,pady=5)

#меню
main_menu = Menu(tearoff = 0)
m_menu = Menu(tearoff = 0)
m_menu.add_command(label="о программе", command=pragromma)
m_menu.add_command(label="о авторе", command=avtor)
main_menu.add_cascade(label="меню", menu=m_menu)
root. config(menu=main_menu)


root.mainloop()