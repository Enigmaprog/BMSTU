from math import *

a = []
b = []
c = []

P_start = float(input("Введите начальное давление P(n):"))
T_start = float(input("Введите начальную температуру T(n):"))
m = float(input("Введите степень m:"))
T0 = float(input("Введите температуру T0:"))
Tw = float(input("Введите температуру Tw:"))

#Количество разбиения отрезка на графике
n = 40
#Начальное и конечное давления
p1 = 3
p2 = 25

f = lambda z: z / (T0 + (Tw - T0) * z**m)

def trapez(f, a, b, n):
    h = float(b - a) / n
    temp = 0.5 * (f(a) + f(b))
    for i in range(1, n - 1):
        temp += f(a + i * h)
    temp *= h
    return temp

def dihitomi_b(I, p):
    f_p = (7242 * P_start / T_start) - 14484 * I * p
    return f_p


def dihitomi(I):
    p_a = p1
    p_b = p2
    while (fabs((p_b - p_a) / p_a) > 10**(-4)):
        p_c = (p_b + p_a) / 2
        f_a = dihitomi_b(I, p_a)
        f_b = dihitomi_b(I, p_b)
        f_c = dihitomi_b(I, p_c)
        if ((f_a * f_c) < 0):
            p_b = p_c
            print(p_a, p_b)
        elif ((f_b * f_c) < 0):
            p_a = p_c
            print(p_a, p_b)

#for i in range(n):
#    z =  round((i * h), 4)
#    a.append(z)

#for i in range(n):
#    if (i == 0 and i == 39):
#        z_b = round((a[i] / (T0 + (Tw - T0) * a[i]**n)), 5)
#        b.append(z_b)
#    else:
#        z_b = round((a[i] / (T0 + (Tw - T0) * a[i]**n)), 5)
#        b.append(z_b)


#summa = 0
#for i in range(len(b)):
#    summa += b[i]


#print(a)
#print(b)

#print("Summa: ", summa)
        else:
            break

    return p_c


I = trapez(f, 0, 1, n)
result = dihitomi(I)
print("P:", round(result, 4))


