from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Сортировка выбором")


def ustgal():
    ekran1.delete(0, END)
    ekran2.delete(0, END)


def sort():
    a = str(ekran1.get())
    b = ''
    for i in a:
        b += i
    b = list(map(float, b.split(",")))
    if a == '':
        messagebox.showinfo("ERROR")
    else:
        for i in range(len(b)):
            min = b[i]
            k = i
            for j in range(i, len(b)):
                if min > b[j]:
                    min = b[j]
                    k = j
            if b[i] > min:
                b[i], b[k] = b[k], b[i]
        ekran2.insert(0, b)





m = StringVar()
ekran1 = Entry(textvariable = m, width = 40)
ekran1.grid(row = 1, column = 1, padx = 10, pady = 10)
n = StringVar()
ekran2 = Entry(textvariable = n, width = 40)
ekran2.grid(row = 1, column = 3, padx =10, pady = 10)

Ustgal = Button(text = "стереть", command = ustgal, width = 10)
Ustgal.grid(row = 1, column = 4, padx = 10, pady = 5)
Sort = Button(text = "--->", command = sort, width = 10)
Sort.grid(row =1, column = 2, padx = 10, pady =10)
root.mainloop()
