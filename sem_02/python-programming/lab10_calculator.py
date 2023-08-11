from tkinter import *
from tkinter import messagebox
import math
import parser
import math as m

root = Tk()
root.title("Калькулятор")
root.geometry('330x230')
i = 0


text_pragromma = "Программа: Калькулятор, который действует три действия вычисления,\
 точнее плюс[+], минус[-] и корень. Кроме цифри[0,1,2,3,4,5,6,7,8,9] и \
 трёх действий вычеслений нельзя добавить буквы и знаки, у которых нет \
 в калькуляторе. При нажатий кнопа[=] ответ появится на поле вычисления.\
При нажатий в меню, выводятся информации о авторе и о праграмме.\n\n\n\n"
text_avtor = "Автор: Батбилэг Номуундалай Программист из BND "

#Функции для меню
def pragromma():
    messagebox.showinfo("О программе", text_pragromma)
def avtor():
    messagebox.showinfo("О разработчике", text_avtor)

#функции для калькулятора
def ustgal():
    a_cripz.delete(0, END)

def hewlelt(num):
    global i
    a_cripz.insert(i, num)
    i += 1

def hewlelt2():
    global i
    try:
        temp = a_cripz.get()
        a_cripz.delete(0, END)
        a_cripz.insert(END, temp[:-1])
    except:
        pass
    i += 1

def hewlelt3():
    a_cripz.insert(0, '-')


def math_operation(operator):
    global i
    length = len(operator)
    a_cripz.insert(i, operator)
    i += length

def tentsvv():
    whole_string = a_cripz.get()
    if whole_string.find("√")!=-1:
        whole_string = whole_string.replace("√", "math.sqrt(") + ')'

    print(whole_string)
    try:
        formulas = parser.expr(whole_string).compile()
        result = eval(formulas)
        ustgal()
        a_cripz.insert(0, result)
    except Exception:
        ustgal()
        a_cripz.insert(0, "Error!")

#меню
main_menu = Menu(tearoff = 0)
m_menu = Menu(tearoff = 0)
m_menu.add_command(label="о программе", command=pragromma)
m_menu.add_command(label="о авторе", command=avtor)
main_menu.add_cascade(label="меню", menu=m_menu)
root. config(menu=main_menu)

#поле
a = StringVar()
a_cripz = Entry(textvariable=a, width=50)
a_cripz.grid(row=1, column=1, columnspan=4, padx=10, pady=5)

#кнопки
zero = Button(text="0", command = lambda : hewlelt(0), width=8)
zero.grid(row=6 ,column=2 ,padx=5 ,pady=5 )
one = Button(text="1", command = lambda : hewlelt(1), width=8)
one.grid(row=5 ,column=1 ,padx=5 ,pady=5 )
two = Button(text="2", command = lambda : hewlelt(2), width=8)
two.grid(row=5 ,column=2 ,padx=5 ,pady=5 )
three = Button(text="3", command = lambda : hewlelt(3), width=8)
three.grid(row=5 ,column=3 ,padx=5 ,pady=5 )
four = Button(text="4", command = lambda : hewlelt(4), width=8)
four.grid(row=4 ,column=1 ,padx=5 ,pady=5 )
five = Button(text="5", command = lambda : hewlelt(5), width=8)
five.grid(row=4 ,column=2 ,padx=5 ,pady=5 )
six = Button(text="6", command = lambda : hewlelt(6), width=8)
six.grid(row=4 ,column=3 ,padx=5 ,pady=5 )
seven = Button(text="7", command = lambda : hewlelt(7), width=8)
seven.grid(row=3 ,column=1 ,padx=5 ,pady=5 )
eight = Button(text="8", command = lambda : hewlelt(8), width=8)
eight.grid(row=3 ,column=2 ,padx=5 ,pady=5 )
nine = Button(text="9", command = lambda : hewlelt(9), width=8)
nine.grid(row=3 ,column=3 ,padx=5 ,pady=5 )

plus = Button(text="+", command = lambda : math_operation("+"), width=8)
plus.grid(row=3 ,column=4 ,padx=5 ,pady=5 )
minus = Button(text="-", command = lambda : math_operation("-"), width=8)
minus.grid(row=4 ,column=4 ,padx=5 ,pady=5 )
multiply = Button(text="*", command = lambda : math_operation("*"), width=8)
multiply.grid(row=2 ,column=1 ,padx=5 ,pady=5 )
split = Button(text="/", command = lambda : math_operation("/"), width=8)
split.grid(row=2 ,column=2 ,padx=5 ,pady=5 )
root = Button(text="√", command = lambda : math_operation("√"), width=8)
root.grid(row=5 ,column=4 ,padx=5 ,pady=5 )


tentsvvlt = Button(text="=", command = tentsvv, width=8)
tentsvvlt.grid(row=6 ,column=4 ,padx=5 ,pady=5)

bvrustgal = Button(text="C", command = ustgal, width=8)
bvrustgal.grid(row=2 ,column=4 ,padx=5 ,pady=5)

tseg = Button(text=".",command = lambda : hewlelt("."), width=8)
tseg.grid(row=6 ,column=3 ,padx=5 ,pady=5)

negustgal = Button(text="<-", command = hewlelt2, width=8)
negustgal.grid(row=2 ,column=3 ,padx=5 ,pady=5)

surugutag = Button(text="-x", command = hewlelt3, width=8)
surugutag.grid(row=6 ,column=1 ,padx=5 ,pady=5)

root.mainloop()