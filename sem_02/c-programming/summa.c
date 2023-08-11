#include<stdio.h>
#include<math.h>
#include<conio.h>

void temp(float x, float eps);

int main()
{
    float x, eps;
    printf("Enter number x:");
    scanf("%f", &x);
    printf("Enter an accuracy that compares to a member of the sequence eps:");
    scanf("%f", &eps);
    if (x > 1)
    {
        printf("Enter a number that is less than one");
    }
    if (eps > powf(1, -1))
    {
        printf("Enter an accuracy less than zero whole one tenth");
    }
    if (x < eps)
    {
        printf("%f", x);
    }
    else
    {
        temp(x, eps);
    }
    getch();
    return 0;
}

void temp(float x, float eps)
{
    float f = x, s = x;
    int i = 3, k = 1;
    float t = asin(f);
    while (fabs(f) > eps)
    {
        f *= (x * x * (i - 2)) / ((i - 1) * i) * k;
        s += f;
        i += 2;
        k += 2;
    }
    printf("approximate value of the function s(x): %f\n", s);
    printf("The exact value of the function f(x): %f\n", t);
    float m = fabs(t - s);
    printf("Calculation of the absolute error of the approximate value |f(x)-s(x)|: %f\n", m);
    float n = fabs(m / t);
    printf("Calculation of the relative error of the approximate value |(f(x)-s(x)) / f(x)|: %f\n", n);
}
