#include <stdio.h>
#include <locale.h>
#include <conio.h>
#include <stdlib.h>
#define ERROR_OPEN_FILE -3
int input(FILE *f);
int write_numbers(FILE *f);
int process(FILE *f, int);
int main () 
{
    FILE *f;
    int len = input(f);
    int count = process(f, len);
    printf("\namount of local max = %d", count);
    getch();
    return 0;
}
int input(FILE *f)
{
    char name[] = "text.txt";
    f = fopen(name, "w");
    int len = write_numbers(f);
    return len;
}
int write_numbers(FILE *f)
{
    float numb;
    printf("Input numbers: ");
    int len = 1;
    while (scanf("%f", &numb)) 
    {
        fprintf(f,"%f ",numb);
        len += 1;
    }
    fclose(f);
    return len;
}
int process(FILE *f, int len)
{
    f = fopen("text.txt", "r");
    if (f == NULL) {
        printf("Error opening file");
        getch();
    }

    float array[len];

    float num;
    int i = 0;
    while (!feof(f))
    {
        fscanf(f, "%f", &array[i]);
        i++;
    }
    int count = 0;
    printf("\nArray: ");
    for (int i = 0; i < len; i++)
        if (i == (len - 1))
            break;
        else
            printf("%f ", array[i]);

    for (int i = 1; i < len - 2; i++)
    {
        if (array[i] > array[i - 1] && array[i] > array[i + 1])
            count++;
    }
    fclose(f);
    return count;
}