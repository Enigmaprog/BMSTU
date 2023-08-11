my_numbers = list(map(int, input('Введите одномерный массив:').split()))
x = int(input('Введите один целое число:'))
z = max(my_numbers)

i = 0
while i < len(my_numbers):
    if my_numbers[i] == z:
        my_numbers.insert(i + 1, x)
        i += 2
    else:
        i += 1

print(my_numbers)


#Изменение элемента массива
numbers[3] = 'a'
print(numbers)

#Добавление элемента массива
numbers.append('7')
print(numbers)

numbers.insert(4,'b')
print(numbers)

#Удаление элемента массива
del numbers[3]
print(numbers)
numbers.remove('b')
print(numbers)

#Изменение места элементов массива
numbers.reverse()
print(numbers)

my_numbers = list(map(int, input('Введите одномерный массив:').split()))
x = int(input('Введите один целое число:'))
z = max(my_numbers)

i = 0
while i < len(my_numbers):
    if my_numbers[i] == z:
        my_numbers.insert(i + 1, x)
        i += 2
    else:
        i += 1

print(my_numbers)