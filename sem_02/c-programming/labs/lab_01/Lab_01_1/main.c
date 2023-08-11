#include <stdio.h>
#include <conio.h>
#include <math.h>
int main()
{
    float base_sm, base_b, alpha;
    printf("Enten small base, big base and angle to big base: ");
    scanf("%f %f %f", &base_sm, &base_b, &alpha);

    if (base_sm > base_b)
    {
        float term = base_sm;
        base_sm = base_b;
        base_b = term;
    }

    float val = (float)3.14 / 180;
    float part = (float)(base_b - base_sm) / 2;
    // "part" is the half of the piece of base_b , which makes it more then base_sm
    float h = (float)part * tan(alpha * val);
    float area = (float)((base_b + base_sm ) / 2) * h;

    printf("Area is %.2f", area);
    getch();
    return 0;
}
