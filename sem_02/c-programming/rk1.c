#include <stdio.h>
#include <stdbool.h>
#define OK 0
#define ERR_IO 1
int main()
{
    int size, k, rc = OK;
    printf("Enter the size of the array :");
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
                printf("Can't read size array");
                check_reading = false;
                break;
            }
        }
        if (check_reading)
        {
            for (int i = 0; i < size; i++)
            {
                if(a[i] % 7 == 0)
                {
                    k = i;
                    printf("Serial number of a multiple of seven: %d", k);
                    break;
                }
            }
        }
    }
    return rc;
}
