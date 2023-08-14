file1 = open("file1.txt","r")
print(file1.read())
file1.close()
file1 = open("file1.txt","r")
q = int(input("Введите количество строк:"))
for i in range(q):
    t = file1.readline()
    x = tuple(t)
    A = []
    B = []
    C = []
    sum = 0
    for i in range(len(x)):
        if x[i]<'a' or 'z'<x[i]:
            A.append(x[i])
    for i in range(len(A)):
        B.append(A[i])
    for i in range(len(B)):
        sum = sum + B[i]
    print(sum,end = " ")
    for i in range(len(x)):
        if x[i]<'a' or x[i]>'z':
            A.append(x[i])
        else:
            C.append(x[i])
    for i in range(len(C)):
        temp = "%s" % (C[i])
        print(temp,end="")
file1 = open("file1.txt","w")
file1.write(str(sum)+' ')
file1.write(str(temp))
file1.close()
file1 = open("file1.txt","r")
print(file1.read())
file1.close()