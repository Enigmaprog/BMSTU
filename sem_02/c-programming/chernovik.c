#include<stdio.h>
int main()
{
    int x;
    printf("x:");
    scanf("%d", &x);
    while (x>1)
    {
        x -= 1;
        printf("%d\n", x);
    }

}
