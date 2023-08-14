import random
import string

list = []
def func1():
    t = random.choice(string.ascii_letters)
    return t
def func_generation(list):
    for i in range(b):
        s = random.randrange(1, a - 1)
        list2 = []
        for j in range(b):
            if j == s:
                list2.append(x)
            else:
                list2.append(func1())
        list.append(list2)
    return list

def func_bodolt(list):
    C = []
    D = []
    F = []
    for i in list:
        print(i)
    for i in range(a):
        n = 0
        N = 0
        for j in range(0, list[i].index(x)):
            if list[i][j] <= 'a' or list[i][j] >= 'z':
                n += 1
            elif list[i][j] <= 'A' or list[i][j] >= 'Z':
                N += 1
        C.append(n)
        D.append(N)

    for i in range(a):
        if C[i] >= D[i]:
            F.append(list[i])
    print('_'*50)
    for i in F:
        print(i)    


a = 5
b = 5

x = str(input("Введите символ, который разделит строку:"))
while True:
    if x in string.ascii_letters:
        x = str(input("Введите символ, который разделит строку:"))
    else:
        break
list = func_generation(list)
func_bodolt(list)