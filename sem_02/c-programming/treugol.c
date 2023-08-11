#include<stdio.h>
#include<math.h>
#include<conio.h>
#include<stdbool.h>

float ress_l(float Ax, float Ay, float Bx, float By);

void print_ip(float x1, float y1, float x2, float y2,
              float x3, float y3);

int main()
{
    float Ax, Ay, Bx, By, Cx, Cy;
    printf("Ax,Ay:");
    scanf("%f%f", &Ax, &Ay);
    printf("Bx,By:");
    scanf("%f%f", &Bx, &By);
    printf("Cx,Cy:");
    scanf("%f%f", &Cx, &Cy);
    print_ip(Ax, Ay, Bx, By, Cx, Cy);
    getch();
    return 0;
}

float ress_l(float Ax, float Ay, float Bx, float By)
{
    return sqrtf(powf((Bx - Ax), 2) + powf((By - Ay), 2));
}

void print_ip(float x1, float y1, float x2, float y2,
              float x3, float y3)
{
    float l1 = ress_l(x1, y1, x2, y2);
    float l2 = ress_l(x2, y2, x3, y3);
    float l3 = ress_l(x3, y3, x1, y1);

    if (l1 == l2 && l2 == l3 && l1 == l3)
    {
        printf("ploshadi");
    }
    else
    {
        printf("ne ploshadi");
    }
}
