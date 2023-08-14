from math import *

def func_math(r):
    g = cos((pi/2) * r)
    return g

def differ_1(n):
    global x0
    global step
    x0 = float(input('Введите  координату начальной точки x : '))
    step = float(input('Введите  шаг на увлечение step : '))
    global x1
    x1 = x0 + step
    global y0
    y0 = func_math(x0)
    global y1
    y1 = func_math(x1)
    print("\n")
    print('_' * 45)
    print('|' + '            ТАБЛИЦА ЗНАЧЕНИЙ X N Y         ' + '|')
    print('_' * 45)
    print('|' + ' ' * 9 + ' x ' + ' ' * 9 + '|' + ' ' * 9 + ' y ' + ' ' * 9 + ' |')
    print('|       {:3.5f}       |        {:3.5f}      |'.format(x0, y0))
    print('|       {:3.5f}       |        {:3.5f}      |'.format(x1, y1))

    m1 = (y0 - y1)/(x0 - x1)  # Первая разделённая разность
    return m1

def differ_2(n):
    raz1 = differ_1(n)
    global x2
    x2 = x1 + step
    global y2
    y2 = func_math(x2)
    print('|       {:3.5f}       |        {:3.5f}      |'.format(x2, y2))
    n1 = (y1 - y2)/(x1 - x2)
    m2 = (raz1 - n1)/(x0 - x2)  # Вторая разделённая разность
    return (m2, raz1)

def differ_3(n):
    raz2, raz1 = differ_2(n)
    global x3
    x3 = x2 + step
    global y3
    y3 = func_math(x3)
    print('|       {:3.5f}       |        {:3.5f}      |'.format(x3, y3))
    n2 = (y2 - y3)/(x2 - x3)
    m3 = (raz1 - raz2 - n2)/(x0 - x3)  # Третья разделённая разность
    return (m3, raz2, raz1)

def differ_4(n):
    raz3, raz2, raz1 = differ_3(n)
    global x4
    x4 = x3 + step
    global y4
    y4 = func_math(x4)
    print('|       {:3.5f}       |        {:3.5f}      |'.format(x4, y4))
    n3 = (y3 - y4)/(x3 - x4)
    m4 = (raz1 - raz2 - raz3 - n3)/(x0 - x4) # Четвёртая разделённая разность
    return (m4, raz3, raz2, raz1)

def differ_5(n):
    raz4, raz3, raz2, raz1 = differ_4(n)
    global x5
    x5 = x4 + step
    global y5
    y5 = func_math(x5)
    print('|       {:3.5f}       |        {:3.5f}      |'.format(x5, y5))
    n4 = (y4 - y5)/(x4 - x5)
    m5 = (raz1 - raz2 - raz3 - raz4 - n4)/(x0 - x5)  # Пятая разделённая разность
    return (m5, raz4, raz3, raz2, raz1)

#=======================================================================================================================

n = int(input('Введите степень полниома n = '))

t = float(input('Введите переменную для функции x = '))

d = func_math(t)

#=======================================================================================================================

if n == 0:
    x0 = float(input('Введите  координату начальной точки x : '))
    step = float(input('Введите  шаг на увлечение step : '))
    y0 = func_math(x0)
    print("\n")
    print('_' * 45)
    print('|' + '            ТАБЛИЦА ЗНАЧЕНИЙ X N Y         ' + '|')
    print('_' * 45)
    print('|' + ' ' * 9 + ' x ' + ' ' * 9 + '|' + ' ' * 9 + ' y ' + ' ' * 9 + ' |')
    print('|       {:3.5f}       |        {:3.5f}      |'.format(x0, y0))
    print('_' * 45)
    print('\n')
    print(' ' * 10 + 'РЕЗУЛЬТАТЫ' + ' ' * 10)
    polinom0 = x0 + y0
    print("1. Полином Ньютона Ф(x) = {:3.5f}". format(polinom0))
    print("2. Точное значение y(x) = {:3.5f}". format(d))
    if (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
    else:
        print("3. Не нашёлся корень этой функции из данных")

elif n == 1:
    raz1 = differ_1(n)
    polinom1 = y0 + (t - x0) * raz1
    print('_' * 45)
    print('\n')
    print(' ' * 10 + 'РЕЗУЛЬТАТЫ' + ' ' * 10)
    print("1. Полином Ньютона Ф(x) = {:3.5f}". format(polinom1))
    print("2. Точное значение y(x) = {:3.5f}". format(d))
    if (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
    else:
        print ("3. Не нашёлся корень этой функции из данных")

elif n == 2:
    raz2, raz1 = differ_2(n)
    polinom2 = y0 + (t - x0) * raz1 + (t - x0) * (t - x1) * raz20
    print('_' * 45)
    print('\n')
    print(' ' * 10 + 'РЕЗУЛЬТАТЫ' + ' ' * 10)
    print("1. Полином Ньютона Ф(x) = {:3.5f}". format(polinom2))
    print("2. Точное значение y(x) = {:3.5f}". format(d))
    if (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x2)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x2)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x2)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
    elif (round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x2)
    else:
        print("3. Не нашёлся корень этой функции из данных")

elif n == 3:
    raz3, raz2, raz1 = differ_3(n)
    polinom3 = y0 + (t - x0) * raz1 + (t - x0) * (t - x1) * raz2 + (t - x0) * (t - x1) * (t - x2) * raz3
    print('_' * 45)
    print('\n')
    print(' ' * 10 + 'РЕЗУЛЬТАТЫ' + ' ' * 10)
    print("1. Полином Ньютона Ф(x) = {:3.5f}". format(polinom3))
    print("2. Точное значение y(x) = {:3.5f}". format(d))
    if (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x2)
        print("6. Четвёртый корень этой функции: ", x3)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x2)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x2)
        print("5. Третий корень этой функции: ", x3)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x3)
    elif (round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x2)
        print("5. Третий корень этой функции: ", x3)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x2)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x2)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x3)
    elif (round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x2)
        print("4. Второй корень этой функции: ", x3)
    elif (round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x3)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
    elif (round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x2)
    elif (round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x3)
    else:
        print("3. Не нашёлся корень этой функции из данных")

elif n == 4:
    raz4, raz3, raz2, raz1 = differ_4(n)
    polinom4 = y0 + (t - x0) * raz1 + (t - x0) * (t - x1) * raz2 + (t - x0) * (t - x1) * (t - x2) * raz3 + \
               + (t - x0) * (t - x1) * (t - x2) * (t - x3) * raz4
    print('_' * 45)
    print('\n')
    print(' ' * 10 + 'РЕЗУЛЬТАТЫ' + ' ' * 10)
    print("1. Полином Ньютона Ф(x) = {:3.5f}".format(polinom4))
    print("2. Точное значение y(x) = {:3.5f}".format(d))
    if (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001) :
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x2)
        print("6. Четвёртый корень этой функции: ", x3)
        print("7. Пятий корень этой функции: ", x4)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x2)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x2)
        print("5. Третий корень этой функции: ", x3)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x3)
        print("5. Третий корень этой функции: ", x4)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x3)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x2)
        print("5. Третий корень этой функции: ", x4)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x4)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x2)
        print("5. Третий корень этой функции: ", x3)
    elif (round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x2)
        print("4. Второй корень этой функции: ", x3)
        print("5. Третий корень этой функции: ", x4)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x2)
        print("5. Третий корень этой функции: ", x4)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x3)
        print("5. Третий корень этой функции: ", x4)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x2)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x3)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x4)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x2)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x3)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x4)
    elif (round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x2)
        print("4. Второй корень этой функции: ", x3)
    elif (round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x2)
        print("4. Второй корень этой функции: ", x4)
    elif (round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x3)
        print("4. Второй корень этой функции: ", x4)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
    elif (round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x2)
    elif (round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x3)
    elif (round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x4)
    else:
        print("3. Не нашёлся корень этой функции из данных")

elif n == 5:
    raz5, raz4, raz3, raz2, raz1 = differ_5(n)
    polinom5 = y0 + (t - x0) * raz1 + (t - x0) * (t - x1) * raz2 + (t - x0) * (t - x1) * (t - x2) * raz3 + \
               + (t - x0) * (t - x1) * (t - x2) * (t - x3) * raz4 + (t - x0) * (t - x1) * (t - x2) * (t - x3) * (t - x4) * (raz5)
    print('_' * 45)
    print('\n')
    print(' ' * 10 + 'РЕЗУЛЬТАТЫ' + ' ' * 10)
    print("1. Полином Ньютона Ф(x) = {:3.5f}".format(polinom5))
    print("2. Точное значение y(x) = {:3.5f}".format(d))
    if (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x2)
        print("6. Четвёртый корень этой функции: ", x3)
        print("7. Пятий корень этой функции: ", x4)
        print("8. Шестой корень этой функции: ", x5)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x2)
        print("6. Четвёртый корень этой функции: ", x3)
        print("7. Пятий корень этой функции: ", x4)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x2)
        print("5. Третий корень этой функции: ", x3)
        print("6. Четвёртый корень этой функции: ", x4)
        print("7. Пятий корень этой функции: ", x5)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x3)
        print("6. Четвёртый корень этой функции: ", x4)
        print("7. Пятий корень этой функции: ", x5)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x2)
        print("6. Четвёртый корень этой функции: ", x4)
        print("7. Пятий корень этой функции: ", x5)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x2)
        print("6. Четвёртый корень этой функции: ", x3)
        print("7. Пятий корень этой функции: ", x5)
    elif (round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x2)
        print("5. Третий корень этой функции: ", x3)
        print("6. Четвёртый корень этой функции: ", x4)
        print("7. Пятий корень этой функции: ", x5)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x2)
        print("6. Четвёртый корень этой функции: ", x3)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x2)
        print("5. Третий корень этой функции: ", x3)
        print("6. Четвёртый корень этой функции: ", x4)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x3)
        print("5. Третий корень этой функции: ", x4)
        print("6. Четвёртый корень этой функции: ", x5)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x4)
        print("6. Четвёртый корень этой функции: ", x5)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x2)
        print("5. Третий корень этой функции: ", x3)
        print("6. Четвёртый корень этой функции: ", x5)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x2)
        print("6. Четвёртый корень этой функции: ", x5)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x2)
        print("6. Четвёртый корень этой функции: ", x4)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x3)
        print("6. Четвёртый корень этой функции: ", x5)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x3)
        print("6. Четвёртый корень этой функции: ", x4)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x2)
        print("5. Третий корень этой функции: ", x4)
        print("6. Четвёртый корень этой функции: ", x5)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x2)
        print("5. Третий корень этой функции: ", x3)
        print("6. Четвёртый корень этой функции: ", x4)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x2)
        print("5. Третий корень этой функции: ", x3)
        print("6. Четвёртый корень этой функции: ", x5)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x3)
        print("5. Третий корень этой функции: ", x4)
        print("6. Четвёртый корень этой функции: ", x5)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x2)
        print("5. Третий корень этой функции: ", x4)
        print("6. Четвёртый корень этой функции: ", x5)
    elif (round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x2)
        print("4. Второй корень этой функции: ", x3)
        print("5. Третий корень этой функции: ", x4)
        print("6. Четвёртый корень этой функции: ", x3)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x2)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x2)
        print("5. Третий корень этой функции: ", x3)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x2)
        print("5. Третий корень этой функции: ", x4)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x2)
        print("5. Третий корень этой функции: ", x5)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x3)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x4)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
        print("5. Третий корень этой функции: ", x5)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x3)
        print("5. Третий корень этой функции: ", x4)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x3)
        print("5. Третий корень этой функции: ", x5)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x4)
        print("5. Третий корень этой функции: ", x5)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x2)
        print("5. Третий корень этой функции: ", x3)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x2)
        print("5. Третий корень этой функции: ", x4)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x2)
        print("5. Третий корень этой функции: ", x5)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x3)
        print("5. Третий корень этой функции: ", x4)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x3)
        print("5. Третий корень этой функции: ", x5)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x4)
        print("5. Третий корень этой функции: ", x5)
    elif (round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x2)
        print("4. Второй корень этой функции: ", x3)
        print("5. Третий корень этой функции: ", x4)
    elif (round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x2)
        print("4. Второй корень этой функции: ", x3)
        print("5. Третий корень этой функции: ", x5)
    elif (round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x2)
        print("4. Второй корень этой функции: ", x4)
        print("5. Третий корень этой функции: ", x5)
    elif (round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x3)
        print("4. Второй корень этой функции: ", x4)
        print("5. Третий корень этой функции: ", x5)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x1)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x2)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x3)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x4)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
        print("4. Второй корень этой функции: ", x5)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x2)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x3)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x4)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001  and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
        print("4. Второй корень этой функции: ", x5)
    elif (round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x2)
        print("4. Второй корень этой функции: ", x3)
    elif (round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x2)
        print("4. Второй корень этой функции: ", x4)
    elif (round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x2)
        print("4. Второй корень этой функции: ", x5)
    elif (round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x3)
        print("4. Второй корень этой функции: ", x4)
    elif (round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x3)
        print("4. Второй корень этой функции: ", x5)
    elif (round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001 and round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x4)
        print("4. Второй корень этой функции: ", x5)
    elif (round(y0, 3) >= -0.001 and round(y0, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x0)
    elif (round(y1, 3) >= -0.001 and round(y1, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x1)
    elif (round(y2, 3) >= -0.001 and round(y2, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x2)
    elif (round(y3, 3) >= -0.001 and round(y3, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x3)
    elif (round(y4, 3) >= -0.001 and round(y4, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x4)
    elif (round(y5, 3) >= -0.001 and round(y5, 3) <= 0.001):
        print("3. Первый корень этой функции: ", x5)
    else:
        print("3. Не нашёлся корень этой функции из данных")

else:
    print("Введите корректное значение n!")