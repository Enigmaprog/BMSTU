#include<stdio.h>
#define OK 0
#define ERR_IO 1
int main()
{
    int a, b, t, s = 0, rc = OK;
    printf("a, b:");
    if (scanf("%d %d", &a, &b) == 0)
    {
        rc = ERR_IO;
        printf("Can't read number");
    }
    else
    {
        while(a > 0)
        {
            t = a % 10;
            if (t == b)
                s += 1;
            a /= 10;
        }
        printf("Result: %d", s);
    }
    return rc;
}
