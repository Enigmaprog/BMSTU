from tkinter import *
import parser

root = Tk()
root.title('Calculator')
i = 0



def clear_all():
    """clears all the content in the Entry widget"""
    display.delete(0, END)

def get_variables(num):
    """Gets the user input for operands and puts it inside the entry widget"""
    global i
    display.insert(i, num)
    i += 1

def get_operation(operator):
    """Gets the operand the user wants to apply on the functions"""
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def undo():
    """removes the last entered operator/variable from entry widget"""
    whole_string = display.get()
    if len(whole_string):        ## repeats until
        ## now just decrement the string by one index
        new_string = whole_string[:-1]
        print(new_string)
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all() 
        display.insert(0, "Error, press AC")

def calculate():
    
    whole_string = display.get()
    try:
        formulae = parser.expr(whole_string).compile()
        result = eval(formulae)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error!")

root.columnconfigure(0,pad=3)
root.columnconfigure(1,pad=3)
root.columnconfigure(2,pad=3)
root.columnconfigure(3,pad=3)
root.columnconfigure(4,pad=3)

root.rowconfigure(0,pad=3)
root.rowconfigure(1,pad=3)
root.rowconfigure(2,pad=3)
root.rowconfigure(3,pad=3)

display = Entry(root,bg = 'grey',font = ("Calibri", 13))
display.grid(row = 1, columnspan = 90, sticky = W+E+N+S)

one = Button(root, text = "1",bg = 'grey', command = lambda : get_variables(1), font=("Calibri", 12))
one.grid(row = 2, column = 0, sticky = W+E+N+S)
two = Button(root, text = "2",bg = 'grey', command = lambda : get_variables(2), font=("Calibri", 12))
two.grid(row = 2, column = 1, sticky = W+E+N+S)
three = Button(root, text = "3",bg = 'grey', command = lambda : get_variables(3), font=("Calibri", 12))
three.grid(row = 2, column = 2, sticky = W+E+N+S)

four = Button(root, text = "4",bg = 'grey', command = lambda : get_variables(4), font=("Calibri", 12))
four.grid(row = 3 , column = 0, sticky = W+E+N+S)
five = Button(root, text = "5",bg = 'grey', command = lambda : get_variables(5), font=("Calibri", 12))
five.grid(row = 3, column = 1, sticky = W+E+N+S)
six = Button(root, text = "6",bg = 'grey', command = lambda : get_variables(6), font=("Calibri", 12))
six.grid(row = 3, column = 2, sticky = W+E+N+S)

seven = Button(root, text = "7",bg = 'grey', command = lambda : get_variables(7), font=("Calibri", 12))
seven.grid(row = 4, column = 0, sticky = W+E+N+S)
eight = Button(root, text = "8",bg = 'grey', command = lambda : get_variables(8), font=("Calibri", 12))
eight.grid(row = 4, column = 1, sticky = W+E+N+S)
nine = Button(root , text = "9",bg = 'grey', command = lambda : get_variables(9), font=("Calibri", 12))
nine.grid(row = 4, column = 2, sticky = W+E+N+S)

cls = Button(root, text = "AC", command = clear_all, font=("Calibri", 12), foreground = "red")
cls.grid(row = 5, column = 0, sticky = W+E+N+S)
zero = Button(root, text = "0", command = lambda : get_variables(0), font=("Calibri", 12))
zero.grid(row = 5, column = 1, sticky = W+E+N+S)
result = Button(root, text = "=",bg = 'white', command = calculate, font=("Calibri", 12), foreground = "red")
result.grid(row = 5, column = 2, sticky = W+E+N+S)

plus = Button(root, text = "+",bg = 'orange', command =  lambda : get_operation("+"), font=("Calibri", 12))
plus.grid(row = 2, column = 3, sticky = W+E+N+S)
minus = Button(root, text = "-",bg = 'orange', command =  lambda : get_operation("-"), font=("Calibri", 12))
minus.grid(row = 3, column = 3, sticky = W+E+N+S)
multiply = Button(root,text = "*",bg = 'orange', command =  lambda : get_operation("*"), font=("Calibri", 12))
multiply.grid(row = 4, column = 3, sticky = W+E+N+S)
divide = Button(root, text = "/",bg = 'orange', command = lambda :  get_operation("/"), font=("Calibri", 12))
divide.grid(row = 5, column = 3, sticky = W+E+N+S)

root.mainloop()







