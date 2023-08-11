#include <stdio.h>

void input(FILE *f, int *p_start, int **p_end)
{
    int *p_cur = p_start;
    int count = 0;
    while (1)
    {
        fscanf(f, "%d", p_cur);
        p_cur++;
        count++;
        if (feof(f))
            break;
        if (count >= 100)
        {
            printf("The size of array has exceeded limit. Input terminated.");
            break;
        }
    }
    *p_end = p_cur;
}

void output(FILE *f, const int res)
{
    fprintf(f, "Result: %d", res);
}