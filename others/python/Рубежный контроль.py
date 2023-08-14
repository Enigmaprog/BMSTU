file = open("file.txt","r")
a = []
b = []
for i in range (3):
    t = file.readline()
    a.append(t)
for n in range(len(a)):
    for m in range(0,5,2):
        b.append(int(a[n][m]))

if b[1] == 0 and b[2] == 0 and b[5] == 0 and b[3] != 0 and b[4] != 0 and b[6] != 0 and b[7] != 0 and b[0] != 0 and b[7] == 0:
    print("В верхней части треугольник")
elif b[1] != 0 and b[2] != 0 and b[5] != 0 and b[2] == 0 and b[3] == 0 and b[4] == 0 and b[6] == 0 and b[7] == 0 and b[8] == 0:
    print("В верхней части нет треугольника")
elif b[3] == 0 and b[6] == 0 and b[7] == 0 and b[1] != 0 and b[2] != 0 and b[5] != 0 and b[4] != 0 and b[5] !=0 and b[8] != 0:
    print("В нижней части треугольник")
elif b[3] != 0 and b[6] != 0 and b[7] != 0 and b[1] == 0 and b[2] == 0 and b[5] == 0 and b[4] == 0 and b[5] ==0 and b[8] == 0:
    print("В нижней части нет  треугольника")
elif b[0] != 0 and b[1] == 0 and b[2] == 0 and b[3] == 0 and b[4] != 0 and b[5] == 0 and b[6] ==0 and b[7] ==0 and b[8] != 0 :
    print("В нижней и верхней частях треугольникы")
elif b[0] == 0 and b[1] != 0 and b[2] != 0 and b[3] != 0 and b[4] == 0 and b[5] != 0 and b[6] !=0 and b[7] !=0 and b[8] != 0 :
    print("В матрице нет треугольника")
elif b[0] == 0 and b[1] == 0 and b[2] == 0 and b[3] == 0 and b[4] == 0 and b[5] == 0 and b[6] ==0 and b[7] ==0 and b[8] == 0 :
    print("Пустая матрица")
else:
    print("В матрице нет треугольника")
x = b[0]*(b[4]*b[8]-b[7]*b[5]) - b[1]*(b[3]*b[8]-b[6]*b[5]) + b[2]*(b[3]*b[7]-b[6]*b[4])
if x == 0:
    print("Вырожденная матрица")
else:
    print("Невырожденная матрица")
file.close()