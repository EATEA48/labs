#include <stdio.h>
#include <math.h>


int main()
{
    float a, x, sh, g, f, y;
    int p, i, fun, quest;
    double pi = 3.1415926;


    printf("Введите a: ");
    scanf("%f", &a);

    printf("Введите x; ");
    scanf("%f", &x);

    printf("Введите ф-ю которую хотите посчитать(g-1, f-2, y-3): ");
    scanf("%d", &fun);

    printf("Сколько считать?: ");
    scanf("%d", &p);

    printf("С каким шагом?: ");
    scanf("%f", &sh);

    for (i = 0; i <= p; p--)
        if (p == 0)
        {
            printf("Вы хотите продолжить?(y-1, n-2): ");
            scanf("%d", &quest);
            if (quest == 1)
            {
                printf("Сколько считать? ");
                scanf("%d", &p);

                printf("С каким шагом? ");
                scanf("%f", &sh);
            }
            else
            {
                printf("END");
            }
        }
        else
        {
            switch(fun)
            {
                case 1:
                    g = (-1 *(2 * (-5 * pow(a, 2) + 3 * a * x + 2 * pow(x, 2)) / (5 *pow(a, 2) + 9 * a * x - 2 * pow (x, 2))));
                    if ((5 *pow(a, 2) + 9 * a * x - 2 * pow (x, 2)) == 0)
                    {
                        printf("ERROR");
                    } else
                    {
                        printf("g = %f\n\n", g);
                    }
                    a += sh;
                    break;
                case 2:
                    f = (sin(pi * (10 * pow(a, 2) + 37 * a * x + 7 * pow(x, 2))));
                    printf("f = %f\n\n", f);
                    a += sh;
                    break;
                case 3:
                    y = (log(-5 * pow(a, 2) - 16 * a * x + 16 * pow(x, 2) + 1) / log(2));
                    printf("y = %f\n\n", y);
                    a += sh;
                    break;
                default:
                    printf("Неправельный ввод");
            }
        }

    return 0;
}
