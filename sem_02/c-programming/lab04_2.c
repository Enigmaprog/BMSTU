#include <stdio.h>
#include <stdbool.h>
#define OK 0
#define ERR_IO 1

void func(int *, int);

int main()
{
    int a[10], size, rc = OK;
    printf("Enter the size of the array:");
    if (scanf("%d", &size) != 1)
    {
        rc = ERR_IO;
        printf("Can't read size");
    }
    else if ( size > 10 || size < 0)
    {
        rc = ERR_IO;
        printf("Enter >0 and < 10");
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
                printf("Can't read array");
                check_reading = false;
                break;
            }
        }
        if (check_reading)
        {
            func(a, size);
        }
    }
    return rc;
}

void func(int *a, int size)
{
    int b[100], size2 = 0, s = 0;
    for (int i = 0; i < size; i++)
        s += a[i];
    s = s / size;
    printf("%d\n", s);
    for (int i = 0; i < size; i++)
    {
        if (a[i] > s)
        {
            b[size2] = a[i];
            size2 ++;
        }
    }
    printf("New Arr: ");
    for (int i = 0; i < size2; i++)
        printf("%d ", b[i]);
}






















