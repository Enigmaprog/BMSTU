#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#define ERROR_OPEN_FILE -3
void fill_with_r_n();
void show_nums();
int safety();
void sort_nums();
void put_number_by_pos();
int get_number_by_pos();
void swapping();
void main()
{
	FILE *iofile = NULL;
	int key, res;
	do
	{
		printf("Menu. Press 1 - 3 \n[1 - to create file and fill it with random numbers]\n");
		printf("[2 - to show numbers from the file]\n[3 - to sort numbers in the file\n");
		printf("[Any number - to exit the programm]");
		key = safety();
		switch (key)
		{
		case 1:
			fill_with_r_n();
			break;
		case 2:
			show_nums();
			break;
		case 3:
			sort_nums();
			break;
		default:
			exit(0);
		}
	}
	while(1 || 2 || 3);
	getch();
}
int safety()
{
	int res, num = 0;
	do
	{
		do
		{
			res = scanf("%d", &num);
			fflush(stdin);
			if (res != 1) printf("%s","Invalid input. Try again.\n");
		}
		while(res != 1);
		if (0 > num > 100) printf("%s","Invalid number. Try again.\n");
	}
	while (0 > num > 100);
	return num;
}
void fill_with_r_n()
{
	FILE *iofile = NULL;
	unsigned counter = 0;
	srand(time(NULL));
	
	iofile = fopen("numbers.bin", "w+b");
	if (iofile == NULL)
	{
		printf("Error opening file");
		getch();
	}
	
	printf("Write the quantity of random numbers you wanna write to the file: ");
	int quantity = safety();
	
	fwrite(&quantity, sizeof(int), 1, iofile);
	for (int i = 0; i < quantity; i++)
	{
		int rand_val = 0 + rand() % (100);
		fwrite(&rand_val, sizeof(int), 1, iofile);
		counter++;
	}
	
	fclose(iofile);
}
void show_nums()
{
	FILE *iofile = NULL;
	unsigned counter;
	iofile = fopen("numbers.bin", "r+b");
	
	if (iofile == NULL)
	{
		printf("Error opening file");
		getch();
	}
	
	fread(&counter, sizeof(int), 1, iofile);
	for (int i = 0; i < counter; i++)
	{
		int num;
		fread(&num, sizeof(int), 1, iofile);
		printf("%d\n", num);
	}
	fclose(iofile);
}
void sort_nums()
{
	FILE *iofile = NULL;
	unsigned counter;
	
	iofile = fopen("numbers.bin", "r+b");
	if (iofile == NULL)
	{
		printf("Error opening file");
		getch();
	}
	
	int noSwap;
	fread(&counter, sizeof(int), 1, iofile);
	for (int i = counter; i >= 0; i--)
	{
		noSwap = 1;
		for (int j = 0; j < i; j++)
		{
			int value_1 = get_number_by_pos(j);
			int value_2 = get_number_by_pos(j + 1);
			if (value_1 > value_2)
			{
				swapping(j, j + 1);
				noSwap = 0;
			}
		}
		if (noSwap == 1)
			break;
	}
	fclose(iofile);
}
void put_number_by_pos(int pos, int value)
{
	FILE *iofile = NULL;
	unsigned counter;
	iofile = fopen("numbers.bin", "r+b");
	
	fseek(iofile, pos*sizeof(int), SEEK_SET);
	fwrite(&value, sizeof(int), 1, iofile);
	
	fclose(iofile);
}
int get_number_by_pos(int pos)
{
	FILE *iofile = NULL;
	unsigned counter;
	iofile = fopen("numbers.bin", "r+b");
	
	int value;
	fseek(iofile, pos*sizeof(int), SEEK_SET);
	fread(&value, sizeof(int), 1, iofile);
	
	fclose(iofile);
	return value;
}
void swapping(int i, int j)
{
	int value_1 = get_number_by_pos(i);
	int value_2 = get_number_by_pos(j);
	
	put_number_by_pos(j, value_1);
	put_number_by_pos(i, value_2);
}