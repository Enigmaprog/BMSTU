from tkinter import *
from tkinter import messagebox
import time
import random



root = Tk()
root.title("Пузырьковая сортировка")
root.geometry('985x280')

text_pragromma = "Программа, которая сортирует методом Пузырька.\
 Программа состоит из двух части, первая часть для знакомства сортировки и количества вводящих элементов\
 а вторая работает при разных троих условиях и выдаёт времена, сортирующие в этих условиях.\
 При нажатий в меню, выводятся информации о авторе и о праграмме.\n\n\n"
text_avtor = "Автор: Батбилэг Н" \
             "[" \
             "омуундалай Программист из BND "

#Функции для меню
def pragromma():
    messagebox.showinfo("О программе", text_pragromma)
def avtor():
    messagebox.showinfo("О разработчике", text_avtor)

def ustgal():
    ekran1.delete(0, END)
    ekran2.delete(0, END)
    too1.delete(0, END)
    too2.delete(0, END)
    too3.delete(0, END)

def sort1():
    a = str(ekran1.get())
    b = ''
    for i in a:
        b += i
    b = list(map(float, b.split(",")))
    if a == '':
        messagebox.showinfo("ERROR", "Не задан массив\n\n\n\nВведите сначало \
    массив, затем нажмите на кнопку (Решить))\n\nНапример:\n")
    else:
        try:
            flag = True
            n = 1
            while n < len(b):
                for i in range(len(b) - n):
                    if b[i] > b[i + 1]:
                        b[i], b[i + 1] = b[i + 1], b[i]
                        flag = False
                n += 1
                if flag:
                    break


        except ValueError:
            messagebox.showinfo("ERROR", "Неправельно введены данные")
        else:
            ekran2.insert(0, b)


def sort3(array):
    n = 1
    while n < len(array):
        flag = True
        for i in range(len(array)-n):
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
                flag = False
        n += 1
        if flag:
            break
    return array


def sort2():
    b1 = str(too1.get())
    a1 = ''
    for i in b1:
        a1 += i
    b1 = a1.split(",")

    b2 = str(too2.get())
    a2 = ''
    for j in b2:
        a2 += j
    b2 = a2.split(",")

    b3 = str(too3.get())
    a3 = ''
    for k in b3:
        a3 += k
    b3 = a3.split(",")
    if (len(b1) != 1) and (len(b2) != 1) and (len(b3) != 1):
        messagebox.showinfo("ERROR", "Пожалуюста вводите размер массивов \
правильно и потом нажмите кнопку Решить")
    else:
        try:
            b1 = int(b1[0])
            b2 = int(b2[0])
            b3 = int(b3[0])

            # Создаём массив a[x], a[y], a[z]
            # ----------------------------------------------
            def Random_List(k):
                # Считаем элементы для списков в случайном
                List = []
                for i in range(k):
                    List.append(random.randrange(0, k, 1))
                return List

            # ----------------------------------------------
            def Count_Time(List):
                # Подсчёт времени
                start_time = time.clock()
                sort3(List)
                stop_time = time.clock() - start_time
                return round(stop_time, 10)

            # ----------------------------------------------
            mass_x_v = list(range(0, b1))
            mass_y_v = list(range(0, b2))
            mass_z_v = list(range(0, b3))

            mass_x_u = [x for x in range(b1, 0, -1)]
            mass_y_u = [x for x in range(b2, 0, -1)]
            mass_z_u = [x for x in range(b3, 0, -1)]

            mass_x_random = Random_List(b1)
            mass_y_random = Random_List(b2)
            mass_z_random = Random_List(b3)
            # Создание списка замеров времени для вывода
            out_list = []
            out_list.append(Count_Time(mass_x_v))
            out_list.append(Count_Time(mass_y_v))
            out_list.append(Count_Time(mass_z_v))
            out_list.append(Count_Time(mass_x_u))
            out_list.append(Count_Time(mass_y_u))
            out_list.append(Count_Time(mass_z_u))
            out_list.append(Count_Time(mass_x_random))
            out_list.append(Count_Time(mass_y_random))
            out_list.append(Count_Time(mass_z_random))
            # --------------------------------------------------------------------------------
            b1_label = Label(
                text="|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------| ")
            b1_label.grid(row=4, column=1, columnspan=7, sticky="nsew")

            b2_label = Label(text="|")
            b2_label.grid(row=5, column=1, sticky="w")

            b3_label = Label(text="Таблица")
            b3_label.grid(row=5, column=2, columnspan=5, sticky="nsew")

            b4_label = Label(text="| ")
            b4_label.grid(row=5, column=7, sticky="e")

            b5_label = Label(
                text="|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------| ")
            b5_label.grid(row=6, column=1, columnspan=7, sticky="nsew")

            b6_label = Label(text="|   Размеры массивов    |")
            b6_label.grid(row=7, column=1, columnspan=1, sticky="w")

            b7_label = Label(text=str(b1))
            b7_label.grid(row=7, column=2, columnspan=2, sticky="nsew")

            b8_label = Label(text=str(b2))
            b8_label.grid(row=7, column=4, columnspan=2, sticky="nsew")

            b9_label = Label(text=str(b3))
            b9_label.grid(row=7, column=6, columnspan=2, sticky="nsew")

            b10_label = Label(text="|   Возрастающие           |")
            b10_label.grid(row=8, column=1, columnspan=1, sticky="w")

            b11_label = Label(text=str(format(out_list[0])))
            b11_label.grid(row=8, column=2, columnspan=2, sticky="nsew")

            b12_label = Label(text=str(format(out_list[1])))
            b12_label.grid(row=8, column=4, columnspan=2, sticky="nsew")

            b13_label = Label(text=str(format(out_list[2])))
            b13_label.grid(row=8, column=6, columnspan=2, sticky="nsew")

            b14_label = Label(text="|      Убывающие             |")
            b14_label.grid(row=9, column=1, columnspan=1, sticky="w")

            b15_label = Label(text=str(format(out_list[3])))
            b15_label.grid(row=9, column=2, columnspan=2, sticky="nsew")

            b16_label = Label(text=str(format(out_list[4])))
            b16_label.grid(row=9, column=4, columnspan=2, sticky="nsew")

            b17_label = Label(text=str(format(out_list[5])))
            b17_label.grid(row=9, column=6, columnspan=2, sticky="nsew")

            b18_label = Label(text="|        Случайные             |")
            b18_label.grid(row=10, column=1, columnspan=1, sticky="w")

            b19_label = Label(text=str(format(out_list[6])))
            b19_label.grid(row=10, column=2, columnspan=2, sticky="nsew")

            b20_label = Label(text=str(format(out_list[7])))
            b20_label.grid(row=10, column=4, columnspan=2, sticky="nsew")

            b21_label = Label(text=str(format(out_list[8])))
            b21_label.grid(row=10, column=6, columnspan=2, sticky="nsew")

            b22_label = Label(
                text="|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------| ")
            b22_label.grid(row=11, column=1, columnspan=7, sticky="nsew")

        except ValueError:
            messagebox.showinfo("ERROR", "Пожалуста вводите размер массива \
правильо\n(размер массива = целому числу)")

#меню
main_menu = Menu(tearoff = 0)
m_menu = Menu(tearoff = 0)
m_menu.add_command(label="о программе", command=pragromma)
m_menu.add_command(label="о авторе", command=avtor)
main_menu.add_cascade(label="меню", menu=m_menu)
root. config(menu=main_menu)

#поля
m = StringVar()
ekran1 = Entry(textvariable=m, width=40)
ekran1.grid(row=1, column=1, columnspan=3, padx=10, pady=5)
n = StringVar()
ekran2 = Entry(textvariable=n, width=40)
ekran2.grid(row=1, column=5, columnspan=3, padx=10, pady=5)

a = StringVar()
too1 = Entry(textvariable=a, width=10)
too1.grid(row=2, column=2, padx=10, pady=5)
too1_label = Label(text = "a")
too1_label.grid(row=2, column=1, padx=0, pady=5)
b = StringVar()
too2 = Entry(textvariable=b, width=10)
too2.grid(row=2, column=4, padx=10,  pady=5)
too2_label = Label(text = "b")
too2_label.grid(row=2, column=3, padx=0,  pady=5)
c = StringVar()
too3 = Entry(textvariable=c, width=10)
too3.grid(row=2, column=6, padx=10, pady=5)
too3_label = Label(text = "c")
too3_label.grid(row=2, column=5, padx=0,  pady=5)


#кнопки
bvrustgal = Button(text="стереть", command = ustgal, width=10)
bvrustgal.grid(row=2 ,column=8 ,padx=10 ,pady=5)
hurwuulelt1 = Button(text="--->", command = sort1 , width=10)
hurwuulelt1.grid(row=1 ,column=4 ,padx=10 ,pady=5)
hurwuulelt2 = Button(text="===>", command = sort2, width=10)
hurwuulelt2.grid(row=2 ,column=7 ,padx=10 ,pady=5)


root.mainloop()






