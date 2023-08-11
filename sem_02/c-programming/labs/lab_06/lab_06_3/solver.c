#include "solver.h"

int solver(FILE *fsrc)
{
    int a[maxN];
	int *p_start = a, *p_end;
	input(fsrc, p_start, &p_end);

	int max = -99999, temp = 0;
	for (int *i = p_start, *j = p_end; i != p_end; i++)
	{
		j -= 1;
		if (i > j)
			break;
		temp = *i + *j;
		printf("temp = %d\n", temp);
		if (temp > max)
			max = temp;
	}
    return max;
}