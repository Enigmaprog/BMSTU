#include<stdio.h>
#include<conio.h>

void def(int n);

int main()
{
    int F[] = {0, 1};
    int n;
    printf("Write a number: ");
    scanf("%d", &n);
    def(n);
    getch();
    return 0;
}

void def(int n)
{
    if (n == 0 || n == 1)
    printf("%d \n",F[n]);
    if (n >= 2)
    {
        for (int i=2; i <= n; i++)
        {
            int k = F[1];
            F[1] = F[0] + F[1];
            F[0] = k;
        }
        printf("%d\n",F[1]);
    }
    else
        printf("Write a number more than -1");
}

