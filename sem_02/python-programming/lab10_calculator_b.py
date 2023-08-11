from tkinter import *
from tkinter import messagebox
import math as m

text_pragromma = "Программа: Калькулятор, который действует три действия вычисления,\
 точнее плюс[+], минус[-] и корень. Кроме цифри[0,1,2,3,4,5,6,7,8,9] и \
 трёх действий вычеслений нельзя добавить буквы и знаки, у которых нет \
 в калькуляторе. При нажатий кнопа[=] ответ появится на поле вычисления.\
При нажатий в меню, выводятся информации о авторе и о праграмме.\n\n\n\n"
text_avtor = "Автор: Батбилэг Номуундалай Программист из BND "


def pragromma():
    messagebox.showinfo("О программе", text_pragromma)


def avtor():
    messagebox.showinfo("О разработчике", text_avtor)


root = Tk()
root.title("Калкулятор BND")


def batbileg(event):
    a_entry.insert(END, "9")
    a_entry.insert(END, "8")
    a_entry.insert(END, "7")
    a_entry.insert(END, "6")
    a_entry.insert(END, "5")
    a_entry.insert(END, "4")
    a_entry.insert(END, "3")
    a_entry.insert(END, "2")
    a_entry.insert(END, "1")
    a_entry.insert(END, "0")
    a_entry.insert(END, ".")
    a_entry.insert(END, "sqrt(x)")
    a_entry.insert(END, "-x")
    a_entry.insert(END, "C")
    a_entry.insert(END, "|>")
    a_entry.insert(END, ".")
    a_entry.insert(END, ",")
    a_entry.insert(END, "=")


# меню
main_menu = Menu(tearoff = 0)
m_menu = Menu(tearoff = 0)
m_menu.add_command(label="о программе", command=pragromma)
m_menu.add_command(label="о авторе", command=avtor)
main_menu.add_cascade(label="меню", menu=m_menu)
root.config(menu=main_menu)

# поле вычисления
a = StringVar()
a_entry = Entry(textvariable=a, width=40)
a_entry.grid(row=1, column=1, columnspan=4, padx=5, pady=5)

# ======================================кнопки=======================================
tentsvv = Button(text="=", command=batbileg, width=8)
tentsvv.grid(row=6, column=4, padx=5, pady=5)

ustgalt = Button(text="|>", command=batbileg, width=8)
ustgalt.grid(row=2, column=3, padx=5, pady=5)
ustgalt.bind("<Button-1>", batbileg)

bvrustgalt = Button(text="C", command=batbileg, width=8)
bvrustgalt.grid(row=2, column=4, padx=5, pady=5)
bvrustgalt.bind("<Button-1>", batbileg)

yazguur = Button(text="sqrt(x)", command=batbileg, width=8)
yazguur.grid(row=5, column=4, padx=5, pady=5)
yazguur.bind("<Button-1>", batbileg)

nemhas = Button(text="-x", command=batbileg, width=8)
nemhas.grid(row=6, column=1, padx=5, pady=5)
nemhas.bind("<Button-1>", batbileg)

# ===============================================================

vrjih = Button(text="*", command=batbileg, width=8)
vrjih.grid(row=2, column=1, padx=5, pady=5)
vrjih.bind("<Button-1>", vrjih)

huwaah = Button(text="/", command=batbileg, width=8)
huwaah.grid(row=2, column=2, padx=5, pady=5)
huwaah.bind("<Button-1>", huwaah)

nemeh = Button(text="+", command=batbileg, width=8)
nemeh.grid(row=3, column=4, padx=5, pady=5)
nemeh.bind("<Button-1>", nemeh)

hasalt = Button(text="-", command=batbileg, width=8)
hasalt.grid(row=4, column=4, padx=5, pady=0)
hasalt.bind("<Button-1>", hasalt)

eys = Button(text="9", command=batbileg, width=8)
eys.grid(row=3, column=3, padx=5, pady=5)
eys.bind("<Button-1>", eys)

naim = Button(text="8", command=batbileg, width=8)
naim.grid(row=3, column=2, padx=5, pady=5)
naim.bind("<Button-1>", naim)

doloo = Button(text="7", command=batbileg, width=8)
doloo.grid(row=3, column=1, padx=5, pady=5)
doloo.bind("<Button-1>", doloo)

zurgaa = Button(text="6", command=batbileg, width=8)
zurgaa.grid(row=4, column=3, padx=5, pady=5)
zurgaa.bind("<Button-1>", zurgaa)

taw = Button(text="5", command=batbileg, width=8)
taw.grid(row=4, column=2, padx=5, pady=5)
taw.bind("<Button-1>", taw)

duruw = Button(text="4", command=batbileg, width=8)
duruw.grid(row=4, column=1, padx=5, pady=5)
duruw.bind("<Button-1>", duruw)

guraw = Button(text="3", command=batbileg, width=8)
guraw.grid(row=5, column=3, padx=5, pady=5)
guraw.bind("<Button-1>", guraw)

hoyr = Button(text="2", command=batbileg, width=8)
hoyr.grid(row=5, column=2, padx=5, pady=5)
hoyr.bind("<Button-1>", hoyr)

neg = Button(text="1", command=batbileg, width=8)
neg.grid(row=5, column=1, padx=5, pady=5)
neg.bind("<Button-1>", neg)

teg = Button(text="0", command=batbileg, width=8)
teg.grid(row=6, column=2, padx=5, pady=5)
teg.bind("<Button-1>", teg)

tseg = Button(text=".", command=batbileg, width=8)
tseg.grid(row=6, column=3, padx=5, pady=5)
tseg.bind("<Button-1>", tseg)

root.mainloop()
