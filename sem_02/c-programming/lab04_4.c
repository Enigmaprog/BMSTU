#include <stdio.h>
#include <stdbool.h>
#define OK 0
#define ERR_IO 1

void func( int *, int);

int main()
{
    int a[10], size, rc = OK;
    printf("Enter the size of the array :");
    if (scanf("%d", &size) != 1)
    {
        rc = ERR_IO;
        printf("Can't read number");
    }
    else if (size > 10 || size < 0)
    {
        rc = ERR_IO;
        printf("Enter less than 10");
    }
    else
    {
        int check_reading = true;
        for (int i = 0; i < size; i++)
        {
            printf("a[%d]=", i);
            if (scanf("%d", &a[i]) != 1)
            {
                rc = ERR_IO;
                printf("Can't read number");
                check_reading = false;
                break;
            }
        }
        if (check_reading)
            func(a, size);
    }
    return rc;
}

void func(int *a, int size)
{
    int min, m;
    for (int i = 0; i < size; i++)
    {
        min = a[i];
        for (int j = i + 1; j < size; j++)
        {
            if (min > a[j])
            {
                min = a[j];
                m = j;
            }
        }
        if (m != i)
        {
            min = a[m];
            a[m] = a[i];
            a[i] = min;
        }
    }
    for (int i = 0; i < size; i++)
        printf("%d ", a[i]);
}
