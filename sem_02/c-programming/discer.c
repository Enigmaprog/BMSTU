#include<stdio.h>
#include<conio.h>
#include<math.h>
int main()
{
	int a, b, c;
	printf("a * x ^ 2 + b * x + c = 0\n");
	printf(" a:\n b:\n c:\n");
	scanf("%d%d%d", &a, &b, &c);
	int f = b * b - 4 * a * c;
	int d1 = (- b + sqrt(f)) / 2 * a;
	int d2 = (- b - sqrt(f)) / 2 * a;
	if(f > 0) printf("%d %d", d1, d2);
	if(f == 0) printf("%d", d1);
	if(f < 0) printf("False");
	getch();
	return 0;
	
}
