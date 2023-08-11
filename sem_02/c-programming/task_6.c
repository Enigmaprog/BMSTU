#include <stdio.h>
#include <stdbool.h>
#define OK 0
#define ERR_IO 1

float func(int *, int);

int main()
{
    int size, rc = OK;
    printf("Enter the size of the array:");
    if (scanf("%d", &size) != 1)
    {
        rc = ERR_IO;
        printf("Can't read number");
    }
    else
    {
        int a[size], checking_reading = true;
        for (int i = 0; i < size; i++)
        {
            printf("a[%d]=", i);
            if(scanf("%d", &a[i]) != 1)
            {
                rc = ERR_IO;
                printf("Can't read element of the array");
                checking_reading = false;
                break;
            }
        }
        if(checking_reading)
        {
            printf("Composition of negative members: %.3f", func(a, size));
        }
    }
    return rc;
}

float func(int *a, int size)
{
    int s = 1;
    for(int i = 0; i < size; i++)
    {
        if (a[i] < 0)
        {
            s *= a[i];
        }
    }
    return s;
}
