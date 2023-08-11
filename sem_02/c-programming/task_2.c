#include<stdio.h>
#define OK 0
#define ERR_IO 1
int main()
{
    unsigned int x, max, min, rc = OK;
    printf("Enter the number:");
    if (scanf("%d", &x) != 1)
    {
        rc = ERR_IO;
        printf("Can't read number");
    }
    else
    {
        max = x % 10;
        min = max;
        int d = x / 10;
        while(d > 0)
        {
            x = d % 10;
            if (x > max)
                max = x;
            else if(x < min)
                min = x;
            d /= 10;
        }
        printf("%d", max + min);
    }
    return rc;
}
