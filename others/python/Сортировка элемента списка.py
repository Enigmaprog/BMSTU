n = int(input('введите количество элементов списка:'))
x = [0]*n
print('введите список элементов (по одному на строку): ')
x = [int(input()) for i in range(n)]
print(x)
for i in range(n-1):
    for j in range(n-2, i-1, -1):
        if x[j] > x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]
print(x)