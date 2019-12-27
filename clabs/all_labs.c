#include <stdio.h>
#include <math.h>
#include <string.h>

int main()
{
    float a, x, sh, g, f, y, mf[100], mg[100], my[100], mg_max = 0, mf_max = 0, my_max = 0;
    int p, i, fun, quest, c = 0, out;
    double pi = 3.1415926;
    FILE *file_mg, *file_mf, *file_my;


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

    memset(mg, 0, 100*4);
    memset(mf, 0, 100*4);
    memset(my, 0, 100*4);

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
                    printf("g = %f\n", g);
                    if ((5 *pow(a, 2) + 9 * a * x - 2 * pow (x, 2)) == 0)
                    {
                        printf("ERROR");
                    }
                    else
                    {
                        if (mg_max < g)
                        {
                            mg_max = g;
                        }
                        for (int i = 0;i <= c; i++)
                            mg[i] = g;
                    }
                    a += sh;
                    c += 1;
                    break;
                case 2:
                    f = (sin(pi * (10 * pow(a, 2) + 37 * a * x + 7 * pow(x, 2))));
                    printf("f = %f\n", f);
                    if (a == 0)
                    {
                        printf("ERROR");
                    }
                    else
                    {
                        if (mf_max < f)
                        {
                            mf_max = f;
                        }
                        for (i = 0; i<= c; i++)
                            mf[i] = f;
                    }
                    a += sh;
                    c += 1;
                    break;
                case 3:
                    y = (log(-5 * pow(a, 2) - 16 * a * x + 16 * pow(x, 2) + 1) / log(2));
                    printf("y = %f\n", y);
                    if (log(2 ) == 0)
                    {
                        printf("ERROR");
                    }
                    else
                    {
                        if (my_max < y)
                        {
                            my_max = y;
                        }
                        for (i = 0; i <= c; i++)
                            my[i] = y;
                    }
                    a += sh;
                    c += 1;
                    break;
                default:
                    printf("Неправельный ввод");
            }
        }
    if (p == -1 && quest == 2)
    {
        printf("Как вывести ответ?(tabl - 1, str - 2)");
        scanf("%d", &out);
        switch(out)
        {
            case 1:
                if (fun == 1)
                {
                    printf("Максимальный элемент массива: \n", mg_max);
                    for (i = 0; i <= c; i++)
                        printf("%f\n", mg[i]);
                }
                if (fun == 2)
                {
                    printf("Максимальный элемент массива: \n", mf_max);
                    for (i = 0; i <= c; i++)
                        printf("%f\n", mf[i]);
                }
                if (fun == 3)
                {
                    printf("Максимальный элемент массива: \n", my_max);
                    for (i = 0; i <= c; i++)
                        printf("%f\n", my[i]);
                }
            case 2:
                if (fun == 1)
                {
                    printf("Максимальный элемент массива:  ", mg_max);
                    printf("\n");
                    for (i = 0; i <= c; i++)
                        printf("%f  ", mg[i]);
                }
                if (fun == 2)
                {
                    printf("Максимальный элемент массива:  ", mf_max);
                    printf("\n");
                    for (i = 0; i <= c; i++)
                        printf("%f  ", mf[i]);
                }
                if (fun == 3)
                {
                    printf("Максимальный элемент массива:  ", my_max);
                    printf("\n");
                    for (i = 0; i <= c; i++)
                        printf("%f  ", my[i]);
                }
            default:
                printf("Введен неверный параметр");
        }
    }

    file_mg = fopen("file_mg.txt", "w");
    for (i = 0; i <= c; i++)
        fprintf(file_mg, "%f\n" , mg[i]);
    fclose(file_mg);

    file_mf = fopen("file_mf.txt", "w");
    for (i = 0; i <= c; i++)
        fprintf(file_mf, "%f\n", mf[i]);
    fclose(file_mf);

    file_my = fopen("file_my.txt", "w");
    for (i = 0; i <= c; i++)
        fprintf(file_my, "%f\n", my[i]);
    fclose(file_my);

    for (i = 0; i <= c; i++)
    {
        mg[i] = 0;
        mf[i] = 0;
        my[i] = 0;
    }

    file_mg = fopen("file_mg.txt", "r");
    for (i = 0; i <= c; i++)
        fscanf(file_mg, "%f\n", mg[i]);
    fclose(file_mg);
    printf(mg);
    for (i = 0; i <= c; i++)
        printf("%f\n", mg[i]);


    file_mf = fopen("file_mf.txt", "r");
    for (i = 0; i <= c; i++)
        fscanf(file_mf, "%f\n", mf[i]);
    fclose(file_mf);
    printf(mf);

    file_my = fopen("file_my", "r");
    for (i = 0; i <= c; i++)
        fscanf(file_my, "%f\n", my[i]);
    fclose(file_my);
    printf(my);

    printf("С равно: %d", c);
    return 0;
}
