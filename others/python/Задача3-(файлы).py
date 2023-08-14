file4 = open("file4.txt","r")
print(file4.read())
x = int(input('x:'))
file4 = open("file4.txt","r")
A = []
for i in range(x):
    k = file4.readline()
    y = len(k)
    print(k)
    print(y-1)
    A.append(y-1)
    z = min(A)
print(z, end=" ")
print(x)