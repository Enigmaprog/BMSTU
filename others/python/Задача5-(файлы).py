lst1 = open('file3.txt', 'r').readlines()
print(lst1)
with open('file3.txt', 'w') as f3:
    for i in range(len(lst1)):
        if i == 1:
            continue
        else:
            f3.write(lst1[i])
f3.close()