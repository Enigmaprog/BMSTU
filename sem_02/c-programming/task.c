#include<stdio.h>
int main()
{
    int x;
    printf("Enter the size of the array:");
    scanf("%d", &x);
    int a[100];
    for (int i = 0; i < x; i ++)
    {
        printf("Enter the %d elements of the array:", i+1);
        scanf("%d",a + i);
    }
    int max = a[0];
    for(int i = 1; i < x; i++)
    {
       if (a[i] > max )
           max = a[i];
    }
    printf("%d", max);
    return 0;
}
