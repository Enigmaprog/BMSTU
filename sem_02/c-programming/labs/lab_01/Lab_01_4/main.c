#include <stdio.h>
#include <conio.h>
int main()
{
    int appartament;
    printf("Enter the number of appartments: ");
    scanf("%d", &appartament);
    int part = 36;
    int height = 9;

    int floor = part / height;
    int term_part = (appartament + part - 1) / part;
    int term = appartament - part * (term_part - 1);

    if (term / floor - (term - 1) / floor == 1)
    {
        term_floor = term / floor;
    }
    else
    {
        term_floor = term / floor + 1;
    }

    printf("Appartaments number %d are situated on %d floor of %d part of the building", appartament, term_floor, term_part);
    getch();
    return 0;
}
