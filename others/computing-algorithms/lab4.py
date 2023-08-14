import image
from tkinter import *
from math import *

root = Tk()
root.title('Computer graphics')
root.geometry('1260x800')

# Кнопка изменения координат точки
b_var = BooleanVar()
i_var = IntVar()

# Редактирует координаты точки
def change_points():
    #Если включен режим редактирования точки, выключаем его
    if b2['text'] == 'Отмена':
        cancel()
        return 0

    temp = list(lbox.curselection())
    b_var.set(0)
    i_var.set(temp[0])

    if len(temp) < 1:  # Если вообще ни одна точка не выбрана
        return 0

    # Включаем режим редактирования точки
    b1.config(text='Сохранить', bg='red')
    b2.config(text='Отмена', bg='red')
    x_field.insert(END, lbox.get(i_var.get())[0])
    y_field.insert(END, lbox.get(i_var.get())[1])
    p_field.insert(END, lbox.get(i_var.get())[2])

# Вторая функция для добавления точек
def add_points2(x_field, y_field, p_field, lbox, table, pos):
    flag = 1

    try:
        x = float(x_field.get())
        y = float(y_field.get())
        p = float(p_field.get())
    except:
        flag = 0

    if flag:
        lbox.insert(pos, (x, y, p))
        x_field.delete(0, END)
        y_field.delete(0, END)
        p_field.delete(0, END)
        return 1

    else:
        table.delete(1.0, END)
        table.insert(END, "Вводите коректнные координаты")
        return 0

# Принимает координаты на листбохс
def add_points():
    #table.config(state = NORMAL)

    if b2['text'] == 'Отмена':
        if add_points2(x_field, y_field, p_field, lbox, table, i_var.get()) == 1:
            lbox.delete(i_var.get() + 1)
        cancel()
    else:
        add_points2(x_field, y_field, p_field, lbox, table, END)

    #table.config(state = DISABLED)
    clear_entry()

# Отменяет редактирование точки
def cancel():
    clear_entry()
    b1.config(text = 'Добавить координаты', bg = 'white')
    b2.config(text = 'Изменить координаты', bg = 'white')

# Очистка координатных полей
def clear_entry():
    x_field.delete(0, END)
    y_field.delete(0, END)
    p_field.delete(0, END)

# Удаляет по одному из листбохса
def delete_points():
    select = list(lbox.curselection())
    select.reverse()
    for i in select:
        lbox.delete(i)

# Удаляет все координаты из списка
def delete_all_points():
    lbox.delete(0, END)
    screen_paint.delete("all")


def math_2(a, b):
    x1 = a[0]
    y1 = a[1]
    p1 = a[2]
    x2 = b[0]
    y2 = b[1]
    p2 = b[2]

    m1 = (p1 + p1)
    m2 = ((p1 * x1) + (p2 * x2))
    m3 = m2
    m4 = ((p1 * x1**2) + (p2 * x2**2))
    m5 = ((p1 * y1) + (p2 * y2))
    m6 = ((p1 * y1 * x1) + (p2 * y2 * x2))

    h1 = m3 / m1
    m3 = m3 - (h1 * m1)
    m4 = m4 - (h1 * m2)
    m6 = m6 - (h1 * m5)

    if (m3  == 0):
        m2 = m2 / m1
        m5 = m5 / m1
        m1 = m1 / m1
        m6 = m6 / m4
        m4 = m4 / m4

        if (m1 == 1 and m4 == 1):
            a_1 = m6
            a_0 = m5 - (m2 * a_1)
            print(a_1, a_0)

        else:
            table.delete(1.0, END)
            table.insert(END, "Элементы главной диагонали матрицы не равнялись на один")

    else:
        table.delete(1.0, END)
        table.insert(END, "Третий элемент матрицы не равнялся на нуль")


def math_3(a, b, c):
    x1 = a[0]
    y1 = a[1]
    p1 = a[2]
    x2 = b[0]
    y2 = b[1]
    p2 = b[2]

def math_4(a, b, c, d):
    x1 = a[0]
    y1 = a[1]
    p1 = a[2]
    x2 = b[0]
    y2 = b[1]
    p2 = b[2]

def math_5(a, b, c, d, e):
    x1 = a[0]
    y1 = a[1]
    p1 = a[2]
    x2 = b[0]
    y2 = b[1]
    p2 = b[2]


def draw():
    temp = lbox.get(0, END)

    if len(temp) == 1:
        table.delete(1.0, END)
        table.insert(END, "Не хватает множества точек для построения графики : ")
        table.insert(END, "Y = {:2.0f}".format(temp[0][2]))

    elif len(temp) == 2:
        math_2(temp[0], temp[1])

    elif len(temp) == 3:
        math_3(temp[0], temp[1], temp[2])

    elif len(temp) == 4:
        math_4(temp[0], temp[1], temp[2], temp[3])

    elif len(temp) == 5:
        math_5(temp[0], temp[1], temp[2], temp[3], temp[4])







#Labels
plur_points = Label(text = "Множество точек", bg = "#63b8ff", width = 30, height = 2, font = "Calibri 12")
plur_points.place(x = 0, y = 0)

x_i = Label(text = "x(i)", width = 10, height = 2, bg = "#5CACEE", font = "Calibri 12")
x_i.place(x = 0, y = 44)

y_i = Label(text = "y(i)", width = 10, height = 2, bg = "#5CACEE", font = "Calibri 12")
y_i.place(x = 80, y = 44)

p_i = Label(text = "p(i)", width = 10, height = 2, bg = "#5CACEE", font = "Calibri 12")
p_i.place(x = 160, y = 44)

axis_x = Label(text = "X :", width = 4, height = 2, font = "Calibri 12")
axis_x.place(x = 0, y = 410)

axis_y = Label(text = "Y :", width = 4, height = 2, font = "Calibri 12")
axis_y.place(x = 78, y = 410)

weight_p = Label(text = "P :", width = 4, height = 2, font = "Calibri 12")
weight_p.place(x = 160, y = 410)

# Listbox
lbox = Listbox(width = 40, height = 20)
lbox.place(x = 0, y = 90)

# Enters
x_field = StringVar()
x_field = Entry(textvariable = x_field, width = 8)
x_field.place(x = 30, y = 422)

y_field = StringVar()
y_field = Entry(textvariable = y_field, width = 8)
y_field.place(x = 110, y = 422)

p_field = StringVar()
p_field = Entry(textvariable = p_field, width = 8)
p_field.place(x = 190, y = 422)

# Buttons
close_button = Button(text = "X", width = 3, height = 2, command = delete_all_points)
close_button.place(x = 215, y = 0)

b1 = Button(text = "Добавить координаты", font = "Calibri 10", width = 20, command = add_points)
b1.place(x = 50, y = 455)

b2 = Button(text = "Изменить координаты", font = "Calibri 10", width = 20, command = change_points)
b2.place(x = 50, y = 490)

b3 = Button(text = "Удалить координаты", font = "Calibri 10", width = 20, command = delete_points)
b3.place(x = 50, y = 525)

b4 = Button(text = "Построить", font = "Calibri 10", width = 20, command = draw)
b4.place(x = 50, y = 560)

# Text
table = Text(font = "Calibri 10", bg = 'white')
table.place(x = 1, y = 600, width = 245, height = 190)

# Canvas
screen_paint = Canvas(root, bg = "#fffafa", width = 1000, height = 785)
screen_paint.place(x = 248, y = 0)


root.mainloop()