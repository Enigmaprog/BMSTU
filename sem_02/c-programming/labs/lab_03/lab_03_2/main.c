#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <math.h>
//найти число, наиболее близкое к среднему значению всех чисел
#define ERROR_OPEN_FILE -3
void input();
float process();
void process2(float);
float safety();
void main()
{
	input();
	float average = process();
	process2(average);
	getch();
}
float safety()
{
	float res, num;
	do
	{
		res = scanf("%f", &num);
		fflush(stdin);
		if(res != 1) printf("%s","Invalid input. Try again.\n");
	}
	while(res != 1);
	return num;
}
void input()
{
	FILE *iofile = NULL;
	unsigned counter = 0;
	float num;
	int yn;
	
	iofile = fopen("numbers.bin", "w+b");
	if (iofile == NULL)
	{
		printf("Error opening file");
		getch();
	}
	
	fwrite(&counter, sizeof(float), 1, iofile);
	do
	{
		printf("enter new number? [1 - yes, 2 - no]");
		yn = safety();
		if (yn == 1) 
		{
			num = safety();
			fwrite(&num, sizeof(float), 1, iofile);
			counter++;
		}
		else
		{
			rewind(iofile);
			fwrite(&counter, sizeof(float), 1, iofile);
			break;
		}
	}
	while(1);
	fclose(iofile);
}
float process()
{
	FILE *iofile = NULL;
	unsigned counter;
	
	iofile = fopen("numbers.bin", "rb");
	if (iofile == NULL)
	{
		printf("Error opening file");
		getch();
	}
	
	float sum = 0, num = 0, average = 0;
	
	fread(&counter, sizeof(float), 1, iofile);
	for (int i = 0; i < counter; i++)
	{
		fread(&num, sizeof(float), 1, iofile);
		sum += num;
		if (sum != 0) average = (float)sum / (i + 1);
		else average = 0;
	}
	fclose(iofile);
	return average;
}
void process2(float average)
{
	float min_diff = 10000, close_to_av, num, close_to_av_2;
	
	FILE *iofile = NULL;
	unsigned counter;
	iofile = fopen("numbers.bin", "rb");
	
	if (iofile == NULL)
	{
		printf("Error opening file");
		getch();
	}
	int k = 1;
	fread(&counter, sizeof(float), 1, iofile);
	for (int i = 0; i < counter; i++)
	{
		fread(&num, sizeof(float), 1, iofile);
		if (num == average)
		{
			close_to_av = num;
			break;
		}
		float diff = sqrt(num * num - average * average);
		if (diff < min_diff)
		{
			min_diff = diff;
			close_to_av = num;
			k = 1;
		}
		else if (diff == min_diff)
		{
			close_to_av_2 = num;
			k = 0;
		}
	}
	if (k == 1) printf("\nThe closest to the average is %f", close_to_av);
	else printf("\nThe closests to the average are %f and %f", close_to_av, close_to_av_2);
	fclose(iofile);
}