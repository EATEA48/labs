#include <math.h>
#include <stdio.h>     

int main()
{
	float a, x, s, f, g, y;
	int funct;
	double pi = 3.141592653589;
	printf("Введите x: ");
	scanf_s("%f", &x);
	printf("Введите a: ");
	scanf_s("%f", &a);
	printf("Выберите какую ф-ию посчитать: f - 1, g -2, y - 3 ");
	scanf_s("%i", &funct);

	if (funct == 1) {
		f = (sin(pi * (10 * a * a + 37 * a * x + 7 * x * x)));
		printf("%f", f);
	}
	else if (funct == 2) {
		g = -1 * (2 * (-5 * a * a + 3 * a * x + 2 * x * x) / (5 * a * a + 9 * a * x - 2 * x * x));
		printf("%f", g);
	}
	else if (funct == 3) {
		y = (log(-5 * a * a - 16 * a * x + 16 * x * x + 1) / log(2));
		printf("%f", y);
	}
	else {
		printf("ERROR");
	}
}

