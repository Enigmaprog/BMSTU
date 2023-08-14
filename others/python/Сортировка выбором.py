print('введите список элементов (в строчку): ')
x = list(map(int, input().split(',')))
print(x)

n = len(x)
for i in range(n-1):
    nmin = i
    for j in range(i+1,n):
        if x[j] < x[nmin]:
            nmin = j
    x[i], x[nmin] = x[nmin], x[i]
print(x)