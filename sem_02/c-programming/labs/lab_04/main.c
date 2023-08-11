/*
Написать программу, которая запрашивает у пользователя элементы целочисленного
статического массива и выполняет его обработку. Максимальное количество элементов,
которое может ввести пользователь, равно 10.
Задача 1
Найдите
1. произведение нечетных элементов массива;
Задача 2
Поместите в новый массив
1. элементы исходного массива, которые являются простыми числами;
Задача 3
1. Вставьте в исходный массив после каждого элемента, кратного трем, очередное число
Фибоначчи (первое число Фибоначчи равно 0, второе – 1).
Задача 4
Упорядочите исходный массив по возрастанию
1. вставками ;
*/
#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <math.h>
void input_array();
void output();
void odd_nums();
int safety();
void prime_nums();
int prime_check();
void fibonacci_nums();
int fibonacci();
void sort_array();
int main()
{
	FILE *iofile = NULL;
	int key, array[20], res;
	do
	{
		printf("Menu. Press 1 - 5 \n[1 - to enter new array]\n");
		printf("[2 - to multiply odd elements there]\n[3 - to make array from prime numbers of this array\n");
		printf("[4 - to insert Fibonacci numbers]\n[5 - to sort the array\n");
		printf("[Any number - to exit the programm]");
		key = safety();
		switch(key)
		{
		case 1:
			input_array();
			break;
		case 2:
			odd_nums();
			break;
		case 3:
			prime_nums();
			break;
		case 4:
			fibonacci_nums();
			break;
		case 5:
			sort_array();
			break;
		default:
			exit(0);
		}
	}
	while(1 || 2 || 3 || 4 || 5);
	getch();
	return 0;
}
int safety()
{
	int res, num;
	do
	{
		res = scanf("%d", &num);
		fflush(stdin);
		if(res != 1) printf("%s","Invalid input. Try again.\n");
	}
	while(res != 1);
	return num;
}
void input_array()
{
	printf("Enter the lenth of the array: ");
	FILE *iofile = NULL;
	unsigned counter = 0;
	iofile = fopen("numbers.bin", "w+b");
	
	int len = safety();
	if (0 < len <= 10)
	{
		fwrite(&len, sizeof(int), 1, iofile);
		int number;
		int array[len];
		for (int i = 0; i < len; i++)
		{
			printf("a[%d] = ", i);
			number = safety();
			array[i] = number;
			fwrite(&number, sizeof(int), 1, iofile);
			counter++;
		}
		output(array, len);
	}
	else
	{
		printf("The lenth of the array should be <=10 \n");
		input_array();
	}
	fclose(iofile);
}
void odd_nums()
{
	FILE *iofile = NULL;
	unsigned len;
	iofile = fopen("numbers.bin", "r+b");
	fread(&len, sizeof(int), 1, iofile);
	
	int multiply = 1;
	for (int i = 0; i < len; i++)
	{
		int element;
		fread(&element, sizeof(int), 1, iofile);
		if (i == 0 || i % 2 == 0) multiply *= element;
	}
	printf("Multiplication is : %d\n", multiply);
	fclose(iofile);
}
void prime_nums()
{
	FILE *iofile = NULL;
	unsigned len;
	iofile = fopen("numbers.bin", "r+b");
	fread(&len, sizeof(int), 1, iofile);
	int prime[10];
	int j = 0;
	for (int i = 0; i < len; i++)
	{
		int element;
		fread(&element, sizeof(int), 1, iofile);
		int check = prime_check(element);
		if (check == 0)
		{
			prime[j] = element;
			j++;
		}
	}
	output(prime, j);
	printf("\n");
	fclose(iofile);
}
int prime_check(int n)
{
	if (n == 0 || n == 1)
		return 0;
	int divider, remain;
	divider = 2;
	do
	{
		remain = n % divider;
		if (remain != 0)
		{
			divider++;
		}
	}
	while (remain != 0);
	
	if (divider == n)
	{
		divider = 0;
	}
	return divider;
}
void fibonacci_nums()
{
	FILE *iofile = NULL;
	unsigned len;
	iofile = fopen("numbers.bin", "r+b");
	fread(&len, sizeof(int), 1, iofile);

	int n = 0, k = 0;
	int nArr[len];
	for (int i = 0; i < len; i++)
	{
		int element;
		fread(&element, sizeof(int), 1, iofile);
		nArr[i + k] = element;
		if (nArr[i + k] % 3 == 0)
		{
			k++;
			nArr[i + k] = fibonacci(n);
			n++;
		}
	}
	len += n;
	fclose(iofile);
	//
	iofile = fopen("numbers.bin", "w+b");
	fwrite(&len, sizeof(int), 1, iofile);
	
	for (int i = 0; i < len; i++)
	{
		int element = nArr[i];
		fwrite(&element, sizeof(int), 1, iofile);
	}
	output(nArr, len);
	fclose(iofile);
}
int fibonacci(int n)
{
	int fib, a = 1, b = 1;
	if (n > 1)
	{
		while (n > 1)
		{
			fib = a + b;
			a = b;
			b = fib;
			n--;
		}
	}
	else
	{
		if (n == 0)
			fib = 0;
		if (n == 1)
			fib = 1;
	}
	return fib;
}
void sort_array()
{
	FILE *iofile = NULL;
	unsigned len;
	iofile = fopen("numbers.bin", "r+b");
	fread(&len, sizeof(int), 1, iofile);
	
	int array[len];
	for (int i = 0; i < len; i++)
	{
		fread(&array[i], sizeof(int), 1, iofile);
	}
    fclose(iofile);
	
	int newElement, location;
	for (int i = 1; i < len; i++)
	{
		newElement = array[i];
		location = i - 1;
		while(location >= 0 && array[location] > newElement)
		{
			array[location + 1] = array[location];
			location = location - 1;
		}
		array[location + 1] = newElement;
	}
	
	iofile = fopen("numbers.bin", "w+b");
	fwrite(&len, sizeof(int), 1, iofile);
	
	for (int i = 0; i < len; i++)
	{
		fwrite(&array[i], sizeof(int), 1, iofile);
	}
	printf("\n");
	output(array, len);
	fclose(iofile);
}
void output(int array[], int len)
{
	for (int i = 0; i < len; i++)
	{
		printf("%d ", array[i]);
	}
	printf("\n");
}