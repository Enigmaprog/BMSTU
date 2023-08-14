A = list(map(int,input("Введите одномерный массив:").split(",")))
x = len(A)
n = 1
while n < len(A):

    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            A[i],A[i+1] = A[i+1],A[i]

    n = n + 1

print(A)