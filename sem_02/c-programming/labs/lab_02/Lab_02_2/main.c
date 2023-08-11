#include <stdio.h>
#include <conio.h>
#include <math.h>
void input_coords();
float scale();
int main()
{
	int coords[6];
	input_coords(&coords);
	float square = scale(&coords);
	printf("Scale of triangle is: %f", square);
	getch();
	return 0;
}

void input_coords(int * coords)
{
	for (int i = 1; i < 7; i += 2)
	{
		printf("Input coordinates of the point: ");
		scanf("%d %d", &coords[i - 1], &coords[i]);
	}
}

float scale(int * coords)
{
	int arr_x[3] = {coords[0], coords[2], coords[4]};
	int arr_y[3] = {coords[1], coords[3], coords[5]};
	
	float a = sqrt(powf((arr_x[0] - arr_x[1]), 2) + powf((arr_y[0] - arr_y[1]), 2));
	float b = sqrt(powf((arr_x[2] - arr_x[1]), 2) + powf((arr_y[2] - arr_y[1]), 2));
	float c = sqrt(powf((arr_x[2] - arr_x[0]), 2) + powf((arr_y[2] - arr_y[0]), 2));
	double p = (double)(a + b + c) / 2;
	float square = sqrt(p * (p - a) * (p - b) * (p - c));
	return square;
}
