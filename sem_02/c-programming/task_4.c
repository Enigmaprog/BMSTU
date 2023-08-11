#include<stdio.h>
#define OK 0
#define ERR_IO 1
int main()
{
    int a, x[100];
    printf("Enter the size of the array:");
    scanf("%d", &a);
    for(int i = 0; i < a; i++)
    {
        printf("x[%d]:", i);
        scanf("%d", &x[i]);
    }
    for(int i = 0; i < a; i++)
        printf("%d ", x[i]);
    return 0;
}
