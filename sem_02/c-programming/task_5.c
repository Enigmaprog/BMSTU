#include <stdio.h>
#define OK 0
#define ERR_IO 1

int main()
{
    int rc = OK, x, t;
    printf("Enter the number: ");
    if (scanf("%d", &x) != 1)
    {
        rc = ERR_IO;
        printf("Can't read number");
    }
    else
    {
        int y = x % 100;
        int z = x % 10;
        int d = (y - z) / 10;
        printf("%d", d);
    }
    int s = x % 10;
    while(x > 0)
    {
        x /= 10;
        t = x % 10;
        s = s + t;
    }
    printf("\nsumma:%d", s);
    return rc;
}
