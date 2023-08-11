#include<stdio.h>
#include<math.h>
#include<conio.h>

float temp(float x, float eps)
{
    float s = 1, f = x, m = 2, n = 3, k =-1;
    while (f > eps)
    {
        f *= (m * n * k) / 2;
        m += 1;
        n += 1;
        k *= (-1);
        s += f;
    }
    return s;
}

int main()
{
    float x, eps;
    printf("x:");
    scanf("%f", &x);
    printf("eps:");
    scanf("%f", &eps);
    temp(x, eps);
    float t = temp(x, eps);
    printf("%f", t);
    getch();
    return 0;
}
