#include <assert.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include "solver.h"

#define n_test 10
#define maxV 20

int min(int a, int b)
{
    int c;
    if (a < b)
        c = a;
    else
        c = b;
    return c;
}

void make_test()
{
    srand(time(NULL));
    for (int i = 0; i < n_test; i++)
    {
        int a[maxN];
        long long res = 0, res1 = 1;
        char fname[20], temp[20];
        // make input
        strcpy(fname, "in_");
        sprintf(temp, "%d", i);
        strcat(fname, temp);
        strcat(fname, ".txt");

        FILE *fsrc = fopen(fname, "w");
        int n = rand() % maxN + 1;
        for (int j = 0; j < n - 1; j++)
        {
            a[j] = rand() % maxV - 10;
            fprintf(fsrc, "%d ", a[j]);
        }
        a[n - 1] = rand() % maxV - 10;
        fprintf(fsrc, "%d", a[n - 1]);
        fclose(fsrc);

        // make output
        strcpy(fname, "out_");
        strcat(fname, temp);
        strcat(fname, ".txt");

        FILE *fdst = fopen(fname, "w");
        for (int j = 0; j < min(n, 100); j++)
        {
            res1 *= (long long)a[j];
            res += res1;
            if (a[j] < 0)
                break;
        }

        fprintf(fdst, "%d", res);
        fclose(fdst);
    }
}

void test_solver()
{
    for (int i = 0; i < n_test; i++)
    {
        char fname[20], temp[20];
        strcpy(fname, "in_");
        sprintf(temp, "%d", i);
        strcat(fname, temp);
        strcat(fname, ".txt");

        FILE *fsrc = fopen(fname, "r");
        int solver_result = solver(fsrc);
        fclose(fsrc);

        strcpy(fname, "out_");
        strcat(fname, temp);
        strcat(fname, ".txt");
        FILE *fdst = fopen(fname, "r");

        int expected_result;
        fscanf(fdst, "%d", &expected_result);
        fclose(fdst);

        //printf("%d %d\n", solver_result, expected_result);
        assert(solver_result == expected_result);
        printf("TEST %d: ACCEPTED\n", i);
    }
}

int main()
{
    make_test();
    test_solver();
    return 0;
}