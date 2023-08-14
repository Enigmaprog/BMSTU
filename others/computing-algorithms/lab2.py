from tkinter import *
from math import *
from tkinter import messagebox as mb

root = Tk()
root.title('Laboratory work 2')
root.geometry('700x400')

def func_math(x):
    y = sin(pi/2 * x)
    return y

def clear_table():
    table.delete(1.0, END)

def clear_Fk():
    l6.delete(1.0, END)

def print_table():
    coor_x, coor_y, tact = trans_table()
    for i in range(tact):
        table.insert(END, "{:2.0f}.        {:3.2f}      |        {:3.2f}\n".format(i + 1, coor_x[i], coor_y[i]))
        table.insert(END, "------------------------------------------")

def trans_table():
    try:
        coor_x = []
        coor_y = []
        tact = 0
        start_x = float(l1_field.get())
        finish_x = float(l2_field.get())
        step = float(l3_field.get())

        while(start_x <= finish_x):
            coor_x.append(round(start_x, 2))
            start_y = func_math(start_x)
            coor_y.append(round(start_y, 2))
            start_x += step
            tact += 1

        return coor_x, coor_y, tact

    except:
        mb.askyesno(title = "Ошибка", message = "Вводите число")

def comput_inter():
    try:
        x = float(l4_field.get())
        step = float(l3_field.get())
        coor_x, coor_y, tact = trans_table()
        k = 0
        if (x > coor_x[0] or x < coor_x[tact]):
            while (x > coor_x[0]):
                coor_x[0] += step
                k += 1

            return k, x

        else:
            mb.askyesno(title = "Ошибка", message = "Вводите коректное число")

    except:
        mb.askyesno(title = "Ошибка", message = "Вводите число")

def interpolation():
    k, x = comput_inter()
    coor_x, coor_y, tact = trans_table()

    C = []

    H = []
    I = []
    G = []
    Laym = []

    H.append(coor_x[1] - coor_x[0])
    H.append(coor_x[2] - coor_x[1])
    I.append((coor_y[1] - coor_y[0]) / H[0])
    I.append((coor_y[2] - coor_y[1]) / H[1])

    G.append(-H[1] / 2*(H[0] + H[1]))
    Laym.append(3 * (I[1] - I[0]) / 2 * (H[0] + H[1]))

    C.append(0)

    for i in range(k - 1):
        H.append(round(coor_x[i+3] - coor_x[i+2], 3))
        g = -(H[i+2]) / (2 * (H[i+1] + H[i+2]) + H[i+1] * G[i])
        G.append(round(g, 3))

        I.append(round((coor_y[i+3] - coor_y[i+2]) / H[i+2] ,3))
        laym = (3 * (I[i+2] - I[i+1]) - H[i+1] * Laym[i])
        Laym.append(round(laym, 3))

        c = C[i] - Laym[i] / G[i]
        C.append(round(c, 3))

    d_k = (C[k-1] - C[k-2]) / 3 * H[k-1]
    b_k = I[k-1] + (2 * C[k-1] * H[k-1] + H[k-1] * C[k-2]) / 3
    a_k = coor_y[k]

    F = a_k + b_k * (x - coor_x[k]) + C[k-1] * pow((x - coor_x[k]), 2) + d_k * pow((x - coor_x[k]), 3)

    l6.insert(END, "    {:5.4}".format(F))


#=======================================================================================================================
# Labels
main_screen = Label(bg = "#deb887", width = 1000, height = 600)
main_screen.place(x = 0, y = 0)

x = Label(text = "x", bg = "#dcdcdc", font = "Calibri 15", width = 10, height = 1)
x.grid(row = 1, column = 1, padx = 10)

y = Label(text = "y", bg = "#dcdcdc", font = "Calibri 15", width = 10, height = 1)
y.grid(row = 1, column = 2, pady = 5)

table = Text(font = 'bold', bg = 'white')
table.place(x = 10, y = 50, width = 220, height = 330)

l1 = Label(text = "Начальное значение x :", bg = "#dcdcdc", font = "Calibri 15")
l1.grid(row = 1, column = 3, padx = 10, pady = 10)

l2 = Label(text = "Конечное значение x :", bg = "#dcdcdc", font = "Calibri 15")
l2.grid(row = 2, column = 3, padx = 10, pady = 10)

l3 = Label(text = "Шаг :", bg = "#dcdcdc", font = "Calibri 15")
l3.grid(row = 3, column = 3, padx = 10, pady = 10)

l4 = Label(text = "Переменная для функции :", bg = "#dcdcdc", font = "Calibri 14")
l4.grid(row = 5, column = 3, padx = 10, pady = 10)

l5 = Label(text = "Fk(x) :", bg = "#dcdcdc", font = "Calibri 13")
l5.grid(row = 7, column = 3, padx = 10, pady = 10)

l6 = Text(font = 'bold', bg = 'white')
l6.place(x = 480, y = 305, width = 195, height = 20)

# Enters
l1_field = StringVar()
l1_field = Entry(textvariable = l1_field,  bg = "#dcdcdc", width = 30)
l1_field.grid(row = 1, column = 4, padx = 10, pady = 10)

l2_field = StringVar()
l2_field = Entry(textvariable = l2_field, bg = "#dcdcdc", width = 30)
l2_field.grid(row = 2, column = 4, padx = 10, pady = 10)

l3_field = StringVar()
l3_field = Entry(textvariable = l3_field, bg = "#dcdcdc", width = 30)
l3_field.grid(row = 3, column = 4, padx = 10, pady = 10)

l4_field = StringVar()
l4_field = Entry(textvariable = l4_field,  bg = "#dcdcdc", width = 30)
l4_field.grid(row = 5, column = 4, padx = 10, pady = 10)


# Buttons
b1 = Button(text = "Построить таблицу",  bg = "#dcdcdc", font = "Calibri 10", command = print_table, width = 20)
b1.grid(row = 4, column = 3, padx = 10, pady = 10)

b2 = Button(text = "Вычислить Fk(x)",  bg = "#dcdcdc", font = "Calibri 10", command = interpolation,  width = 20)
b2.grid(row = 6, column = 3, padx = 10, pady = 10)

b3 = Button(text = "Очистить таблицу", bg = "#dcdcdc", font = "Calibri 10", command = clear_table, width = 20)
b3.grid(row = 4, column = 4, padx = 10, pady = 10)

b4 = Button(text = "Очистить Fk(x)",  bg = "#dcdcdc", font = "Calibri 10", command = clear_Fk, width = 20)
b4.grid(row = 6, column = 4, padx = 10, pady = 10)

root.mainloop()