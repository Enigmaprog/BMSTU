#include <stdio.h>
#include <stdbool.h>
#define OK 0
#define ERR_IO 1

float func(int *, int);

int main()
{
    int rc = OK;
    int x[10], size;
    printf("Enter the size of the array:");

    if (scanf("%d", &size) != 1)
    {
        rc = ERR_IO;
        printf("Did not carry a number\n");
    }
    else if (size > 10 || size < 0)
    {
        printf("Did not carry a number\n");
    }
    else
    {
        int check_reading = true;
        for (int i = 0; i < size; i++)
        {
            printf("a[%d] = ", i);
            if (scanf("%d", &x[i]) != 1)
            {
                rc = ERR_IO;
                printf("Did not carry a number\n");
                check_reading = false;
                break;
            }
        }
        if (check_reading)
            printf("Arithmetic mean of negative numbers = %.3f\n", func(x, size));
    }
    return rc;
}

float func(int *a, int n)
{
    float sum = 0;
    int count = 0;
    for (int i = 0; i < n; i++)
        if (a[i] < 0)
        {
            sum += a[i];
            count++;
        }
    float result = 0;
    if (count > 0)
    result = sum / count;
    return result;
}
