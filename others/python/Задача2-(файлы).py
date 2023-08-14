file3 = open("file3.txt","r")
print(file3.read())
file3.close()

x = tuple("1g2g3g4g5g6g7g8g9")
A = []
B = []
C = []
sum = 0
for i in range(len(x)):
    if x[i]!='q' and  x[i]!='w' and x[i]!='e' and x[i]!='r' and x[i]!='t' and x[i]!='y' \
    and x[i]!='u' and x[i]!='i' and x[i]!='o' and x[i]!='p' and x[i]!='a' and x[i]!='s' \
    and x[i]!='d' and x[i]!='f' and x[i]!='g' and x[i]!='h' and x[i]!='j' and x[i]!='k' \
    and x[i]!='l' and x[i]!='z' and x[i]!='x' and x[i]!='c' and x[i]!='v' and x[i]!='b' \
    and x[i]!='n' and x[i]!='m' :
        A.append(x[i])
for i in range(len(A)):
    k = int(A[i])
    B.append(k)
for i in range(len(B)):
    sum = sum + B[i]
print(sum,end ="")


for i in range(len(x)):
    if x[i]!='q' and  x[i]!='w' and x[i]!='e' and x[i]!='r' and x[i]!='t' and x[i]!='y' \
    and x[i]!='u' and x[i]!='i' and x[i]!='o' and x[i]!='p' and x[i]!='a' and x[i]!='s' \
    and x[i]!='d' and x[i]!='f' and x[i]!='g' and x[i]!='h' and x[i]!='j' and x[i]!='k' \
    and x[i]!='l' and x[i]!='z' and x[i]!='x' and x[i]!='c' and x[i]!='v' and x[i]!='b' \
    and x[i]!='n' and x[i]!='m' :
        A.append(x[i])
    else:
        C.append(x[i])
for i in range(len(C)):
    h = "%s" % (C[i])
print(h, end="")