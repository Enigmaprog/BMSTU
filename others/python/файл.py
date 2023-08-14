a = []
file3 = open("file3.txt","r")
x = file3.readline()
for i in range(len(x)-1):
    a.append(x[i])
    if a[i] < a[i+1]:
        a[i],a[i+1] = a[i+1],a[i]

print(a)