#include <stdio.h>
#include <stdbool.h>
#define OK 0
#define ERR_IO 1

void func(int *, int );

int main()
{
    int x, rc = OK;
    printf("Enter the number:");
    if(scanf("%d", &x) != 1)
    {
        rc = ERR_IO;
        printf("Can't read number");
    }
    else
    {
        int a[100], size = 1, t = x;
        a[0] = x % 10;
        t /= 10;
        while(t > 0)
        {
            x /= 10;
            x %= 10;
            a[size] = x;
            size ++;
            t /= 10;
        }
        func(a, size);
    }
    return rc;
}

void func(int *a, int size)
{
    for (int i = 0; i < size; i++)
        printf("%d", a[i]);
}

