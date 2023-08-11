#include <stdio.h>
#include <conio.h>

int main(void)
{
    int n, m;
    printf("Input size of 1st list: ");
    scanf("%d",&n);
    int x[n];
    for(int i=0;i<n;i++)
    {
        printf("Input %d element: ", i+1);
        scanf("%d",x+i);
    }

    printf("Input size of 2nd list: ");
    scanf("%d",&m);

    int y[m];
    for(int j = 0; j<m; j++)
    {
        printf("Input %d element: ", j+1);
        scanf("%d", y+j);
    }
    int eq = 0;
    int count1 = 0, count2 =0;
    for(int i = 0; i<n; i++)
    {
        eq = 0;
        for(int j = 0; j<n; j++)
        {
            if(x[i] == y[j])
                eq += 1;
        }
        if (eq == 0)
            count1 += 1;
    }
    printf("count1 %d ",count1);
    int z[count1];
    for(int i = 0; i<n; i++)
        for(int j = 0; j<n; j++)
            if(x[i] != y[j])
                z[count2] = x[i];
                count2 ++;
                printf("%d\n",count2);
    printf("Array Z\n");
    for(int i=0; i<count1; i++)
    {
        printf("%d ", z[i]);
    }
    getch();
    return 0;
}
