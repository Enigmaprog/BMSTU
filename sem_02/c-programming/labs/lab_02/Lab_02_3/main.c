#include <stdio.h>
#include <conio.h>
#include <math.h>
#define PI 3.14159265
float func(float, float);
void additional(float, float);
int main()
{
    float x, eps;

    printf("Input x and eps:");
    scanf(" %f %у", &x, &eps);
    
    float rad = x * (PI / 180.0);
    float sin_x = sinf(rad);
    printf("Sinus x is : %.3f\n", sin_x);
    if (x < 2.1364 && x > -2.1364)
    {
        float sum;
        sum = func(x, eps);
        printf("S(x) is : %.6f\n", sum);
        additional(sum, sin_x);
    }
    else
        printf("The series is endless");
    getch();
    return 0;
}

void additional(float s, float f)
{
    float absolute_error = fabs(f - s);
    float relative_error = fabs((f - s) / f);

    printf("\nAbs mistake: %f \nRel mistake: %f", absolute_error, relative_error);
}

float func(float x, float eps)
{
    //s(x) = x^1/1 - x^3/3! + x^5/5! - x^7/7! + ...
    float element = x, sum = 0;
    int factorial = 1, above_num = 1, i = 1;
	if (x == 0)
		return sum = 0;
	if (element > 0)
			x = element;
		else
			x = (-1) * element;
    while (x > eps)
    {
        element = (double) pow(x, above_num) / factorial;
		if (element > 0)
			x = element;
		else
			x = (-1) * element;
        if (i % 2 == 0)
        {
            element *= (-1);
        }
		//
		printf("element %f\n", element);
		//
        sum += element;
		if (fabs(element) <= eps)
			break;
        above_num += 2;
        i += 1;
        factorial *= ((above_num - 1) * above_num);
    }
    return sum;
}
