#include <stdio.h>
#include <stdbool.h>
#define OK 0
#define ERR_IO 1

void func(int *, int);

int main()
{
    int size, rc = OK;
    printf("Enter the size if the array:");
    if (scanf("%d", &size) != 1)
    {
        rc = ERR_IO;
        printf("Can't read size of the array");
    }
    else
    {
        int a[size], check_reading = true;
        for (int i = 0; i < size; i++)
        {
            printf("a[%d]=", i);
            if (scanf("%d", &a[i]) != 1)
            {
                rc = ERR_IO;
                printf("Can't read element");
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
    int max = a[0], s = 0, d = 0;
    float t;
    int min = max;
    for(int i = 1; i < size; i++)
    {
        if (min > a[i])
        {
            min = a[i];
        }
        else if (max < a[i])
        {
            max = a[i];
        }
    }
    for(int i = 0; i < size; i++)
    {
        if (max != a[i] && min != a[i])
        {
            s += a[i];
            d += 1;
        }
    }
    printf("%d %d", s, d);
    t = s / d;
    printf("\n%.2f ", t);
}
