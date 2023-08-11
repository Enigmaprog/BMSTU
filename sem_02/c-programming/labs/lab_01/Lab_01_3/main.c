#include <conio.h>
#include <stdio.h>
#include <math.h>

int main()
{
    float v1, v2, t1, t2;
    printf("Enter v1, v2 , t1 and t2(in celcius)\n");
    scanf("%f %f %f %f", &v1, &v2, &t1, &t2);
	float v3 = fabs(v1) + fabs(v2);
	float t3 = (t1 * abs(v1) + t2 * abs(v2)) / (abs(v1) + abs(v2));
	if (v3 == 0)
	{
		t3 = 0;
	}
	printf("v3 = %.2f, t3 = %.2f C", v3, t3);
    getch();
    return 0;
}
