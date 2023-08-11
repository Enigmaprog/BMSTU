#include<stdio.h>
int main(void)
{
    FILE *f1;
    f1 = fopen("x.txt", "r");
    int size = 0;
    int a[100];

    //while(1)
    //{
    //    fscanf(f, "%d", a+size);
    //    if (feof(f))
    //        break;
    //    printf("%d ",a[size]);
    //    size ++;
    //}
    while(fscanf(f, "%d", &a[size]) == 1)
        printf("%d ", a[size ++]);

    int max = a[0];
    for (int i = 0; i < size; i++)
    {
        if (a[i] > max)
            max = a[i];
    }
    printf("\n%d", max);

    fclose(f);
    return 0;
}
