#include<stdio.h>
#include<conio.h>
int int_division(int, int);
int remain_division(int, int);
int main()
{
    int dividend, divider;
    printf("Input dividend and divider: ");
    scanf("%d %d", &dividend, &divider);

    if (dividend <= 1 || divider <= 1)
        printf("Invalid input");
    else
	{
        printf("Whole part and remain: ");
        printf("%d %d", int_division(dividend, divider), remain_division(dividend, divider));
	}
    getch();
    return 0;
}

int int_division(int dividend, int divider)
{
    int whole = 0;
    while (dividend >= divider)
    {
        dividend -= divider;
        whole++;
    }
    return whole;
}

int remain_division(int dividend, int divider)
{
    int whole = 0, copy_dividend = dividend;
    while (dividend >= divider)
    {
        dividend -= divider;
        whole++;
    }
    return copy_dividend - (divider * whole);;
}
