#include<stdio.h>

void func(int size3, int *x, int n, int *y, int m);

int main()
{
    FILE *f1;
    FILE *f2;
    f1 = fopen("x.txt","r");
    f2 = fopen("y.txt","r");
    int x[100], y[100];
    int size1 = 0, size2 = 0, size3 = 0;
    while(1)
    {
        fscanf(f1, "%d", &x[size1]);
        if (feof(f1))
            break;
        else if (size1 == 0)
            printf("%d\n", x[size1]);
        else
            printf("%d ", x[size1]);
        size1 ++;
    }
    int n = x[0];
    while(1)
    {
        fscanf(f2, "%d", &y[size2]);
        if (feof(f2))
           break;
        else if (size2 == 0)
            printf("\n%d\n", y[size2]);
        else
            printf("%d ", y[size2]);
        size2 ++;
    }
    int m = y[0];
    func(size3, x, n, y, m);
    fclose(f2);
    fclose(f1);
    return 0;
}


void func(int size3, int *x, int n, int *y, int m)
{
    int z[100];
    for(int  i = 1; i <= n; i ++)
    {
        int d = 0;
        for(int j = 1; j <= m ; j++)
        {
            if (x[i] == y[j])
                d ++;
        }
        if (d == 0)
        {
            z[size3] = x[i];
            size3 ++;
        }
    }
    for(int i = 0; i < size3; i++)
        if (i == 0)
            printf("\n%d ", z[i]);
        else if(i >= 1)
            printf("%d ", z[i]);
}
