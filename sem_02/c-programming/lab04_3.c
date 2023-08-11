#include <stdio.h>
#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#define OK 0
#define ERR_IO 1

void func(int *, int);

void del_elem(int *, int, int);

void print(int *, int, int);

int main()
{
    int a[10], size, rc = OK;
    printf("Enter the size of the array:");
    if (scanf("%d", &size) != 1)
    {
        rc = ERR_IO;
        printf("Can't read number");
    }
    else if( size > 10 || size < 0)
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
    int d, m, n, k;
    for(int i = 0; i < size; i++)
    {
        n = a[i];
        k = i;
        m = sqrt(n);
        d = pow(m, 2);
        if (n == d)
            del_elem(a, size, k);
    }
    print(a, size, k);
}

void del_elem(int *a, int size, int k)
{
    for(int i = k; i < size; i++)
        a[i] = a[i + 1];
    size--;
}

void print(int *a, int size, int k)
{
    for(int i = 0; i < size; i ++)
        printf("%d ", a[i]);
}

