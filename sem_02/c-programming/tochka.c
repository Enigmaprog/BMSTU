#include <stdio.h>
#include <conio.h>
#include <math.h>
#include <stdbool.h>
#define EPS 1e-5

/* Finds a side of a between two points */
float find_l(float x1, float y1, float x2, float y2);

/* Finds perimeter of a triangle */
float find_p(float a, float b, float c);

/* Finds  area of a triangle*/
float find_s(float a, float b, float c);

/* Check can sides a, b and c can create a triangle */
bool is_tr(float a, float b, float c);

/* Finds information about point and print it */
void print_ip(float x1, float y1, float x2, float y2,
              float x3, float y3, float xp, float yp);

int main()
{
    float Ax, Ay, Bx, By, Cx, Cy, Kx, Ky;

    printf("Enter the coordinates of points A:" );
    scanf("%f %f", &Ax, &Ay);

    printf("Enter the coordinates of points B:" );
    scanf("%f %f", &Bx, &By);

    printf("Enter the coordinates of points C:" );
    scanf("%f %f", &Cx, &Cy);

    printf("Enter the coordinates of points K:" );
    scanf("%f %f", &Kx, &Ky);
    print_ip(Ax, Ay, Bx, By, Cx, Cy, Kx, Ky);

    getch();
    return 0;
}

float find_l(float x1, float y1, float x2, float y2)
{
    return sqrtf(powf((x1 - x2), 2) + powf((y1 - y2), 2));
}

float find_p(float a, float b, float c)
{
    return (a + b + c) / 2.0;
}

float find_s(float a, float b, float c)
{
    float p = find_p(a, b, c);

    return sqrtf(p * (p - a) * (p - b) * (p - c));
}

bool is_tr(float a, float b, float c)
{
    return ((a + b > c) && (a + c > b) && (b + c > a));
}

void print_ip(float x1, float y1, float x2, float y2,
              float x3, float y3, float xp, float yp)
{
    float a = find_l(x2, y2, x3, y3);
    float b = find_l(x1, y1, x3, y3);
    float c = find_l(x1, y1, x2, y2);

    if (!is_tr(a, b, c))
        printf("Can't create a triangle");
    else
    {
        float pa = find_l(x1, y1, xp, yp);
        float pb = find_l(x2, y2, xp, yp);
        float pc = find_l(x3, y3, xp, yp);

        float s = find_s(a, b, c);

        float s1 = find_s(a, pb, pc);
        float s2 = find_s(b, pa, pc);
        float s3 = find_s(c, pa, pb);

        if ((abs(s1) < EPS && abs(s2 + s3 - s) < EPS) ||
             (abs(s2) < EPS && abs(s1 + s3 - s) < EPS) ||
             (abs(s3) < EPS && abs(s1 + s3 - s) < EPS))
        {
            printf("Point is on the side of the S triangle");
        }
        else if (s1 + s2 + s3 > s)
        {
            printf("Point is outside of the triangle\n");
        }
        else
        {
            printf("Point is inside of the triangle\n");
        }
    }
}
