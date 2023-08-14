#s = bytearray('sel2sel','pic2pic')
#s[0] = 'fdsaf'
#print(s)

#x = bytes("стр str","cp1251")
#print(len(x))

#s = "world1 world2 world3"
#print(s.split())

#x = ['e', 'r', 'j', 'k', 's', 'd']
#y = tuple(x)
#print(y)


#t = (1,2,3,4,3)
#for i in range(len(t)):
#    x = t.index(t[i])
#    print(x, end="")

#s = set([1,2,3,4,5])
#t = s | set([6,7,8,9,10])
#print(t)

#s = (set([1,2,3]) - set([1,2,4]))
#print(s)

#s = set([1,2,3,4,5])
#s.update(set([1,2,3,6,7,8,9]))
#print(s)

#x = set([1,2,3]) & set([1,2,4])
#print(x)

#s = set([1,2,3,4,5])
#s.add(6)
#print(s)

#s.remove(1)
#print(s)

#s.pop()
#print(s)

#x = frozenset('fdsgfsd')
#print(x)

#x = frozenset([1,2,3,4,5,6])
#print(x)

#x = frozenset((1,2,3,4,5,6))
#print(x)

#d = dict()
#print(d)

#d = dict({'a':1 ,'b':2})
#print(d)

#d = dict(a=1,b=2 )
#print(d)

#d = {
#    'a' : 1,
#    'b' : 2
#}
#print('k:'+str(d['a']))
#d['a'] = 3
#d['c'] = '4'
#print(d)

#x = len(d)
#print(x)

#del d['c']
#print(d)

#print(d.keys())
#print(d.values())

#d1,d2 = {"a":1, "b":2},{"a":3,"c":4,"d":5}
#x = d1.keys() | d2.keys()
#print(x)

#def func():
#    print("Batbileg")

#func()

#def summa(x,y):
#    return(x+y)

#x = summa(2,5)
#print(x)


#def summa(a,b,c):
#    return(a+b+c)

#t1 = (1,2,3)
#t2 = [1,2,3]
#t3 = {2,3,4}
#t4 = { "a":0 , "b":0, "c":0}

#print(summa(*t1))
#print(summa(*t2))
#print(summa(*t3))
#print(summa(**t4))


#def func(a=None):
#    if a is None:
#        a = []
#    a.append(2)
#    return(a)

#print(func())
#print(func())
#print(func([1]))


#def summa(*t):
#    res = 0
#    for i in t:
#        res += i
#    return(res)

#print(summa(10,20,30))


#def func(x,y):
#    for i in range(1,x+1):
#        t = i**y
#        yield(t)

#for i in func(10,3):
 #   print(i, end=" ")

#i = func(3,3)
#print(i.__next__())
#print(i.__next__())
#print(i.__next__())


#def func(glob2):
#    print("Значение глобальной переменной glob1:",glob1)
#    glob2 += glob1
#    print("Значение локальной переменной glob2:", glob2)
#
#glob1,glob2 = 10,5
#func(77)
#print("Значение локальной переменной glob2:", glob2)


#def func1(x):
#    def func2():
#        print(x)
#    return(func2)

#f1 = func1(10)
#f2 = func1(90)

#f1()
#f2()


#file3 = open("file3.txt","r")
#print(file3.read())
#file3.close()


#file3 = open("file3.txt","w")
#file3.write("cripz1\rcripz2")
#file3.close()


#file3 = open("file3.txt",'r')
#print(file3.read())
#file3.close()

#with open("file3.txt", "r") as f:
#    for line in f:
#        print(repr(line))

#print("===================================Задача===========================================")

#file1 = open("file1.txt","r")
#print(file1.read())
#file1.close()

#def func(x):
#    for i in range(x):
#        k = file1.readline()
#        return(k)

#x = int(input("Введите количество строк:"))
#print(func(x))
#file1 = open("file1.txt","r")

#file1 = open("file1.txt","r")
#print(file1.read())
#file1.close()

#file1 = open("file1.txt","r")
#x = int(input("Введите количество строк:"))
#for i in range(x):
#    k = file1.readline()
#    print(k)

#import pickle
#file3 = open(r"file3.txt","wb")
#obj = ("Строка",(2,3))
#pickle.dump(obj, file3)
#file3.close()


#f = open(r"file3.txt","rb")
#obj = pickle.load(f)
#f.close()


#n = int(input("количество:"))
#x = [0]*n
#print("элементы:")
#x = [int(input()) for i in range(n)]
#print(x)
#n = 1
#while n < len(x):
#    for i in range(len(x)-1):
#        if x[i]<x[i+1]:
#            x[i],x[i+1] = x[i+1],x[i]
#    n += 1
#print(x)


print("===============Первый файл==================")
file1 = open("file1.txt", "r")
print(file1.read())
file1.close()
print("===============Второй файл==================")
file2 = open("file2.txt", "r")
print(file2.read())
file2.close()
print("============================================")

#=============================================================

#from math import *
#x = int(input("x:"))
#y = sqrt(x)
#print(int(y))



#def temp(x):
#    y = sqrt(x)
#    return(int(y))


#x = int(input("x:"))
#print(temp(x))