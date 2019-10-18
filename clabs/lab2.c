


#include <stdio.h>
#include <math.h>

int main(void)
{
        float a, x, s, f, g, y;
        int funct;
        double pi = 3.141592653589;
        printf("Введите x: ");
        scanf("%f", &x);
        printf("Введите a: ");
        scanf("%f", &a);
        printf("Выберите какую ф-ию посчитать: f - 1, g -2, y - 3: ");
        scanf("%i", &funct);

        switch(funct) {
            case 1:
		if (a ){
                	f = (sin(pi * (10 * a * a + 37 * a * x + 7 * x * x)));
                	printf("%f\n", f);
                	break;
		}
            case 2:
                g = -1 * (2 * (-5 * a * a + 3 * a * x + 2 * x * x) / (5 * a * a + 9 * a * x - 2 * x * x));
                printf("%f\n", g);
                break;
            case 3:
                y = (log(-5 * a * a - 16 * a * x + 16 * x * x + 1) / log(2));
                printf("%f\n", y);
                break;
            default:
                printf("ERROR");
        }
	return 0;
}

