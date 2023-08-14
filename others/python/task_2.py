a = [77, 46, 11, 89, 48, 14, 67, 73, 22, 26]

t = len(a)
n = 1

# while n < t:
#     for i in range(t - 1):
#         if (a[i] > a[i+1]):    
#             a[i], a[i+1] = a[i+1], a[i]
#     n += 1

for i in range(t - 1):
    for j in range(t - 1):
        if (a[j] > a[j+1]):
            a[j], a[j + 1] = a[j + 1], a[j]
    
    
print(a)