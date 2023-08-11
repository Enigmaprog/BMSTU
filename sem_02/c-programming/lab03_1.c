#include <stdio.h>
//#include <stdbool.h>
//#include <stdlib.h>
//#include <string.h>
//#include <errno.h>
#define OK 0
#define ERR_IO 1
#define ERR_FILE 2

int process(int *, int, int s);

int main()
{
    int s = 0, rc = OK;

    FILE *f1, *f2;
    f1 = fopen("in_z.txt", "r");
    if (!f1)
    {
        rc = ERR_FILE;
        printf("Can't open first file\n");
    }
    else
    {
        f2 = fopen("out_z.txt", "w");
        if (!f2)
        {
            rc = ERR_FILE;
            printf("Can't open second file\n");
        }
        else
        {
            int x[100];
            int size = 0;

            while (fscanf(f1, "%d", &x[size]) == 1)
                printf("%d ", x[size++]);

            if (size == 0)
            {
                rc = ERR_IO;
                printf("Can't read numbers\n");
            }
            else
            {
                int d = process(x, size, s);
                fprintf(f2, "%d", d);
            }

            fclose(f2);
        }

        fclose(f1);
    }
    return rc;
}

int process(int *x, int t, int s)
{
    for (int i = 0; i < (t - 2); i++)
        if (x[i + 1] > x[i] && x[i + 1] > x[i + 2])
            s ++;

    int i = 0;

    if (x[i] > x[i + 1] && x[t - 1] > x[t - 2])
        s += 2;

    else if (x[i] > x[i + 1])
    {
        s = 1;

        for (int i = 0; i < (t - 2); i++)
            if (x[i + 1] > x[i] && x[i + 1] > x[i + 2])
                s ++;
    }
    else if (x[t - 1] > x[t - 2])
    {
        s = 1;

        for (int i = 0; i < (t - 2); i++)
            if (x[i + 1] > x[i] && x[i + 1] > x[i + 2])
                s ++;
    }
    else if (x[i] > x[i + 1] && x[t - 1] > x[t - 2])
    {
        s = 2;

        for (int i = 0; i < (t - 2); i++)
            if (x[i + 1] > x[i] && x[i + 1] > x[i + 2])
                s ++;
    }

    return s;
}
