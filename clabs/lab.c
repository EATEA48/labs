
#include <stdio.h>
#include <math.h>
#include <locale.h>


int main()
{
//    setlocale(LC_ALL, "Rus");
    float a, x, sh, g, f, y;
    int p, i, fun;
    double pi = 3.1415926;
    float mg_max, mf_max, my_max;
    float mg[50], mf[50], my[50];


    printf("Введите a: ");
    scanf("%f", &a);

    printf("Введите x; ");
    scanf("%f", &x);

    printf("Введите ф-ю которую хотите посчитать: ");
    scanf("%d", &fun);

    printf("Сколько считать?: ");
    scanf("%d", &p);

    printf("С каким шагом?: ");
    scanf("%f", &sh);


    for (i = 0; i < p; i++)
        if (p == 0)
        {
            char quest;
            scanf("Вы хотете продолжить?(y, n) %c\n", quest);
            if (quest == "y")
            {
                scanf("Сколько считать?: %d\n", &p);
                scanf("С каким шагом?: %f\n", &sh);
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
                        printf("%s", "ERROR");
                    }
                    else
                    {
                        if (g > mg_max)
                        {
                            mg_max = g;
                        }
                        printf("g = %f\n\n", g);
                        a += sh;
                    }
                    break;
                case 2:
                    f = (sin(pi * (10 * pow(a, 2) + 37 * a * x + 7 * pow(x, 2))));
                    if (a == 0)
                    {
                        printf("%s", "ERROR");
                    }
                    else
                    {
                        if (f > mf_max)
                        {
                            mf_max = f;
                        }
                        //                    for (int i = 50; i > 0; i--)
                        //                        mf_max[i] = mf_max[i - 1];
                        printf("f = %f\n\n", f);
                        a += sh;
                    }
                    break;
                case 3:
                    y = (log(-5 * pow(a, 2) - 16 * a * x + 16 * pow(x, 2) + 1) / log(2));
                    if (log(2) == 0)
                    {
                        printf("%s", "ERROR");
                    }
                    else
                    {
                        if (y > my_max)
                        {
                            my_max = y;
                        }
                        printf("y = %f\n\n", y);
                        a += sh;
                    }
                    break;
                default:
                    printf("%s", "ERROR");
            }
        }

    return 0;
}