f1 = open('file1.txt', 'r')
f3 = open('file2.txt', 'w')

temp = ''
a = []
b = []


def stoi(temp):
    res1 = 0
    count = 1
    while temp != '':
        res1 += count * int(temp[len(temp) - 1])
        temp = temp[:len(temp) - 1]
        count *= 10
    return res1


for line in f1:
    res = 0
    s = ''
    for char in line:
        if (char < 'a' or char > 'z') and char != '\n' and char != ' ':
            temp = temp + char
        else:
            s += char
            if stoi(temp) != 0:
                print(stoi(temp))
            temp = ''
    a.append(res)
    b.append(s)

for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[j] < a[i]:
            a[i], a[j] = a[j], a[i]
            b[i], b[j] = b[j], b[i]

for i in range(len(a)):
    f3.write(str(a[len(a) - i - 1]) + ' ' + b[i])

f1.close()
f3.close()
